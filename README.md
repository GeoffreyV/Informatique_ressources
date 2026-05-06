# Scaffolder LaTeX

Ce projet permet de générer automatiquement une arborescence LaTeX pour :
- Semestres
- Séquences
- Documents T (TP/TD/C/DS/QCM) basés sur un template commun

## Commandes principales

### Créer un semestre
```bash
python -m scaffolder semestre S1 "GEII"
```

### Créer une séquence
```bash
python -m scaffolder sequence S1_GEII
```

### Créer un TP/TD/C/DS/QCM
```bash
python -m scaffolder t S1_GEII/Seq01_Intro tp "Variables et types"
python -m scaffolder t S1_GEII/Seq02_Boucles ds "Contrôle 1"
python -m scaffolder t S1_GEII/Seq03_Logique qcm "QCM de base"
```

### Renommer
```bash
python -m scaffolder rename S1_GEII/Seq01_Intro --num 02 --title "Introduction"
python -m scaffolder rename S1_GEII/Seq02_Boucles/TP01_Variables --num 05 --title "Variables et types"
```

## Placeholders disponibles
- `__SEM_CODE__`, `__SEM_TITLE__`
- `__SEQ_NUM__`, `__SEQ_TITLE__`
- `__T_NUM__`, `__T_TITLE__`
- `__DOC_TITLE__`, `__DOC_TYPE__`

## Structure des templates
```
templates/
├── SX_SemestreTemplate/
│   ├── SeqXX_SemestreTemplate/
│   │   ├── TXX_template/
│   │   │   ├── TXX_template.tex
│   │   │   └── sources/
│   │   └── preamble.tex
│   └── preamble_module.tex
└── branches/
    ├── tp/
    ├── td/
    ├── c/
    ├── ds/
    └── qcm/
```
