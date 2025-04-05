import streamlit as st
import pandas as pd
import pickle
import shap
import os
import matplotlib.pyplot as plt
from report_generator import generate_pdf_report

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Set up SHAP explainer once
explainer = shap.TreeExplainer(model)

# Title and Logo
st.image("assets/sushrutadx_logo.png", width=150)
st.title("SushrutaDx - Diabetes Risk Predictor")

# Upload input data
uploaded_file = st.file_uploader("Upload patient data (CSV with 1 row only):", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if len(df) != 1:
        st.error("Please upload a file with exactly 1 row (1 patient).")
    else:
        st.write("🧾 Patient Input:")
        st.dataframe(df)

        # Prediction
        prediction = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]
        st.markdown(f"### Prediction: {'🟥 Diabetic' if prediction == 1 else '🟩 Non-Diabetic'}")
        st.markdown(f"**Confidence:** {round(prob * 100, 2)}%")

        # SHAP values
        shap_explanation = explainer(df)
        shap_contrib_flat = shap_explanation.values[0]
        # Ensure values are flat floats
        flat_values = [float(val) for val in shap_contrib_flat.ravel()]
        feature_impacts = list(zip(df.columns, flat_values))
        feature_impacts_sorted = sorted(feature_impacts, key=lambda x: abs(x[1]), reverse=True)
        # Display SHAP values
        st.subheader("SHAP Values")
        st.write("The following features contributed to the prediction:")
        st.write(pd.DataFrame(feature_impacts, columns=["Feature", "SHAP Value"]))

        # PDF Report
        output_path = "sushruta_report.pdf"
        generate_pdf_report(df.iloc[0].to_dict(), prediction, prob, feature_impacts_sorted, output_path)
        with open(output_path, "rb") as f:
            st.download_button("📄 Download PDF Report", f, file_name="SushrutaDx_Report.pdf")
        os.remove(output_path)

        # SHAP Bar Chart
        st.subheader("Top Feature Impact (Bar Chart)")
        bar_df = pd.DataFrame(feature_impacts_sorted[:5], columns=["Feature", "SHAP Value"]).set_index("Feature")
        st.bar_chart(bar_df)

        # SHAP Summary Plot
        # SHAP Summary Plot (Custom for 1 row)
        st.subheader("SHAP Summary Plot (Single Patient)")
        fig_summary, ax = plt.subplots(figsize=(8, 4))
        ax.barh([x[0] for x in feature_impacts_sorted[:5]], [x[1] for x in feature_impacts_sorted[:5]])
        ax.set_xlabel("SHAP Value")
        ax.set_title("Top 5 Feature Impacts")
        plt.tight_layout()
        st.pyplot(fig_summary)


        st.success("✅ Report and SHAP visualizations generated successfully!")
