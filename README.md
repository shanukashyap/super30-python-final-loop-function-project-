# Super30 Python Final Loop & Function Project

## Project Objective

This project combines the concepts covered in 5Loop, 6Functions, and While Loop into practical Python mini-programs.

The project demonstrates how functions and loops can be used to build interactive, reusable, and beginner-friendly applications.

## Programs Completed

| Task | Program |
|---|---|
| 01 | Student Result Management System |
| 02 | Banking Application |
| 03 | Inventory Management |
| 04 | Quiz Application |
| 05 | Number Analysis Tool |
| 06 | Employee Salary Analyzer |
| 07 | Shopping Cart |
| 08 | Password Strength Checker |
| 09 | Prime Number Analyzer |
| 10 | Expense Tracker |
| 11 | Mini Authentication System |
| 12 | Super30 Python Utility Application |

## How to Execute

Make sure Python 3 is installed.

From the repository root, open the required task directory and run its Python file.

Example:

```bash
cd task_01
python student_result.py
```

For another task:

```bash
cd task_02
python banking_application.py
```

No external Python packages are required.

## Concepts Used

- Functions
- Function parameters and return values
- Function docstrings
- `for` loops
- `while` loops
- Conditional statements
- Lists
- Dictionaries
- Strings
- Input validation
- Exception handling with `try` / `except`
- Menu-driven applications
- Basic calculations
- Searching and updating data

## Learning Outcomes

By completing this project, I learned how to:

1. Break a large problem into smaller functions.
2. Select `for` loops when iterating over collections or a known range.
3. Select `while` loops for menus and repeated user interaction.
4. Validate user input and handle common errors.
5. Work with lists and dictionaries.
6. Build practical command-line applications.
7. Reuse functions instead of writing repetitive code.
8. Test programs with different inputs and edge cases.

## Testing

Each program should be tested with:
- Normal valid input
- Invalid input
- Empty input where applicable
- Boundary values
- Repeated menu selections
- Exit conditions

## YouTube Demonstration

Add my YouTube demonstration link here after recording:

**https://youtu.be/IjxUZWOD7ug**

The video explain the problem statement, approach, important functions, loop choices, execution, test cases, challenges/errors, and learning outcomes.

## GitHub Submission

Repository name:

`super30-python-final-loop-function-project-`

Final submission should contain exactly:
1. GitHub Repository link
2. YouTube Demonstration link


Super30 Python Final Loop Function Project
Project Objective
This project combines the concepts learned in Python Loops, Functions, and While Loops.

The objective is to build practical mini-applications using:

Functions
Parameters and arguments
Return values
for loops
while loops
Lists
Dictionaries
Conditional statements
Input/output
Error handling
Menu-driven applications
Programs Completed
Student Result Management System
Banking Application
Inventory Management
Quiz Application
Number Analysis Tool
Employee Salary Analyzer
Shopping Cart
Password Strength Checker
Prime Number Analyzer
Expense Tracker
Mini Authentication System
Super30 Python Utility Application
Project Structure
super30-python-final-loop-function-project/
│
├── README.md
├── requirements.txt
├── task_01/
├── task_02/
├── task_03/
├── task_04/
├── task_05/
├── task_06/
├── task_07/
├── task_08/
├── task_09/
├── task_10/
├── task_11/
└── task_12/



some uscases for some input and output

PS E:\super30-python-final-loop-function-project> python .\task_01\student_result.py
Enter marks for subject 1: 78
Enter marks for subject 2: 45
Enter marks for subject 3: 56
Enter marks for subject 4: 87
Enter marks for subject 5: 90

--- STUDENT RESULT ---
Marks: [78.0, 45.0, 56.0, 87.0, 90.0]
Total: 356.0
Percentage: 71.2
Grade: B
Result: Pass

PS E:\super30-python-final-loop-function-project> python .\task_02\banking_application.py

--- BANKING MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice: 1
Current balance: 10000

--- BANKING MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice: 2
Enter deposit amount: 2000
Deposit successful.

--- BANKING MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice: 3
Enter withdrawal amount: 3000
Withdrawal successful.

--- BANKING MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice: 4

--- TRANSACTION HISTORY ---
Deposited: 2000.0
Withdrawn: 3000.0

--- BANKING MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice: 5
Thank you for using the banking application.
PS E:\super30-python-final-loop-function-project> python .\task_03\inventory_management.py
Enter product name: laptop
Enter price: 70000
Enter quantity: 2
Product added successfully.
Enter product name: python
Enter price: 400000 
Enter quantity: 3
Product added successfully.

