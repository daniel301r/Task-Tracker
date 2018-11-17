# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:41:38 2018

@author: Me
"""

# data structure
data = { 'weeklyGoal' : 0, 'totalMinutes': 0}


#getting the weekly target
print('How many hours of Spanish do you want to do this week?')
data['weeklyGoal'] = int(input())
print('You want to do ' + str(data['weeklyGoal']) + ' hours of Spanish this week')



while data['totalMinutes'] < data['weeklyGoal'] * 60:
    print('How many minutes of Spanish did you do today?')
    data['totalMinutes'] += int(input())
    
    percentageDone = str((data['totalMinutes'] / (data['weeklyGoal'] * 60)) * 100)
       
    if data['totalMinutes'] < data['weeklyGoal'] * 60:
        print('You have completed ' + percentageDone[0:2] + '% of your target')
        print('Keep going, you can do it!!')
    elif data['totalMinutes'] >= data['weeklyGoal'] * 60:

        print('Well done!! You completed your weekly target')