# 🎓 Student Performance Analysis & Prediction Dashboard

An interactive data analysis and prediction application built with **Streamlit**, designed to explore student academic performance and estimate final outcomes based on academic, demographic, and social attributes.

---

## 📌 Overview

This dashboard allows users to analyze student records, explore performance patterns, and predict student outcomes through a simple, easy-to-use interface. It uses the **UCI Student Performance Dataset**, which contains academic, demographic, social, and school-related information from Portuguese secondary schools.

---

## 🧠 How It Works

1. **Data Collection** — Loads the Student Performance Dataset (Math and Portuguese course records).
2. **Data Integration** — Merges `student-mat.csv` and `student-por.csv` into a single structured dataset.
3. **Data Analysis** — Examines key attributes such as age, study time, past failures, and previous grades (G1 & G2).
4. **Performance Prediction** — Takes user input through an interactive form and predicts:
   - Final Grade (G3)
   - Pass/Fail Status

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📊 Interactive Data Overview | Explore student records, statistics, and dataset details |
| 🔗 Dataset Merging | Combines Math and Portuguese datasets into one unified structure |
| 🤖 Performance Prediction | Predicts academic outcomes from user-provided student data |
| 🧭 Simple Interface | Clean Streamlit UI with easy navigation |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **Data Processing:** Pandas
- **Dataset:** UCI Student Performance Dataset

---

## 📂 Dataset Information

| File | Description |
|---|---|
| `student-mat.csv` | Mathematics course performance data |
| `student-por.csv` | Portuguese course performance data |

**Dataset attributes include:**
- Student demographic information (age, family background, etc.)
- Academic grades (G1, G2, G3)
- Study-related attributes (study time, past failures)
- Social and school factors (activities, support, absences)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ParshantRaja/student-performance-analysis.git
cd student-performance-analysis
```

### 2. Install Dependencies
```bash
pip install streamlit pandas
```

### 3. Run the App
```bash
streamlit run app.py
```

### 4. Open in Browser
```
http://localhost:8501
```

---

## 🚀 Usage

1. Run the Streamlit application.
2. Open **Data Overview & Merged Data** to explore dataset insights and statistics.
3. Navigate to **Student Performance Prediction**.
4. Enter student details.
5. Click **Predict**.
6. View the predicted final grade and Pass/Fail result.

---

## 📸 Screenshots

*(Add dashboard screenshots here)*

---

## 🎯 Future Improvements

- Integration of advanced machine learning models
- Additional performance visualization dashboards
- Student risk prediction system
- Cloud deployment support
- Real-time analytics

---

## 📬 Contact

**Parshant Raja**
- GitHub: [ParshantRaja](https://github.com/ParshantRaja)
- Email: parshantraja888@gmail.com

---

⭐ If you like this project, consider giving it a star!