--- PRODUCTS ---
laptop | Price: 70000.0 | Quantity: 2
python | Price: 400000.0 | Quantity: 3
Enter product name to search: python                                  
Product found: {'name': 'python', 'price': 400000.0, 'quantity': 3}
Enter product name: iphone
Product not found.
Total inventory value: 1340000.0
PS E:\super30-python-final-loop-function-project>  python .\task_04\quiz_application.p    
C:\Users\URMIL\anaconda3\python.exe: can't open file 'E:\\super30-python-final-loop-function-project\\task_04\\quiz_application.p': [Errno 2] No such file or directory
PS E:\super30-python-final-loop-function-project>  python .\task_04\quiz_application.py   

What keyword is used to define a function in Python?
Your answer: iio
Incorrect.

Which loop is commonly used when the number of iterations is known?
Your answer: i fodn
Incorrect.

Which keyword is used to return a value from a function?
Your answer: uop
Incorrect.

Which data type stores key-value pairs?
Your answer: rtyuio
Incorrect.

Which loop continues while a condition is true?
Your answer: tyuio
Incorrect.

--- QUIZ RESULT ---
Score: 0 / 5
Percentage: 0.0

PS E:\super30-python-final-loop-function-project> python .\task_06\employee_salary.py
Total payroll: 190000
Average salary: 38000.0
Highest salary: 60000
Lowest salary: 25000
Employees above average: [45000, 60000]
PS E:\super30-python-final-loop-function-project> python .\task_05\number_analysis.py
Largest: 20
Smallest: -5
Total: 49
Average: 7.0
Even count: 4
Odd count: 3
Positive count: 5
Negative count: 2
PS E:\super30-python-final-loop-function-project> python .\task_07\shopping_cart.py  

--- SHOPPING CART ---
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit
Enter choice: 1
Enter product name: laptop
Enter product price: 700000
Enter quantity: 2
Product added.

--- SHOPPING CART ---
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit
Enter choice: 2
Enter product name to remove: phone
Product not found.

--- SHOPPING CART ---
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit
Enter choice: 3
{'name': 'laptop', 'price': 700000.0, 'quantity': 2}

--- SHOPPING CART ---
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit
Enter choice: 4
Total bill: 1400000.0

--- SHOPPING CART ---
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit
Enter choice: 5
Thank you for shopping.
PS E:\super30-python-final-loop-function-project> python .\task_08\password_checker.py
Enter password: tyui
Weak password
 
PS E:\super30-python-final-loop-function-project> python .\task_09\prime_analyzer.py                   
Enter start number: 3
Enter end number: 9
Prime numbers: [3, 5, 7]
Number of primes: 3
Sum of primes: 15
Largest prime: 7
PS E:\super30-python-final-loop-function-project> python .\task_10\expense_tracker.py

--- EXPENSE TRACKER ---
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Exit
Enter choice: 1
Enter expense name: laptop
Enter amount: 56789
Expense added.

--- EXPENSE TRACKER ---
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Exit
Enter choice: 2
laptop : 56789.0

--- EXPENSE TRACKER ---
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Exit
Enter choice: 3
Total expenses: 56789.0

--- EXPENSE TRACKER ---
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Exit
Enter choice: 4
Highest expense: laptop 56789.0

--- EXPENSE TRACKER ---
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Exit
Enter choice: 5
Expense tracker closed.
PS E:\super30-python-final-loop-function-project> python .\task_11\authentication.py
Enter username: urmikl
Enter password: 567890
Login failed.
Attempts remaining: 2
Enter username: tyuio
Enter password: 5278
Login failed.
Attempts remaining: 1
Enter username: admin
Enter password: python123
Login successful.

1. Logout
Enter choice: 1
You have been logged out.

PS E:\super30-python-final-loop-function-project> python .\task_12\utility_application.py

===== SUPER30 PYTHON UTILITY =====
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial
5. Multiplication Table
6. Number Analyzer
7. Exit
Enter your choice: 1
Enter first number: 24
Enter operator (+, -, *, /): -
Enter second number: 24
Result: 0.0

===== SUPER30 PYTHON UTILITY =====
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial
5. Multiplication Table
6. Number Analyzer
7. Exit
Enter your choice: 2
Enter text: urmil
It is not a palindrome.

===== SUPER30 PYTHON UTILITY =====
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial
5. Multiplication Table
6. Number Analyzer
7. Exit
Enter your choice: 3
Enter number: 5
Prime number.

===== SUPER30 PYTHON UTILITY =====
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial
5. Multiplication Table
6. Number Analyzer
7. Exit
Enter your choice: 4
Enter number: 6
Factorial: 720

===== SUPER30 PYTHON UTILITY =====
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial
5. Multiplication Table
6. Number Analyzer
7. Exit
Enter your choice: 6
Enter number: 34
Positive
Even

===== SUPER30 PYTHON UTILITY =====
1. Calculator
2. Palindrome Checker
3. Prime Checker
4. Factorial
5. Multiplication Table
6. Number Analyzer
7. Exit
Enter your choice: 7
Thank you for using Super30 Python Utility.
