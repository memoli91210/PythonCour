"""
StringVar() : chaine de caractere
IntVar() = int
DoublVar() = float
BouleanVar() = boulean
"""

#def update_label(*args):
    #var_label.set(var_entry.get())
    
def update_oberveur(*args):
    if var_gender.get():
        var_label_gender.set("Sexe homme")
    else:
        var_label_gender.set("Sexe femme")
    
import tkinter


app = tkinter.Tk()
app.geometry("400x300")
app.title("variable tkinter")

var_gender = tkinter.IntVar()
var_gender.trace("w", update_oberveur)
radio1=tkinter.Radiobutton(app, text="homme",value=1,variable=var_gender)
radio2=tkinter.Radiobutton(app, text="femme",value=0,variable=var_gender)
# var_label=tkinter.StringVar()
# var_entry=tkinter.StringVar()

# entry=tkinter.Entry(app, textvariable=var_entry)
# label=tkinter.Label(app, textvariable=var_label)

# var_label.set("coucou")
# var_entry.trace("w", update_label)

var_label_gender=tkinter.StringVar()
label_gender= tkinter.Label(app, textvariable=var_label_gender)

# label.pack()
# entry.pack()
radio1.pack()
radio2.pack()
label_gender.pack()

app.mainloop()