import customtkinter as ctk

class Sub_interface:
    def __init__(self,parent,Task_manage,refresh_tasks):
        self.parent=parent
        self.Task_manage=Task_manage
        self.refresh_tasks=refresh_tasks
    
    def add_task_interface(self):
        self.add_win=ctk.CTkToplevel(self.parent,fg_color="#0f172a")
        self.add_win.title("Add Your Task.")

        #to open window in center in the screen
        #get display width and height
        display_width= self.winfo_screenwidth()
        display_height=self.winfo_screenheight()
        
        #set window width and height
        win_width=600
        win_height=340
        #set top and left
        left=int(display_width/2-win_width/2)
        top=int(display_height/2-win_height/2)

        self.add_win.geometry(f"{win_width}x{win_height}+{left}+{top}")
        self.add_win.resizable(False, False)

        #add label and entry fields 
        main_label=ctk.CTkLabel(self.add_win,text="Add your task.",font=("Arial",20,"bold"),width=200,height=50)
        main_label.place(relx=0.32,rely=0.06)

        #name label and entry
        name_label=ctk.CTkLabel(self.add_win,text="Task name",font=("Arial",15),width=80,height=40)
        name_label.place(relx=0.1,rely=0.25)

        self.name_entry=ctk.CTkEntry(self.add_win,placeholder_text="add task name")
        self.name_entry.place(relx=0.3,rely=0.25)

        #description and text box
        des_label=ctk.CTkLabel(self.add_win,text="Task description",font=("Arial",15),width=80,height=40)
        des_label.place(relx=0.1,rely=0.35)

        self.des_entry=ctk.CTkTextbox(self.add_win,width=300,height=100)
        self.des_entry.place(relx=0.,rely=0.35)

