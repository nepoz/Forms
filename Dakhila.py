from tkinter import *
from FormUtils import clear_form_button, submit_form_button
 
window = Tk()
window.geometry('850x600')
 
window.title("दाखिल")

##start of header section
header = Label(window, text= "नेपाल सरकार", font=("bold",15))
header.place(x=400, y=10)
header2 = Label(window, text="भूमि व्यवस्था सरकारी तथा गरिवी निवारण मन्‍न्नालय", font=("bold",15))
header2.place(x= 270, y=35)
header3 = Label(window, text="भूमि व्यवस्थापन तथा अभिलेख विभाग", font=("bold",15))
header3.place(x= 330, y=60)
header4 = Label(window, text="मालपोत कार्यालय", font=("bold",15))
header4.place(x= 390, y=85)
header5 = Label(window, text="साँखु (काठमाण्डौ)", font=("bold",15))
header5.place(x= 390, y=110)
print ("\n")
print ("\n")
##end of header section

##labels and textboxes
lblDate = Label(window, text="मिति:", font = ("Ganesh",12))
lblDate.place(x=10, y = 150)
txtDate = Entry(window, width=25, name="miti1")
txtDate.place(x=160, y=150)

lblM = Label(window, text="मिसिल नं. :", font = ("Ganesh",12))
lblM.place(x=10, y = 180)
txtM = Entry(window, width=25, name="misil")
txtM.place(x = 160, y=180)

lbl1 = Label(window, text="बादी/धनी म/हामी: ", font =("Ganesh",12))
lbl1.place(x=10, y=210)
txt1 = Entry(window, width=25, name="hami")
txt1.place(x = 160, y=210)

lbl2 = Label(window, text="ऋणी / प्रतिबादी: ", font =("Ganesh",12))
lbl2.place(x=10, y=240)
txt2 = Entry(window, width=25, name="pratibadi")
txt2.place(x=160, y=240)

lbl3 = Label(window, text="र.नं. / चलान पुर्जी नं.", font =("Ganesh",12))
lbl3.place(x=10, y=270)
txt3 = Entry(window, width=25, name="chalan")
txt3.place(x=160, y=270)

lbl4 = Label(window, text="मिति: ", font =("Ganesh",12))
lbl4.place(x=550, y=150)
txt4 = Entry(window, width=25, name="miti2")
txt4.place(x=650, y=150)

lbl5 = Label(window, text="मा.पो.का: ", font = ("Ganesh",12))
lbl5.place(x=550, y = 180)
txt5 = Entry(window, width=25, name="ma")
txt5.place(x = 650, y=180)

lbl6 = Label(window, text="द.नं: ", font =("Ganesh",12))
lbl6.place(x=550, y=210)
txt6 = Entry(window, width=25, name="darta")
txt6.place(x = 650, y=210)

lbl7 = Label(window, text="मिति: ", font =("Ganesh",12))
lbl7.place(x=550, y=240)
txt7 = Entry(window, width=25, name="miti3")
txt7.place(x=650, y=240)

lb8 = Label(window, text="निवेदकको नाम, थर, वतन: ", font =("Ganesh",12))
lb8.place(x=10, y=300)
txt8 = Entry(window, width=25, name="naam")
txt8.place(x=230, y=300)

lbl9 = Label(window, text="कैफियत: ", font =("Ganesh",12))
lbl9.place(x=10, y=360)
txt9 = Entry(window, width=25, name="faikiyat")
txt9.place(x=160, y=360)

lbl10 = Label(window, text="पति/पिता: ", font =("Ganesh",12))
lbl10.place(x=550, y=270)
txt10= Entry(window, width=25, name="pita")
txt10.place(x = 650, y=270)

lbl11= Label(window, text="बाजे: ", font =("Ganesh",12))
lbl11.place(x=550, y=300)
txt11 = Entry(window, width=25, name="baaje")
txt11.place(x=650, y=300)

lbl12 = Label(window, text="ऋणी / प्रतिबादीको नाम, थर, वतन: ", font =("Ganesh",12))
lbl12.place(x=10, y=330)
txt12 = Entry(window, width=25, name="rindi_naam")
txt12.place(x=230, y=330)

lbl13 = Label(window, text="गा.वि.स: ", font =("Ganesh",12))
lbl13.place(x=10, y=390)
txt13 = Entry(window, width=25, name="gawisa")
txt13.place(x=230, y=390)

lbl14 = Label(window, text="वा.नं.: ", font =("Ganesh",12))
lbl14.place(x=10, y=420)
txt14 = Entry(window, width=25, name="wana")
txt14.place(x=230, y=420)

lbl15 = Label(window, text="कि.नं.: ", font =("Ganesh",12))
lbl15.place(x=10, y=450)
txt15 = Entry(window, width=25, name="kina")
txt15.place(x=230, y=450)

lbl16 = Label(window, text="तर्फ: ", font =("Ganesh",12))
lbl16.place(x=10, y=480)
txt16 = Entry(window, width=25, name="tarfa")
txt16.place(x=230, y=480)

lbl17= Label(window, text="कि. नं.: ", font =("Ganesh",12))
lbl17.place(x=550, y=330)
txt17 = Entry(window, width=25, name="kina2")
txt17.place(x=650, y=330)

lbl18= Label(window, text="क्षेत्रफल: ", font =("Ganesh",12))
lbl18.place(x=550, y=360)
txt18 = Entry(window, width=25, name="chhetrafal")
txt18.place(x=650, y=360)

lbl19= Label(window, text="तर्फ: ", font =("Ganesh",12))
lbl19.place(x=550, y=390)
txt19 = Entry(window, width=25, name="tarfa2")
txt19.place(x=650, y=390)

lbl20= Label(window, text="कि. नं.: ", font =("Ganesh",12))
lbl20.place(x=550, y=420)
txt20 = Entry(window, width=25, name="kina3")
txt20.place(x=650, y=420)

lbl21= Label(window, text="क्षेत्रफल: ", font =("Ganesh",12))
lbl21.place(x=550, y=450)
txt21 = Entry(window, width=25, name="chhetrafal2")
txt21.place(x=650, y=450)

##end of labels and textboxes

## List of all Entry widgets 
## Will be supplied as parameter to helper functions clearing contents of form // submitting data
entry_fields = [
    txtDate, txtM, txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9, txt10, txt11, txt12,
    txt13, txt14, txt15, txt16, txt17, txt18, txt19, txt20, txt21
]

## ------------ BUTTONS --------------

## Will clear all the text boxes.
clear_form_button(window, entry_fields).place(x=650, y=480)        ## I leave it to you to decide where the actual placement of this button should be

## Will render completed html form and open it in default web browser, new tab
submit_form_button(window, entry_fields, 'Dakhila.html').place(x=650, y=500)

window.mainloop()    ##for the window to wait for any interaction from the user. otherwise the window won't appear to the user.












