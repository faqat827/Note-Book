def book():
    while True:
        print("\n1 Write")
        print("2 Read")
        print("3 Exit")
        
        try:
            choice = int(input("Select a number 1-3: "))
            
            if choice == 1:
                text = input("Enter text to write: ")
                with open("Write.txt", "a") as f:
                    f.write(text + "\n")
                print("Successfully written!")
                
            elif choice == 2:
                with open("Write.txt", "r") as f:
                    lines = f.readlines()
                    
                    if not lines:
                        print("\nFile is empty.")
                    else:
                        print("\n--- File Content with Line Numbers ---")
                        for line_num, line in enumerate(lines, start=1):
                            print(f"{line_num}: {line.strip()}")
                    
            elif choice == 3:
                print("Exiting...")
                break
                
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                
        except FileNotFoundError:
            print("The file 'Write.txt' does not exist yet.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")

book()