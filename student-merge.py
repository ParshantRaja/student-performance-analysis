import pandas as pd

try:
    d1 = pd.read_csv("student-mat.csv", sep=";")
    d2 = pd.read_csv("student-por.csv", sep=";")

    merge_cols = ["school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"]
    d3 = pd.merge(d1, d2, on=merge_cols)
    print(len(d3)) # Should be 382 students
except ImportError:
    print("pandas is not installed. Please install pandas to run this script.")
except Exception as e:
    print(f"An error occurred: {e}")
