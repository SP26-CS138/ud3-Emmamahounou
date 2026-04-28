'''
DEVELOPER(S): Emma Mahounou
COLLABORATORS: N/A
DATE: 04/17/2025
'''

"""
Campus Assignment Tracker
A program that helps students track assignments for different classes.

This program allows the user to add assignments, view saved assignments,
mark assignments as done, and save assignment data to a file so the data
can still be used the next time the program runs.
I used a dictionary for assignments because each assignment name can connect to a class name.
This makes it easy to save and find each assignment.

I used a list for completed assignments because it can store all assignment names that are done.
This makes it easy to check if an assignment is finished.

"""

##########################################
# IMPORTS:
# <list of modules needed for the program and their purpose>
##########################################
# No imports needed for this program.


##########################################
# FUNCTIONS:
##########################################
def load_assignments():
    """
    Loads saved assignments from the text file.
    Returns the assignments dictionary and completed list.
    """
    assignments = {}
    completed = []

    try:
        file = open("assignments.txt", "r")

        for line in file:
            line = line.strip()
            parts = line.split(",")

            if len(parts) == 3:
                name = parts[0]
                course = parts[1]
                status = parts[2]

                assignments[name] = course

                if status == "done":
                    completed.append(name)

        file.close()

    except FileNotFoundError:
        file = open("assignments.txt", "w")
        file.close()

    return assignments, completed


def save_assignments(assignments, completed):
    """
    Saves all assignments to the text file.
    It also saves if each assignment is done or not done.
    """
    file = open("assignments.txt", "w")

    for name in assignments:
        course = assignments[name]

        if name in completed:
            status = "done"
        else:
            status = "not done"

        file.write(name + "," + course + "," + status + "\n")

    file.close()


def add_assignment(assignments):
    """
    Asks the user to enter an assignment name and class name.
    Adds the assignment to the assignments dictionary.
    """
    name = input("Enter assignment name: ")
    course = input("Enter class name: ")

    assignments[name] = course
    print("Assignment added.")


def view_assignments(assignments, completed):
    """
    Shows all saved assignments.
    It also shows if each assignment is done or not done.
    """
    if len(assignments) == 0:
        print("No assignments saved.")
    else:
        print("\nAssignments:")
        for name in assignments:
            course = assignments[name]

            if name in completed:
                status = "done"
            else:
                status = "not done"

            print(name, "-", course, "-", status)


def mark_done(assignments, completed):
    """
    Asks the user which assignment is done.
    Adds the assignment name to the completed list.
    """
    name = input("Enter the assignment name to mark as done: ")

    if name in assignments:
        if name not in completed:
            completed.append(name)
        print("Assignment marked as done.")
    else:
        print("Assignment not found.")


def menu(assignments, completed):
    """
    Shows the menu options to the user.
    Runs the user's choice until they choose to exit.
    """
    print("\nCampus Assignment Tracker")
    print("1. Add assignment")
    print("2. View assignments")
    print("3. Mark assignment as done")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_assignment(assignments)
        save_assignments(assignments, completed)
        menu(assignments, completed)

    elif choice == "2":
        view_assignments(assignments, completed)
        menu(assignments, completed)

    elif choice == "3":
        mark_done(assignments, completed)
        save_assignments(assignments, completed)
        menu(assignments, completed)

    elif choice == "4":
        save_assignments(assignments, completed)
        print("Goodbye!")

    else:
        print("Invalid choice.")
        menu(assignments, completed)


##########################################
# MAIN PROGRAM:
##########################################
def main():
    assignments, completed = load_assignments()
    menu(assignments, completed)


main()
