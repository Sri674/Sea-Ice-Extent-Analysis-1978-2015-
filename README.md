 # Sea Ice Extent Analysis (1978–2015)

## Project Overview

This project analyzes historical sea ice extent data from the National Snow and Ice Data Center (NSIDC), focusing on understanding long-term trends and seasonal patterns of sea ice in both the Arctic and Antarctic regions from 1978 to 2015. The analysis includes data cleaning, exploratory data analysis (EDA), and the development of an interactive web dashboard using **Streamlit** to visualize the trends.

### Tools & Technologies Used:
- Python
- Pandas
- Streamlit
- Matplotlib / Plotly (for data visualization)

## Dataset Overview

The dataset is sourced from the **National Snow and Ice Data Center (NSIDC)**, covering the years **1978–2015**. The dataset includes the following variables:

- **Year**: Year of the data point.
- **Month**: Month of the data point.
- **Day**: Day of the data point.
- **Extent**: Sea ice extent in million square kilometers.
- **Hemisphere**: Arctic or Antarctic.
- **Missing**: Data quality indicator (removed during cleaning).
- **Source**: Data collection method (removed during cleaning).

### Final Cleaned Dataset Columns:
- **Date**: Combined from Year, Month, and Day.
- **Extent**: Sea ice extent (in million sq. km).
- **Hemisphere**: Arctic or Antarctic region.

## Data Cleaning Process

The data cleaning process involved:
1. Combining the **Year**, **Month**, and **Day** columns to create a new **Date** column.
2. Removing irrelevant columns such as **Source** and **Missing**.
3. Keeping only the necessary columns: **Date**, **Extent**, and **Hemisphere**.
4. Extracting the **Year** and **Month** from the **Date** column for grouped analysis.
5. Saving the cleaned dataset as `df_s.csv` for use in the Streamlit application.

## Exploratory Data Analysis (EDA)

1. **Yearly Trend Analysis**:
   - The Arctic region shows a declining trend in sea ice extent from 1978 to 2015.
   - The Antarctic region shows fluctuations but no consistent upward trend.
  
2. **Monthly Seasonality Analysis**:
   - The Arctic shows maximum sea ice around **March** and minimum around **September**.
   - The Antarctic shows maximum sea ice around **September** and minimum around **February**.

## Streamlit Dashboard

The **Streamlit** dashboard allows for interactive exploration of the sea ice extent data:
- **Hemisphere Selection**: Select either the Arctic or Antarctic region to view the data.
- **Yearly Trend Visualization**: A line chart that shows average sea ice extent per year based on the selected hemisphere.
- **Monthly Seasonality Chart**: A line chart that displays seasonal variations in sea ice extent across months.
- **Raw Data Display**: A table showing the filtered dataset for further exploration.

### Benefits:
- Provides an interactive and visual tool for exploring climate change trends.
- Makes the analysis accessible to non-technical users.
- Helps in comparing sea ice trends between the Arctic and Antarctic regions.
