# 🔐 Password Validator

A beginner-friendly **Python command-line application** that validates passwords against predefined security rules and provides clear reasons when a password is invalid.

The project focuses on Python fundamentals such as **functions, loops, conditional statements, string methods, lists, modules, and input validation**.

## ✨ Features

* Validates password length between **8 and 16 characters**
* Requires the password to start with an **uppercase letter**
* Checks for at least one:

  * Uppercase letter
  * Lowercase letter
  * Number
  * Allowed special character
* Rejects spaces
* Rejects unsupported characters
* Displays **specific reasons** when a password is invalid
* Displays all validation errors instead of stopping at the first error
* Allows the user to validate multiple passwords in one session
* Uses separate modules for validation logic and user interaction

## 🔑 Password Requirements

A valid password must:

```text
✓ Contain 8–16 characters
✓ Start with an uppercase letter
✓ Contain at least one uppercase letter
✓ Contain at least one lowercase letter
✓ Contain at least one number
✓ Contain at least one special character
✓ Not contain spaces
✓ Not contain unsupported characters
```

### Allowed Special Characters

```text
! @ # $ & * _
```

## 🛠️ Technologies Used

* Python 3
* Functions
* Lists
* Loops
* Conditional Statements
* String Methods
* Modules
* Input Validation

## 📂 Project Structure

```text
Password_Validator/
│
├── main.py
├── password_validator.py
└── README.md
```

### `main.py`

Handles the user interface and:

* Displays password requirements
* Accepts user input
* Displays validation results
* Shows reasons for invalid passwords
* Allows multiple password checks

### `password_validator.py`

Contains the core password validation logic.

It checks:

* Password length
* First character
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Spaces
* Unsupported characters

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Password-Validator.git
```

### 2. Open the project directory

```bash
cd Password-Validator
```

### 3. Run the application

```bash
python main.py
```

No external Python packages are required.

## 💻 Example

### Valid Password

```text
Enter your password: Mohan@123

--------------------------------------------------
✅ VALID PASSWORD
Your password satisfies all requirements.
--------------------------------------------------
```

### Invalid Password

```text
Enter your password: mohan123

--------------------------------------------------
❌ INVALID PASSWORD

Reasons:
❌ Password must start with an uppercase letter.
❌ Password must contain at least one special character (! @ # $ & * _).
--------------------------------------------------
```

## 🔄 Application Flow

```text
Start
  ↓
Enter Password
  ↓
Validate Password
  ↓
Check Each Requirement
  ↓
Collect Errors
  ↓
Are There Any Errors?
  ↓
 ┌───────────────┐
 │               │
 No              Yes
 │               │
 ↓               ↓
VALID         INVALID
Password      Password
                 ↓
          Display Reasons
```

## 🧠 What I Learned

This project helped me practice:

* Writing reusable Python functions
* Breaking a project into multiple modules
* Working with strings and string methods
* Using loops for character-by-character validation
* Managing multiple validation conditions
* Collecting and displaying error messages
* Handling user input
* Designing a simple command-line application

## 🚀 Future Improvements

Planned enhancements:

* Password strength levels such as Weak, Medium, and Strong
* Password Generator
* Password Generator + Validator integration
* Unit testing
* Tkinter GUI
* Improved duplicate-error handling
* Configurable password rules

## ⚠️ Disclaimer

This project is intended for **learning and demonstration purposes**.

It performs rule-based password validation and should not be considered a complete measure of real-world password security.

Avoid entering your actual personal passwords into demonstration applications.

## 👨‍💻 Author

**Mohan K**

Python Developer | DSA | SQL | Software Development

