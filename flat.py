class Bill:
    """
    Object that contains data about a bill, like total amount and the period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = float(amount)
        self.period = period


class Flatmate:
    """
    Object that contains data about a flatmate(roommate)
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = int(days_in_house)

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 2) # The bill divided by weight rounded to two decimal places
