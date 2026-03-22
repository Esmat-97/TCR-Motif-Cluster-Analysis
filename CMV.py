import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# جرب مع الفاصل كـ comma
df = pd.read_csv("P16125_WDFJJYZL7L (1).csv", sep=",", encoding="utf-8")

# تأكيد وجود العمود
print("Columns:", df.columns.tolist())
print(df.head(5))

# عرض عدد كل motif
motif_counts = df['pattern'].value_counts()
print("Motif counts:\n", motif_counts)

# عرض كل TCRs لكل motif
for motif in df['pattern'].unique():
    tcrs = df[df['pattern'] == motif]['TcRb']
    print(f"\nMotif {motif}: {len(tcrs)} TCRs")
    print(tcrs.head(10).tolist())

# عرض كل TCRs لكل cluster
cluster_groups = df.groupby('index')['TcRb'].apply(list)
print("\nClusters and their TCRs:\n", cluster_groups)





# Count motifs
motif_counts = df['pattern'].value_counts().head(10)

# Plot motif distribution
plt.figure(figsize=(10,6))
sns.barplot(x=motif_counts.index, y=motif_counts.values, palette="viridis")
plt.title("Number of TCRs per Motif")
plt.xlabel("Motif")
plt.ylabel("Number of TCRs")
plt.xticks(rotation=45)
plt.savefig("Number of TCRs per Motif")
plt.show()




# Count clusters
cluster_sizes = df['index'].value_counts().head(10)

# Plot cluster distribution
plt.figure(figsize=(10,6))
sns.barplot(x=cluster_sizes.index, y=cluster_sizes.values, palette="magma")
plt.title("Number of TCRs per Cluster")
plt.xlabel("Cluster Index")
plt.ylabel("Number of TCRs")
plt.xticks(rotation=45)
plt.savefig("Number of TCRs per Cluster")
plt.show()
