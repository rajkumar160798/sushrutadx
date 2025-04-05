
from fpdf import FPDF

def generate_pdf_report(patient_data, prediction, probability, shap_impact, output_path="sushruta_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "SushrutaDx Diabetes Risk Report", ln=True, align='C')
    
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}", ln=True)
    pdf.cell(0, 10, f"Confidence: {round(probability * 100, 2)}%", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Patient Input Features:", ln=True)
    pdf.set_font("Arial", '', 12)
    for key, val in patient_data.items():
        pdf.cell(0, 10, f"{key}: {val}", ln=True)
    
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Top Influencing Factors (via SHAP):", ln=True)
    pdf.set_font("Arial", '', 12)
    for feature, impact in shap_impact[:5]:  # Top 5
        pdf.cell(0, 10, f"{feature}: {round(impact, 4)}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'I', 11)
    pdf.multi_cell(0, 10, "Disclaimer: This is a predictive risk estimation tool. It does not constitute a medical diagnosis. Please consult a physician for further testing.")

    pdf.output(output_path)
    print(f"PDF generated: {output_path}")

