import tkinter as tk
from tkinter import ttk
from FormUtils import available_forms
from Dakhila import DakhilaForm
from Trial import TrialForm

class Main:

    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, padx=5, pady=5)

        self.title_label = tk.Label (
            self.frame, 
            text="Please select a form",
            font=("bold", 40), 
            padx=5, 
            pady=5
        )
        self.title_label.pack(side=tk.TOP)

        self.dropdown = ttk.Combobox(self.frame, values=available_forms)
        self.dropdown.current(0)
        self.dropdown.pack()

        self.button_frame = tk.Frame(self.frame, padx=5, pady=10)
        self.submit_button = tk.Button (
            self.button_frame, 
            text="Launch", 
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
        if (form_option == "Dakhila"):
            self.newWin.geometry("900x800")
            self.newWin.title("दाखिल")
            self.now = DakhilaForm(self.newWin)
        elif (form_option == "Trial"):
            self.newWin.geometry("850x500")
            self.newWin.title("ट्रायल")
            self.now = TrialForm(self.newWin)

root = tk.Tk()
root.title("Forms")

main_window = Main(root)
root.mainloop()