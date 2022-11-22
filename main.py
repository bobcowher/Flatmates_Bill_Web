import os.path

from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

import flat
from flat import Bill, Flatmate
import webbrowser


app = Flask(__name__)



class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(billform.amount.data, billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, billform.days_in_house1.data)
        flatmate2 = flat.Flatmate(billform.name2.data, billform.days_in_house2.data)

        return render_template('bill_form_page.html',
                               result=True,
                               billform=billform,
                               name1=flatmate1.name,
                               name2=flatmate2.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               amount2=flatmate2.pays(the_bill, flatmate1))

# class ResultsPage(MethodView):
#
#     def post(self):
#         billform = BillForm(request.form)
#
#         the_bill = flat.Bill(billform.amount.data, billform.period.data)
#         flatmate1 = flat.Flatmate(billform.name1.data, billform.days_in_house1.data)
#         flatmate2 = flat.Flatmate(billform.name2.data, billform.days_in_house2.data)
#
#         return render_template('results.html', name1=flatmate1.name,
#                                                name2=flatmate2.name,
#                                                amount1=flatmate1.pays(the_bill, flatmate2),
#                                                amount2=flatmate2.pays(the_bill, flatmate1))

class BillForm(Form):
    amount = StringField('Bill Amount: ', default="100")
    period = StringField('Bill Period: ', default="December 2021")

    name1 = StringField("Name: ", default="Robert")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Mary")
    days_in_house2 = StringField("Days in the house: ", default=30)

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)



