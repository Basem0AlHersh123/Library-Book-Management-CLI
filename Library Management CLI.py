import os
import time

library_catalog = {}

menu = """
📚 Library Menu:
1. Add Book
2. Check Out Book
3. Check In Book
4. Show Catalog
5. Exit
"""

def clear_screen():
    os.system('cls' if os.name == "nt" else "clear")

def add_book():
    while True:
        clear_screen()
        try:
            isbn = int(input('Enter the ISBN (number): '))
        except ValueError:
            print("❌ Invalid ISBN. Please enter a number.")
            time.sleep(2)
            continue
        title = input('Enter the book title: ').strip()
        author = input('Enter the author name: ').strip()
        library_catalog[isbn] = {
            "Title": title,
            "Author": author,
            "Available": True,
        }
        print(f"✅ Book '{title}' by {author} added to the catalog with ISBN {isbn}.")
        if input('Add another book? (y/n): ').lower() != 'y':
            break

def check_out_book():
    while True:
        clear_screen()
        try:
            isbn = int(input('Enter ISBN to check out: '))
        except ValueError:
            print("❌ Invalid ISBN. Please enter a number.")
            time.sleep(2)
            continue
        if isbn in library_catalog:
            if library_catalog[isbn]['Available']:
                library_catalog[isbn]['Available'] = False
                print(f"✅ Book '{library_catalog[isbn]['Title']}' checked out successfully.")
            else:
                print("⚠️ Sorry, the book is currently checked out.")
        else:
            print("❌ Sorry, the book is not found in the catalog.")
        if input('Check out another book? (y/n): ').lower() != 'y':
            break

def check_in_book():
    while True:
        clear_screen()
        try:
            isbn = int(input('Enter ISBN to check in: '))
        except ValueError:
            print("❌ Invalid ISBN. Please enter a number.")
            time.sleep(2)
            continue
        if isbn in library_catalog:
            if not library_catalog[isbn]['Available']:
                library_catalog[isbn]['Available'] = True
                print(f"✅ Book '{library_catalog[isbn]['Title']}' checked in successfully.")
            else:
                print("⚠️ The book is already checked in.")
        else:
            print("❌ Sorry, the book is not found in the catalog.")
        if input('Check in another book? (y/n): ').lower() != 'y':
            break

def show_catalog():
    clear_screen()
    if not library_catalog:
        print("📭 The catalog is empty.")
    else:
        print("📖 Library Catalog:\n")
        for isbn, info in library_catalog.items():
            status = "Available" if info['Available'] else "Checked Out"
            print(f"ISBN: {isbn}, Title: {info['Title']}, Author: {info['Author']}, Status: {status}")
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        clear_screen()
        choice = input(menu + "\nEnter your choice (1-5): ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            check_out_book()
        elif choice == "3":
            check_in_book()
        elif choice == "4":
            show_catalog()
        elif choice == "5":
            print("👋 Exiting the program. Goodbye!")
            time.sleep(2)
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")
            time.sleep(2)

if __name__ == "__main__":
    main()
