import streamlit as st 
from function.handling_missing_value import handling_missing_value
from function.handle_categorical_variables import handling_categorical_values
from function.explore_dataset import explore_datasets 
# from function.fn import *
import io
from config import get_data, get_cleaned_data

missing_value_technique = None
missing_value_summary = None

def perform_eda(data):
    st.subheader("Exploratory Data Analysis 📊")

    # Show data summary
    st.write("Data Summary:")
    st.dataframe(data.describe())

    # Show data info
    st.write("Data Info:")
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

data = get_data()
cleaned_data = get_cleaned_data()

def fe():
    with st.container():
        st.title("Feature Engineering")
        sidebar = st.selectbox("", ["Explore Dataset", "Handle Missing Values 🧩", "Handle Categorical Variables 🧩", "Scale Down-Data 📏"])
        
        if sidebar == "Handle Missing Values 🧩":
            # Assign initial values to the variables here
            # missing_value_technique = "Some Technique"  # Assign your technique
            # missing_value_summary = "Summary"  # Assign your summary
            missing_value_technique = None
            missing_value_summary = None
            handling_missing_value(data,cleaned_data)

        elif sidebar == "Handle Categorical Variables 🧩":
            handling_categorical_values(data, cleaned_data)

        elif sidebar == "Scale Down-Data 📏":
            # Handle scaling here
            pass
        
        elif sidebar == "Explore Dataset":
            explore_datasets(data, cleaned_data)

if __name__ == "__main__":
    fe()
