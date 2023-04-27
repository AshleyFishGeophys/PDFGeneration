from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=10)

df = pd.read_csv("topics.csv")

# ln is a break line
# h should be the same number as the set_font size
# L in align is left-justified
for idx, row in df.iterrows():
    # Set the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    # RGB. Below produces gray
    pdf.set_text_color(100, 100, 100)
    # RGB. Below produces blue
    # pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # x1, y1, x2, y2
    pdf.line(10, 21, 200, 21)

    # Set the footer
    # Add break lines so that the footer is placed at the bottom of the page
    pdf.ln(265)

    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")


    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(277)

        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

pdf.output("output.pdf")
