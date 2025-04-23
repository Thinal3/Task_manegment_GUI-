import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):# Inherit from CTk main window

    def __init__(self):# create main window
       super().__init__()
       self.title("My Manager")
       self.geometry("600x600")

       #create frames
       self.welcome=ctk.CTkFrame(self)
       self.main_frame=ctk.CTkFrame(self)

       # set up the frames of GUI
       self.setup_welcome()
       self.setup_mainframe()
    
    def setup_welcome():
        #create img to welcome frame
        welcome_img=ctk.CTkImage(light_image=Image.open(""),dark_image=Image.open("img/welcome.png"))
       
        






if __name__=="__main__":
    app=App()
    app.mainloop()

