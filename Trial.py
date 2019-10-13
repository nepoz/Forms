from tkinter import *
 
window = Tk()
window.geometry('850x600')
 
window.title("ट्रायल")

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

lbl2 = Label(window, text="गा.पा  / न.पा: ", font =("Ganesh",12))
lbl2.place(x=10, y=240)
txt2 = Entry(window, width=25)
txt2.place(x=160, y=240)

lbl3 = Label(window, text="वडा नं.: ", font =("Ganesh",12))
lbl3.place(x=10, y=270)
txt3 = Entry(window, width=25)
txt3.place(x=160, y=270)

lbl4 = Label(window, text="कि.नं: ", font =("Ganesh",12))
lbl4.place(x=550, y=150)
txt4 = Entry(window, width=25)
txt4.place(x=650, y=150)

lbl4 = Label(window, text="निवेदकको नाम : ", font =("Ganesh",12))
lbl4.place(x=520, y=180)
txt4 = Entry(window, width=25)
txt4.place(x=650, y=180)

lbl4 = Label(window, text="द.नं: ", font =("Ganesh",12))
lbl4.place(x=550, y=210)
txt4 = Entry(window, width=25)
txt4.place(x=650, y=210)

lbl4 = Label(window, text="मिति: ", font =("Ganesh",12))
lbl4.place(x=550, y=240)
txt4 = Entry(window, width=25)
txt4.place(x=650, y=240)


##end of labels and textboxes

window.mainloop()    ##for the window to wait for any interaction from the user.
