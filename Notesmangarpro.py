notes = {}

def add_note(title, content):
    notes[title] = content
    print(f"Note '{title}' added.")

def view_notes():
    if not notes:
        print("No notes available.")
    else:
        for title, content in notes.items():
            print(f"\nTitle: {title}\nContent: {content}")

def search_note(keyword):
    found = False
    for title, content in notes.items():
        if keyword.lower() in title.lower() or keyword.lower() in content.lower():
            print(f"\nFound in '{title}': {content}")
            found = True
    if not found:
        print("No matching notes found.")

def edit_note(title, new_content):
    if title in notes:
        notes[title] = new_content
        print(f"Note '{title}' updated.")
    else:
        print("Note not found.")

def delete_note(title):
    if title in notes:
        del notes[title]
        print(f"Note '{title}' deleted.")
    else:
        print("Note not found.")

while True:
    print("\n--- Notes Manager Pro ---")
    print("1. Add Note\n2. View Notes\n3. Search Note\n4. Edit Note\n5. Delete Note\n6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif choice == "2":
        view_notes()
    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        search_note(keyword)
    elif choice == "4":
        title = input("Enter note title to edit: ")
        new_content = input("Enter new content: ")
        edit_note(title, new_content)
    elif choice == "5":
        title = input("Enter note title to delete: ")
        delete_note(title)
    elif choice == "6":
        print("Exiting Notes Manager. Stay organized!")
        break
    else:
        print("Invalid choice. Try again.")
