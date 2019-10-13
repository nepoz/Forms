from tkinter import *
from jinja2 import Environment, PackageLoader, select_autoescape
import webbrowser
import tempfile
import os

## Setup the environment used by Jinja to find html templates
env = Environment(
    loader=PackageLoader('Forms', 'templates'),
    autoescape=select_autoescape(['html','xml'])
)

'''
Helper method to clear all text fields on a form.
Assume entry_fields is an iterable with all Text Field objects
to be cleared of text.
'''
def clear_form(entry_fields):
    for text_box in entry_fields:
        text_box.delete(0, END)


'''
Helper method to collect all the entries made in the 
Entry fields. Will be the information used to complete
the appropriate form.
'''
def submit_form(entry_fields, form_template):
    ## This dictionary will hold form entries in the format "nth_blank" : "data_to_be_entered"
    form_entries = {}

    for text_box in entry_fields:
        form_entries[str(text_box)[1:]] = text_box.get()

    template = env.get_template(form_template)
    clear_form(entry_fields)

    ## Filled form is created as a temporary file, as storage not needed
    tmp = tempfile.NamedTemporaryFile(delete=True)
    path = tmp.name+'.html'

    with open(path, 'wb') as tmp_form:
        tmp_form.write(template.render(form_entries).encode("utf-8"))
        tmp_form.close()
    
    webbrowser.open("file://" + path)

'''
Generates submit button that will fill out 
template form and then clears the fields
that have been filled.
'''
def submit_form_button(master, entry_fields, form_template):
    return Button(
        master=master,
        text="Submit Form",
        command=lambda: submit_form(entry_fields, form_template)
    )

'''
Generates button to clear all entries
'''
def clear_form_button(master, entry_fields):
    return Button(
        master=master,
        text="Clear",
        command=lambda: clear_form(entry_fields)
    )