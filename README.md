# Library Management System — Python CLI Application

A **Python-based Library Management System** built using **Object-Oriented Programming (OOP)** and **JSON-based file persistence**.

This application simulates basic library operations such as **adding books, registering members, borrowing and returning books**, and generating a simple analytics report.

The project demonstrates how core **Python programming concepts** like classes, data structures, and file storage can be used to build a practical command-line application.

---

# Project Overview

The **Library Management System** is designed to manage library records through a simple **command-line interface (CLI)**.

The system allows users to:

* Add and manage books in the library
* Register new library members
* Borrow and return books
* Maintain persistent records using JSON files
* Generate simple analytics reports about library usage

This project highlights the use of **Object-Oriented Programming for structuring applications** and **JSON storage for lightweight data persistence**.

---

# Problem Statement

Managing books and members manually in a library can become difficult as records grow over time.

This project addresses the problem by providing a **simple digital system** that:

* Tracks books available in the library
* Records borrowing and returning transactions
* Maintains persistent records
* Generates useful usage insights

---

# Solution Approach

The application is implemented using **Python classes and JSON files** for data storage.

Core components include:

* **Book Management Module** – handles adding and storing books
* **Member Management Module** – manages registered members
* **Borrow/Return System** – tracks book transactions
* **Analytics Module** – generates reports on library activity
* **JSON Persistence Layer** – stores and retrieves data from JSON files

This architecture keeps the application **modular, scalable, and easy to maintain**.

---

#  Key Features

### 📖 Book Management

Add and manage books available in the library collection.

###  Member Registration

Register and maintain records of library members.

###  Borrow & Return Books

Members can borrow books and return them after use.

###  JSON-Based Data Storage

All data is stored using **JSON files**, ensuring persistent records even after the program closes.

###  Basic Analytics Report

The system can generate a simple report showing library activity and usage statistics.

###  Command-Line Interface

Runs entirely in the terminal, making it lightweight and easy to execute.

---

#  Tech Stack

| Technology                            | Purpose                      |
| ------------------------------------- | ---------------------------- |
| **Python 3**                          | Core programming language    |
| **Object-Oriented Programming (OOP)** | Application structure        |
| **JSON**                              | Data storage and persistence |
| **CLI (Command Line Interface)**      | User interaction             |

---

#  System Architecture

```
User Input (CLI)
        │
        ▼
Library Management System
│           │           │
▼           ▼           ▼
Book Module Member Module Borrow/Return Module
        │
        ▼
JSON Storage (Data Persistence)
        │
        ▼
Analytics Report Generation
```

---

#  Project Structure

```
LibraryManagement
│
├── main.py              # Main program entry point
├── books.json           # Stored book records
├── members.json         # Registered member records
├── transactions.json    # Borrow/return logs
└── README.md            # Project documentation
```

*(File names may vary depending on implementation.)*

---

#  Example Usage

Example interaction in the terminal:

```
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Analytics Report
6. Exit

Select an option: 1
Enter Book Title: Python Programming
Enter Author: John Smith

Book added successfully.
```

---

#  Example Analytics Output

```
Library Analytics Report
------------------------
Total Books: 25
Registered Members: 10
Books Borrowed: 8
Books Available: 17
```

---

#  Challenges & Learnings

### Object-Oriented Design

Designing the system using classes helped maintain a clear and modular structure.

### JSON Data Persistence

Using JSON files allowed the program to maintain records without requiring a full database.

### CLI Workflow Design

Creating a simple menu-driven interface improved usability and program interaction.

---

#  Future Improvements

Possible enhancements for this system include:

* Add **search functionality for books**
* Implement **due dates and fine calculation**
* Add **admin authentication system**
* Store data using a **database (SQLite or PostgreSQL)**
* Build a **GUI interface using Tkinter or PyQt**
* Create a **web-based version using Flask or Django**

---

# 👨‍💻 Author

**Vinayak Sharma**

GitHub
https://github.com/vebeginner

LinkedIn
https://www.linkedin.com/in/vinayak-sharma-24a8aa384/

---
