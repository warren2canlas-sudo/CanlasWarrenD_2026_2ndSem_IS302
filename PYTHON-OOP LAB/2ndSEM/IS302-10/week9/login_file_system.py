def apd_register():
    apd_username = input("Create username: ")
    apd_password = input("Create password: ")
    
    with open("users.txt", "a") as apd_file:
        # I-save ang username at password na may separator
        apd_file.write(f"{apd_username},{apd_password}\n")
    print("Registration successful!")

def apd_login():
    apd_username = input("Username: ")
    apd_password = input("Password: ")
    apd_success = False

    try:
        with open("users.txt", "r") as apd_file:
            for apd_line in apd_file:
                # Paghiwalayin ang username at password sa file
                apd_stored_user, apd_stored_pass = apd_line.strip().split(",")
                
                if apd_username == apd_stored_user and apd_password == apd_stored_pass:
                    apd_success = True
                    break
        
        if apd_success:
            print("Login successful! Welcome.")
        else:
            print("Invalid username or password.")
            
    except FileNotFoundError:
        print("No users registered yet.")

# Main Menu Loop
while True:
    print("\n1 Register\n2 Login\n3 Exit")
    apd_choice = input("Select an option: ")

    if apd_choice == "1":
        apd_register()
    elif apd_choice == "2":
        apd_login()
    elif apd_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")