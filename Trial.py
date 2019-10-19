from tkinter import *
from FormUtils import clear_form_button, submit_form_button
from PIL import Image, ImageTk

class TrialForm:

    def __init__(self, main):
        self.window = main

        ##### NEPAL GOV LOGO #######
        self.image_frame1 = Frame(self.window)
        self.image_frame2 = Frame(self.window)

        self.logo_path = "Forms/static/images/Nepal.png"
        self.logoimg = ImageTk.PhotoImage(Image.open(self.logo_path).resize((128, 128)))

        self.img1 = Label(self.image_frame1, image=self.logoimg)
        self.img2 = Label(self.image_frame2, image=self.logoimg)

        self.img1.pack()
        self.img2.pack()
        
        self.image_frame1.pack(side=LEFT, anchor="nw")
        self.image_frame2.pack(side=RIGHT, anchor="ne")
        ##### END OF IMAGE FRAMES

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
        self.txt1 = Entry(self.window, width=25, name="chalani")
        self.txt1.place(x = 160, y=210)

        self.lbl2 = Label(self.window, text="गा.पा  / न.पा: ", font =("Ganesh",12))
        self.lbl2.place(x=10, y=240)
        self.txt2 = Entry(self.window, width=25, name="jilla")
        self.txt2.place(x=160, y=240)

        self.lbl3 = Label(self.window, text="वडा नं.: ", font =("Ganesh",12))
        self.lbl3.place(x=10, y=270)
        self.txt3 = Entry(self.window, width=25, name="oda")
        self.txt3.place(x=160, y=270)

        self.lbl4 = Label(self.window, text="कि.नं: ", font =("Ganesh",12))
        self.lbl4.place(x=550, y=150)
        self.txt4 = Entry(self.window, width=25, name="kina")
        self.txt4.place(x=650, y=150)

        self.lbl5 = Label(self.window, text="निवेदकको नाम : ", font =("Ganesh",12))
        self.lbl5.place(x=520, y=180)
        self.txt5 = Entry(self.window, width=25, name="naam")
        self.txt5.place(x=650, y=180)

        self.lbl6 = Label(self.window, text="द.नं: ", font =("Ganesh",12))
        self.lbl6.place(x=550, y=210)
        self.txt6 = Entry(self.window, width=25, name="darta")
        self.txt6.place(x=650, y=210)

        self.lbl7 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl7.place(x=550, y=240)
        self.txt7 = Entry(self.window, width=25, name="miti2")
        self.txt7.place(x=650, y=240)

        self.entry_fields = [
            self.txtDate,
            self.txtM,
            self.txt1,
            self.txt2,
            self.txt3,
            self.txt4,
            self.txt5,
            self.txt6,
            self.txt7
        ]

        self.template_and_fields = [
            {
                'template' : 'Trial.html',
                'entry_fields' : self.entry_fields
            }
        ]

        #### BUTTONS #####
        clear_form_button(self.window, self.entry_fields).place(x=650, y=270)
        submit_form_button(self.window, self.template_and_fields).place(x=700, y=270)