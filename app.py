import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Meu App Streamlit na EC2 🚀")
st.write("Exemplo de gráfico com matplotlib + pandas")

data = pd.DataFrame({
    "Ano": [2020, 2021, 2022, 2023],
    "Vendas": [100, 120, 130, 170]
})

fig, ax = plt.subplots()
ax.plot(data["Ano"], data["Vendas"], marker='o')
st.pyplot(fig)
