
"""
<nom_variable>=<nom_widget>(<widget_parent,<params>)

"""


import tkinter

def hello():
    print("hello")
    
app= tkinter.Tk()

label_welcome= tkinter.Label(app, text="coucou")

#msg_welcome= tkinter.Message(app, text="coucou")

#entry_name=tkinter.Entry(app, with=45) show="*" pour mdp, exportselection=0 ppour ne pas enregistrer

#btn_ok=tkinter.Button(app, text="ok", command=hello)

label_welcome.pack()

app.mainloop()