import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from FormUtils import available_forms
from Dakhila import DakhilaForm
from Trial import TrialForm
from Naamsaari import NaamsaariForm
from Form4 import Form4

class Main:

    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, padx=5, pady=5)

        ##### NEPAL GOV LOGO #######
        self.image_frame1 = tk.Frame(self.frame)
        self.image_frame2 = tk.Frame(self.frame)

        self.logo_path = "Forms/static/images/Nepal.png"
        self.logoimg = ImageTk.PhotoImage(Image.open(self.logo_path).resize((128, 128)))

        self.img1 = tk.Label(self.image_frame1, image=self.logoimg)
        self.img2 = tk.Label(self.image_frame2, image=self.logoimg)

        self.img1.pack()
        self.img2.pack()
        
        self.image_frame1.pack(side=tk.LEFT, anchor="nw")
        self.image_frame2.pack(side=tk.RIGHT, anchor="ne")

        ##### GOVT HEADER ##########
        self.header_frame = tk.Frame(self.frame, pady=5)
        
        self.header_line1 = tk.Label(self.header_frame, text="नेपाल सरकार", font=("bold", 15))
        self.header_line2 = tk.Label(self.header_frame, text="भूमि व्यवस्था सरकारी तथा गरिवी निवारण मन्‍न्नालय", font=("bold", 15), padx=10)
        self.header_line3 = tk.Label(self.header_frame, text="भूमि व्यवस्थापन तथा अभिलेख विभाग", font=("bold", 15))
        self.header_line4 = tk.Label(self.header_frame, text="मालपोत कार्यालय", font=("bold", 15))
        self.header_line5 = tk.Label(self.header_frame, text="साँखु (काठमाण्डौ)", font=("bold", 15))

        self.header_line1.grid(row=0, column=1, sticky="EW")
        self.header_line2.grid(row=1, column=1, sticky="EW")
        self.header_line3.grid(row=2, column=1, sticky="EW")
        self.header_line4.grid(row=3, column=1, sticky="EW")
        self.header_line5.grid(row=4, column=1, sticky="EW")

        self.header_frame.pack(side=tk.TOP)

        ##### END GOVT HEADER ##########
        
        self.title_label = tk.Label (
            self.frame, 
            text="तपाई कुन फारम भर्न चाहनु हुन्छ?",
            font=("bold", 20), 
            padx=10, 
            pady=10
        )
        self.title_label.pack(side=tk.TOP)

        self.dropdown = ttk.Combobox(self.frame, values=available_forms)
        self.dropdown.current(0)
        self.dropdown.pack()

        self.button_frame = tk.Frame(self.frame, padx=5, pady=10)
        self.submit_button = tk.Button (
            self.button_frame, 
            text="Next", 
            font=("Arial", 14),
            relief=tk.GROOVE,
            command=self.launch_form
        )
        self.submit_button.pack()
        self.button_frame.pack(side=tk.BOTTOM)

        self.frame.pack()

    def launch_form(self):
        form_option = self.dropdown.get()

        self.newWin = tk.Toplevel(self.root)

        ##Different opening sequences depending on selected form
        if (form_option == "दाखिल"):
            self.newWin.geometry("900x800")
            self.newWin.title("दाखिल")
            self.now = DakhilaForm(self.newWin)
        elif (form_option == "ट्रायल"):
            self.newWin.geometry("850x500")
            self.newWin.title("ट्रायल")
            self.now = TrialForm(self.newWin)
        elif(form_option == "नामसारी"):
            self.newWin.geometry("850x750")
            self.newWin.title("नामसारी")
            self.now = NaamsaariForm(self.newWin)
        else:
            self.newWin.geometry("850x600")
            self.newWin.title(form_option)
            self.now = Form4(self.newWin, form_option)

root = tk.Tk()
root.title("फारम")

main_window = Main(root)
root.mainloop()