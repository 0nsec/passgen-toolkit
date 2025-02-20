# Passgen-toolkit: Versatile Password List Generator

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

**Description:**

`passgen-toolkit` is a Python script designed to create highly customizable password lists (wordlists) for various security-related tasks such as penetration testing, security research, and password complexity analysis.  This tool allows you to generate password lists based on different character sets, lengths, and even sequential number ranges. It's designed to be flexible and easy to use, providing options for various common password patterns.

---

**Features:**

*   **Customizable Password Length:** Generate passwords of lengths ranging from 1 to 8 characters.
*   **Character Set Options:**
    *   **Random:** Includes a mix of lowercase and uppercase English letters, digits (0-9), and punctuation symbols.
    *   **Numbers Only:** Generates passwords consisting solely of digits (0-9).
    *   **English Lowercase Letters:** Uses only lowercase English alphabet characters.
    *   **English Uppercase Letters:** Uses only uppercase English alphabet characters.
    *   **English Both Case Letters:**  Combines both lowercase and uppercase English alphabet characters.
    *   **Alphanumeric Lowercase:** Includes digits and lowercase English letters.
    *   **Alphanumeric Uppercase:** Includes digits and uppercase English letters.
    *   **Alphanumeric Both Case:** Combines digits, lowercase, and uppercase English letters.
    *   **Sequential Numbers:** Generates password lists based on sequential numbers within a user-defined range and length (e.g., 0000 to 9999, or 00 to 99, etc.).
*   **Sequential Number Range:** For sequential number lists, you can specify both the starting and ending numbers of the sequence.
*   **File Output:** Option to save the generated password list to a text file within a "wordlist" folder.
*   **User-Friendly Interface:** Simple command-line prompts to guide you through the password list generation process.

**Usage:**

1.  **Clone the repository:**

    ```bash
    git clone github.com/0nsec/passgen-toolkit 
    cd passgen-toolkit
    ```

2.  **Run the script:**

    ```bash
    python pwlistgen.py
    ```

3.  **OPTIONS:** The script will guide you through the following options:

    *   **Password Length:** Enter the desired length for your passwords (between 1 and 8 characters).
    *   **Character Type:** Choose a character type option from the numbered list:
        ```
        Character Type Options:
        1. Random (numbers, letters, symbols)
        2. Numbers only (0-9)
        3. English lowercase letters
        4. English uppercase letters
        5. English both case letters
        6. Numbers and lowercase letters
        7. Numbers and uppercase letters
        8. Numbers, uppercase, and lowercase letters
        9. Sequential numbers (user-defined range and length)
        ```
        
    *   **Save to File:**
    *    You will be asked if you want to save the generated list to a file.
    *   If you choose "yes". The file will be saved in a folder named `wordlist` within the script's directory.

**Output:**

*   **Console Output:** By default, the generated password list will be printed to your console.
*   **File Output (Optional):** If you choose to save to a file, the password list will be saved as a plain text file (one password per line) in the `wordlist` folder. If the `wordlist` folder doesn't exist, it will be created automatically.

---
```python
██████╗ ███╗   ██╗███████╗███████╗ ██████╗
██╔═████╗████╗  ██║██╔════╝██╔════╝██╔════╝
██║██╔██║██╔██╗ ██║███████╗█████╗  ██║     
████╔╝██║██║╚██╗██║╚════██║██╔══╝  ██║     
╚██████╔╝██║ ╚████║███████║███████╗╚██████╗
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝  
```

