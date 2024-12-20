import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df, target):
    """
    מצייר התפלגויות של התכונות מול עמודת המטרה.
    """
    sns.set_style("darkgrid")
    f, (axis1, axis2) = plt.subplots(2, 1, sharex=True, figsize=(11, 5))
    bins = 70

    axis1.hist(df.Time[df[target] == 1], bins=bins, color='red', alpha=0.7)
    axis1.set_title('Fraud', fontsize=14)
    axis1.set_ylabel('Transaction Count', fontsize=12)

    axis2.hist(df.Time[df[target] == 0], bins=bins, color='green', alpha=0.7)
    axis2.set_title('Normal', fontsize=14)
    axis2.set_xlabel('Time (in Seconds)', fontsize=12)
    axis2.set_ylabel('Transaction Count', fontsize=12)

    plt.tight_layout()
    plt.show()
