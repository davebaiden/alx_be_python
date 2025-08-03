🐍 Python Practice Projects
This document contains four beginner-to-intermediate Python projects to help reinforce fundamental concepts in programming — especially Object-Oriented Programming (OOP), error handling, and testing. Each script is designed to be run and tested individually.
📘 1. Bank Account Display
**File:** bank_account.py
**Concepts Covered:** Encapsulation, Class & Method Design
Implements a BankAccount class that keeps track of a user’s balance using encapsulation. It features a public method display_balance() to output the current balance.
Example Output:
Current Balance: $1000
➗ 2. Robust Division Calculator
**Files:** robust_division_calculator.py, main.py
**Concepts Covered:** Exception Handling, Command-line Arguments
This project creates a basic calculator that performs division while handling errors such as division by zero and non-numeric inputs.
How to Run:
python main.py 10 2
python main.py 10 0
python main.py ten 5
✅ 3. Simple Calculator with Unit Tests
**Files:** simple_calculator.py, test_simple_calculator.py
**Concepts Covered:** Unit Testing, Arithmetic Operations, Test Functions
Defines a SimpleCalculator class that supports basic math operations. Unit tests are written using the unittest framework.
How to Run Tests:
python -m unittest test_simple_calculator.py
📚 4. Library Management System
**Files:** library_management.py, main.py
**Concepts Covered:** OOP, Object Interaction, Encapsulation, State Management
A simple simulation of a library system. Users can add books, check out books, return them, and view which books are currently available.
Sample Output:
Available books after setup:
Brave New World by Aldous Huxley
1984 by George Orwell

Available books after checking out '1984':
Brave New World by Aldous Huxley

Available books after returning '1984':
Brave New World by Aldous Huxley
1984 by George Orwell
🛠 Requirements
Python 3.x
No external libraries required
🧠 Learning Goals
These projects help build hands-on experience with:
- Writing reusable classes and methods
- Handling errors using try-except blocks
- Creating and running unit tests
- Structuring Python programs for readability and reuse
📁 Project Structure
alx_be_python/
└── programming_paradigm/
    ├── bank_account.py
    ├── main-0.py
    ├── robust_division_calculator.py
    ├── main.py
    ├── simple_calculator.py
    ├── test_simple_calculator.py
    ├── library_management.py
    ├── new.py  

