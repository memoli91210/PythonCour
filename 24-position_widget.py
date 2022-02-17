from cgitb import grey
import tkinter


app = tkinter.Tk()
app.geometry("640x480")
app.title("position des widget")


# mainframe=tkinter.LabelFrame(app, text="titre")
# mainframe.pack()

label = tkinter.Label(app, text="label")
entry = tkinter.Entry(app)
btn = tkinter.Button(app, text="bienvenue")


label.pack(side="top", expand=0, fill="y") 
entry.pack()#padx= margin, ipadx pardding
btn.pack()

#on peu grid au lieu de pack 
#row column

#on peu place au lieu de pack
#x=pixel y=pixel

app.mainloop()