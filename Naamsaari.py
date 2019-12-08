from tkinter import *
from FormUtils import submit_form_button, clear_form_button
from PIL import Image, ImageTk


class NaamsaariForm:

    def __init__(self, main):
        self.top_window = main
        
        ##Container where all the form fields go. Has scroll functionality
        self.canvas = Canvas(self.top_window)
        
        self.scrollbar = Scrollbar(self.top_window, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(fill="y", side="right")
        
        self.window = Frame(self.canvas)
        self.window.columnconfigure(2, minsize=100)
        self.window.rowconfigure(20, minsize=20)

        ##### IMAGE FRAMES
        self.image_frame1 = Frame(self.top_window, bg='yellow')
        self.image_frame2 = Frame(self.top_window)

        self.logo_path = "Forms/static/images/Nepal.png"
        self.logoimg = ImageTk.PhotoImage(Image.open(self.logo_path).resize((128, 128)))

        self.img1 = Label(self.image_frame1, image=self.logoimg)
        self.img2 = Label(self.image_frame2, image=self.logoimg)

        self.img1.pack()
        self.img2.pack()
        
        self.image_frame1.pack(anchor="nw", side=LEFT)
        self.image_frame2.pack(anchor="ne", side=RIGHT)
        ##### END OF IMAGE FRAMES

        ##start of header section
        self.header_frame = Frame(self.top_window, pady=10)

        header = Label(self.header_frame, text= "नेपाल सरकार", font=("bold",15))
        header.pack()
        header2 = Label(self.header_frame, text="भूमि व्यवस्था सरकारी तथा गरिवी निवारण मन्‍न्नालय", font=("bold",15))
        header2.pack()
        header3 = Label(self.header_frame, text="भूमि व्यवस्थापन तथा अभिलेख विभाग", font=("bold",15))
        header3.pack()
        header4 = Label(self.header_frame, text="मालपोत कार्यालय", font=("bold",15))
        header4.pack()
        header5 = Label(self.header_frame, text="साँखु (काठमाण्डौ)", font=("bold",15))
        header5.pack()

        self.header_frame.pack(side=TOP)
        ##end of header section

        ##labels and textboxes
        self.lblDate = Label(self.window, text="मिति:", font = ("Ganesh",12))
        self.lblDate.grid(row=0, column=0, sticky=E)
        self.txtDate = Entry(self.window, width=25, name="miti1")
        self.txtDate.grid(row=0, column=1)

        self.lblM = Label(self.window, text="मिसिल नं. :", font = ("Ganesh",12))
        self.lblM.grid(row=1, column=0, sticky=E)
        self.txtM = Entry(self.window, width=25, name="misil")
        self.txtM.grid(row=1, column=1)

        self.lbl1 = Label(self.window, text="द.नं : ", font =("Ganesh",12))
        self.lbl1.grid(row=2, column=0, sticky=E)
        self.txt1 = Entry(self.window, width=25, name="dana")
        self.txt1.grid(row=2, column=1)

        self.lbl2 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl2.grid(row=3, column=0, sticky=E)
        self.txt2 = Entry(self.window, width=25, name="miti2")
        self.txt2.grid(row=3, column=1)

        ##for table
        self.lbl3 = Label(self.window, text="निवेदकको नाम, थर, वतन: ", font =("Ganesh",12))
        self.lbl3.grid(row=4, column=0, sticky=E)
        self.txt3 = Entry(self.window, width=25, name="naam")
        self.txt3.grid(row=4, column=1)

        self.lbl4 = Label(self.window, text="नागरिकता नं.: ", font =("Ganesh",12))
        self.lbl4.grid(row=0, column=3, sticky=E)
        self.txt4 = Entry(self.window, width=25, name="nagarikta")
        self.txt4.grid(row=0, column=4)

        self.lbl5 = Label(self.window, text="पिता: ", font = ("Ganesh",12))
        self.lbl5.grid(row=1, column=3, sticky=E)
        self.txt5 = Entry(self.window, width=25, name="pita")
        self.txt5.grid(row=1, column=4)

        self.lbl6 = Label(self.window, text="पति: ", font =("Ganesh",12))
        self.lbl6.grid(row=2, column=3, sticky=E)
        self.txt6 = Entry(self.window, width=25, name="pati")
        self.txt6.grid(row=2, column=4)

        self.lbl7 = Label(self.window, text="बाजे: ", font =("Ganesh",12))
        self.lbl7.grid(row=3, column=3, sticky=E)
        self.txt7 = Entry(self.window, width=25, name="baje")
        self.txt7.grid(row=3, column=4)

        self.lbl8 = Label(self.window, text="कैफियत: ", font =("Ganesh",12))
        self.lbl8.grid(row=4, column=3, sticky=E)
        self.txt8 = Entry(self.window, width=25, name="faikyat")
        self.txt8.grid(row=4, column=4)

        self.lbl9 = Label(self.window, text="मृतक दर्तावालाको नाम, थर, वतन: ", font = ("Ganesh",12))
        self.lbl9.grid(row=5, column=0, sticky=E)
        self.txt9 = Entry(self.window, width=25, name="dartawala")
        self.txt9.grid(row=5, column=1)

        self.lbl10 = Label(self.window, text="जग्गा रहेको गा.वि.स / न.पा: ", font = ("Ganesh",12))
        self.lbl10.grid(row=6, column=0, sticky=E)
        self.txt10= Entry(self.window, width=25, name="gawisa")
        self.txt10.grid(row=6, column=1)

        self.lbl11 = Label(self.window, text="वडा नं.: ", font =("Ganesh",12))
        self.lbl11.grid(row=7, column=0, sticky=E)
        self.txt11 = Entry(self.window, width=25, name="wada")
        self.txt11.grid(row=7, column=1)

        self.lbl12 = Label(self.window, text="कित्ता नं.: ", font =("Ganesh",12))
        self.lbl12.grid(row=8, column=0, sticky=E)
        self.txt12 = Entry(self.window, width=25, name="kina")
        self.txt12.grid(row=8, column=1)

        self.lbl13 = Label(self.window, text="क्षत्रफल: ", font =("Ganesh",12))
        self.lbl13.grid(row=5, column=3, sticky=E)
        self.txt13 = Entry(self.window, width=25, name="chhetrafal")
        self.txt13.grid(row=5, column=4)

        self.lbl14 = Label(self.window, text="मृतकसंगको नाता: ", font = ("Ganesh",12))
        self.lbl14.grid(row=6, column=3, sticky=E)
        self.txt14 = Entry(self.window, width=25, name="nata")
        self.txt14.grid(row=6, column=4)

        self.lbl15 = Label(self.window, text="मिति: ", font =("Ganesh",12))
        self.lbl15.grid(row=7, column=3, sticky=E)
        self.txt15 = Entry(self.window, width=25, name="miti3")
        self.txt15.grid(row=7, column=4)
        ##end of table


        self.lbl16 = Label(self.window, text= "संलग्न प्रमाणहरु: ", font =("Ganesh",15))
        self.lbl16.grid(row=9, column=0)

        self.lbl17 = Label(self.window, text="च .नं.: ",font = ("Ganesh",12))
        self.lbl17.grid(row=10, column=0, sticky=E)
        self.txt17 = Entry(self.window, width=25, name="chana")
        self.txt17.grid(row=10, column=1)

        self.lbl18 = Label(self.window, text="मिति: ",font = ("Ganesh",12))
        self.lbl18.grid(row=11, column=0, sticky=E)
        self.txt18 = Entry(self.window, width=25, name="miti4")
        self.txt18.grid(row=11, column=1)

        self.lbl19 = Label(self.window, text="न.पा / गा. वि. स.: ",font = ("Ganesh",12))
        self.lbl19.grid(row=12, column=0, sticky=E)
        self.txt19 = Entry(self.window, width=25, name="napa")
        self.txt19.grid(row=12, column=1)

        self.lbl20 = Label(self.window, text="वडा नं: ",font = ("Ganesh",12))
        self.lbl20.grid(row=13, column=0, sticky=E)
        self.txt20 = Entry(self.window, width=25, name="wada2")
        self.txt20.grid(row= 13, column=1)

        self.lbl21 = Label(self.window, text="च .नं.: ",font = ("Ganesh",12))
        self.lbl21.grid(row=10, column=3, sticky=E)
        self.txt21 = Entry(self.window, width=25, name="chana2")
        self.txt21.grid(row=10, column=4)

        self.lbl22 = Label(self.window, text="मिति: ",font = ("Ganesh",12))
        self.lbl22.grid(row=11, column=3, sticky=E)
        self.txt22 = Entry(self.window, width=25, name="miti5")
        self.txt22.grid(row=11, column=4)

        self.lbl23 = Label(self.window, text="न.पा / गा. वि. स.: ",font = ("Ganesh",12))
        self.lbl23.grid(row=12, column=3, sticky=E)
        self.txt23 = Entry(self.window, width=25, name="gawisa2")
        self.txt23.grid(row=12, column=4)

        ### PAGE 2 ###
        self.second_page_label = Label(self.window, text="दोस्रो पाना: ", font=("Ganesh", 15))
        self.second_page_label.grid(row=14, column=0)

        self.lbl24 = Label(self.window, text="द. नं: ", font=("Ganesh", 12))
        self.lbl24.grid(row=15, column=0, sticky=E)
        self.txt24 = Entry(self.window, width=25, name="dana2")
        self.txt24.grid(row=15, column=1)

        self.lbl25 = Label(self.window, text="मिति: ", font=("Ganesh", 12))
        self.lbl25.grid(row=16, column=0, sticky=E)
        self.txt25 = Entry(self.window, width=25, name="miti6")
        self.txt25.grid(row=16, column=1)

        self.lbl26 = Label(self.window, text="वडा.नं: ", font=("Ganesh", 12))
        self.lbl26.grid(row=17, column=0, sticky=E)
        self.txt26 = Entry(self.window, width=25, name="wada3")
        self.txt26.grid(row=17, column=1)

        self.lbl27 = Label(self.window, text="मालपोत बुझाएको नं: ", font=("Ganesh", 12))
        self.lbl27.grid(row=18, column=0, sticky=E)
        self.txt27 = Entry(self.window, width=25, name="malpot")
        self.txt27.grid(row=18, column=1)

        self.lbl28 = Label(self.window, text="मिति: ", font=("Ganesh", 12))
        self.lbl28.grid(row=19, column=0, sticky=E)
        self.txt28 = Entry(self.window, width=25, name="miti7")
        self.txt28.grid(row=19, column=1)

        self.lbl29 = Label(self.window, text="सार्वजनिक सूचना प्रकाशन मिति: ", font=("Ganesh", 12))
        self.lbl29.grid(row=15, column=3, sticky=E)
        self.txt29 = Entry(self.window, width=25, name="prakashan")
        self.txt29.grid(row=15, column=4)

        self.lbl30 = Label(self.window, text="हकदार मध्ये: ", font=("Ganesh", 12))
        self.lbl30.grid(row=16, column=3, sticky=E)
        self.txt30 = Entry(self.window, width=25, name="hakdar")
        self.txt30.grid(row=16, column=4)

        self.lbl31 = Label(self.window, text="द.नं : ", font=("Ganesh", 12))
        self.lbl31.grid(row=17, column=3, sticky=E)
        self.txt31 = Entry(self.window, width=25, name="dana3")
        self.txt31.grid(row=17, column=4)

        self.lbl32 = Label(self.window, text="मिति: ", font=("Ganesh", 12))
        self.lbl32.grid(row=18, column=3, sticky=E)
        self.txt32 = Entry(self.window, width=25, name="miti8")
        self.txt32.grid(row=18, column=4)

        self.lbl33 = Label(self.window, text="मिसिल नं. : ", font=("Ganesh", 12))
        self.lbl33.grid(row=19, column=3, sticky=E)
        self.txt33 = Entry(self.window, width=25, name="misil2")
        self.txt33.grid(row=19, column=4)
        
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
        self.clear_form_button.grid(row=21, column=3, sticky=E)

        self.submit_form_button = submit_form_button(self.window, self.template_and_fields)
        self.submit_form_button.grid(row=21, column=4)


        ### ADDING CANVAS TO DISPLAY ###

        self.canvas.create_window((0, 0), anchor="nw", window=self.window)
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar.set)

        self.canvas.pack(fill="both", expand=True, side="left")