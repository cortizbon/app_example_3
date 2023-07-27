import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Primera aplicación en streamlit")

X = np.random.normal(0, 10, 1000)
Y = np.random.normal(5, 10, 1000)

fig, ax = plt.subplots(1, 2, sharex=True)

ax[0].hist(X, bins=50)
ax[1].hist(Y, bins=50)

st.pyplot(fig)
