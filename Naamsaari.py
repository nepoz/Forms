from tkinter import *
from FormUtils import submit_form_button, clear_form_button
from PIL import Image, ImageTk


class NaamsaariForm:

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
        header = Label(self.window, text= "नेपाल सरकार", font=("bold",15))
        header.place(x=400, y=10)
        header2 = Label(self.window, text="भूमि व्यवस्था सरकारी तथा गरिवी निवारण मन्‍न्नालय", font=("bold",15))
        header2.place(x= 270, y=35)
        header3 = Label(self.window, text="भूमि व्यवस्थापन तथा अभिलेख विभाग", font=("bold",15))
        header3.place(x= 330, y=60)
        header4 = Label(self.window, text="मालपोत कार्यालय", font=("bold",15))
        header4.place(x= 390, y=85)
        header5 = Label(self.window, text="साँखु (काठमाण्डौ)", font=("bold",15))
        header5.place(x= 390, y=110)
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

        self.lbl1 = Label(self.window, text="द.नं : ", font =("Ganesh",12))
        self.lbl1.place(x=10, y=210)
        self.txt1 = Entry(self.window, width=25, name="dana")
        self.txt1.place(x = 160, y=210)

        self.lbl2 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl2.place(x=10, y=240)
        self.txt2 = Entry(self.window, width=25, name="miti2")
        self.txt2.place(x=160, y=240)

        ##for table
        self.lbl3 = Label(self.window, text="निवेदकको नाम, थर, वतन: ", font =("Ganesh",12))
        self.lbl3.place(x=10, y=270)
        self.txt3 = Entry(self.window, width=25, name="naam")
        self.txt3.place(x=230, y=270)

        self.lbl4 = Label(self.window, text="नागरिकता नं.: ", font =("Ganesh",12))
        self.lbl4.place(x=550, y=150)
        self.txt4 = Entry(self.window, width=25, name="nagarikta")
        self.txt4.place(x=650, y=150)

        self.lbl5 = Label(self.window, text="पिता: ", font = ("Ganesh",12))
        self.lbl5.place(x=550, y = 180)
        self.txt5 = Entry(self.window, width=25, name="pita")
        self.txt5.place(x = 650, y=180)

        self.lbl6 = Label(self.window, text="पति: ", font =("Ganesh",12))
        self.lbl6.place(x=550, y=210)
        self.txt6 = Entry(self.window, width=25, name="pati")
        self.txt6.place(x = 650, y=210)

        self.lbl7 = Label(self.window, text="बाजे: ", font =("Ganesh",12))
        self.lbl7.place(x=550, y=240)
        self.txt7 = Entry(self.window, width=25, name="baje")
        self.txt7.place(x=650, y=240)

        self.lbl8 = Label(self.window, text="कैफियत: ", font =("Ganesh",12))
        self.lbl8.place(x=550, y=270)
        self.txt8 = Entry(self.window, width=25, name="faikyat")
        self.txt8.place(x=650, y=270)

        self.lbl9 = Label(self.window, text="मृतक दर्तावालाको नाम, थर, वतन: ", font = ("Ganesh",12))
        self.lbl9.place(x=10, y = 300)
        self.txt9 = Entry(self.window, width=25, name="dartawala")
        self.txt9.place(x=230, y=300)

        self.lbl10 = Label(self.window, text="जग्गा रहेको गा.वि.स / न.पा: ", font = ("Ganesh",12))
        self.lbl10.place(x=10, y = 330)
        self.txt10= Entry(self.window, width=25, name="gawisa")
        self.txt10.place(x = 230, y=330)

        self.lbl11 = Label(self.window, text="वडा नं.: ", font =("Ganesh",12))
        self.lbl11.place(x=10, y=360)
        self.txt11 = Entry(self.window, width=25, name="wada")
        self.txt11.place(x = 160, y=360)

        self.lbl12 = Label(self.window, text="कित्ता नं.: ", font =("Ganesh",12))
        self.lbl12.place(x=10, y=390)
        self.txt12 = Entry(self.window, width=25, name="kina")
        self.txt12.place(x=160, y=390)

        self.lbl13 = Label(self.window, text="क्षत्रफल: ", font =("Ganesh",12))
        self.lbl13.place(x=550, y=300)
        self.txt13 = Entry(self.window, width=25, name="chhetrafal")
        self.txt13.place(x=650, y=300)

        self.lbl14 = Label(self.window, text="मृतकसंगको नाता: ", font = ("Ganesh",12))
        self.lbl14.place(x=520, y = 330)
        self.txt14 = Entry(self.window, width=25, name="nata")
        self.txt14.place(x = 650, y=330)

        self.lbl15 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl15.place(x=550, y=360)
        self.txt15 = Entry(self.window, width=25, name="miti3")
        self.txt15.place(x = 650, y=360)
        ##end of table


        self.lbl16 = Label(self.window, text= "संलग्न प्रमाणहरु: ", font =("Ganesh",15))
        self.lbl16.place(x= 10, y = 450)

        self.lbl17 = Label(self.window, text="च .नं.: ",font = ("Ganesh",12))
        self.lbl17.place(x=10, y = 480)
        self.txt17 = Entry(self.window, width=25, name="chana")
        self.txt17.place(x = 160, y=480)

        self.lbl18 = Label(self.window, text="मिति: ",font = ("Ganesh",12))
        self.lbl18.place(x=10, y = 510)
        self.txt18 = Entry(self.window, width=25, name="miti4")
        self.txt18.place(x = 160, y=510)

        self.lbl19 = Label(self.window, text="न.पा / गा. वि. स.: ",font = ("Ganesh",12))
        self.lbl19.place(x=10, y = 540)
        self.txt19 = Entry(self.window, width=25, name="napa")
        self.txt19.place(x = 160, y=540)

        self.lbl20 = Label(self.window, text="वडा नं: ",font = ("Ganesh",12))
        self.lbl20.place(x=10, y = 570)
        self.txt20 = Entry(self.window, width=25, name="wada2")
        self.txt20.place(x = 160, y=570)

        self.lbl21 = Label(self.window, text="च .नं.: ",font = ("Ganesh",12))
        self.lbl21.place(x=550, y = 480)
        self.txt21 = Entry(self.window, width=25, name="chana2")
        self.txt21.place(x = 650, y=480)

        self.lbl22 = Label(self.window, text="मिति: ",font = ("Ganesh",12))
        self.lbl22.place(x=550, y = 510)
        self.txt22 = Entry(self.window, width=25, name="miti5")
        self.txt22.place(x = 650, y=510)

        self.lbl23 = Label(self.window, text="न.पा / गा. वि. स.: ",font = ("Ganesh",12))
        self.lbl23.place(x=520, y = 540)
        self.txt23 = Entry(self.window, width=25, name="gawisa2")
        self.txt23.place(x = 650, y=540)

        ### PAGE 2 ###
        self.second_page_label = Label(self.window, text="दोस्रो पाना: ", font=("Ganesh", 15))
        self.second_page_label.place(x=10, y=620)

        self.lbl24 = Label(self.window, text="द. नं: ", font=("Ganesh", 12))
        self.lbl24.place(x=10, y=650)
        self.txt24 = Entry(self.window, width=25, name="dana2")
        self.txt24.place(x=70, y=650)

        self.lbl25 = Label(self.window, text="मिति: ", font=("Ganesh", 12))
        self.lbl25.place(x=10, y=680)
        self.txt25 = Entry(self.window, width=25, name="miti6")
        self.txt25.place(x=70, y=680)

        self.lbl26 = Label(self.window, text="वडा.नं: ", font=("Ganesh", 12))
        self.lbl26.place(x=10, y=710)
        self.txt26 = Entry(self.window, width=25, name="wada3")
        self.txt26.place(x=70, y=710)

        self.lbl27 = Label(self.window, text="मालपोत बुझाएको नं: ", font=("Ganesh", 12))
        self.lbl27.place(x=10, y=740)
        self.txt27 = Entry(self.window, width=25, name="malpot")
        self.txt27.place(x=150, y=740)

        self.lbl28 = Label(self.window, text="मिति: ", font=("Ganesh", 12))
        self.lbl28.place(x=10, y=770)
        self.txt28 = Entry(self.window, width=25, name="miti7")
        self.txt28.place(x=70, y=770)

        self.lbl29 = Label(self.window, text="सार्वजनिक सूचना प्रकाशन मिति: ", font=("Ganesh", 12))
        self.lbl29.place(x=425, y=650)
        self.txt29 = Entry(self.window, width=25, name="prakashan")
        self.txt29.place(x=650, y=650)

        self.lbl30 = Label(self.window, text="हकदार मध्ये: ", font=("Ganesh", 12))
        self.lbl30.place(x=520, y=680)
        self.txt30 = Entry(self.window, width=25, name="hakdar")
        self.txt30.place(x=650, y=680)

        self.lbl31 = Label(self.window, text="द.नं : ", font=("Ganesh", 12))
        self.lbl31.place(x=575, y=710)
        self.txt31 = Entry(self.window, width=25, name="dana3")
        self.txt31.place(x=650, y=710)

        self.lbl32 = Label(self.window, text="मिति: ", font=("Ganesh", 12))
        self.lbl32.place(x=575, y=740)
        self.txt32 = Entry(self.window, width=25, name="miti8")
        self.txt32.place(x=650, y=740)

        self.lbl33 = Label(self.window, text="मिसिल नं. : ", font=("Ganesh", 12))
        self.lbl33.place(x=550, y=770)
        self.txt33 = Entry(self.window, width=25, name="misil2")
        self.txt33.place(x=650, y=770)

        self.entry_fields_first_page = [
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
            self.txt17, 
            self.txt18, 
            self.txt19, 
            self.txt20, 
            self.txt21,
            self.txt22,
            self.txt23
        ]

        self.entry_fields_second_page = [
            self.txt24,
            self.txt25,
            self.txt26,
            self.txt27,
            self.txt28,
            self.txt29,
            self.txt30,
            self.txt31,
            self.txt32,
            self.txt33
        ]

        self.all_entry_fields = self.entry_fields_first_page + self.entry_fields_second_page

        self.template_and_fields = [
            {
                'template' : 'Naamsaari.html',
                'entry_fields' : self.entry_fields_first_page
            },
            {
                'template' : 'Naamsaari2.html',
                'entry_fields' : self.entry_fields_second_page
            }
        ]


##end of labels and textboxes

##### BUTTONS ############
        self.clear_form_button = clear_form_button(self.window, self.all_entry_fields)
        self.clear_form_button.place(x=650, y=800)

        self.submit_form_button = submit_form_button(self.window, self.template_and_fields)
        self.submit_form_button.place(x=700, y=800)