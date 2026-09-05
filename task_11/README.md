# Task 11 - Mini Authentication System

Uses predefined credentials, maximum login attempts, successful/failed login handling, logout, and retry logic.

### Demo credentials
- Username: `admin`, Password: `Admin@123`
- Username: `student`, Password: `Python@123`

## Run
```bash
python authentication.py
```
Enter username: admin
Enter password: wrong

Login failed.
Attempts remaining: 2

Enter username: admin
Enter password: admin123

Login successful!

Welcome, admin.

Logout successful.


Login failed.
Attempts remaining: 0
Account locked.
