from collections import deque

students={}
stack=[]
queue=deque()
tasks=[]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self,data):
            new=Node(data)
            if not self.head:
                self.head=new
            else:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=new
    def display(self):
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp = temp.next 
            print("None")

Hist = LinkedList()

def add_students():
    Student_Id = input("Enter Student ID: ")
    Student_Name = input("Enter Student NAME: ")
    Student_Age = input("Enter Student Age: ")
    students[Student_Id] = (Student_Name,Student_Age)
    stack.append(f"Added Student{Student_Id}")
    Hist.add(f"StudentID Added: {Student_Id}")
    print("Student Added")

def view():
    for Student_Id,data in students.items():
        print(Student_Id ,":", data)

def del_student():
    sid=input("Enter Student ID needed to Be removed: " )
    if sid in students:
        del students[sid]
        stack.append(sid)
        Hist.add(sid)
        print("Deleted")
    else:
        print("None Found")

def add_Task():
    task=input("Enter Task: ").strip()
    tasks.append(task)
    queue.append(task)
    stack.append(f"Taskk Added: {task}")
    Hist.add(f"Added Task: {task}")
    print("Task Added")

def view_tasks():
    print("Tasks: ",tasks)

def process_task():
    if queue:
        t=queue.popleft()
        stack.append(f"Processed Task: {t}")
        Hist.add(f"Task Processed: {t}")
        print(f"Processed: {t}")

    else:         print("Nothing to Do")

def undo():
    if stack:
        action = stack.pop()
        print(f"Undo: {action}")
        Hist.add(f"Undo performed: {action}")
    else:
        print("Nothing to Undo")

def show_history():
    Hist.display()

while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Add Task")
    print("5. View Task")
    print('6. Process task')
    print('7. Undo')
    print('8. Show History'       )
    print('9. Exit')

    c = input("Enter your Choice: ")

    if c =='1':
        add_students()
    elif c== '2':
        view()
    elif c == '3':
        del_student()
    elif c == '4':
        add_Task()
    elif c == '5':
        view_tasks()
    elif c=='6':
        process_task()
    elif c== '7':
        undo()
    elif c == '8':
        show_history()
    elif c == '9':
        break

    else:
        print("Invalid Code")