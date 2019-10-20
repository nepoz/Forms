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


## ------------ GLOBAL VARS -------------
available_forms = [
    "दाखिल",
    "नामसारी",
    "ट्रायल",
    "संशोधन",
    "प्रतिलिपी",
    "फोटोटास",
    "घर कायम",
    "तिनपुस्ते कायम"
]

logo_path=f"{os.getcwd()}/Forms/static/images/logo.svg".replace(' ', "%20")


##  -------HELPER FUNCTIONS-------
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
def submit_form(fields_templates, **kwargs):
    
    ## List of rendered forms
    rendered_forms = []

    for pair in fields_templates:
        ## This dictionary will hold form entries in the format "nth_blank" : "data_to_be_entered"
        form_entries = {'img_path' : logo_path}
        bisaya = kwargs.get('bisaya', None)

        for text_box in pair['entry_fields']:
            hierarchy = str(text_box).split('.')
            entry_id = hierarchy[len(hierarchy) - 1]
            form_entries[entry_id] = text_box.get()

            if (bisaya):
                form_entries['bisaya'] = bisaya

        template = env.get_template(pair['template'])
        clear_form(pair['entry_fields'])
        
        rendered_form = template.render(form_entries).encode("utf-8")
        rendered_forms.append(rendered_form)

    ## Filled forms are created as temporary files, as storage not needed
    for form in rendered_forms:
        tmp = tempfile.NamedTemporaryFile(delete=True)
        path = tmp.name+'.html'

        with open(path, 'wb') as tmp_form:
            tmp_form.write(form)
            tmp_form.close()
        
        webbrowser.open("file://" + path)

'''
Generates submit button that will fill out 
template form and then clears the fields
that have been filled.
'''
def submit_form_button(master, fields_templates, **kwargs):
    bisaya = kwargs.get('bisaya', None)
    
    return Button(
        master=master,
        text="Submit Form",
        command=lambda: submit_form(fields_templates, bisaya=bisaya)
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