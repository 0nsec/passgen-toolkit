import random
import string
import os

def generate_password_list(length_option, character_type_option, output_filename=None, sequential_start=None, sequential_end=None):
    """
    Generates a password list based on user-defined options and saves to a file if specified.
    Supports sequential number generation with user-defined range and length.

    Args:
        length_option (int): Length of password (1-8, or user-defined for sequential numbers).
        character_type_option (str): Type of characters to include (see function docstring).
        output_filename (str, optional): Filename to save the password list to. Defaults to None (no file saving).
        sequential_start (int, optional): Starting number for sequential generation. Required if character_type_option is 'sequential_numbers'.
        sequential_end (int, optional): Ending number for sequential generation. Required if character_type_option is 'sequential_numbers'.

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
        if sequential_start is None or sequential_end is None:
            return "Error: For sequential numbers, start and end range must be provided."
        if not isinstance(sequential_start, int) or not isinstance(sequential_end, int):
            return "Error: Sequential range start and end must be integers."
        if sequential_start >= sequential_end:
            return "Error: Sequential range start must be less than end."
        if not 1 <= length_option <= 8: # Length restriction still applies for sequential numbers
            return "Error: For sequential numbers, password length should be between 1 and 8."

        for i in range(sequential_start, sequential_end + 1):
            password = str(i).zfill(length_option) # Pad with leading zeros to user-defined length
            password_list.append(password)

        if output_filename:
            os.makedirs("wordlist", exist_ok=True)
            filepath = os.path.join("wordlist", output_filename)
            try:
                with open(filepath, 'w') as f:
                    for password in password_list:
                        f.write(password + '\n')
                return f"Password list saved to: {filepath}"
            except Exception as e:
                return f"Error saving to file: {e}"
        return password_list
    else:
        return ["Invalid character type option."]

    if not 1 <= length_option <= 8:
        return ["Invalid length option. Length should be between 1 and 8."]

    num_passwords = 10000
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for i in range(length_option))
        password_list.append(password)

    if output_filename:
        os.makedirs("wordlist", exist_ok=True)
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
            length_option = int(input("Enter password length (1-8): ")) # Updated prompt - length is now always 1-8
            if not 1 <= length_option <= 8:
                print("Invalid length. Please enter a number between 1 and 8.")
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
    print("9. Sequential numbers (user-defined range and length)") # Updated description

    while True:
        character_choice = input("Choose character type (1-9): ")
        character_type_options_map = {
            '1': 'random',
            '2': 'numbers',
            '3': 'english_lower',
            '4': 'english_upper',
            '5': 'english_both',
            '6': 'alphanumeric_lower',
            '7': 'alphanumeric_upper',
            '8': 'alphanumeric_both',
            '9': 'sequential_numbers'
        }
        character_type_option = character_type_options_map.get(character_choice)
        if character_type_option:
            if character_type_option == 'sequential_numbers':
                while True:
                    try:
                        sequential_start = int(input("Enter starting number for sequential range: "))
                        sequential_end = int(input("Enter ending number for sequential range: "))
                        if sequential_start >= sequential_end:
                            print("Invalid range. Starting number must be less than ending number.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter numbers for the range.")
                break # Valid sequential numbers input
            else:
                break # Valid non-sequential character type
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

    save_to_file = input("\nDo you want to save the password list to a file in the 'wordlist' folder? (yes/no): ").lower()
    output_filename = None
    if save_to_file == 'yes':
        output_filename = input("Enter filename to save (e.g., my_passwords.txt): ")

    if character_type_option == 'sequential_numbers':
        result = generate_password_list(length_option, character_type_option, output_filename, sequential_start, sequential_end)
    else:
        result = generate_password_list(length_option, character_type_option, output_filename)

    if isinstance(result, list):
        if "Invalid" in result[0]:
            print("\nError: " + result[0])
        else:
            print(f"\nGenerated Password List (Length: {length_option}, Type: {character_type_option}):")
            for password in result:
                print(password)
            print(f"\nTotal passwords generated: {len(result)}")
    elif isinstance(result, str):
        print("\n" + result)

