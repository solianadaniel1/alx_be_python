#!/usr/bin/python3

task = input("Enter task description")
priority = input("Priority (high/medium/low) ")
time_bound = input("Is it time-bound?(yes/no) ")

match priority:
    case "high":
        if time_bound:
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note:'{task}' is a low priority task. Consider completing it when you have free time.")   
    case "medium":
        if time_bound:
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note:'{task}' is a low priority task. Consider completing it when you have free time.")
            
    case "low":
        if time_bound:
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _: 
        print("Invalid priority level")
