import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Configuratie
st.set_page_config(layout="centered", page_title="📊 Order Analyse")

# Titel
st.title("📊 Order Analyse Dashboard")

# Stap 1: CSV inlezen zonder datumconversie
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Stap 2: Conversie van 'aankoopdatum' naar datetime
df["aankoopdatum"] = pd.to_datetime(df["aankoopdatum"], dayfirst=True, errors="coerce")

# Stap 3: Alleen geldige datums behouden
df = df[df["aankoopdatum"].notna()]

# Tabs
tab1, tab2 = st.tabs(["📈 Leeftijd per Merk", "📆 Aankopen per Week"])

with tab1:
    st.subheader("Gemiddelde leeftijd per merk")

    leeftijd_per_merk = df.groupby("merk")["leeftijd"].mean().sort_values()

    fig1, ax1 = plt.subplots()
    leeftijd_per_merk.plot(kind="bar", ax=ax1, color="#4CAF50")
    ax1.set_ylabel("Gemiddelde leeftijd")
    ax1.set_xlabel("Merk")
    ax1.set_title("Gemiddelde leeftijd per merk")
    st.pyplot(fig1)

with tab2:
    st.subheader("Aantal aankopen per week")

    # Jaarselectie op basis van beschikbare jaren
    df["Jaar"] = df["aankoopdatum"].dt.year
    available_years = sorted(df["Jaar"].unique(), reverse=True)
    selected_year = st.selectbox("Kies een jaar", available_years)

    # Filter op gekozen jaar
    df_filtered = df[df["Jaar"] == selected_year].copy()
    df_filtered["Week"] = df_filtered["aankoopdatum"].dt.isocalendar().week

    aankopen_per_week = df_filtered["Week"].value_counts().sort_index()

    fig2, ax2 = plt.subplots()
    aankopen_per_week.plot(kind="bar", ax=ax2, color="#2196F3")
    ax2.set_xlabel("Weeknummer")
    ax2.set_ylabel("Aantal aankopen")
    ax2.set_title("Aankopen per week in {selected_year}")
    st.pyplot(fig2)
