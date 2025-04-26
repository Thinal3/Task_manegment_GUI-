import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):# Inherit from CTk main window

    def __init__(self):# create main window
       super().__init__()
       self.title("My Manager")

       #to open window in center in the screen
       #get display width and height
       display_width=self.winfo_screenwidth()
       display_height=self.winfo_screenheight()
       #set window width and height
       win_width=700
       win_height=500
       #set top and left
       left=int(display_width/2-win_width/2)
       top=int(display_height/2-win_height/2)

       self.geometry(f"{win_width}x{win_height}+{left}+{top}")
       self.resizable(False, False)

       #create frames
       self.welcome=ctk.CTkFrame(self,fg_color="#0f172a")
       self.main_frame=ctk.CTkFrame(self,fg_color="#0f172a")

       # set up the frames of GUI
       self.setup_welcome()
       self.setup_mainframe()

       #calling show welcome to display first
       self.show_welcome()
    
    def setup_welcome(self):
    
        #create img to welcome frame
        welcome_img=ctk.CTkImage(light_image=Image.open("../img/welcome_img.png"),dark_image=Image.open("../img/welcome_img.png"),
                                 size=(300,500))
        img_label=ctk.CTkLabel(self.welcome,text="",image=welcome_img)
        img_label.pack(side="left", anchor="nw")
        
        #create label in right conner.
        welcome_label=ctk.CTkLabel(self.welcome,text="Welcome to My Manager.",text_color="white",fg_color="transparent",
                                   font=("Arial",28,"bold"),width=300,height=50)
        welcome_label.place(relx=0.7, rely=0.2, anchor="center")

        note_label=ctk.CTkLabel(self.welcome,
                                text="  This application helps you stay organized and manage\n your tasks effortlessly.\n"
                                     "Simply add, view, and organize your tasks to stay\n productive and on top of things.\n\n"
                                     "Let's get things done with ease and efficiency!",
                                     text_color="#E5E5FF",fg_color="transparent",font=("Segoe UI", 14,"bold"),
                                     width=200,height=150)
        
        note_label.place(relx=0.7,rely=0.5,anchor="center")

        #create get start button
        get_start_button=ctk.CTkButton(self.welcome,text="Get started",command=self.show_main,
                                       text_color="white",fg_color="transparent",font=("Arial",14),
                                       corner_radius=10,hover_color="blue",border_width=2,
                                       border_color="blue",width=140,height=35)
        get_start_button.place(relx=0.7,rely=0.73,anchor="center")

    def setup_mainframe(self):

        #create image for mainframe
        main_img1=ctk.CTkImage(light_image=Image.open("../img/main_frame_img01.jpg"),dark_image=Image.open("../img/main_frame_img01.jpg"),size=(700,80))
        img_label1=ctk.CTkLabel(self.main_frame,text="",image=main_img1)
        img_label1.pack(side="top")

        #add buttons to main frame
        add_button=ctk.CTkButton(self.main_frame,text=" + ",text_color="white",fg_color="blue",command="",
                                 font=("Arial",20,"bold"),corner_radius=10,width=30,height=30)
        add_button.place(relx=0.1,rely=0.2)

        delete_img=ctk.CTkImage(light_image=Image.open("../img/trash_bin.png"),dark_image=Image.open("../img/trash_bin.png"),size=(20,20))

        delete_button=ctk.CTkButton(self.main_frame,text="",image=delete_img,text_color="white",fg_color="red",command="",
                                corner_radius=10,width=25,height=30)
        delete_button.place(relx=0.2,rely=0.2)


    
    
    def show_welcome(self):
        self.main_frame.pack_forget()
        self.welcome.pack(fill="both", expand=True)

    def show_main(self):
        self.welcome.pack_forget()
        self.main_frame.pack(fill="both", expand=True)
 






if __name__=="__main__":
    app=App()
    app.mainloop()

