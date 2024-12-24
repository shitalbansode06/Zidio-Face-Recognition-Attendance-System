import streamlit as st
import pandas as pd
import time 
from datetime import datetime

import win32com.client
from win32com.client import Dispatch
import pandas as pd
from datetime import datetime

# Get the current date in the required format
date = datetime.today().strftime('%d-%m-%Y')

# Correct the file path construction
file_path = f"data/attendance_csv{date}.csv"

# Now try to read the file
try:
    df = pd.read_csv(file_path)
    print(df)
except FileNotFoundError:
    print(f"File not found: {file_path}")

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")
# Assuming 'date' contains '22-10-2024', your current code may look like this:
# df = pd.read_csv("data\\Attendance_22-10-2024.csv" + date + ".csv")

# Fix: Correct the file name to avoid duplication of 'date'
# df = pd.read_csv(f"Attendance_{date}.csv")


df = pd.read_csv("data/attendance.csv22-10-2024.csv22-10-202422-10-202422-10-202422-10-2024.csv")


st.dataframe(df.style.highlight_max(axis=0))