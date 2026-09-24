from rich import print
from rich.console import Console

console = Console()

command_list = (
  "Commands you can use after selecting a project:\n"
  "- create_task\n"
  "- add_employee\n"
  "- remove_employee\n"
  "- update_task\n"
  "- delete_task\n"
  "- complete_task\n"
  "- change_due_date\n"
  "- add_project\n"
  "- view_projects\n"
  "- remove_project\n"
  "- home"
)

employee_list = []

projects = {}

# Commands functions
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
    print("\n[green]Project Added[/green]\n")


def add_project_command():
    project = input("\nProject Name: ")
    employees = input("\nAssign Employees (Separated by a comma and a space): ").split(", ")
    date = input("\nProject Due Date (MM/DD/YYYY): ")
    description = input("\nProject Description: ")
    tasks = input("\nProject Tasks (Separated by ; and a space): ").split("; ")
    add_project(project, employees, date, description, tasks)

def view_projects():
    if len(projects) == 0:
        print("\n[red]There is nothing in your projects.[/red]\n")
        pass
    else:
        print("\n[bold gray]Projects:[/bold gray]\n")
        for project in projects:
            employees = ", ".join(projects[project]["employees"])
            tasks = "\n- ".join(projects[project]["tasks"])
            completed_tasks = "\n- ".join(projects[project]["completed_tasks"]) if projects[project]["completed_tasks"] else "None"

            print(
            f"[bold gray]{project}[/bold gray]\n\n"
            f"[bold]Employees:[/bold] {employees}\n\n"
            f"[bold]Due Date:[/bold] {projects[project]['due_date']}\n\n"
            f"[bold]Description:[/bold] {projects[project]['description']}\n\n"
            f"[bold]Tasks:[/bold]\n- {tasks}\n\n"
            f"[bold]Completed Tasks:[/bold]\n[green]- {completed_tasks}[/green]\n\n"
            + '-' * 40
            )
    project_command_loop()

def create_task():
    task_name = input("\nTask name: ").strip()
    project_name = input("\nProject name: ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    projects[project_name]["tasks"].append(task_name)
    print(f"\n[green]Task '{task_name}' added to {project_name}.[/green]\n")


def add_employee():
    employee_name = input("\nEmployee name: ").strip()
    project_name = input("\nProject name: ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    if employee_name not in projects[project_name]["employees"]:
        projects[project_name]["employees"].append(employee_name)
        if employee_name not in employee_list:
            employee_list.append(employee_name)
    print(f"\n[green]Employee '{employee_name}' added to {project_name}.[/green]\n")


def remove_employee():
    employee_name = input("\nEmployee name: ").strip()
    project_name = input("\nProject name: ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    if employee_name in projects[project_name]["employees"]:
        projects[project_name]["employees"].remove(employee_name)
        print(f"\n[green]Employee '{employee_name}' removed from {project_name}.[/green]\n")
    else:
        print("\n[red]That employee is not assigned to this project.[/red]\n")


def update_task():
    project_name = input("\nProject name: ").strip()
    old_task = input("\nTask to update: ").strip()
    new_task = input("\nNew task name: ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    if old_task in projects[project_name]["tasks"]:
        index = projects[project_name]["tasks"].index(old_task)
        projects[project_name]["tasks"][index] = new_task
        print(f"\n[green]Task updated in {project_name}.[/green]\n")
    else:
        print("\n[red]That task is not in this project.[/red]\n")


def change_due_date():
    project_name = input("\nProject name: ").strip()
    new_date = input("\nNew project due date (MM/DD/YYYY): ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    else:
        projects[project_name]["due_date"] = new_date
        print(f"\n[green]Due date changed for {project_name}.[/green]\n")


def delete_task():
    project_name = input("\nProject name: ").strip()
    task_name = input("\nTask to delete: ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    if task_name in projects[project_name]["tasks"]:
        projects[project_name]["tasks"].remove(task_name)
        print(f"\n[green]Task '{task_name}' deleted from {project_name}.[/green]\n")
    else:
        print("\n[red]That task is not in this project.[/red]\n")


def mark_task_complete():
    project_name = input("\nProject name: ").strip()
    task_name = input("\nTask to mark complete: ").strip()
    if project_name not in projects:
        print("\n[red]That project does not exist.[/red]\n")
        return
    if task_name in projects[project_name]["tasks"]:
        projects[project_name]["completed_tasks"].append(task_name)
        projects[project_name]["tasks"].remove(task_name)
        print(f"\n[green]Task '{task_name}' marked complete in {project_name}.[/green]\n")
    else:
        print("\n[red]That task is not in this project.[/red]\n")


def remove_project():
    project_name = input("\nProject name: ").strip()
    if project_name in projects:
        del projects[project_name]
        print(f"\n[green]Project '{project_name}' removed.[/green]\n")
    else:
        print("\n[red]That project does not exist.[/red]\n")


def view_employees():
    if not employee_list:
        print("\n[red]There are no employees yet.[/red]\n")
    else:
        print("\n[bold gray]Employees:[/bold gray]")
        for employee in employee_list:
            print(f"- {employee}")


def home():
  pass

# Command loop
command_routes = {
    "create_task": create_task,
    "add_employee": add_employee,
    "remove_employee": remove_employee,
    "update_task": update_task,
    "delete_task": delete_task,
    "complete_task": mark_task_complete,
    "change_due_date": change_due_date,
    "add_project": add_project_command,
    "view_projects": view_projects,
    "remove_project": remove_project,
    "home": home
}


def run_project_command(command):
    if command in command_routes:
        command_routes[command]()
    elif command:
        print("\n[red]Unknown command.[/red]\n")


def project_command_loop():
  while True:
    command = input("Command: ").strip()
    if command.lower() == "home":
      return
    run_project_command(command)

# Main loop
while True:

    print("\n" + "=" * 40)
    print("           Project Management")
    print("=" * 40)

    print("1. Add Project")
    print("2. View Projects")
    print("3. View Employees")
    print("4. Command List")
    print("5. Quit")

    choice = input("\nWhat would you like to do? ").strip()

    if choice == "1":
        project = input("\nProject Name: ")
        employees = input("\nAssign Employees (Seperated by a comma and a pace): ").split(", ")
        date = input("\nProject Due Date (MM/DD/YYYY): ")
        description = input("\nProject Description: ")
        tasks = input("\nProject Tasks (Seperated by ; and a space): ").split("; ")
        add_project(project, employees, date, description, tasks)

    elif choice == "2":
        view_projects()

    elif choice == "3":
        view_employees()

    elif choice == "4":
        print(command_list)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("\n[red]Invalid choice. Please choose 1-5.[/red]")