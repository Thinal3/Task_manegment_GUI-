import customtkinter as ctk
import tkinter
from tkinter import ttk
from PIL import Image
from task_manage import Task_manage
from add_delete_interface import Sub_interface

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

       # create object instance
       self.Task_manage=Task_manage()
       self.sub_interface=Sub_interface(self.main_frame,self.Task_manage,self.refresh_tasks)

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
        self.welcome_label=ctk.CTkLabel(self.welcome,text="",text_color="white",fg_color="transparent",
                                   font=("Arial",28,"bold"),width=300,height=50)
        self.welcome_label.place(relx=0.7, rely=0.2, anchor="center")

        self.full_text = "Welcome to My Manager."
        self.current_text = ""
        self.index = 0
        
        self.animate_typing()


        note_label=ctk.CTkLabel(self.welcome,
                                text="  This application helps you stay organized and manage\n your tasks effortlessly.\n"
                                     "Simply add, view, and organize your tasks to stay\n productive and on top of things.\n\n"
                                     "Let's get things done with ease and efficiency!",
                                     text_color="#E5E5FF",fg_color="transparent",font=("Segoe UI", 14,"bold"),
                                     width=200,height=150)
        
        note_label.place(relx=0.7,rely=0.5,anchor="center")

        #create get start button
        get_start_button=ctk.CTkButton(self.welcome,text="Start now",command=self.show_main,
                                       text_color="white",fg_color="transparent",font=("Arial",14),
                                       corner_radius=10,hover_color="blue",border_width=2,
                                       border_color="blue",width=140,height=35)
        get_start_button.place(relx=0.7,rely=0.73,anchor="center")



    def animate_typing(self):
        
        if self.index < len(self.full_text):
            
            self.current_text += self.full_text[self.index]
            self.welcome_label.configure(text=self.current_text)
            self.index += 1
            
            self.after(180, self.animate_typing)  # Speed of typing (180ms per letter)


    def setup_mainframe(self):

        #create image for mainframe
        main_img1=ctk.CTkImage(light_image=Image.open("../img/main_frame_img01.png"),dark_image=Image.open("../img/main_frame_img01.png"),size=(700,80))
        img_label1=ctk.CTkLabel(self.main_frame,text="",image=main_img1)
        img_label1.pack(side="top")

        #add buttons to main frame
        add_button=ctk.CTkButton(self.main_frame,text=" + ",text_color="white",fg_color="blue",command=self.sub_interface.add_task_interface,
                                 font=("Arial",20,"bold"),corner_radius=10,width=25,height=24)
        add_button.place(relx=0.12,rely=0.25)


        delete_img=ctk.CTkImage(light_image=Image.open("../img/trash_bin.png"),dark_image=Image.open("../img/trash_bin.png"),size=(20,20))
        delete_button=ctk.CTkButton(self.main_frame,text="",image=delete_img,text_color="white",fg_color="red",command=lambda:self.sub_interface.delete_task_interface(self.my_tree),
                                corner_radius=10,width=25,height=25)
        delete_button.place(relx=0.2,rely=0.25)


        search_img=ctk.CTkImage(light_image=Image.open("../img/search_img.png"),dark_image=Image.open("../img/search_img.png"),size=(20,20))
        search_button=ctk.CTkButton(self.main_frame,text="",image=search_img,text_color="white",fg_color="blue",command=self.search_task,
                                 font=("Arial",20,"bold"),corner_radius=10,width=25,height=25)
        search_button.place(relx=0.73,rely=0.25)


        reset_img=ctk.CTkImage(light_image=Image.open("../img/reset_img.png"),dark_image=Image.open("../img/reset_img.png"),size=(20,20))
        reset_button=ctk.CTkButton(self.main_frame,text="",image=reset_img,text_color="white",fg_color="blue",command=self.cleaning_search,
                                corner_radius=10,width=25,height=25)
        reset_button.place(relx=0.8,rely=0.25)


        #add entry field to search items
        self.search_entry=ctk.CTkEntry(self.main_frame,placeholder_text="Search with name..",placeholder_text_color="gray",width=150,height=27)
        self.search_entry.place(relx=0.5,rely=0.25)


        #add frame to contain treeview
        self.table_frame=ctk.CTkFrame(self.main_frame)
        self.table_frame.place(relx=0.12,rely=0.33, relwidth=0.75, relheight=0.5)
        
        self.treeview()


    def show_welcome(self):
        self.main_frame.pack_forget()
        self.welcome.pack(fill="both", expand=True)


    def show_main(self):
        self.welcome.pack_forget()
        self.main_frame.pack(fill="both", expand=True)
 

    def treeview(self):
        self.my_tree=ttk.Treeview(self.table_frame,columns=("Task name","Description","Priority","Date"),show="headings")

        #headings
        self.my_tree.heading("Task name",text="Task name")
        self.my_tree.heading("Description",text="Description")
        self.my_tree.heading("Priority",text="Priority")
        self.my_tree.heading("Date",text="Date")

        #column width
        self.my_tree.column("Task name", width=150,anchor="center")
        self.my_tree.column("Description", width=250,anchor="center")
        self.my_tree.column("Priority", width=100,anchor="center")
        self.my_tree.column("Date", width=120,anchor="center")

        #insert values 
        self.refresh_tasks()

        #style the treeview
        self.style_treeview()

        # Pack the Treeview
        self.my_tree.pack(fill="both", expand=True)

    
    def refresh_tasks(self):
        for row in self.my_tree.get_children():
            self.my_tree.delete(row)
        
        for task_id, task_data in self.Task_manage.tasks_dict.items():
            # Insert each task into the treeview
            self.my_tree.insert("", "end",iid=task_id, values=(task_data["task_name"], task_data["description"], task_data["priority"], task_data["date"]))



    def style_treeview(self):
        style=ttk.Style()

        style.theme_use("clam")

        style.configure("Treeview.Heading",font=("Arial",12,"bold"),
                        background="#1e3a8a", foreground="white",relief="flat")
        
        style.configure("Treeview",font=("Arial", 14),
                        background="#0f173a", foreground="white",
                        rowheight=35,  # Adjust row height
                        fieldbackground="#0f173a")

        style.map("Treeview", background=[('selected', '#2563eb')],
                  foreground=[("selected","white")])

    def search_task(self):
        filter_list=[]

        search_item=self.search_entry.get().lower()

        for task_id,task_data in self.Task_manage.tasks_dict.items():
            if search_item in task_data["task_name"]:
                filter_list.append(task_id)

        for item in self.my_tree.get_children():
            self.my_tree.delete(item)

        for task_id in filter_list:
            task=self.Task_manage.tasks_dict[task_id]
            self.my_tree.insert("", "end",iid=task_id, values=(task["task_name"], task["description"], task["priority"], task["date"]))


    def cleaning_search(self):
        self.search_entry.delete(0, ctk.END)
        self.refresh_tasks()

