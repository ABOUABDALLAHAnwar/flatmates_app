import webbrowser

from fpdf import FPDF

class Bill:

    def __init__(self, amount: float, periode: str):
        """
        object that contains data about the bill
        Parameters
        ----------
        amount :
        periode :
        """
        self.amount = amount
        self.periode = periode


class FlateMate:

    def __init__(self, name: str, days_in_house:float):
        """
        class to identifie personne who live in the same house and shae the bill
        Parameters
        ----------
        name :
        days_in_house :
        """
        self.name, self.days_in_house = name, days_in_house

    def pays(self, the_bill : Bill, other_flate_mate): #, others_flatemate_days_inhous : float
        return (the_bill.amount * self.days_in_house)/ (self.days_in_house + other_flate_mate.days_in_house)



