import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):# Inherit from CTk main window

    def __init__(self):# create main window
       super().__init__()
       self.title("My Manager")
       self.geometry("600x600")
 





if __name__=="__main__":
    app=App()
    app.mainloop()

