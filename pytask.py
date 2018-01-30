import json
import os
import date_conversions

save_file = './tasks.json'


class Task(object):
    """ A task, it contains the following attributes:
    status = O/X the task is open or done
    text = the actual task
    duedate = when the tasks needs to be finished.
    """

    status = 'O'

    def __init__(self, task_id, text, date):
        """Create a new task, takes an id, text and date."""
        self.task_id = task_id
        self.text = text
        self.duedate = date

    def task_json(self):
        """Return the Task properties in json acceptable format."""
        return {'status': self.status,
                'text': self.text,
                'duedate': self.duedate
                }

    def edit_task_text(self, text):
        """Change the task text."""
        self.text = text

    def edit_task_duedate(self, date):
        """Date needs to be in datetime format."""
        self.duedate = date


class Task_list(object):
    """The list that contains all the tasks.
    It has functions for openingen, saving, adding, deleting tasks.
    """
    task_list = []

    def schow_list(self):
        """Return the list with tasks."""
        return self.task_list

    def save_tasks(self):
        """Save a list of tasks as json file."""
        with open(save_file, 'w') as task_file:
            json.dump(self.task_list, task_file, indent=4, sort_keys=True)

    def open_tasks(self):
        """Read the saved tasks."""
        with open(save_file, 'r') as task_file:
            self.task_list = json.load(task_file)

    def add_task(self):
        """Interactivally add a new task to the task_list."""
        new_task_id = len(self.task_list) + 1
        new_text = input("New task discription: ")
        date_input = input("When does it needs to be done?: ")
        new_duedate = date_conversions.text_to_date(date_input).isoformat()
        new_task = Task((new_task_id), new_text, new_duedate)
        self.task_list.append(new_task.task_json())

    def mark_as_done(self):
        """Mark a task as done."""
        task_id = int(input("Which task is done? (id): "))
        if task_id < len(self.task_list) and task_id >= 0:
            self.task_list[task_id - 1]['status'] = 'X'
        else:
            print(red("Invalid ID!"))

    def print_task(self):
        """Print all tasks."""
        if len(self.task_list) == 0:
            print("No tasks to display yet, create your first task (n)")
        else:
            for item in self.task_list:
                text_due_date = date_conversions.date_to_text(date_conversions.iso_to_date(item["duedate"]))
                print("#" + str(self.task_list.index(item)+1) + " " + item['status'] + " - " + item['text'] + " // finished due: " + text_due_date)

    def edit_task_by_id(self):
        """Edit a task from a task id number."""
        task_id = int(input("which task do you want to edit? (id): "))
        if task_id < len(self.task_list) and task_id >= 0:
            new_text = input("New task discription: ")
            new_duedate = input("When does it needs to be done?: ")
            edited_task = Task(new_text, new_duedate)
            self.task_list[task_id - 1] = edited_task.task_json()
        else:
            print(red("Invalid ID!"))


# Printing helper functions
# color formatting of text
def red(text):
    """Wrap the tekst in red color code: [31m."""
    return "\033[31m" + text + "\033[39m"


def green(text):
    """Wrap the tekst in green color code: [32m."""
    return "\033[32m" + text + "\033[39m"


def yellow(text):
    """Wrap the tekst in yellow color code: [33m."""
    return "\033[33m" + text + "\033[39m"


def blue(text):
    """Wrap the tekst in blue color code: [34m."""
    return "\033[34m" + text + "\033[39m"


# Helptekst
def print_help_tekst():
    """Function to display the general help text."""
    print("Available commands:")
    print("q / quit          exit the pytasks")
    print("h / help          display this help message again")
    print("p / print         print all the current tasks")
    print("e / edit          edit a task by id")
    print("n / new           create a new task")
    print("x / done          mark task as done")
    print("d / del           delete task")
    print(blue("-------------------------------------------------"))


# Main function
def main():
    """Main function."""
    IS_RUNNING = True
    task_list = Task_list()
    if os.path.isfile(save_file):
        task_list.open_tasks()
    else:
        print("No tasks created yet, enter your first new task! (n)")

    while IS_RUNNING:
        user_input = input(blue("Enter command or 'h' for help: \n")).lower()
        if(user_input == 'q' or user_input == 'quit'):
            IS_RUNNING = False
            task_list.save_tasks()
            print(green("Pytask is exiting, all changes are saved. Goodbye!"))

        elif(user_input == 'n' or user_input == 'new'):
            task_list.add_task()

        elif(user_input == 'p' or user_input == 'print'):
            task_list.print_task()

        elif(user_input == 'e' or user_input == 'edit'):
            task_list.edit_task_by_id()

        elif(user_input == 'x' or user_input == 'done'):
            task_list.mark_as_done()

        elif(user_input == 'h' or user_input == 'help'):
            print_help_tekst()

        else:
            print(red("Unknown command stupid!"))
            print_help_tekst


# Run the main function
main()
