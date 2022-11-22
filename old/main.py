from flat import Bill, Flatmate
from report import PdfReport

class HomePage




# amount = float(input("Hey user, enter the bill amount: "))
# period = input("What is the bill period? E.g. December 2022: ")
#
# name1 = input("What is your name? ")
# days_in_house1 = int(input("How many days did {} stay in the house?: ".format(name1)))
#
# name2 = input("What is your flatmate's name? ")
# days_in_house2 = int(input("How many days did {} stay in the house?: ".format(name2)))
#
# the_bill = Bill(amount, period)
# flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
# flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)
#
# print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
# print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))
#
# pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
# pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)