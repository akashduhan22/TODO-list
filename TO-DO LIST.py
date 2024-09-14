
todo=[]
def add():
    print("you can add total 10 tasks into TO-DO List")
    print()
    for k in range(1,11):
        if k>0:
            enter=input("Enter your task:-")
            print()
            end=input("Enter MORE to add tasks or DONE to end adding tasks:-").lower()
            todo.append(enter)
            if end=="more":
                print()
                print("That task is added now add another task")
                print()
            elif end=="done":
                print()
                print("thanks for adding the tasks")
                print()
                tasks()
            else:
                print()
                print("Enter a proper message")
                print()
                tasks()
            remaining=10-k
            if remaining>0:
                print()
                print(f"Now you can add {remaining} tasks only.")
                print()
            else:
                print()
                print("you can't add more tasks")
                print()
                tasks()
        else:
            print()
            print("Your list is full you can't add more tasks")
            print()

def rem():
    end=input("Enter MORE to remove more tasks or DONE to end removing tasks or CLEAR to clear list:-")    
    if end =="more":
        remove()
    elif end=="done":
        print()
        print("thanks for removing task")
        print()
        tasks()
    elif end=="clear":
        todo.clear()
        print("Your list is cleared")
        tasks()
    else:
        print("Enter a proper message")
        remove()
    remaining=len(todo)
    if remaining>0:
        print(f"Yoh have remaining {remaining} tasks.")
    else:
        print("the list is empty you can't remove more tasks")
        tasks()



def remove():
    removed=input("enter the name of the task you want to remove from the list:-").lower()
    print()
    if removed in todo:
        todo.remove(removed)
        print()
        print("okay that task is removed now remove another task")
        print()
        rem()
    else:
        print()
        print("this task is not into your list")
        rem()
        print()
    rem()
    print()


        
def tasks():
    user=input("Enter add/remove/display to apply operations on list:").lower()
    print()
    if user=="add":
        add()
    elif user=="remove":
        if len(todo)>0:
            remove()
        else:
            print()
            print("sorry your list is empty")
            print()
            tasks()
    elif user=="display":
        if len(todo)>0:
            print("Your list is")
            print()
            for i,j in enumerate(todo,1):
                print(f"{i}.{j}")
            tasks()
        else:
            print()
            print("sorry your list is empty")
            print()
            tasks()
    else:
        print("Enter valid command")
        tasks()
tasks()
















