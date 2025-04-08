import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Styling
st.set_page_config(layout="centered", page_title="Order Dashboard")

# Header
st.title("📦 Order Analyse Dashboard")
st.write("Selecteer een merk om de visualisaties bij te werken.")

# Data inladen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Dropdown (control)
selected_brand = st.selectbox("Kies een merk", df['merk'].unique())

# Filteren op selectie
filtered_df = df[df['merk'] == selected_brand]

# Eerste visual: Aantal orders per persoon
fig1, ax1 = plt.subplots()
filtered_df['klant_naam'].value_counts().plot(kind='bar', ax=ax1)
ax1.set_title("Aantal orders per persoon")
st.pyplot(fig1)

# Tweede visual: Gemiddeld bedrag per maat
fig2, ax2 = plt.subplots()
filtered_df.groupby('maat')['Totaal_Bedrag'].mean().plot(kind='bar', ax=ax2)
ax2.set_title("Gemiddeld bedrag per maat")
st.pyplot(fig2)
