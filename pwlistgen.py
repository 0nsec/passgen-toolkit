import random
import string
import os

# Helper functions for character sets
def _get_chars_random():
    return string.ascii_letters + string.digits + string.punctuation

def _get_chars_numbers():
    return string.digits

def _get_chars_english_lower():
    return string.ascii_lowercase

def _get_chars_english_upper():
    return string.ascii_uppercase

def _get_chars_english_both():
    return string.ascii_letters

def _get_chars_alphanumeric_lower():
    return string.ascii_lowercase + string.digits

def _get_chars_alphanumeric_upper():
    return string.ascii_uppercase + string.digits

def _get_chars_alphanumeric_both():
    return string.ascii_letters + string.digits

# Function to save password list to a file.
def _save_list_to_file(password_list, filename, directory="wordlist"):
    """Saves the given password list to a file in the specified directory."""
    if not filename:
        return "[!] Error: Output filename not provided for saving."
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'w') as f:
            for password in password_list:
                f.write(password + '\n')
        return f"[+] Password list saved to: {filepath}"
    except Exception as e:
        return f"[!] Error saving to file: {e}"

def generate_password_list(length_option, character_type_option, sequential_start=None, sequential_end=None): # output_filename removed
    """
    Generates a password list based on user-defined options.
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

    password_list = []
    characters = ""

    if character_type_option == 'sequential_numbers':
        if sequential_start is None or sequential_end is None:
            return "[!] Error: For sequential numbers, start and end range must be provided."
        if not isinstance(sequential_start, int) or not isinstance(sequential_end, int):
            return "[!] Error: Sequential range start and end must be integers."
        if sequential_start >= sequential_end:
            return "[!] Error: Sequential range start must be less than end."
        if not 1 <= length_option <= 8: # Length restriction still applies
            return "[!] Error: For sequential numbers, password length should be between 1 and 8."

        for i in range(sequential_start, sequential_end + 1):
            password = str(i).zfill(length_option)
            password_list.append(password)
        return password_list # Return the list directly

    # Character set determination using helper functions
    char_set_map = {
        'random': _get_chars_random,
        'numbers': _get_chars_numbers,
        'english_lower': _get_chars_english_lower,
        'english_upper': _get_chars_english_upper,
        'english_both': _get_chars_english_both,
        'alphanumeric_lower': _get_chars_alphanumeric_lower,
        'alphanumeric_upper': _get_chars_alphanumeric_upper,
        'alphanumeric_both': _get_chars_alphanumeric_both,
    }

    if character_type_option in char_set_map:
        characters = char_set_map[character_type_option]()
    else:
        return ["[!] Invalid character type option selected."] # Should be caught by UI ideally

    if not characters: # Should not happen if logic is correct
        return ["[!] Error: Character set is empty."]

    if not 1 <= length_option <= 8: # This check is now primarily for non-sequential
        return ["[!] Invalid length option. Length should be between 1 and 8."]


    num_passwords = 10000 # Default number of passwords for random generation
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for i in range(length_option))
        password_list.append(password)

    return password_list


if __name__ == "__main__":
    # ASCII Art Banner
    banner = """
██████╗ ██╗    ██╗██╗     ██╗██╗ ██████╗██╗  ██╗
██╔══██╗██║    ██║██║     ██║██║██╔════╝██║  ██║
██████╔╝██║ █╗ ██║██║     ██║██║██║     ███████║
██╔═══╝ ██║███╗██║██║     ██║██║██║     ██╔══██║
██║     ╚███╔███╔╝███████╗██║██║╚██████╗██║  ██║
╚═╝      ╚══╝╚══╝ ╚══════╝╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
--------------------------------------https://github.com/0nsec/passgen-toolkit-----------
        Password List Generator v1.0
-------------------------------------------------
"""
    print(banner)
    print("[*] Welcome to the Password List Generator!")
    print("Follow the prompts to generate your custom password list. Press Ctrl+C at any time to exit.\n")

    try:
        # Step 1: Password length
        while True:
            try:
                length_option = int(input("Enter password length (1-8): ").strip())
                if 1 <= length_option <= 8:
                    break
                else:
                    print("[!] Length must be between 1 and 8.")
            except ValueError:
                print("[!] Please enter a valid integer.")

        # Step 2: Character set type
        char_types = [
            ("Random (letters, numbers, symbols)", "random"),
            ("Numbers only (0-9)", "numbers"),
            ("English lowercase letters", "english_lower"),
            ("English uppercase letters", "english_upper"),
            ("English both case letters", "english_both"),
            ("Alphanumeric lowercase (0-9, a-z)", "alphanumeric_lower"),
            ("Alphanumeric uppercase (0-9, A-Z)", "alphanumeric_upper"),
            ("Alphanumeric both case (0-9, a-z, A-Z)", "alphanumeric_both"),
            ("Sequential numbers (user-defined range)", "sequential_numbers")
        ]
        print("\nSelect character set type:")
        for idx, (desc, _) in enumerate(char_types, 1):
            print(f"  {idx}. {desc}")
        while True:
            try:
                type_choice = int(input("Enter option number (1-9): ").strip())
                if 1 <= type_choice <= len(char_types):
                    character_type_option = char_types[type_choice-1][1]
                    break
                else:
                    print(f"[!] Please enter a number between 1 and {len(char_types)}.")
            except ValueError:
                print("[!] Please enter a valid integer.")

        # Step 3: Sequential number range if needed
        sequential_start = None
        sequential_end = None
        if character_type_option == "sequential_numbers":
            print("\nYou selected Sequential Numbers.")
            while True:
                try:
                    sequential_start = int(input("Enter sequential start (integer): ").strip())
                    break
                except ValueError:
                    print("[!] Please enter a valid integer.")
            while True:
                try:
                    sequential_end = int(input("Enter sequential end (integer, greater than start): ").strip())
                    if sequential_end > sequential_start:
                        break
                    else:
                        print("[!] End must be greater than start.")
                except ValueError:
                    print("[!] Please enter a valid integer.")

        # Step 4: Output file
        output_filename = input("\nEnter output filename (leave blank to skip saving to file): ").strip()
        if output_filename == "":
            output_filename = None

        # Step 5: Generate passwords
        print("\n[*] Generating passwords...")
        password_gen_result = generate_password_list(length_option, character_type_option, sequential_start, sequential_end)

        if isinstance(password_gen_result, list):
            if password_gen_result and isinstance(password_gen_result[0], str) and password_gen_result[0].startswith("[!]"):
                print(password_gen_result[0])
            else:
                print(f"[+] Generated Password List (Length: {length_option}, Type: {character_type_option}):")
                print("-" * 40)
                for password in password_gen_result:
                    print(password)
                print("-" * 40)
                print(f"[+] Total passwords generated: {len(password_gen_result)}")
                if output_filename:
                    save_message = _save_list_to_file(password_gen_result, output_filename)
                    print(save_message)
        elif isinstance(password_gen_result, str):
            print(password_gen_result)

        print("\n[*] Done. Thank you for using Password List Generator!")
    except KeyboardInterrupt:
        print("\n[*] Exiting...")
    except Exception as e:
        print(f"[!] Error: {e}")


