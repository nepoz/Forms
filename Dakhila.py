from tkinter import *
from FormUtils import clear_form_button, submit_form_button


class DakhilaForm:

    def __init__(self, main):
        self.window = main

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
        self.lblDate = Label(self.window, text="मिति:", font = ("Ganesh",12))
        self.lblDate.place(x=10, y = 150)
        self.txtDate = Entry(self.window, width=25, name="miti1")
        self.txtDate.place(x=160, y=150)

        self.lblM = Label(self.window, text="मिसिल नं. :", font = ("Ganesh",12))
        self.lblM.place(x=10, y = 180)
        self.txtM = Entry(self.window, width=25, name="misil")
        self.txtM.place(x = 160, y=180)

        self.lbl1 = Label(self.window, text="बादी/धनी म/हामी: ", font =("Ganesh",12))
        self.lbl1.place(x=10, y=210)
        self.txt1 = Entry(self.window, width=25, name="hami")
        self.txt1.place(x = 160, y=210)

        self.lbl2 = Label(self.window, text="ऋणी / प्रतिबादी: ", font =("Ganesh",12))
        self.lbl2.place(x=10, y=240)
        self.txt2 = Entry(self.window, width=25, name="pratibadi")
        self.txt2.place(x=160, y=240)

        self.lbl3 = Label(self.window, text="र.नं. / चलान पुर्जी नं.", font =("Ganesh",12))
        self.lbl3.place(x=10, y=270)
        self.txt3 = Entry(self.window, width=25, name="chalan")
        self.txt3.place(x=160, y=270)

        self.lbl4 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl4.place(x=550, y=150)
        self.txt4 = Entry(self.window, width=25, name="miti2")
        self.txt4.place(x=650, y=150)

        self.lbl5 = Label(self.window, text="मा.पो.का: ", font = ("Ganesh",12))
        self.lbl5.place(x=550, y = 180)
        self.txt5 = Entry(self.window, width=25, name="ma")
        self.txt5.place(x = 650, y=180)

        self.lbl6 = Label(self.window, text="द.नं: ", font =("Ganesh",12))
        self.lbl6.place(x=550, y=210)
        self.txt6 = Entry(self.window, width=25, name="darta")
        self.txt6.place(x = 650, y=210)

        self.lbl7 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl7.place(x=550, y=240)
        self.txt7 = Entry(self.window, width=25, name="miti3")
        self.txt7.place(x=650, y=240)

        self.lb8 = Label(self.window, text="निवेदकको नाम, थर, वतन: ", font =("Ganesh",12))
        self.lb8.place(x=10, y=300)
        self.txt8 = Entry(self.window, width=25, name="naam")
        self.txt8.place(x=230, y=300)

        self.lbl9 = Label(self.window, text="कैफियत: ", font =("Ganesh",12))
        self.lbl9.place(x=10, y=360)
        self.txt9 = Entry(self.window, width=25, name="faikiyat")
        self.txt9.place(x=160, y=360)

        self.lbl10 = Label(self.window, text="पति/पिता: ", font =("Ganesh",12))
        self.lbl10.place(x=550, y=270)
        self.txt10= Entry(self.window, width=25, name="pita")
        self.txt10.place(x = 650, y=270)

        self.lbl11= Label(self.window, text="बाजे: ", font =("Ganesh",12))
        self.lbl11.place(x=550, y=300)
        self.txt11 = Entry(self.window, width=25, name="baaje")
        self.txt11.place(x=650, y=300)

        self.lbl12 = Label(self.window, text="ऋणी / प्रतिबादीको नाम, थर, वतन: ", font =("Ganesh",12))
        self.lbl12.place(x=10, y=330)
        self.txt12 = Entry(self.window, width=25, name="rindi_naam")
        self.txt12.place(x=230, y=330)

        self.lbl13 = Label(self.window, text="गा.वि.स: ", font =("Ganesh",12))
        self.lbl13.place(x=10, y=390)
        self.txt13 = Entry(self.window, width=25, name="gawisa")
        self.txt13.place(x=230, y=390)

        self.lbl14 = Label(self.window, text="वा.नं.: ", font =("Ganesh",12))
        self.lbl14.place(x=10, y=420)
        self.txt14 = Entry(self.window, width=25, name="wana")
        self.txt14.place(x=230, y=420)

        self.lbl15 = Label(self.window, text="कि.नं.: ", font =("Ganesh",12))
        self.lbl15.place(x=10, y=450)
        self.txt15 = Entry(self.window, width=25, name="kina")
        self.txt15.place(x=230, y=450)

        self.lbl16 = Label(self.window, text="तर्फ: ", font =("Ganesh",12))
        self.lbl16.place(x=10, y=480)
        self.txt16 = Entry(self.window, width=25, name="tarfa")
        self.txt16.place(x=230, y=480)

        self.lbl17= Label(self.window, text="कि. नं.: ", font =("Ganesh",12))
        self.lbl17.place(x=550, y=330)
        self.txt17 = Entry(self.window, width=25, name="kina2")
        self.txt17.place(x=650, y=330)

        self.lbl18= Label(self.window, text="क्षेत्रफल: ", font =("Ganesh",12))
        self.lbl18.place(x=550, y=360)
        self.txt18 = Entry(self.window, width=25, name="chhetrafal")
        self.txt18.place(x=650, y=360)

        self.lbl19= Label(self.window, text="तर्फ: ", font =("Ganesh",12))
        self.lbl19.place(x=550, y=390)
        self.txt19 = Entry(self.window, width=25, name="tarfa2")
        self.txt19.place(x=650, y=390)

        self.lbl20= Label(self.window, text="कि. नं.: ", font =("Ganesh",12))
        self.lbl20.place(x=550, y=420)
        self.txt20 = Entry(self.window, width=25, name="kina3")
        self.txt20.place(x=650, y=420)

        self.lbl21= Label(self.window, text="क्षेत्रफल: ", font =("Ganesh",12))
        self.lbl21.place(x=550, y=450)
        self.txt21 = Entry(self.window, width=25, name="chhetrafal2")
        self.txt21.place(x=650, y=450)

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
            self.txt18, 
            self.txt19, 
            self.txt20, 
            self.txt21
        ]

        ## ------------ BUTTONS --------------

        ## Will clear all the text boxes.
        clear_form_button(self.window, self.entry_fields).place(x=650, y=480)        ## I leave it to you to decide where the actual placement of this button should be

        ## Will render completed html form and open it in default web browser, new tab
        submit_form_button(self.window, self.entry_fields, 'Dakhila.html').place(x=700, y=480)