# 📊 Financial Ratio Analysis using Python

This project showcases how to analyze financial ratios from company data using Python and create predictions using Machine Learning. The interactive dashboard allows users to upload their Excel data and view visual insights and future trends of selected financial ratios.

---

## 🚀 Features

- Upload your own Excel file (`.xlsx`)
- View key financial ratios like:
  - Current Ratio
  - Gross Profit Ratio
  - Net Profit Ratio
  - and more...
- Visualize data with bar charts
- Predict future values (next 5 years) using Linear Regression
- Interactive interface built using **Matplotlib**

---

## 📁 Sample Excel File Format

| Year | Current Ratio | Gross Profit Ratio | Net Profit Ratio |
|------|----------------|--------------------|------------------|
| 2020 | 1.8            | 55.2               | 12.1             |
| 2021 | 2.0            | 56.1               | 13.5             |

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- FastAPI
- Uvicorn
- Scikit-learn
- Jinja2

---

## 🖥️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Financial-Ratio-Analysis.git
   cd Financial-Ratio-Analysis
2. Create a virtual environment:
  ```
    python -m venv venv
  ```
3. Install requirements:
  ```
    pip install -r requirements.txt
  ```
4. Run the app:
  ```
    uvicorn main:app --reload
  ```
