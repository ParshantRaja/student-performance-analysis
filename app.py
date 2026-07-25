import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Analysis & Prediction Dashboard")

# Cache the data loading to improve performance
@st.cache_data
def load_data():
    d1 = pd.read_csv("student-mat.csv", sep=";")
    d2 = pd.read_csv("student-por.csv", sep=";")

    merge_cols = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]
    d3 = pd.merge(d1, d2, on=merge_cols)
    return d1, d2, d3

try:
    d1, d2, d3 = load_data()
    
    # Sidebar Navigation for Dashboard options
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose Section", ["Data Overview & Merged Data", "Student Performance Prediction"])
    
    if app_mode == "Data Overview & Merged Data":
        st.write("### Data Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Math Students", len(d1))
        col2.metric("Portuguese Students", len(d2))
        col3.metric("Students in Both", len(d3))
        
        st.write("### Merged Dataset")
        st.write("Below is the preview of the students who are enrolled in both Math and Portuguese courses:")
        st.dataframe(d3)
        
    elif app_mode == "Student Performance Prediction":
        st.write("### 🔮 Student Final Grade & Pass/Fail Prediction")
        st.write("Enter student details to predict performance:")
        
        with st.form("prediction_form"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                age = st.slider("Age", 15, 22, 17)
                studytime = st.selectbox("Weekly Study Time (1:<2h, 2:2-5h, 3:5-10h, 4:>10h)", [1, 2, 3, 4], index=1)
                failures = st.selectbox("Past Class Failures", [0, 1, 2, 3], index=0)
                
            with col2:
                G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
                G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)
                absences = st.slider("Absences", 0, 93, 4)
                
            with col3:
                schoolsup = st.selectbox("Extra Educational Support (schoolsup)", ["yes", "no"])
                higher = st.selectbox("Wants Higher Education (higher)", ["yes", "no"])
                internet = st.selectbox("Internet Access at Home", ["yes", "no"])
                
            submit_button = st.form_submit_button(label="Predict")
            
        if submit_button:
            # Calculation logic based on grades and study parameters
            predicted_score = (G1 * 0.3) + (G2 * 0.5) + (2 if higher == "yes" else 0) - (failures * 1.5)
            predicted_score = max(0, min(20, round(predicted_score, 1)))
            
            st.markdown("---")
            st.subheader("🎯 Prediction Result")
            res_col1, res_col2 = st.columns(2)
            res_col1.metric("Estimated Final Grade (G3)", f"{predicted_score} / 20")
            
            if predicted_score >= 10:
                res_col2.success("Status: **PASS** 🎉")
            else:
                res_col2.error("Status: **FAIL** ⚠️")

except Exception as e:
    st.error(f"Error loading data: {e}")