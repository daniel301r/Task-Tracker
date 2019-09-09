# data structures
data = { 'spanish': {'weekly_goal' : 0, 'total_minutes': 0, 'tasks' : [] },
        'teaching' : {'weekly_goal' : 0, 'total_minutes': 0, 'tasks' : []}, 
        'programming' : {'weekly_goal' : 0, 'total_minutes': 0, 'tasks' : []}}

totals = { 'spanish' : 0,
          'teaching' : 0,
          'programming' : 0,
          'total': 0}
        

class Task:
    def __init__(self, field, description, time, num):
        self.field = field
        self.description = description
        self.time = time
        self.num = num
        self.percentage = 0
        
    def get_percentage(self):
        percentage = self.time / data[self.field]['weekly_goal']
        self.percentage = percentage
        
        
# set weekly goals
def set_weekly_goal():
    print("What weekly goal would you like to set?")
    field = input()
    if field in data.keys():
        print(f"How many hours of {field} do you want to do?")
        hours = int(input())
        data[field]['weekly_goal'] = hours * 60 
        print(f"You want to do {hours} hours of {field} this week")     
    else:
        print(f"{field[0].upper() + field[1:]} is not in your weekly goals")

# adding the instances        
def task_description():
        print("What type of task did you do?")
        field = input()
        print("Write a description of the task or don't")
        description = input()
        print("How long did you spend on the task in minutes?")
        time = int(input())
        
        # assigning the number
        if (len(data[field]['tasks']) > 0):
            num = data[field]['tasks'][len(data[field]['tasks']) - 1].num + 1
        else:
            num = 1
        
        # creating and adding task to data structure
        task = Task(field, description, time, num)
        
        data[field]['tasks'].append(task)

# delete task
def delete_task():
    print("What type of task do you want to delete?")
    field = input()
    print("Have a look at the list of tasks and then delete its number")
    for num in data[field]['tasks']:
        print(f"{num.num} {num.description} {num.time} minutes")
     
    # get the number
    delete_num = int(input())
    
    # find index of task in list
    for task in data[field]["tasks"]:
        if task.num == delete_num:
            task_index = data[field]["tasks"].index(task)
            data[field]['tasks'].pop(task_index)
            print("Deleted Item")
        else:
            print("You entered a wrong number")

def get_percentages(field):
        for task in data[field]['tasks']:
           task.get_percentage() 

# view the individual tasks
def view_tasks():
    print("What type of tasks do you want to see?")
    print("If you want to see all of them type 'all'")
    response = input().lower()
    if response == "all":
        for field in data:
            get_percentages(field)
            for task in data[field]['tasks']:
                print(f"Field: {task.field[0].upper() + task.field[1:]} Number: {task.num} Description: {task.description[0].upper() + task.description[1:]} Time: {task.time} minutes Percentage of weekly goal: {task.percentage}%")
    elif response == "programming":
        get_percentages(response)
        for task in data["programming"]["tasks"]:
           print(f"Number: {task.num} Description: {task.description[0].upper() + task.description[1:]} Time: {task.time} minutes Percentage of weekly goal: {task.percentage}%")
    elif response == "teaching":
        get_percentages(response)
        for task in data["teaching"]["tasks"]:
           print(f"Number: {task.num} Description: {task.description[0].upper() + task.description[1:]} Time: {task.time} minutes Percentage of weekly goal: {task.percentage}%")
    elif response == "spanish":
        get_percentages(response)
        for task in data["spanish"]["tasks"]:
           print(f"Number: {task.num} Description: {task.description[0].upper() + task.description[1:]} Time: {task.time} minutes Percentage of weekly goal: {task.percentage}%")
    else:
       print("You have not entered a correct field")


# view completed percentages of tasks
def calculate_total_time(field):
    total = 0
    for task in data[field]['tasks']:
        total += task.time
    return total 

def print_field_percentages(field):
    print(f"You have completed {str((calculate_total_time(field)) / (data[field]['weekly_goal']))[0:3]}% of your weekly goal")

def view_percentage_completed():
    print("What type of tasks do you want to see?")
    print("If you want to see all of them type 'all'")
    response = input().lower()
    if response == 'all':
        week_total = 0
        for field, goal in data.items():
            for key in goal.keys():
                if 'weekly_goal' in key:
                    week_total += goal[key]
        
        prog_total = calculate_total_time('programming')
        span_total = calculate_total_time('spanish')
        teach_total = calculate_total_time('teaching') 
        
        print(f"You have completed {str((prog_total + span_total + teach_total) / week_total)[0:3]}% of your overall weekly goal")

    elif response == 'spanish':
        print_field_percentages(response)
    elif response == 'programming':
        print_field_percentages(response)
    elif response == 'teaching':
        print_field_percentages(response)
    
# initial start questions
def question():    
    print("How would you like to use your task tracker?")
    print("1. Set goals for the week\n2. Add task\n3. Delete Task\n4. View tasks this week\n5. View percentage of goals completed ")
    ans = int(input())
    
    if ans == 1:
        set_weekly_goal()
    elif ans == 2:
       task_description()
    elif ans == 3:
        delete_task()
    elif ans == 4:
        view_tasks()
    elif ans == 5:
        view_percentage_completed()
        
# just some data so there is a bit of it inside the data structure     
data['spanish']['weekly_goal'] = 600
data['spanish']['tasks'].append(Task('spanish', 'asd', 34, 1))
data['spanish']['tasks'].append(Task('spanish', 'asd', 23, 1))
data['spanish']['tasks'].append(Task('spanish', 'asd', 2, 1))
data['spanish']['tasks'].append(Task('spanish', 'asd', 7, 1))
data['spanish']['tasks'].append(Task('spanish', 'asd', 64, 1))
