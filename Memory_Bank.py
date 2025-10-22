# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 14:10:49 2025

@author: paulg
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:33:56 2025

@author: paulg
"""

# imported modules
import json
import os


def if_parent():
    """
    Function allows parent to display, create, and clear data within the 
    data text file only returning to the menu on users input.
    """
    
    #create a empty variable for loop choice
    parent_choice = ""
    
    #Starting loop
    while parent_choice != "4":
        try:
            dashes = "-" * 15
            print(f"{dashes} Parent Menu {dashes}")
            print("1) Display")
            print("2) Add")
            print("3) Clear")
            print("4) Menu")
            parent_choice = input("Please select from the options given. ").lower()
            
            #check if user has input 1
            if parent_choice == "1":
                with open("Data.txt", 'r') as file:
                    contents = json.load(file)                
                    print(json.dumps(contents, indent=4))        
            # checks if user selected 2         
            elif parent_choice == "2":
                # Safely checks for existing text file
                if os.path.exists("Data.txt") and os.path.getsize("Data.txt") > 0:
                    with open("Data.txt", 'r') as file:
                        try:
                            contents = json.load(file)
                        except json.JSONDecodeError:
                            contents = {}
                else:
                    contents = {}
                # asks for user name while also checking if user name in txt file
                name = input("What is the students name? ").capitalize()
                if name not in contents:
                    contents[name] = []
                    # user can create up to 5 questions at a time
                    for question in range(5):
                        problem = input(f"Enter a math problem. {question+1}  (or press enter to stop) ").strip()
                        if problem == "":
                            break
                        answer = input("Enter the answer to the problem. ").strip()
                        contents[name].append({"problem": problem, "answer": answer})     
                    
                with open("Data.txt", 'w') as file:
                    json.dump(contents, file, indent=4)
                    print(f"Successfully added record for {name}")
            #checks if user selected 3        
            elif parent_choice == "3":
                # Allows parent user to clear data in file
                with open("Data.txt", 'w') as file:
                    json.dump({}, file, indent=4)
                    print("All Data Cleared.")
            elif parent_choice == "4":
                return
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid option, please select from options given.")
            
            
def if_student():
    """
    Function allows student user to answer question based on the data that the
    parent user has input into the txt file.
    """
    stu_choice = ''
    
    # Asks for students name
    print("Welcome to the Memory Bank")
    stu_name = input("Enter your name ").capitalize() 
    
    # Checks for existing text file
    if os.path.exists("Data.txt") and os.path.getsize("Data.txt") > 0:
        with open("Data.txt", 'r') as file:
            try:
                contents = json.load(file)
            except json.JSONDecodeError:
                contents = {}
    else:
        contents = {}
    # Checks if student name exists in file
    if stu_name in contents:
        problems = contents[stu_name]
        
    elif stu_name not in contents:
            print(f"No problems found for {stu_name}. Please ask a parent for questions.")
            return
    # Ask student if they're ready for quiz    
    print(f"Hello {stu_name}")
    stu_choice = input("Are you ready for your quiz? Yes or No ").lower()
        
    # if yes, the start the quiz    
    if stu_choice == "yes".lower():
        score = 0

        
        # iterates throughout the file index and questions
        for i, q in enumerate(problems, start=1):
            stu_lives = 2
            clear_screen()
            correct = False
            
            while stu_lives > 0 and not correct:                
                print(f"\nQuestion {i}: {q['problem']}")
                stu_answer = input("Your answer: ")
                
                
                # Adds point to sccore if student is correct
                if stu_answer.lower() == q["answer"].lower():
                    print("Correct")
                    score += 1
                    correct = True
                else:
                    stu_lives -= 1
                    if stu_lives > 0:
                        print(f"Incorrect, lives remaining {stu_lives}")
                    else:
                        print("Incorrect, out of lives")

            
            # Shows student result of quiz         
        print(f"Quiz is finished. Your score: {score}/{len(problems)}")            
    elif stu_choice == "no":
        print("Returning to main menu.")
        return
    else:
        print("Invalid Input, Please select from options given.")
                


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    """ Function allows users to display, add, and clear information into a txt 
    with Json formatting. 
    """
    choice = ""
    # Starts while loop here.
    while choice != "3":
        try:
            dashes = "-" * 15
            print("Welcome to the memory bank!")
            print(f"{dashes} MENU {dashes}")
            print("1) Parent")
            print("2) Student")
            print("3) Done")
            choice = input("Please select an option. ")
            
            # Checks if user is either parent or child.
            if choice == "1":
                if_parent()
            elif choice == "2":
                if_student()
            elif choice == "3":
                print("Terminating Program, thanks for playing...Goodbye.")
            else:
                print("Invalid Input, Please select from options given.")
        except ValueError:
            print("Invalid Input, Please select from options given.")

# Calling function               
if __name__ == "__main__":
    main()                
                
        
        
        
        
        
        