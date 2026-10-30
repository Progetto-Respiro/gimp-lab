# Roadmap

Tutte le funzioni che mancano a GIMP per competere con Photoshop, divise per area.

**Via** indica la strada più probabile:
- `plugin`: realizzabile come estensione in Python, senza toccare il nucleo
- `UX`: soprattutto lavoro di design e proposta al team
- `patch`: modifica al codice sorgente, da concordare con i manutentori
- `architettura`: cambio profondo del programma, lavoro lungo e da discutere a fondo con il team

**Stato**: ⬜ da fare · 🟨 in corso · 🧪 in test · 📤 proposto a GIMP · ✅ accettato

Prima di iniziare una voce, verificare sul GitLab di GIMP se esiste già o se qualcuno ci sta lavorando.

---

## 1. Modifica non distruttiva

| Funzione | Via | Stato |
|---|---|---|
| Livelli di regolazione (curve, livelli, tonalità/saturazione) | architettura | ⬜ |
| Oggetti avanzati completi (incorporati e collegati) | architettura | ⬜ |
| Stili di livello (ombra, bagliore, traccia, rilievo) | architettura | ⬜ |
| Maschere vettoriali sui livelli | patch | ⬜ |

## 2. Selezione e ritocco

| Funzione | Via | Stato |
|---|---|---|
| Selezione automatica di soggetto e oggetto (IA locale) | plugin | ⬜ |
| Riempimento in base al contenuto nativo | patch | ⬜ |
| Pennello correttivo e toppa più veloci | patch | ⬜ |
| Seleziona e maschera (capelli, bordi difficili) | patch | ⬜ |
| Riempimento generativo con modelli locali | plugin | ⬜ |

## 3. Trasformazioni e deformazioni

| Funzione | Via | Stato |
|---|---|---|
| Puppet warp | patch | ⬜ |
| Perspective warp | patch | ⬜ |
| Fluidifica completo con riconoscimento volti | patch | ⬜ |
| Guide smart (aggancio a oggetti e spaziature) | patch | ⬜ |

## 4. Testo e tipografia

| Funzione | Via | Stato |
|---|---|---|
| Funzioni OpenType complete | patch | ⬜ |
| Stili di paragrafo e carattere | patch | ⬜ |
| Testo su tracciato modificabile | patch | ⬜ |
| Modifica del testo sulla tela più fluida | UX + patch | ⬜ |

## 5. Colore e stampa

| Funzione | Via | Stato |
|---|---|---|
| Flusso di lavoro CMYK completo | architettura | ⬜ |
| Colori spot (Pantone) e separazioni | architettura | ⬜ |
| Gestione del colore end-to-end | patch | ⬜ |
| Supporto LUT e color grading | plugin | ⬜ |

## 6. Prestazioni

| Funzione | Via | Stato |
|---|---|---|
| Accelerazione GPU stabile | architettura | ⬜ |
| File grandi con centinaia di livelli | architettura | ⬜ |
| Anteprime filtri in tempo reale su immagini pesanti | patch | ⬜ |

## 7. Automazione

| Funzione | Via | Stato |
|---|---|---|
| Registratore di azioni (macro) | plugin | ⬜ |
| Elaborazione in batch integrata | plugin | ⬜ |
| Gestore di estensioni | patch | ⬜ |

## 8. Flusso di lavoro professionale

| Funzione | Via | Stato |
|---|---|---|
| Tavole da disegno (artboard) multiple | architettura | ⬜ |
| Esportazione rapida di livelli e risorse | plugin | ⬜ |
| Sviluppo RAW integrato o collegamento migliore | plugin | ⬜ |
| Compatibilità PSD più completa | patch | ⬜ |
| Composizioni di livelli (layer comps) | plugin | ⬜ |
| Istantanee della cronologia | patch | ⬜ |

## 9. Fotografia

| Funzione | Via | Stato |
|---|---|---|
| Unione di panorami | plugin | ⬜ |
| Unione HDR | plugin | ⬜ |
| Focus stacking | plugin | ⬜ |
| Correzione obiettivo con profili | plugin | ⬜ |
| Sostituzione del cielo | plugin | ⬜ |
| Riduzione rumore e upscaling con IA locale | plugin | ⬜ |

## 10. Vettoriale e grafica

| Funzione | Via | Stato |
|---|---|---|
| Livelli forma modificabili | patch | ⬜ |
| Strumento penna più comodo | UX + patch | ⬜ |
| Strumento cornice | plugin | ⬜ |

## 11. Animazione

| Funzione | Via | Stato |
|---|---|---|
| Timeline per animazioni e GIF | plugin | ⬜ |

## 12. Affidabilità

| Funzione | Via | Stato |
|---|---|---|
| Salvataggio automatico e recupero dopo crash | patch | ⬜ |
| API per plugin stabile nel tempo | architettura | ⬜ |

## 13. Interfaccia ed esperienza d'uso

| Funzione | Via | Stato |
|---|---|---|
| Nomi e menu vicini agli standard del settore | UX | ⬜ |
| Scopribilità degli strumenti | UX | ⬜ |
| Spazi di lavoro predefiniti (foto, illustrazione, web) | UX + patch | ⬜ |
| Coerenza visiva di icone, dialoghi e pannelli | UX | ⬜ |
| Scorciatoie "stile Photoshop" attivabili | patch | ⬜ |

## 14. Dispositivi e accessibilità

| Funzione | Via | Stato |
|---|---|---|
| Tavolette grafiche: pressione, inclinazione, gesti | patch | ⬜ |
| Interfaccia per tablet | architettura | ⬜ |
| Accessibilità per lettori di schermo | patch | ⬜ |
| Interfaccia ridimensionabile su schermi HiDPI | patch | ⬜ |

## 15. Lavoro di squadra e comunità

| Funzione | Via | Stato |
|---|---|---|
| Commenti e revisione sui file | architettura | ⬜ |
| Librerie di risorse condivise | plugin | ⬜ |
| Manuale aggiornato per GIMP 3.x | documentazione | ⬜ |

---

## Prossimo passo

Primo lavoro proposto: **registratore di azioni** oppure **esportatore in batch** (area 7), come plugin Python.
