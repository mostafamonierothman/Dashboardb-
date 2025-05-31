# app.py
import streamlit as st
import pandas as pd
from datetime import datetime

# Initial data
data = [
    ["MedJourney+ SEO & Legal Updates", "SEO, GDPR, TOS updates", "In Progress", "High", "2025-05-30", "Implement revised Privacy Policy", ""],
    ["Sweden Health Equity Dashboard", "R Shiny dashboard", "In Progress", "High", "2025-05-15", "Finalize API integration", ""],
    ["Sweden Crime Dashboard", "Interactive crime trends dashboard", "In Progress", "High", "2025-05-21", "Replace with SCB API data", ""],
    ["LinkedIn Optimization", "Profile SEO & content", "In Progress", "Medium", "2025-05-14", "Finalize content plan", ""],
    ["Medical Tourism Global SEO", "New markets", "Not Started", "High", "", "Define target markets", ""],
    ["Shopify Store - Máha Atelier", "Custom Shopify store", "In Progress", "Low", "2025-05-13", "Implement background image", ""],
    ["AI Billionaire Project", "Scalable AI business", "Brainstorming", "High", "2025-05-31", "Finalize action plan", ""],
    ["RA Jobs Monitoring", "Research assistant jobs Sweden", "In Progress", "Medium", "2025-05-12", "Setup auto email alerts", ""],
    ["MedJourney+ Affiliate Program", "Recruit ambassadors", "In Progress", "Medium", "2025-05-25", "Launch LinkedIn ad", ""],
]

columns = ["Project Name", "Description", "Status", "Priority", "Last Updated", "Next Action", "Notes"]

# Create dataframe
df = pd.DataFrame(data, columns=columns)

# Sidebar filters
st.sidebar.title("Filters")
status_filter = st.sidebar.multiselect("Filter by Status", options=df["Status"].unique(), default=df["Status"].unique())
priority_filter = st.sidebar.multiselect("Filter by Priority", options=df["Priority"].unique(), default=df["Priority"].unique())

# Filter dataframe
filtered_df = df[df["Status"].isin(status_filter) & df["Priority"].isin(priority_filter)]

# Main dashboard
st.title("🚀 Next Richest Man - Project Dashboard")
st.write(f"**Total Projects:** {len(filtered_df)}")

# Progress visualization
status_counts = filtered_df["Status"].value_counts()
st.subheader("📊 Project Status Overview")
for status, count in status_counts.items():
    st.write(f"{status}: {count} project(s)")
    st.progress(min(count / len(filtered_df), 1.0))

# Display table
st.subheader("📋 Project List")
