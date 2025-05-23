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

# Function to save password list to a file
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
-------------------------------------------------
        Password List Generator v1.0
-------------------------------------------------
"""
    print(banner)
    print("[*] Starting Password List Generator...")

    # Initialize parameters
    length_option = None
    character_type_option = None
    output_filename = None
    sequential_start = None
    sequential_end = None

    while True:
        try:
            command_input = input(">>> ").strip().lower()
            command_parts = command_input.split()
            command = command_parts[0]

            if command == "exit":
                print("[*] Exiting...")
                break
            elif command == "help":
                print("\n[*] Available commands:")
                print("  set length <value>                - Sets the password length (must be between 1 and 8).")
                print("                                    Example: set length 8")
                print("  set type <option_keyword_or_number> - Sets the character type for password generation.")
                print("                                    Options:")
                print("                                      1 or random: Random (letters, numbers, symbols)")
                print("                                      2 or numbers: Numbers only (0-9)")
                print("                                      3 or english_lower: English lowercase letters")
                print("                                      4 or english_upper: English uppercase letters")
                print("                                      5 or english_both: English lower and uppercase letters")
                print("                                      6 or alphanumeric_lower: Lowercase letters and numbers")
                print("                                      7 or alphanumeric_upper: Uppercase letters and numbers")
                print("                                      8 or alphanumeric_both: Lowercase, uppercase letters, and numbers")
                print("                                      9 or sequential_numbers: Sequential numbers (requires sequential_start and sequential_end)")
                print("                                    Example: set type random")
                print("                                    Example: set type 3")
                print("  set output <filename>             - Sets the filename to save the generated password list.")
                print("                                    The file will be saved in the 'wordlist' directory.")
                print("                                    Example: set output my_passwords.txt")
                print("  set sequential_start <value>      - Sets the starting number for sequential number generation.")
                print("                                    Required if type is 'sequential_numbers'. Must be an integer.")
                print("                                    Example: set sequential_start 100")
                print("  set sequential_end <value>        - Sets the ending number for sequential number generation.")
                print("                                    Required if type is 'sequential_numbers'. Must be an integer and greater than sequential_start.")
                print("                                    Example: set sequential_end 200")
                print("  generate                          - Generates the password list based on the current settings.")
                print("                                    Requires length and type to be set.")
                print("                                    If type is 'sequential_numbers', sequential_start and sequential_end must also be set.")
                print("  help                              - Shows this help message.")
                print("  exit                              - Exits the Password List Generator script.")
                print("-" * 40)
            elif command == "set":
                if len(command_parts) > 1:
                    param = command_parts[1]
                    if param == "length":
                        if len(command_parts) == 3:
                            try:
                                value = int(command_parts[2])
                                if 1 <= value <= 8:
                                    length_option = value
                                    print(f"[*] Length set to: {length_option}")
                                else:
                                    print("[!] Invalid length. Length should be between 1 and 8.")
                            except ValueError:
                                print("[!] Invalid length value. Must be an integer.")
                        else:
                            print("[!] Missing value for length.")
                        print("-" * 40)
                    elif param == "type":
                        if len(command_parts) == 3:
                            value = command_parts[2]
                            character_type_options_map = {
                                '1': 'random', 'random': 'random',
                                '2': 'numbers', 'numbers': 'numbers',
                                '3': 'english_lower', 'english_lower': 'english_lower',
                                '4': 'english_upper', 'english_upper': 'english_upper',
                                '5': 'english_both', 'english_both': 'english_both',
                                '6': 'alphanumeric_lower', 'alphanumeric_lower': 'alphanumeric_lower',
                                '7': 'alphanumeric_upper', 'alphanumeric_upper': 'alphanumeric_upper',
                                '8': 'alphanumeric_both', 'alphanumeric_both': 'alphanumeric_both',
                                '9': 'sequential_numbers', 'sequential_numbers': 'sequential_numbers'
                            }
                            if value in character_type_options_map:
                                character_type_option = character_type_options_map[value]
                                print(f"[*] Character type set to: {character_type_option}")
                            else:
                                print("[!] Invalid character type option.")
                        else:
                            print("[!] Missing value for type.")
                        print("-" * 40)
                    elif param == "output":
                        if len(command_parts) >= 3: # Must have at least "set output filename"
                            output_filename = " ".join(command_parts[2:]) # Join parts to allow spaces in filename
                            print(f"[*] Output filename set to: {output_filename}")
                        else:
                            print("[!] Missing value for output filename.")
                        print("-" * 40)
                    elif param == "sequential_start":
                        if len(command_parts) == 3:
                            try:
                                value = int(command_parts[2])
                                sequential_start = value
                                print(f"[*] Sequential start set to: {sequential_start}")
                            except ValueError:
                                print("[!] Invalid sequential_start value. Must be an integer.")
                        else:
                            print("[!] Missing value for sequential_start.")
                        print("-" * 40)
                    elif param == "sequential_end":
                        if len(command_parts) == 3:
                            try:
                                value = int(command_parts[2])
                                sequential_end = value
                                print(f"[*] Sequential end set to: {sequential_end}")
                            except ValueError:
                                print("[!] Invalid sequential_end value. Must be an integer.")
                        else:
                            print("[!] Missing value for sequential_end.")
                        print("-" * 40)
                    else:
                        print(f"[!] Unknown parameter: {param}")
                else:
                    print("[!] Missing parameter for set command.")
                print("-" * 40)
            elif command == "generate":
                print("[*] Generating passwords...")
                if length_option is None or character_type_option is None:
                    print("[!] Please set length and type before generating passwords.")
                elif character_type_option == 'sequential_numbers' and (sequential_start is None or sequential_end is None):
                    print("[!] Please set sequential_start and sequential_end for sequential numbers.")
                else:
                    # Generate passwords
                    password_gen_result = generate_password_list(length_option, character_type_option, sequential_start, sequential_end)

                    if isinstance(password_gen_result, list):
                        # Check if the first item is an error message string from generate_password_list
                        if password_gen_result and isinstance(password_gen_result[0], str) and password_gen_result[0].startswith("[!]"):
                            print(password_gen_result[0]) # Print the error message
                        else:
                            # Successfully generated list
                            print(f"[+] Generated Password List (Length: {length_option}, Type: {character_type_option}):")
                            print("-" * 40)
                            for password in password_gen_result:
                                print(password)
                            print("-" * 40)
                            print(f"[+] Total passwords generated: {len(password_gen_result)}")

                            # Save to file if output_filename is set
                            if output_filename:
                                save_message = _save_list_to_file(password_gen_result, output_filename)
                                print(save_message)
                            elif output_filename is None and command_input.startswith("set output"): # User cleared output, then generated
                                pass # Don't attempt to save
                            
                    elif isinstance(password_gen_result, str): # This means an error message string was returned
                        print(password_gen_result)
                print("-" * 40)
            else:
                print(f"[!] Invalid command: {command}")
                print("-" * 40)

        except KeyboardInterrupt:
            print("\n[*] Exiting...")
            break
        except Exception as e:
            print(f"[!] Error: {e}")
            print("-" * 40)

