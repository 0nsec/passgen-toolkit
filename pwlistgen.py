import random
import string

def generate_password_list(length_option, character_type_option):
    """
    Generates a password list based on user-defined options.

    Args:
        length_option (int): Length of password (1-8).
        character_type_option (str): Type of characters to include:
            - 'random': Random characters (numbers, letters, symbols).
            - 'numbers': Only numbers (0-9).
            - 'english_lower': Lowercase English letters.
            - 'english_upper': Uppercase English letters.
            - 'english_both': Uppercase and lowercase English letters.
            - 'alphanumeric_lower': Numbers and lowercase English letters.
            - 'alphanumeric_upper': Numbers and uppercase English letters.
            - 'alphanumeric_both': Numbers, uppercase, and lowercase English letters.

    Returns:
        list: A list of passwords.
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
    else:
        return ["Invalid character type option."]

    if not 1 <= length_option <= 8:
        return ["Invalid length option. Length should be between 1 and 8."]

    num_passwords = 10000 # Generating a reasonable number of passwords for demonstration
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for i in range(length_option))
        password_list.append(password)
    return password_list

if __name__ == "__main__":
    print("Password List Generator Script")
    print("==============================\n")

    while True:
        try:
            length_option = int(input("Enter password length (1-8): "))
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

    while True:
        character_choice = input("Choose character type (1-8): ")
        character_type_options_map = {
            '1': 'random',
            '2': 'numbers',
            '3': 'english_lower',
            '4': 'english_upper',
            '5': 'english_both',
            '6': 'alphanumeric_lower',
            '7': 'alphanumeric_upper',
            '8': 'alphanumeric_both'
        }
        character_type_option = character_type_options_map.get(character_choice)
        if character_type_option:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    password_list = generate_password_list(length_option, character_type_option)

    if "Invalid" in password_list[0]: # Check for error message
        print("\nError: " + password_list[0])
    else:
        print(f"\nGenerated Password List (Length: {length_option}, Type: {character_type_option}):")
        for password in password_list:
            print(password)
        print(f"\nTotal passwords generated: {len(password_list)}")

