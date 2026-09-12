# 🎓 Student & Admin Management System

A beginner-friendly **Student & Admin Management System** built using **Python, Object-Oriented Programming (OOP), and CSV file handling**.

This project provides separate functionality for **Administrators and Students**, including registration, login, student management, updating student details, deleting students, and viewing student records.

---

## 📌 Project Overview

The **Student & Admin Management System** is a console-based Python application designed to manage student information using CSV files as a simple database.

The system provides two roles:

* 👨‍💼 **Admin**
* 👨‍🎓 **Student**

Each role has different permissions and functionality.

---

## ✨ Features

### 👨‍💼 Admin Features

* Admin registration with a secret key
* Admin login
* View all students
* Search for a student by username and age
* Update student information
* Delete student records
* Add/register a new student
* Prevent duplicate student usernames

### 👨‍🎓 Student Features

* Student registration
* Student login
* View/update personal information
* Update:

  * Username
  * Password
  * Age

---

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **Classes & Inheritance**
* **Class Methods**
* **CSV File Handling**
* **File Handling**
* **Command Line Interface (CLI)**

### Python Module Used

```python
import csv
```

The built-in `csv` module is used to store and retrieve student and admin information.

---

## 📂 Project Structure

```text
student-admin-management-system/
│
├── student.py
├── admin.csv
├── student.csv
└── README.md
```

> **Note:** `admin.csv` and `student.csv` contain local application data and should not contain real passwords or sensitive information when sharing the project publicly.

---

## 🧱 Main Classes

### `manage`

The parent class responsible for common user functionality.

It handles:

* Username
* Password
* Role
* Registration
* Login
* Login status

---

### `student`

The `student` class inherits from the `manage` class.

It handles student-specific information such as:

* Age
* Course
* Student profile updates

---

### `admin`

The `admin` class inherits from the `manage` class.

It provides administrative functionality such as:

* Showing all students
* Finding students
* Updating students
* Deleting students
* Adding students

---

## 🗃️ CSV Data Storage

The project uses CSV files instead of a database.

### `student.csv`

Student records are stored with the following fields:

```text
username
password
age
course
role
```

### `admin.csv`

Admin records are stored with:

```text
username
password
role
```

CSV files make this project simple and suitable for learning **Python file handling and basic data management**.

---

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/Malkinder-singh/student-admin-management-system.git
```

---

### 3. Open the Project Folder

```bash
cd student-admin-management-system
```

---

### 4. Run the Program

```bash
python student.py
```

The application will start in the terminal.

---

## 🔐 Admin Registration

Admin registration requires an **admin secret key**.

The current project uses:

```python
secretKey = "admin123"
```

⚠️ This is included only as a learning-project implementation. A real-world application should never store passwords or secret keys directly in the source code.

---

## 🖥️ Application Flow

```text
                    Student & Admin Management System
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                 Register                    Login
                    │                           │
              ┌─────┴─────┐               ┌─────┴─────┐
              │           │               │           │
            Admin      Student           Admin      Student
              │           │               │           │
         Secret Key    Details          Admin       Student
              │           │               Panel       Panel
              │           │                 │           │
              └───────────┘                 │           │
                                            │           │
                                    ┌───────┼───────┐   │
                                    │       │       │   │
                                  View   Update  Delete Update
                                Students Student Student Details
```

---

## 🎯 Learning Objectives

This project was created to practice and understand:

* Python classes
* Inheritance
* Constructors
* Class methods
* Object-oriented programming
* CSV file handling
* Reading and writing files
* User authentication
* Conditional statements
* Loops
* Functions
* Basic CRUD operations

CRUD stands for:

* **C** — Create
* **R** — Read
* **U** — Update
* **D** — Delete

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* 🔒 Password hashing
* 🗄️ Database integration using MySQL or MongoDB
* 🔍 Better student search functionality
* 📧 Email verification
* 👤 Improved user authentication
* 🖥️ Graphical User Interface (GUI)
* 🌐 Web-based version
* 📊 Student dashboard
* 📝 Better input validation
* 🚪 Logout functionality
* 🔑 Secure configuration for admin credentials

---

## 👨‍💻 Author

**Malkinder Singh**

Aspiring Software / Frontend Developer

GitHub: [Malkinder-singh](https://github.com/Malkinder-singh)

---

## ⭐ Project

If you find this project useful for learning Python and OOP concepts, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **educational and learning purposes**.
