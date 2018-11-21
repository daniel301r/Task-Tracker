# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:41:38 2018

@author: Me
"""

# data structure
data = { 'Spanish': {'weeklyGoal' : 0, 'totalMinutes': 0 },
        'Teaching' : {'weeklyGoal' : 0, 'totalMinutes': 0},
        'Programming' : {'weeklyGoal' : 0, 'totalMinutes': 0}}


def addTask(task):
    if task in data.keys():
        print('How many hours of ' + str(task) + ' do you want to do this week?')
        data[task]['weeklyGoal'] = int(input())
        print('You want to do ' + str(data[task]['weeklyGoal']) + ' hours of Spanish this week')
    else:
        print('You need to enter an existing task - remember, first letter is upper case')
 
def addTime(task):
    while data[task]['totalMinutes'] < data[task]['weeklyGoal'] * 60:
        print('How many minutes of ' + task + ' did you do today?')
        data[task]['totalMinutes'] += int(input())
        
        percentageDone = str((data[task]['totalMinutes'] / (data[task]['weeklyGoal'] * 60)) * 100)
           
        if data[task]['totalMinutes'] < data[task]['weeklyGoal'] * 60:
            print('You have completed ' + percentageDone[0:2] + '% of your target')
            print('Keep going, you can do it!!')
        elif data[task]['totalMinutes'] >= data[task]['weeklyGoal'] * 60:
            print('Well done!! You completed your weekly target')

       
print('What would you like to do this week?')
task = input()
addTask(task)
addTime(task)

