#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:58:19 2025

@author: raaz
"""

import streamlit as st
import pandas as pd


# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Razieh Morad"
field = "Physicist"
institution = "University of South Africae"


col1, col2 = st.columns([0.7, 0.3])

with col1:
    # Display basic profile information
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

with col2:
    st.image('image.jpg')

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
#uploaded_file = pd.read_csv("./citations.csv")
#uploaded_file = st.dataframe(uploaded_file)

if uploaded_file:
    #publications = pd.read_csv(uploaded_file)
    publications = uploaded_file
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "rmorad@tlabs.ac.za"
st.write(f"You can reach {name} at {email}.")
