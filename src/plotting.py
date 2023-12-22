import matplotlib.pyplot as plt
import seaborn as sns


def plot_distribution(list_of_values):
    "Example function to plot a distribution of values"
    fig, ax = plt.subplots()
    sns.histplot(list_of_values, ax=ax)
    fig.tight_layout()

    return fig, ax
