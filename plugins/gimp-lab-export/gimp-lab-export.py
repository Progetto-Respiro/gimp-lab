#!/usr/bin/env python3
# GIMP Lab Export
# Export the current image to several social and web formats in one step.
#
# Part of GIMP Lab: https://github.com/Progetto-Respiro/gimp-lab
# License: GPL-3.0-or-later

import os
import sys

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
from gi.repository import GObject, GLib, Gio

PROC_NAME = 'plug-in-gimp-lab-export'

# (argument name, label, width, height, mode, file suffix)
# mode "crop": center-crop to the exact aspect ratio, then scale to width x height
# mode "fit":  scale so the longest side equals width, never enlarging the image
PRESETS = [
    ('ig-square',   'Instagram square (1080 x 1080)',   1080, 1080, 'crop', 'ig-square'),
    ('ig-portrait', 'Instagram portrait (1080 x 1350)', 1080, 1350, 'crop', 'ig-portrait'),
    ('ig-story',    'Instagram story (1080 x 1920)',    1080, 1920, 'crop', 'ig-story'),
    ('web',         'Website (2000 px longest side)',   2000, 2000, 'fit',  'web'),
    ('portfolio',   'Portfolio (3000 px longest side)', 3000, 3000, 'fit',  'portfolio'),
]


def base_name(image):
    name = image.get_name() or 'image'
    name = os.path.splitext(name)[0]
    # GIMP names unsaved images like "Untitled-1"; keep it simple and file-safe
    return ''.join(c if c.isalnum() or c in '-_' else '_' for c in name)


def default_folder(image):
    f = image.get_file()
    if f is not None and f.get_path():
        return os.path.join(os.path.dirname(f.get_path()), 'export')
    pictures = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_PICTURES)
    return os.path.join(pictures or GLib.get_home_dir(), 'export')


def center_crop(img, ratio):
    w, h = img.get_width(), img.get_height()
    if w / h > ratio:
        new_w, new_h = max(1, round(h * ratio)), h
    else:
        new_w, new_h = w, max(1, round(w / ratio))
    img.crop(new_w, new_h, (w - new_w) // 2, (h - new_h) // 2)


def fit_longest(img, longest):
    w, h = img.get_width(), img.get_height()
    if max(w, h) <= longest:
        return
    if w >= h:
        img.scale(longest, max(1, round(h * longest / w)))
    else:
        img.scale(max(1, round(w * longest / h)), longest)


def export_preset(image, preset, folder, base):
    _, _, width, height, mode, suffix = preset
    dup = image.duplicate()
    try:
        dup.flatten()
        if mode == 'crop':
            center_crop(dup, width / height)
            dup.scale(width, height)
        else:
            fit_longest(dup, width)
        path = os.path.join(folder, f'{base}_{suffix}.jpg')
        Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, dup,
                       Gio.File.new_for_path(path), None)
        return path
    finally:
        dup.delete()


class GimpLabExport(Gimp.PlugIn):

    def do_query_procedures(self):
        return [PROC_NAME]

    def do_set_i18n(self, name):
        return False

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(
            self, name, Gimp.PDBProcType.PLUGIN, self.run, None)
        procedure.set_image_types('*')
        procedure.set_sensitivity_mask(
            Gimp.ProcedureSensitivityMask.DRAWABLE
            | Gimp.ProcedureSensitivityMask.DRAWABLES
            | Gimp.ProcedureSensitivityMask.NO_DRAWABLES)
        procedure.set_menu_label('Export for _Social and Web...')
        procedure.add_menu_path('<Image>/File/Export')
        procedure.set_documentation(
            'Export the image to several social and web formats at once',
            'Creates JPEG copies of the image for Instagram (square, portrait, '
            'story), website and portfolio. Instagram formats are center-cropped '
            'to the exact size; web and portfolio keep the proportions and are '
            'never enlarged. The original image is not modified.',
            name)
        procedure.set_attribution('Francesco Carta', 'GIMP Lab', '2026')

        for arg, label, *_ in PRESETS:
            default = arg in ('ig-portrait', 'web')
            procedure.add_boolean_argument(
                arg, label, f'Export {label}', default,
                GObject.ParamFlags.READWRITE)

        procedure.add_file_argument(
            'output-folder', 'Output folder',
            'Where to save the files (empty: an "export" folder next to the image)',
            Gimp.FileChooserAction.SELECT_FOLDER, True, None,
            GObject.ParamFlags.READWRITE)
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        if run_mode == Gimp.RunMode.INTERACTIVE:
            GimpUi.init(PROC_NAME)
            dialog = GimpUi.ProcedureDialog.new(
                procedure, config, 'Export for Social and Web')
            dialog.fill(None)
            if not dialog.run():
                dialog.destroy()
                return procedure.new_return_values(
                    Gimp.PDBStatusType.CANCEL, GLib.Error())
            dialog.destroy()

        chosen = [p for p in PRESETS if config.get_property(p[0])]
        if not chosen:
            return self.error(procedure, 'No format selected.')

        folder_file = config.get_property('output-folder')
        folder = folder_file.get_path() if folder_file else default_folder(image)
        try:
            os.makedirs(folder, exist_ok=True)
        except OSError as e:
            return self.error(procedure, f'Cannot create folder {folder}: {e}')

        base = base_name(image)
        Gimp.context_push()
        Gimp.context_set_interpolation(Gimp.InterpolationType.LOHALO)
        Gimp.progress_init('Exporting...')
        saved = []
        try:
            for i, preset in enumerate(chosen):
                saved.append(export_preset(image, preset, folder, base))
                Gimp.progress_update((i + 1) / len(chosen))
        except Exception as e:
            return self.error(procedure, f'Export failed: {e}')
        finally:
            Gimp.context_pop()

        Gimp.message(f'Exported {len(saved)} file(s) to {folder}')
        return procedure.new_return_values(
            Gimp.PDBStatusType.SUCCESS, GLib.Error())

    def error(self, procedure, msg):
        return procedure.new_return_values(
            Gimp.PDBStatusType.EXECUTION_ERROR,
            GLib.Error.new_literal(Gimp.PlugIn.error_quark(), msg, 0))


Gimp.main(GimpLabExport.__gtype__, sys.argv)
