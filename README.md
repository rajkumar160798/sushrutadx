
# SushrutaDx - Diabetes Risk Predictor

![SushrutaDx Logo](assets/sushrutadx_logo.png)

> From Ancient Wisdom to AI Precision 🩺

SushrutaDx is an AI-powered diabetes risk prediction web app inspired by ancient Indian medical wisdom and powered by modern machine learning. It takes key health inputs and provides:

- 📊 A diabetes risk prediction (Diabetic / Non-Diabetic)
- 🔍 SHAP explainability to highlight key factors
- 📝 PDF report generation for clinical sharing
- 📈 Interactive visualizations to explore impact of features

---

## 🚀 Live App

👉 [Click to Launch SushrutaDx](https://sushrutadx.streamlit.app)

---

## 🧪 Tech Stack

- Python 3.10
- Streamlit
- Scikit-Learn (RandomForestClassifier)
- SHAP for Explainability
- FPDF for Report Generation
- Pandas, Matplotlib

---

## ⚙️ How It Works

1. Upload a patient CSV file (single row)
2. The model predicts diabetic risk
3. SHAP shows top features contributing to the decision
4. Visualize + download report

---

## 📁 Run Locally

```bash
git clone https://github.com/rajkumar160798/sushrutadx.git
cd sushrutadx
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 Sample CSV Format

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI | DiabetesPedigreeFunction | Age |
|-------------|---------|----------------|---------------|---------|-----|---------------------------|-----|
| 2           | 120     | 70             | 29            | 180     | 30.5| 0.32                      | 33  |

---

## 📦 Deployment

- Deployed on **Streamlit Cloud** using `requirements.txt`
- Simple, lightweight, fast & secure
- No backend servers required

---

## 👨‍⚕️ Meet the Developer

Hi, I'm Raj – passionate about building explainable and impactful AI tools in healthcare.  
🔗 [LinkedIn](https://www.linkedin.com/in/rajkumar160798) | [Medium](https://medium.com/@myakalarajkumar1998) | [GitHub](https://github.com/rajkumar160798)

---

## 📢 License

MIT License. Use it, fork it, improve it! 💖
