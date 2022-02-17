
"""
showerror
showinfo
showwarning
askquestion
askokcancel
askretrycancel
etc..
"""


import tkinter
from tkinter import messagebox

app = tkinter.Tk()

#check_widget=tkinter.Checkbutton(app, text="publier ?")
#adio_widget=tkinter.Radiobutton(app, text="homme",value=1)
#radio_widget2=tkinter.Radiobutton(app, text="femme",value=0)

#scale_w=tkinter.Scale(app, from_=10, to=100)
#spin_w=tkinter.Spinbox(app, from_=1, to=10)

#lb=tkinter.Listbox(app)
#lb.insert(1, "windows")
#lb.insert(2, "linux")

def show_modal_windows():
    messagebox.showerror("Erreur" , "un probleme est survenue")

btn=tkinter.Button(app, text="erreur", command=show_modal_windows)

#check_widget.pack()
#radio_widget.pack()
#radio_widget2.pack()
btn.pack()
app.mainloop()