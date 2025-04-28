import customtkinter as ctk
from tkcalendar import Calendar

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
        display_width=self.add_win.winfo_screenwidth()
        display_height=self.add_win.winfo_screenheight()
        
        #set window width and height
        win_width=630
        win_height=420
        #set top and left
        left=int(display_width/2-win_width/2)+10
        top=int(display_height/2-win_height/2)+60

        # bring popup to front
        self.add_win.focus()
        self.add_win.grab_set()

        self.add_win.geometry(f"{win_width}x{win_height}+{left}+{top}")
        self.add_win.resizable(False, False)

        #add label and entry fields 
        main_label=ctk.CTkLabel(self.add_win,text="Add your task.",font=("Arial",20,"bold"),width=200,height=50)
        main_label.place(relx=0.32,rely=0.01)

        #name label and entry
        name_label=ctk.CTkLabel(self.add_win,text="Task name",font=("Arial",15),width=80,height=40)
        name_label.place(relx=0.07,rely=0.12)

        self.name_entry=ctk.CTkEntry(self.add_win,placeholder_text="add task name")
        self.name_entry.place(relx=0.25,rely=0.15)

        #description and text box
        des_label=ctk.CTkLabel(self.add_win,text="Task description",font=("Arial",15),width=80,height=40)
        des_label.place(relx=0.07,rely=0.25)

        self.des_textbox=ctk.CTkTextbox(self.add_win,width=300,height=100)
        self.des_textbox.place(relx=0.25,rely=0.25)

        #priority and combo box
        priority_label=ctk.CTkLabel(self.add_win,text="Task priority",font=("Arial",15),width=80,height=40)
        priority_label.place(relx=0.52,rely=0.12)

        priority=["High","Medium","Low"]
        self.priority_combo=ctk.CTkComboBox(self.add_win,values=priority)
        self.priority_combo.place(relx=0.7,rely=0.15)

        #add date using tkcalendar library
        date_label=ctk.CTkLabel(self.add_win,text="Due date",font=("Arial",15),width=80,height=40)
        date_label.place(relx=0.07,rely=0.48)

        self.calendar=Calendar(self.add_win,selectmode="day",date_pattern="yyyy-mm-dd")
        self.calendar.place(relx=0.25, rely=0.52)

        #add button for submit
        add_button = ctk.CTkButton(self.add_win, text="Add Task", command=self.get_task,
                                   fg_color="blue",text_color="white",hover_color="dark blue",
                                   font=("Arial",12,"bold"),corner_radius=10)
        add_button.place(relx=0.5, rely=0.95, anchor="center")


    def get_task(self):
        name=self.name_entry.get()
        des=self.des_textbox.get("1.0", "end-1c")
        priority=self.priority_combo.get()
        date=self.calendar.get()

        #add task to task manage
        self.Task_manage.add_task(name,des,priority,date)

        #auto close window
        self.add_win.destroy()

        #add task to treeview
        self.refresh_tasks()





