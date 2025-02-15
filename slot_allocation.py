import pandas as pd
import random
from datetime import datetime, timedelta
import streamlit as st
import os
import time
from pyngrok import ngrok
import requests

def install_requirements():
    if "google.colab" in os.sys.modules:
        os.system("pip install streamlit pyngrok pandas")

def start_ngrok():
    if "google.colab" in os.sys.modules:
        print("Starting Streamlit...")
        os.system("nohup streamlit run slot_allocation.py &")

        timeout = 30  # Set timeout in seconds
        elapsed_time = 0
        time.sleep(5)  # Initial delay before checking
        while elapsed_time < timeout:
            try:
                response = requests.get("http://localhost:8501")
                if response.status_code == 200:
                    break
            except requests.exceptions.RequestException:
                pass
            time.sleep(2)
            elapsed_time += 2
        
        if elapsed_time >= timeout:
            print("⚠ Streamlit did not start within the expected time.")
        else:
            print("Starting ngrok...")
            public_url = ngrok.connect(8501).public_url
            print(f"Public URL: {public_url}")

st.title("Airport Slot Allocation DSS")

if st.button("Run Slot Allocation"):
    st.write("Processing slot allocation...")
