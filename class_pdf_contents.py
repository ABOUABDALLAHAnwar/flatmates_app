from fpdf import FPDF
import webbrowser
from classes_flatemates import FlateMate, Bill

class PdfReport:

    def generate(self, flatemate1 : FlateMate, flatemate2 : FlateMate, the_bill : Bill):
        """

        Parameters
        ----------
        flatemate1 :
        flatemate2 :
        the_bill :

        Returns
        -------

        """
        flatemate1_pays = flatemate1.pays(the_bill, flatemate2)
        flatemate2_pays = flatemate2.pays(the_bill, flatemate1)

        pdf = FPDF(orientation="P", unit="pt", format='A4')
        pdf.add_page()
        pdf.image("ressources/Capture du 2025-01-28 18-39-31.png", w=30, h=30)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, text="Flatemates Bill", border=0, align="C", ln=1)
        pdf.cell(w=100, h=40, text="Periode ", border=0)
        pdf.cell(w=300, h=40, text=the_bill.periode , border=0, ln=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=20, text=flatemate1.name, border=0)
        pdf.cell(w=100, h=20, text=str(round(flatemate1_pays, 2)), border=0, ln=1)
        pdf.cell(w=100, h=20, text=flatemate2.name, border=0)
        pdf.cell(w=100, h=20, text=str(round(flatemate2_pays, 2)), border=0, ln=1)

        filename = "ressources/" + the_bill.periode.replace(" ", "_") + ".pdf"
        pdf.output(filename)
        webbrowser.open(filename)


