from collections import deque

students = {}
stack = []
queue = deque()
tasks = []

# ---------- Linked List ----------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

Hist = LinkedList()

# ---------- Functions ----------
def add_students():
    Student_Id = input("Enter Student ID: ")
    Student_Name = input("Enter Student NAME: ").strip().upper()   # FIX: string formatting
    Student_Age = input("Enter Student Age: ")

    if Student_Id in students:   # IMPROVEMENT: avoid duplicates
        print("Student already exists")
        return

    students[Student_Id] = (Student_Name, Student_Age)
    stack.append(f"Added Student {Student_Id}")   # FIX: spacing
    Hist.add(f"Student Added: {Student_Id}")
    print("Student Added")

def view():
    if not students:   # IMPROVEMENT: empty check
        print("No students found")
        return

    for Student_Id, data in students.items():
        print(Student_Id, ":", data)

def del_student():
    sid = input("Enter Student ID needed to be removed: ")
    if sid in students:
        del students[sid]
        stack.append(f"Deleted Student {sid}")   # FIX: meaningful action
        Hist.add(f"Student Deleted: {sid}")
        print("Deleted")
    else:
        print("Not Found")

def add_Task():
    task = input("Enter Task: ").strip()

    if not task:   # IMPROVEMENT: avoid empty input
        print("Empty task not allowed")
        return

    tasks.append(task)
    queue.append(task)
    stack.append(f"Task Added: {task}")   # FIX: typo "Taskk"
    Hist.add(f"Task Added: {task}")
    print("Task Added")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("Tasks:", tasks)

def process_task():
    if queue:
        t = queue.popleft()
        stack.append(f"Processed Task: {t}")
        Hist.add(f"Task Processed: {t}")
        print(f"Processed: {t}")
    else:
        print("Nothing to Do")

def undo():
    if stack:
        action = stack.pop()
        print(f"Undo: {action}")
        Hist.add(f"Undo: {action}")   # IMPROVEMENT: consistent message
    else:
        print("Nothing to Undo")

def show_history():
    Hist.display()

# ❌ REMOVED: empty function (causes error)
# def Repeat():

# ---------- Menu ----------
while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Add Task")
    print("5. View Task")
    print("6. Process task")
    print("7. Undo")
    print("8. Show History")
    print("9. Exit")

    c = input("Enter your Choice: ")

    if c == '1':
        add_students()
    elif c == '2':
        view()
    elif c == '3':
        del_student()
    elif c == '4':
        add_Task()
    elif c == '5':
        view_tasks()
    elif c == '6':
        process_task()
    elif c == '7':
        undo()
    elif c == '8':
        show_history()
    elif c == '9':
        break
    else:
        print("Invalid Choice")   # FIX: message1
        