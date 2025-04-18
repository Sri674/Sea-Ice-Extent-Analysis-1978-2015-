import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Set Seaborn style
sns.set(style="whitegrid") 

# Title
st.title("🌍 Sea Ice Extent Dashboard (1978–2015)")

# Load the cleaned dataset
df = pd.read_csv("H:\CarDekho_session\env\Scripts\df_s.csv") 
df['Date'] = pd.to_datetime(df['Date'])

# Extract year and month for analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Sidebar filters
hemispheres = df['hemisphere'].unique()
selected_hemisphere = st.sidebar.selectbox("Select Hemisphere", hemispheres)

# Filter by hemisphere
filtered_df = df[df['hemisphere'] == selected_hemisphere]

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["📉 Yearly Trends", "📆 Monthly Seasonality", "📄 Raw Data"])

with tab1:
    st.subheader(f"Average Yearly Sea Ice Extent - {selected_hemisphere.capitalize()}")
    yearly = filtered_df.groupby('Year')['Extent'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=yearly, x='Year', y='Extent', ax=ax)
    ax.set_title("Average Sea Ice Extent by Year")
    ax.set_ylabel("Extent (Million sq. km)")
    ax.grid(True)
    st.pyplot(fig)

with tab2:
    st.subheader(f"Seasonality - Average Monthly Sea Ice Extent - {selected_hemisphere.capitalize()}")
    monthly_avg = filtered_df.groupby('Month')['Extent'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=monthly_avg, x='Month', y='Extent', ax=ax)
    ax.set_title("Seasonal Pattern (Monthly Averages)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Extent (Million sq. km)")
    ax.set_xticks(range(1, 13))
    ax.grid(True)
    st.pyplot(fig)

with tab3:
    st.subheader("📄 View Raw Data")
    st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.markdown("🔬 Built with Streamlit | 🌡️ Data from NSIDC")
