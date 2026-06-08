import math
import re

def check_length(text):
    return len(text) >= 8

def check_upper(text):
    for ch in text:
        if ch.isupper():
            return True
    return False

def check_lower(text):
    for ch in text:
        if ch.islower():
            return True
    return False

def check_digit(text):
    for ch in text:
        if ch.isdigit():
            return True
    return False

def check_special(text):
    special = "@#$%&*!?"
    for ch in text:
        if ch in special:
            return True
    return False

def common(text):
    common_passwords = ["password", "12345678", "pass1234"]
    for x in common_passwords:
        if text == x:
            return False
    return True

def password_strength(text):
    score = 0

    if not common(text):
        score -= 6

    if check_length(text):
        score += 1
    if check_upper(text):
        score += 1
    if check_lower(text):
        score += 1
    if check_digit(text):
        score += 1
    if check_special(text):
        score += 1

    if score <= 0:
        return "Password not accepted. It is too common."
    elif score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def suggest_password():
    return "Abc@1234"

s = input("ENTER YOUR PASSWORD: ")

result = password_strength(s)
print("Password Strength:", result)

if result == "Password not accepted. It is too common.":
    print("Suggested Password:", suggest_password())






#project 2 to do list

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 3:
                    tasks.append({
                        "task": data[0],
                        "status": data[1],
                        "priority": data[2]
                    })
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['status']}|{task['priority']}\n")

def add_task(tasks):
    name = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    tasks.append({
        "task": name,
        "status": "Pending",
        "priority": priority
    })
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n----- TASK LIST -----")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} | {task['status']} | {task['priority']}")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

def mark_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["status"] = "Completed"
                save_tasks(tasks)
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

def search_task(tasks):
    keyword = input("Enter task to search: ").lower()
    found = False

    for i, task in enumerate(tasks, start=1):
        if keyword in task["task"].lower():
            print(f"{i}. {task['task']} | {task['status']} | {task['priority']}")
            found = True

    if not found:
        print("Task not found.")

def statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = total - completed

    print("\n----- STATISTICS -----")
    print("Total Tasks:", total)
    print("Completed Tasks:", completed)
    print("Pending Tasks:", pending)

tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Search Task")
    print("6. Task Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        mark_task(tasks)
    elif choice == "5":
        search_task(tasks)
    elif choice == "6":
        statistics(tasks)
    elif choice == "7":
        print("Exiting application...")
        break
    else:
        print("Invalid choice. Try again.")