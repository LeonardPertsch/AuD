# AuD Exercises 📚

Meine Sammlung aus **Algorithmen und Datenstrukturen (AuD)** – selbst implementierte
Algorithmen, Übungsblätter, Notebooks und Mitschriften aus dem Semester.

## 📂 Struktur

```
AuD_Exercises/
├── algorithmen/                  # Eigene Implementierungen, nach Themen sortiert
│   ├── grundlagen/               #   Schriftliche Addition
│   ├── sortieren/                #   Bubblesort, Mergesort, Quicksort, Random Sort
│   ├── divide_and_conquer/       #   Potenzieren durch Halbieren
│   ├── dynamische_programmierung/#   Top-down (Memoisierung) vs. Bottom-up
│   ├── greedy/                   #   Münzrückgabe, Rucksackproblem
│   ├── brute_force/              #   Maximum-Suche, Rucksackproblem (optimal)
│   ├── graphen/
│   │   ├── dijkstra/             #   Kürzeste Wege (inkl. Visualisierung)
│   │   ├── kruskal/              #   Minimaler Spannbaum (inkl. Union-Find)
│   │   └── zyklensuche/          #   Zyklenerkennung per DFS
│   ├── datenstrukturen/
│   │   ├── heaps/                #   Min-/Max-Heap, Heapify, Remove
│   │   └── hashing/              #   Hash-Tabellen mit Verkettung
│   └── optimierung/              #   Bisektion, Gradient Descent, Evolutionsstrategie
│
└── uebungen/                     # Übungsblätter mit Notebooks, PDFs & Mitschriften
    ├── uebung_03_python_grundlagen/
    ├── uebung_04_komplexitaet/
    ├── uebung_05_basis_datenstrukturen/
    ├── uebung_06_dict_hash/
    ├── uebung_08_graphdatenstrukturen/
    ├── uebung_09_baeume/
    ├── uebung_10_rekursion/
    ├── uebung_11_divide_and_conquer/
    ├── uebung_12_greedy_brute_force/
    ├── uebung_13_randomisierte_algorithmen/
    └── uebung_14_particle_methods/
```

## 🧠 Themenüberblick

| Thema | Kernidee | Wichtige Skripte |
|---|---|---|
| Sortieren | Vergleichen & Tauschen vs. Divide and Conquer | `sortieren/mergesort.py`, `sortieren/quicksort.py` |
| Dynamische Programmierung | Teilergebnisse speichern statt neu berechnen | `dynamische_programmierung/dp_wiederholung.py` |
| Greedy | Lokal beste Wahl treffen | `greedy/muenzrueckgabe.py`, `graphen/dijkstra/` |
| Brute Force | Alle Möglichkeiten durchprobieren | `brute_force/rucksackproblem.py` |
| Graphen | Kürzeste Wege, Spannbäume, Zyklen | `graphen/dijkstra/`, `graphen/kruskal/`, `graphen/zyklensuche/` |
| Datenstrukturen | Heaps & Hash-Tabellen von Hand | `datenstrukturen/heaps/`, `datenstrukturen/hashing/` |
| Optimierung | Nullstellen & Minima numerisch finden | `optimierung/gradient_descent.py`, `optimierung/bisektion.py` |

Viele Themen liegen bewusst in mehreren Varianten vor
(`*_eigene_version.py`, `*_auswendig.py`, `*_wiederholung_*.py`) –
das waren meine Übungs- und Klausurvorbereitungs-Durchläufe.

## 🚀 Ausführen

Jedes Skript ist eigenständig lauffähig und enthält am Anfang einen
Docstring mit Beschreibung und Laufzeit:

```bash
python3 algorithmen/sortieren/mergesort.py
```

Für die Visualisierungen und Notebooks werden zusätzliche Pakete benötigt:

```bash
pip install numpy matplotlib networkx jupyter
```

Die Notebooks (`.ipynb`) in `uebungen/` lassen sich mit Jupyter öffnen:

```bash
jupyter lab uebungen/uebung_10_rekursion/10_uebung_recursion.ipynb
```

## 📝 Hinweise

- `algorithmen/graphen/dfs_zusammenhang.py` ist noch ein leerer Platzhalter (TODO).
- Die `mitschriften.txt`-Dateien in den Übungsordnern sind meine Notizen aus den Übungen.
- Kurs: Algorithmen und Datenstrukturen (AuD).
