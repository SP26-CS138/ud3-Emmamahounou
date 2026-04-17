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
    name = input("Enter assignment name: ")
    course = input("Enter class name: ")

    assignments[name] = course
    print("Assignment added.")


def view_assignments(assignments, completed):
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
    name = input("Enter the assignment name to mark as done: ")

    if name in assignments:
        if name not in completed:
            completed.append(name)
        print("Assignment marked as done.")
    else:
        print("Assignment not found.")


def menu(assignments, completed):
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
