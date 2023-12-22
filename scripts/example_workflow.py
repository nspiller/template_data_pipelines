# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: template
#     language: python
#     name: python3
# ---

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

# %% [markdown]
# # Example 2
# In case the pipelines become more complex, we can also outsource them to a separate script file.
# This is useful to keep the workflow scripts clean and readable.
#
# Note that this should often 

# %%
# call function from another script file
from scripts.more_complex_pipeline import many_steps
processed_data = many_steps(data)
fig, ax = plotting.plot_distribution(processed_data)

# %%
