# GIMP Lab Export

Esporta l'immagine aperta in più formati per social e web, in un solo passaggio.

Menu: **File → Export → Export for Social and Web...**

## Formati

| Formato | Dimensioni | Come |
|---|---|---|
| Instagram square | 1080 × 1080 | ritaglio centrato |
| Instagram portrait | 1080 × 1350 | ritaglio centrato |
| Instagram story | 1080 × 1920 | ritaglio centrato |
| Website | 2000 px lato lungo | proporzioni originali, mai ingrandita |
| Portfolio | 3000 px lato lungo | proporzioni originali, mai ingrandita |

Tutti i file sono JPEG e si chiamano `nomeimmagine_formato.jpg`. Se non scegli una cartella, finiscono in una cartella `export` accanto all'immagine. L'immagine originale non viene modificata.

## Installazione (GIMP 3.2, Linux)

Il file deve stare in una cartella con lo stesso nome dentro la cartella dei plugin di GIMP ed essere eseguibile:

```
~/.config/GIMP/3.2/plug-ins/gimp-lab-export/gimp-lab-export.py
```

Con GIMP installato da Flatpak la cartella è `~/.var/app/org.gimp.GIMP/config/GIMP/3.2/plug-ins/`.

Riavvia GIMP dopo l'installazione.

## Stato

🧪 In test. Limiti noti:
- Il ritaglio è sempre centrato
- Solo JPEG, con la qualità predefinita di GIMP
- Le dimensioni dei formati sono fisse nel codice
