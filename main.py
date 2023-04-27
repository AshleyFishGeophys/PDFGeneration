from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

# ln is a break line
# h should be the same number as the set_font size
# L in align is left-justified
for idx, row in df.iterrows():
    # for num_pages in row["Pages"]:
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    # RGB. Below produces gray
    # pdf.set_text_color(100, 100, 100)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["topic"], align="L", ln=1, border=1)
    # x1, y1, x2, y2
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")
