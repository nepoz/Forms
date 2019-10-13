from tkinter import *
 
window = Tk()
window.geometry('850x600')
 
window.title("Form4")

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
##end of header section

##labels and textboxes
lblDate = Label(window, text="मिति: ", font = ("Ganesh",12))
lblDate.place(x=10, y = 150)
txtDate = Entry(window, width=25)
txtDate.place(x=160, y=150)

lblM = Label(window, text="पत्र संख्या: ", font = ("Ganesh",12))
lblM.place(x=10, y = 180)
txtM = Entry(window, width=25)
txtM.place(x = 160, y=180)

lbl1 = Label(window, text="चलानी नं: ", font =("Ganesh",12))
lbl1.place(x=10, y=210)
txt1 = Entry(window, width=25)
txt1.place(x = 160, y=210)

##make space for one label that should have the selected option in the txtbox

lbl3 = Label(window, text="बस्ने: ", font=("Ganesh",12))
lbl3.place(x=10,y=270)
txt3 = Entry(window, width=25)
txt3.place(x=160,y=270)

##make space for that third blank between basne and ko

lbl5 = Label(window, text="द.नं: ", font=("Ganesh",12))
lbl5.place(x=10, y=300)
txt5 = Entry(window, width=25)
txt5.place(x=160, y=300)

lbl6 = Label(window, text="मिति: ", font=("Ganesh",12))
lbl6.place(x=550, y=150)
txt6 = Entry(window, width=25)
txt6.place(x=650, y=150)

lbl7 = Label(window, text="जग्गा दर्ता नाउ: ", font=("Ganesh",12))
lbl7.place(x=550, y=180)
txt7 = Entry(window, width=25)
txt7.place(x=650, y=180)












