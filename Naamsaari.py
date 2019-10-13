from tkinter import *
 
window = Tk()
window.geometry('850x600')
 
window.title("नामसारी")

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
txtDate = Entry(window, width=25)
txtDate.place(x=160, y=150)

lblM = Label(window, text="मिसिल नं. :", font = ("Ganesh",12))
lblM.place(x=10, y = 180)
txtM = Entry(window, width=25)
txtM.place(x = 160, y=180)

lbl1 = Label(window, text="द.नं : ", font =("Ganesh",12))
lbl1.place(x=10, y=210)
txt1 = Entry(window, width=25)
txt1.place(x = 160, y=210)

lbl2 = Label(window, text="मिति: ", font =("Ganesh",12))
lbl2.place(x=10, y=240)
txt2 = Entry(window, width=25)
txt2.place(x=160, y=240)

##for table
lbl3 = Label(window, text="निवेदकको नाम, थर, वतन: ", font =("Ganesh",12))
lbl3.place(x=10, y=270)
txt3 = Entry(window, width=25)
txt3.place(x=230, y=270)

lbl4 = Label(window, text="नागरिकता नं.: ", font =("Ganesh",12))
lbl4.place(x=550, y=150)
txt4 = Entry(window, width=25)
txt4.place(x=650, y=150)

lbl5 = Label(window, text="पिता: ", font = ("Ganesh",12))
lbl5.place(x=550, y = 180)
txt5 = Entry(window, width=25)
txt5.place(x = 650, y=180)

lbl6 = Label(window, text="पति: ", font =("Ganesh",12))
lbl6.place(x=550, y=210)
txt6 = Entry(window, width=25)
txt6.place(x = 650, y=210)

lbl7 = Label(window, text="बाजे: ", font =("Ganesh",12))
lbl7.place(x=550, y=240)
txt7 = Entry(window, width=25)
txt7.place(x=650, y=240)

lbl8 = Label(window, text="कैफियत: ", font =("Ganesh",12))
lbl8.place(x=550, y=270)
txt8 = Entry(window, width=25)
txt8.place(x=650, y=270)

lbl9 = Label(window, text="मृतक दर्तावालाको नाम, थर, वतन: ", font = ("Ganesh",12))
lbl9.place(x=10, y = 300)
txt9 = Entry(window, width=25)
txt9.place(x=230, y=300)

lbl10 = Label(window, text="जग्गा रहेको गा.वि.स / न.पा: ", font = ("Ganesh",12))
lbl10.place(x=10, y = 330)
txt10= Entry(window, width=25)
txt10.place(x = 230, y=330)

lbl11 = Label(window, text="वडा नं.: ", font =("Ganesh",12))
lbl11.place(x=10, y=360)
txt11 = Entry(window, width=25)
txt11.place(x = 160, y=360)

lbl12 = Label(window, text="कित्ता नं.: ", font =("Ganesh",12))
lbl12.place(x=10, y=390)
txt12 = Entry(window, width=25)
txt12.place(x=160, y=390)

lbl13 = Label(window, text="क्षत्रफल: ", font =("Ganesh",12))
lbl13.place(x=550, y=300)
txt13 = Entry(window, width=25)
txt13.place(x=650, y=300)

lbl14 = Label(window, text="मृतकसंगको नाता: ", font = ("Ganesh",12))
lbl14.place(x=520, y = 330)
txt14 = Entry(window, width=25)
txt14.place(x = 650, y=330)

lbl15 = Label(window, text="मिति: ", font =("Ganesh",12))
lbl15.place(x=550, y=360)
txt15 = Entry(window, width=25)
txt15.place(x = 650, y=360)
##end of table


lbl16 = Label(window, text= "संलग्न प्रमाणहरु: ", font =("Ganesh",12))
lbl16.place(x= 10, y = 450)

lbl17 = Label(window, text="च .नं.: ",font = ("Ganesh",12))
lbl17.place(x=10, y = 480)
txt17 = Entry(window, width=25)
txt17.place(x = 160, y=480)

lbl18 = Label(window, text="मिति: ",font = ("Ganesh",12))
lbl18.place(x=10, y = 510)
txt18 = Entry(window, width=25)
txt18.place(x = 160, y=510)

lbl19 = Label(window, text="न.पा / गा. वि. स.: ",font = ("Ganesh",12))
lbl19.place(x=10, y = 540)
txt19 = Entry(window, width=25)
txt19.place(x = 160, y=540)

lbl20 = Label(window, text="वडा नं: ",font = ("Ganesh",12))
lbl20.place(x=10, y = 570)
txt20 = Entry(window, width=25)
txt20.place(x = 160, y=570)

lbl21 = Label(window, text="च .नं.: ",font = ("Ganesh",12))
lbl21.place(x=550, y = 480)
txt21 = Entry(window, width=25)
txt21.place(x = 650, y=480)

lbl22 = Label(window, text="मिति: ",font = ("Ganesh",12))
lbl22.place(x=550, y = 510)
txt22 = Entry(window, width=25)
txt22.place(x = 650, y=510)

lbl23 = Label(window, text="न.पा / गा. वि. स.: ",font = ("Ganesh",12))
lbl23.place(x=520, y = 540)
txt23 = Entry(window, width=25)
txt23.place(x = 650, y=540)


##end of labels and textboxes

window.mainloop()    ##for the window to wait for any interaction from the user. otherwise the window won't appear to the user.

