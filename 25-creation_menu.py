import tkinter

def hello():
    print("hello")
    
def show_about():
    about_window=tkinter.Toplevel(app)
    about_window.title("a propos")
    

app = tkinter.Tk()
app.geometry("640x480")
app.title("creation menu")

main_menu=tkinter.Menu(app)

fisrt_menu=tkinter.Menu(main_menu , tearoff=0)
fisrt_menu.add_command(label="Option1", command=hello)
fisrt_menu.add_command(label="Option2")
fisrt_menu.add_separator()
fisrt_menu.add_command(label="quitter", command=app.quit)

second_menu=tkinter.Menu(main_menu)
second_menu.add_command(label="Commande1")
second_menu.add_command(label="a propos" , command=show_about)

main_menu.add_cascade(label="Premier", menu=fisrt_menu)
main_menu.add_cascade(label="second", menu=second_menu)


app.config(menu=main_menu)


app.mainloop()