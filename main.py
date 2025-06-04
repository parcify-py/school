import os,time

while True:
    os.system('cls')
    print("     TODO MENU \n Add task - 1 \n Print tasks - 2 \n Exit - 3")
    tdp = int(input(" "))
    if tdp == 1:
        os.system('cls')
        task = input("Enter a task: ")
        with open("todo.txt", "a") as file:
            file.write(task + "\n")
        os.system('cls')
        print("Task saved!")
        time.sleep(2)
            
    elif tdp == 2:
        os.system('cls')
        print("\nYour tasks:")
        with open("todo.txt", "r") as file:
            print(file.read())
        time.sleep(1)
        
    elif tdp == 3:
        os.system('cls')
        print('Goodbye')
        time.sleep(1)
        break
    
    
        
        





























