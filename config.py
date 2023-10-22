import streamlit as st

def initialize_data(data):
    st.session_state.shared_data = {
        "data": data
    }



def update_data(data, cleaned_data):
    st.session_state.shared_data["data"] = data
    st.session_state.shared_data["cleaned_data"] = cleaned_data

def get_data():
    return st.session_state.shared_data["data"]

def get_cleaned_data():
    return st.session_state.shared_data["cleaned_data"]
