command_list = (
  "Commands you can use after selecting a project:\n"
  "- create_task\n"
  "- add_employee\n"
  "- remove_employee\n"
  "- assign_employee\n"
  "- update_task\n"
  "- delete_task\n"
  "- view_tasks\n"
  "- mark_task_complete\n"
  "- add_project\n"
  "- view_projects\n"
  "- update_project\n"
  "- remove_project"
)

employee_list = []

projects = {}

# TODO: Add a new item to the store
def add_project(project, employees, date, description, tasks):
  projects[project] = {}
  projects[project]['employees'] = []
  projects[project]['completed_tasks'] = []

  for employee in employees:
    if employee in employee_list:
      projects[project]["employees"].append(employee)
    else:
      projects[project]["employees"].append(employee)
      employee_list.append(employee)

  projects[project]["due_date"] = date
  projects[project]["description"] = description
  projects[project]["tasks"] = tasks
  print("\nProject Added\n")

# TODO: Display the items in the store
def view_projects():
  if len(projects) == 0:
    print("\nThere is nothing in your projects.\n")
  else:
    print("\nProjects:\n")
    for project in projects:
      employees = ", ".join(projects[project]["employees"])
      tasks = "\n- ".join(projects[project]["tasks"])

      print(
        f"{project}\n\n"
        f"Employees: {employees}\n\n"
        f"Due Date: {projects[project]['due_date']}\n\n"
        f"Description: {projects[project]['description']}\n\n"
        f"Tasks:\n- {tasks}\n\n"
        '-' * 40
      )
  
  command = input("Command: ").strip()
  run_project_command(command)

# TODO: Change the quantity of an item
def update_quantity(food, quantity):
  projects[food]['quantity'] = quantity
  print("\nUpdated the quantity.\n")

# TODO: Remove an item from the store
def remove_item(food):
    pass

# TODO: Calculate the total and update the store
def checkout(cart):
    pass

# Project command stubs
def create_task():
    pass

def add_employee():
    pass

def remove_employee():
    pass

def assign_employee():
    pass

def update_task():
    pass

def delete_task():
    pass

def view_tasks():
    pass

def mark_task_complete():
    pass

def update_project(project_name):
    if project_name not in projects:
        print("\nThat project does not exist.\n")
        return

    project = projects[project_name]
    employees = ", ".join(project["employees"])
    tasks = "\n- ".join(project["tasks"])

    print(
      f"\nProject: {project_name}\n\n"
      f"Employees: {employees}\n\n"
      f"Due Date: {project['due_date']}\n\n"
      f"Description: {project['description']}\n\n"
      f"Tasks:\n- {tasks}\n\n"
      '-' * 40
    )

    command = input("Command: ").strip()
    run_project_command(command)


def remove_project():
    pass


command_routes = {
    "create_task": create_task,
    "add_employee": add_employee,
    "remove_employee": remove_employee,
    "assign_employee": assign_employee,
    "update_task": update_task,
    "delete_task": delete_task,
    "view_tasks": view_tasks,
    "mark_task_complete": mark_task_complete,
    "add_project": add_project,
    "view_projects": view_projects,
    "update_project": update_project,
    "remove_project": remove_project
}


def run_project_command(command):
    if command in command_routes:
        command_routes[command]()
    elif command:
        print("\nUnknown command.\n")


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print("\n" + "=" * 40)
    print("           Project Management")
    print("=" * 40)

    print("1. Add Project")
    print("2. View Projects")
    print("3. Update Projects")
    print("4. Remove Projects")
    print("5. Add Employee")
    print("6. Command List")
    print("7. Quit")

    choice = input("\nWhat would you like to do? ").strip()

    if choice == "1":
      project = input("\nProject Name: ")
      employees = input("\nAssign Employees (Seperated by a comma and a pace): ").split(", ")
      date = input("\nProject Due Date (MM/DD/YYYY): ")
      description = input("Project Description: ")
      tasks = input("Project Tasks (Seperated by ; and a space): ").split("; ")
      add_project(project, employees, date, description, tasks)

    elif choice == "2":
      view_projects()

    elif choice == "3":
      project_name = input("\nWhich project would you like to update? ").strip()
      update_project(project_name)

    elif choice == "4":
      item = input("\nWhich item would you like to remove? ")
      if item in projects:
        pass
      else:
        print("\nThat is not an item in your projects.\n")
        pass

    elif choice == "5":
        pass

    elif choice == "6":
      print(command_list)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please choose 1-7.")