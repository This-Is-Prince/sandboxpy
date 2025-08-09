from diary.diary_manager import DiaryManager

def print_menu():
    """Prints the main menu options."""
    print("\n--- Personal Diary Manager ---")
    print("1. Add New Entry")
    print("2. View All Entry Titles")
    print("3. Read an Entry")
    print("4. Search Entries")
    print("5. Exit")
    print("----------------------------")

def main():
    """The main application loop."""
    diary = DiaryManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            diary.add_entry(title, content)

        elif choice == "2":
            print("\n--- All Entries ---")
            titles = diary.list_titles()
            for title in titles:
                print(title)
        
        elif choice == "3":
            try:
                entry_num = int(input("Enter entry number to read: "))
                entry = diary.get_entry(entry_num - 1)
                if entry:
                    print("\n--- Entry Details ---")
                    print(entry)
                else:
                    print("Invalid entry number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            keyword = input("Enter search keyword: ")
            results_generator = diary.search_entries(keyword)
            for entry in results_generator:
                print("\n--- Found Match ---")
                print(entry)
            
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()