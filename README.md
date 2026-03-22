# 🧬 TCR Motif and Clustering Analysis (CMV Dataset)

## 📌 Overview

This project explores T-cell receptor (TCR) repertoire data to identify sequence patterns (motifs) and functionally similar groups (clusters) associated with Cytomegalovirus (CMV) response.

The analysis highlights how a highly diverse immune repertoire can be organized into meaningful biological signatures using motif frequency analysis and clustering approaches.

---

## 🎯 Objectives

* Analyze TCR sequence diversity
* Identify recurring sequence motifs (patterns)
* Group structurally similar TCRs into clusters
* Visualize immune repertoire structure

---

## 🧪 Dataset

* Input: CSV file containing TCR beta chain sequences (TcRb)
* Key columns:

  * `pattern`: Motif pattern of TCR sequences
  * `TcRb`: TCR beta sequence
  * `index`: Cluster ID (from clustering algorithm)

---

## ⚙️ Methods

* Data loading and preprocessing using Python
* Motif frequency analysis using `value_counts()`
* Grouping TCRs by motif and cluster
* Visualization using bar plots

Libraries used:

* pandas
* matplotlib
* seaborn

---

## 📊 Results

### 1. Motif Distribution

* The majority of TCR sequences (~7000+) were labeled as **"single"**, meaning they appeared only once.
* This reflects a highly diverse, non-expanded background repertoire.
* A small number of motifs (e.g., APG%TNEK, SSA%YG) appeared multiple times.

👉 Interpretation:
The immune repertoire is dominated by unique sequences, with limited shared motifs.

---

### 2. Clustering Analysis

* Clustering grouped similar TCRs into functional families.
* Example findings:

  * **Cluster 865**: ~60 TCRs (dominant immune response group)
  * Other clusters (e.g., 19, 24): 40+ TCRs each

👉 Interpretation:
Clustering reveals biologically meaningful T-cell groups likely targeting specific CMV epitopes.

---

## 🧠 Key Insights

* TCR repertoire is highly diverse (many singletons)
* Motif analysis alone shows limited expansion
* Clustering uncovers hidden immune structure
* Functional grouping is more informative than exact sequence matching

---

## 🚀 Future Improvements

* Apply advanced clustering methods (e.g., GLIPH2)
* Integrate antigen specificity data
* Perform diversity metrics (Shannon index)
* Compare across disease conditions

---

## 📁 Output

* Motif distribution plot
* Cluster size distribution plot

---

## 🧑‍💻 Author

Mohamed Esmat

---

## 📎 Notes

This project demonstrates basic bioinformatics analysis of immune receptor repertoires and can be extended to cancer immunology or infectious disease research.
