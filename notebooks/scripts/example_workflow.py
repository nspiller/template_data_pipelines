# %%
import numpy as np
from src import computations, plotting

# %% [markdown]
# # Example 1
# Here we can explain that we are
# 1. generating an array of random numbers using `numpy`
# 2. calculating the mean using our custom code in the `src` module

# %%
# Generate data
data = []
for _ in range(10000):
    arr = np.random.rand(10)
    value = computations.compute_mean(arr)
    data.append(value)

# %% [markdown]
# Next, we plot the data.
# The plot is visible when we run the script file cell-by-cell or as a Jupyter notebook.
# We could also run the entire script file top to bottom and save the plot to a file.

# %%
fig, ax = plotting.plot_distribution(data)
# fig.savefig("/some/other/folder/plot.png")
