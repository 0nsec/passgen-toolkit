import random
import string
import os

def generate_password_list(length_option, character_type_option, output_filename=None):
    """
    Generates a password list based on user-defined options and saves to a file if specified.

    Args:
        length_option (int): Length of password (1-8).
        character_type_option (str): Type of characters to include (see function docstring).
        output_filename (str, optional): Filename to save the password list to. Defaults to None (no file saving).

    Returns:
        list or str: A list of passwords if not saving to file, or a success/error message string.
    """

    password_list = []
    characters = ""

    if character_type_option == 'random':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif character_type_option == 'numbers':
        characters = string.digits
    elif character_type_option == 'english_lower':
        characters = string.ascii_lowercase
    elif character_type_option == 'english_upper':
        characters = string.ascii_uppercase
    elif character_type_option == 'english_both':
        characters = string.ascii_letters
    elif character_type_option == 'alphanumeric_lower':
        characters = string.ascii_lowercase + string.digits
    elif character_type_option == 'alphanumeric_upper':
        characters = string.ascii_uppercase + string.digits
    elif character_type_option == 'alphanumeric_both':
        characters = string.ascii_letters + string.digits
    elif character_type_option == 'sequential_numbers':
        if length_option != 4:
            return "Error: Sequential numbers option requires password length to be exactly 4."
        for i in range(10000): # 0000 to 9999
            password = str(i).zfill(4) # Pad with leading zeros to ensure 4 digits
            password_list.append(password)
        if output_filename:
            os.makedirs("wordlist", exist_ok=True) # Create 'wordlist' folder if it doesn't exist
            filepath = os.path.join("wordlist", output_filename)
            try:
                with open(filepath, 'w') as f:
                    for password in password_list:
                        f.write(password + '\n')
                return f"Password list saved to: {filepath}"
            except Exception as e:
                return f"Error saving to file: {e}"
        return password_list # Return list even if saving failed for sequential numbers (for console output)
    else:
        return ["Invalid character type option."]

    if not 1 <= length_option <= 8:
        return ["Invalid length option. Length should be between 1 and 8."]

    num_passwords = 10000 # Generating a reasonable number of passwords for demonstration
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for i in range(length_option))
        password_list.append(password)

    if output_filename:
        os.makedirs("wordlist", exist_ok=True) # Create 'wordlist' folder if it doesn't exist
        filepath = os.path.join("wordlist", output_filename)
        try:
            with open(filepath, 'w') as f:
                for password in password_list:
                    f.write(password + '\n')
            return f"Password list saved to: {filepath}"
        except Exception as e:
            return f"Error saving to file: {e}"
    else:
        return password_list


if __name__ == "__main__":
    print("Password List Generator Script")
    print("==============================\n")

    while True:
        try:
            length_option = int(input("Enter password length (1-8, or 4 for sequential numbers): "))
            if not 1 <= length_option <= 8 and length_option != 4: # Allow 4 for sequential later
                print("Invalid length. Please enter a number between 1 and 8, or 4 for sequential numbers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nCharacter Type Options:")
    print("1. Random (numbers, letters, symbols)")
    print("2. Numbers only (0-9)")
    print("3. English lowercase letters")
    print("4. English uppercase letters")
    print("5. English both case letters")
    print("6. Numbers and lowercase letters")
    print("7. Numbers and uppercase letters")
    print("8. Numbers, uppercase, and lowercase letters")
    print("9. Sequential numbers (0000-9999, length must be 4)") # Added sequential option

    while True:
        character_choice = input("Choose character type (1-9): ") # Updated to 1-9
        character_type_options_map = {
            '1': 'random',
            '2': 'numbers',
            '3': 'english_lower',
            '4': 'english_upper',
            '5': 'english_both',
            '6': 'alphanumeric_lower',
            '7': 'alphanumeric_upper',
            '8': 'alphanumeric_both',
            '9': 'sequential_numbers' # Added sequential option
        }
        character_type_option = character_type_options_map.get(character_choice)
        if character_type_option:
            if character_type_option == 'sequential_numbers' and length_option != 4:
                print("Error: Sequential numbers option requires password length to be exactly 4. Please re-enter length and character type.")
                while True: # Re-enter length specifically for sequential numbers
                    try:
                        length_option = int(input("Enter password length (must be 4 for sequential numbers): "))
                        if length_option != 4:
                            print("Invalid length for sequential numbers. Please enter 4.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                continue # Go back to character type choice after fixing length

            break # Valid character type and length (or sequential numbers with correct length)
        else:
            print("Invalid choice. Please enter a number between 1 and 9.") # Updated to 1-9

    save_to_file = input("\nDo you want to save the password list to a file in the 'wordlist' folder? (yes/no): ").lower()
    output_filename = None
    if save_to_file == 'yes':
        output_filename = input("Enter filename to save (e.g., my_passwords.txt): ")

    result = generate_password_list(length_option, character_type_option, output_filename)

    if isinstance(result, list): # If result is a list, it's a password list (not saving to file or sequential numbers not saved to file)
        if "Invalid" in result[0]: # Check for error message
            print("\nError: " + result[0])
        else:
            print(f"\nGenerated Password List (Length: {length_option}, Type: {character_type_option}):")
            for password in result:
                print(password)
            print(f"\nTotal passwords generated: {len(result)}")
    elif isinstance(result, str): # If result is a string, it's a message (success or error from file saving or sequential numbers)
        print("\n" + result)
