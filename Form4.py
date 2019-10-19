from tkinter import *
from FormUtils import submit_form_button, clear_form_button

class Form4:

    def __init__(self, main, option):
        self.window = main
        self.option = option

        ##start of header section
        self.header = Label(self.window, text= "नेपाल सरकार", font=("bold",15))
        self.header.place(x=400, y=10)
        self.header2 = Label(self.window, text="भूमि व्यवस्था सरकारी तथा गरिवी निवारण मन्‍न्नालय", font=("bold",15))
        self.header2.place(x= 270, y=35)
        self.header3 = Label(self.window, text="भूमि व्यवस्थापन तथा अभिलेख विभाग", font=("bold",15))
        self.header3.place(x= 330, y=60)
        self.header4 = Label(self.window, text="मालपोत कार्यालय", font=("bold",15))
        self.header4.place(x= 390, y=85)
        self.header5 = Label(self.window, text="साँखु (काठमाण्डौ)", font=("bold",15))
        self.header5.place(x= 390, y=110)
        ##end of header section

        ##labels and textboxes
        self.lblDate = Label(self.window, text="मिति: ", font = ("Ganesh",12))
        self.lblDate.place(x=10, y = 150)
        self.txtDate = Entry(self.window, width=25, name="miti1")
        self.txtDate.place(x=160, y=150)

        self.lblM = Label(self.window, text="पत्र संख्या: ", font = ("Ganesh",12))
        self.lblM.place(x=10, y = 180)
        self.txtM = Entry(self.window, width=25, name="patra")
        self.txtM.place(x = 160, y=180)

        self.lbl1 = Label(self.window, text="चलानी नं: ", font =("Ganesh",12))
        self.lbl1.place(x=10, y=210)
        self.txt1 = Entry(self.window, width=25, name="chalan")
        self.txt1.place(x = 160, y=210)

        self.lbl2 = Label(self.window, text="जग्गामा ___ गरिपाऊ", font=("Ganesh",12))
        self.lbl2.place(x=10, y=240)
        self.txt2 = Entry(self.window, width=25, name="garipau")
        self.txt2.place(x=180, y=240)

        self.lbl3 = Label(self.window, text="बस्ने: ", font=("Ganesh",12))
        self.lbl3.place(x=10,y=270)
        self.txt3 = Entry(self.window, width=25, name="address")
        self.txt3.place(x=160,y=270)
        
        self.lbl4 = Label(self.window, text="निवेदकको नाम: ", font=("Ganesh",12))
        self.lbl4.place(x=10,y=330)
        self.txt4 = Entry(self.window, width=25, name="niwedak")
        self.txt4.place(x=160,y=330)

        self.lbl5 = Label(self.window, text="द.नं: ", font=("Ganesh",12))
        self.lbl5.place(x=10, y=300)
        self.txt5 = Entry(self.window, width=25, name="darta")
        self.txt5.place(x=160, y=300)

        self.lbl6 = Label(self.window, text="मिति: ", font=("Ganesh",12))
        self.lbl6.place(x=550, y=150)
        self.txt6 = Entry(self.window, width=25, name="miti2")
        self.txt6.place(x=650, y=150)

        self.lbl7 = Label(self.window, text="जग्गा दर्ता नाउ: ", font=("Ganesh",12))
        self.lbl7.place(x=550, y=180)
        self.txt7 = Entry(self.window, width=25, name="naam")
        self.txt7.place(x=650, y=180)

        self.lbl8 = Label(self.window, text="जग्गामा _____ हुने", font=("Ganesh",12))
        self.lbl8.place(x=520, y=210)
        self.txt8 = Entry(self.window, width=25, name="jagga")
        self.txt8.place(x=650, y=210)

        self.lbl9 = Label(self.window, text="असुली रकम: ", font=("Ganesh",12))
        self.lbl9.place(x=550, y=240)
        self.txt9 = Entry(self.window, width=25, name="asuli")
        self.txt9.place(x=650, y=240)

        self.lbl10 = Label(self.window, text="दर्ता वाला: ", font=("Ganesh",12))
        self.lbl10.place(x=550, y=270)
        self.txt10 = Entry(self.window, width=25, name="darta2")
        self.txt10.place(x=650, y=270)

        self.lbl11 = Label(self.window, text="गा.वि.श/न.पा: ", font=("Ganesh",12))
        self.lbl11.place(x=520, y=300)
        self.txt11 = Entry(self.window, width=25, name="gawisa")
        self.txt11.place(x=650, y=300)

        self.lbl12= Label(self.window, text="वडा नं: ", font=("Ganesh",12))
        self.lbl12.place(x=550, y=330)
        self.txt12 = Entry(self.window, width=25, name="wada")
        self.txt12.place(x=650, y=330)

        self.lbl13 = Label(self.window, text="कि.नं: ", font=("Ganesh",12))
        self.lbl13.place(x=550, y=360)
        self.txt13 = Entry(self.window, width=25, name="kina")
        self.txt13.place(x=650, y=360)

        self.lbl14 = Label(self.window, text="क्षेत्रफल: ", font=("Ganesh",12))
        self.lbl14.place(x=520, y=390)
        self.txt14 = Entry(self.window, width=25, name="chhetrafal")
        self.txt14.place(x=650, y=390)

        self.label= Label(self.window,text = "संलग्न प्रमाण: ", font=("Ganesh",13))
        self.label.place(x=10, y=430)

        self.lbl15= Label(self.window, text="वडा नं: ", font=("Ganesh",12))
        self.lbl15.place(x=550, y=460)
        self.txt15 = Entry(self.window, width=25, name="wada2")
        self.txt15.place(x=650, y=460)

        self.lbl16= Label(self.window, text="गा .वि .स / न .पा: ", font=("Ganesh",12))
        self.lbl16.place(x=10, y=460)
        self.txt16 = Entry(self.window, width=25, name="gawisa2")
        self.txt16.place(x=160, y=460)

        self.lbl17= Label(self.window, text="च.नं: ", font=("Ganesh",12))
        self.lbl17.place(x=10, y=490)
        self.txt17 = Entry(self.window, width=25, name="chana")
        self.txt17.place(x=160, y=490)

        self.lbl18= Label(self.window, text="मिति: ", font=("Ganesh",12))
        self.lbl18.place(x=550, y=490)
        self.txt18 = Entry(self.window, width=25, name="miti3")
        self.txt18.place(x=650, y=490)
        ##end of labels and textboxes

        self.entry_fields = [
            self.txtDate, 
            self.txtM, 
            self.txt1, 
            self.txt2, 
            self.txt3,
            self.txt4,  
            self.txt5, 
            self.txt6, 
            self.txt7, 
            self.txt8, 
            self.txt9, 
            self.txt10, 
            self.txt11, 
            self.txt12,
            self.txt13, 
            self.txt14,
            self.txt15, 
            self.txt16, 
            self.txt17, 
            self.txt18
        ]

        
        ## ------------ BUTTONS --------------

        ## Will clear all the text boxes.
        clear_form_button(self.window, self.entry_fields).place(x=650, y=520)
        ## Will render completed html form and open it in default web browser, new tab
        submit_form_button(self.window, self.entry_fields, 'Form4.html', bisaya=self.option).place(x=700, y=520)