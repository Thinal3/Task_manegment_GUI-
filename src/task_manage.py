import json

class Task_manage:
    def __init__(self):
        self.tasks_dict={}
        self.load_file()

    def add_task(self,name,description,priority,date):
        task_id=len(self.tasks_dict)+1
        
        self.tasks_dict[task_id]={
            "task_name":name,
            "description":description,
            "priority":priority,
            "date":date
        }
        self.save_file()
    
    def load_file(self):
        try:
            with open("tasks.json","r") as file:
                self.tasks_dict=json.load(file)
        except FileNotFoundError:
            self.tasks_dict={}
            
    def save_file(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks_dict, file, indent=4)

    
