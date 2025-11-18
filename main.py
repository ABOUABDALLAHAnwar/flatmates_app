from classes_flatemates import FlateMate, Bill
from class_pdf_contents import PdfReport

marry = FlateMate("marry", days_in_house=25)
john = FlateMate("John", days_in_house=20)
bill = Bill(120, "decembre 2022")

repport = PdfReport()

repport.generate(marry, john, bill)