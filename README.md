# GIMP Lab

Laboratorio per migliorare GIMP e renderlo un programma di grafica professionale, alla pari di Photoshop.

Qui raccogliamo plugin, proposte di interfaccia, patch al codice sorgente e note di test. Quando un lavoro è maturo e provato, lo proponiamo al team di sviluppo di GIMP.

## Come lavoriamo

1. **Scegliamo una voce** dalla [roadmap](ROADMAP.md).
2. **La sviluppiamo** come plugin, proposta UX o patch, a seconda di cosa richiede.
3. **La testiamo** nell'uso reale e annotiamo i risultati.
4. **La proponiamo a GIMP** tramite il loro GitLab (gitlab.gnome.org/GNOME/gimp): prima si apre una discussione, poi si invia il codice.

## Struttura

| Cartella | Contenuto |
|---|---|
| `plugins/` | Plugin in Python per GIMP 3, installabili sulla versione normale |
| `ux/` | Proposte di interfaccia: mockup, motivazioni, confronti |
| `patches/` | Modifiche al codice sorgente di GIMP (C, GEGL) |
| `test/` | Note di test: cosa è stato provato, cosa funziona, cosa no |

Le cartelle vengono create quando arriva il primo lavoro per ciascuna.

## Ambiente

- GIMP 3.2.x
- Fedora Linux (Sway)

## Persone

- **Francesco Carta**: product designer, test e proposte UX
- Sviluppo svolto con l'assistenza di Claude (Anthropic)
