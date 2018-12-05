# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:36:56 2018

@author: Me
"""

data = { 'spanish': {'weekly_goal' : 0, 'total_minutes': 0, 'tasks' : [] },
        'teaching' : {'weekly_goal' : 0, 'total_minutes': 0, 'tasks' : []}, 
        'programming' : {'weekly_goal' : 0, 'total_minutes': 0, 'tasks' : []}}

class Task:
    def __init__(self, field, description, time, num):
        self.field = field
        self.description = description
        self.time = time
        self.num = num

def set_weekly_goal():
    print("What weekly goal would you like to set?")
    field = input()
    if field in data.keys():
        print(f"How many hours of {field} do you want to do?")
        data[field]['weekly_goal'] = int(input())
        print(f"You want to do {data[field]['weekly_goal']} hours of {field} this week")     
    else:
        print(f"{field[0].upper() + field[1:]} is not in your weekly goals")
    
         
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
        
def delete_task():
    print("What type of task do you want to delete?")
    field = input()
    print("Have a look at the list of tasks and then delete its number")
    for num in data[field]['tasks']:
        print(f"{num.num} {num.description} {num.time} minutes")
     
    # get the number
    delete_num = int(input())
    
    # find index of task in list
    # ** returning the else statement before deleting the object from the list
    for task in data[field]["tasks"]:
        if task.num == delete_num:
            task_index = data[field]["tasks"].index(task)
            data[field]['tasks'].pop(task_index)
            print("Deleted Item")
        else:
            print("You entered a wrong number")

            
def view_tasks():
    print("What type of tasks do you want to see?")
    print("If you want to see all of them type 'all'")
    response = input()
    if respsonse == "all":
        for field in data:
            ## nested loop to print all of the tasks
   
    
    


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
    

    
    

# questions

# what would you like to do
# 1. set goals for the week
# 1. add task
# 2. delete task
# 3. view tasks from this week - spanish, teaching, programming
# 4. view percentage of goal completed
