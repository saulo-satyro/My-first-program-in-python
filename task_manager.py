#Heyy, I created this task manager for you to keep your tasks, but actually, it's more for me to look at in the future and see that I improved lol, in the future I intend to improve this task manager, so, enjoy it!
task_list = []

def display_menu():
 print("--- TASK MANAGER ---")
 print("1. Add task ")
 print("2. View tasks ")
 print("3. Remove task ")
 print("4. Exit ")
 return input("Choose an option: ")

 

while True:
 option = display_menu()

 if option == "1":
  task = input("Enter a task: ")
  task_list.append(task)
  print("Task added successfully!")
  
 elif option == "2":
  print("--- YOUR TASKS ---")
  if not task_list:
   print("The list is empty.")
  else:
   for index, task in enumerate(task_list, start=1):
    print(f"{index}. {task}")

 elif option == "3":
  if not task_list:
   print("Nothing to remove")
  else:
   try:
    for i, t in enumerate(task_list, start=1):
     print(f"{i}. {t}")

     index_to_remove = int(input("Enter the task number to remove"))
     removed_task = task_list.pop(index_to_remove - 1)
     print(f"Task '{removed_task}' removed!")
   except (ValueError, IndexError):
      print("Invalid number! Please try again.")
    
 elif option == "4":
  print("Exiting... See you later!")
  break
 
 else: 
  print("Invalid option, please try again.")