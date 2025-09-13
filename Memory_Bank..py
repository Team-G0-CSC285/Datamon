# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:33:56 2025

@author: paulg
"""
import json


def Memory_bank():
    """ Function allows users to display, add, and clear information into a txt 
    with Json formatting. 
    """
    choice = ""
    # Starts while loop here.
    while choice != "exit":
        
        # Asks user for input
        print("Welcome to the memory bank")
        choice = input("Please select a option (display, add, clear, or exit) ").lower()
        
        # Allows user to display txt file in a json format
        if choice == "display":
            with open ("Data.txt", "r") as dt:
                player = json.load(dt)
                for name, details in player.items():
                    print(f"{name}: problem: {details['problem']} answer: {details['answer']} correct: {details['correct']}")
        # Allows user to add info to txt file via input
        elif choice == "add":
            with open ("Data.txt", "r") as dt:
                player = json.load(dt)
               
                name = input("Enter player's name. ")
                problem = input("Enter the problem given. ")
                user_answer = input("Enter player's answer. ")
                check_answer = input("Was the answer correct? (true for yes, false for no.) ")
               
                player[name] = {"problem": problem, "answer": user_answer, "correct": check_answer}
               
                with open ("Data.txt", "w") as dt:
                    json.dump(player, dt, indent=4)
                    print("data added successfully")
        # Allows user to clear all data from the txt file
        elif choice == "clear":
                with open ("Data.txt" , "w") as dt:
                    json.dump({}, dt, indent=4)
                    print("Memory cleared")
        elif choice == "exit":
                print("Terminating program...goodbye")
                break
        else:
            print("Invalid input, please select from options given")
            
# Calling function               
Memory_bank()                
                
        
        
        
        
        
        