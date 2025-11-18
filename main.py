from classes_flatemates import FlateMate, Bill
from class_pdf_contents import PdfReport

name1 = input("your name")
day_inhouse = float(input("days_in_house"))
marry = FlateMate(name1, day_inhouse)
name2 = input("roomate name ")
day_inhouse2 = float(input("days_in_house"))
john = FlateMate(name2, day_inhouse2)

amount = float(input("amount"))
periode = input("the periode")
bill = Bill(amount, periode)

repport = PdfReport()

repport.generate(marry, john, bill)