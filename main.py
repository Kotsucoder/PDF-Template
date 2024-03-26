from fpdf import FPDF
import pandas as pd

for i in range(2):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    df = pd.read_csv("topics.csv")

    for index, row in df.iterrows():
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)

        pdf.ln(260)

        if i == 1:
            for lines in range(3, 41):
                pdf.line(10, 21 * (lines/3), 200, 21 * (lines/3))

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for pages in range(row["Pages"] - 1):
            pdf.add_page()
            pdf.ln(272)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
            if i == 1:
                for lines in range(3, 41):
                    pdf.line(10, 21 * (lines/3), 200, 21 * (lines/3))
    
    match i:
        case 0:
            pdf.output("output.pdf")
        case 1:
            pdf.output("output_lined.pdf")