# 🧩 Algorithmic Problem Solving & Python Foundations

The `Problem Solving/` directory is the core learning and algorithmic section of this repository.

It contains a structured collection of Python assignments and exercises based on **Elzero Web School** learning materials, covering Python fundamentals, data structures, functions, file handling, exception handling, Object-Oriented Programming, databases, and practical problem-solving.

The main goal of this section is to strengthen **logical thinking, programming fundamentals, and the ability to design clear and maintainable solutions**.

---

# 🎯 Learning Objectives

This section focuses on developing the ability to:

* Understand Python fundamentals deeply
* Break complex problems into smaller steps
* Choose appropriate data structures
* Write reusable functions
* Work with files and external data
* Handle errors and unexpected input
* Apply Object-Oriented Programming principles
* Work with relational databases
* Process images and structured data
* Combine multiple Python concepts in practical problems

---

# 🗺️ Module Roadmap

| Module                    | Main Topics                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| `Ass_1.py` – `Ass_10.py`  | Python syntax, variables, data types, conditions, loops, and basic problem solving  |
| `Ass_11.py` – `Ass_13.py` | Lists, tuples, sets, dictionaries, and data manipulation                            |
| `Ass_14/`                 | File handling, reading and writing files, directory operations, and data processing |
| `Ass_15.py` – `Ass_19.py` | Functions, `*args`, `**kwargs`, lambda expressions, modules, and decorators         |
| `Ass_20/`                 | Image processing and manipulation using Pillow                                      |
| `Ass_21/`                 | Exception handling, built-in exceptions, and defensive programming                  |
| `Ass_22.py` – `Ass_23.py` | Classes, objects, inheritance, encapsulation, and OOP concepts                      |
| `Ass_24/`                 | SQLite databases, tables, CRUD operations, and SQL queries                          |
| `Ass_25.py`               | Integrated practical problem-solving and multi-concept challenges                   |

---

# 📚 Topics Covered

## 🐍 Python Fundamentals

The early assignments focus on understanding the foundations of Python:

* Variables
* Data types
* Operators
* Strings
* Conditional statements
* Loops
* Input and output
* Basic program structure

---

## 🧱 Data Structures

The repository explores Python's built-in data structures and their practical usage:

* Lists
* Tuples
* Sets
* Dictionaries
* Nested data structures
* Data transformation
* Searching and filtering

The goal is to understand not only how these structures work, but also **when each structure is appropriate**.

---

## ⚙️ Functions & Functional Programming

Several modules focus on creating reusable and flexible Python logic.

Topics include:

* User-defined functions
* Function parameters
* Return values
* `*args`
* `**kwargs`
* Lambda expressions
* Higher-order functions
* Modules
* Decorators

Example:

```python
def calculate_total(*numbers):
    return sum(numbers)
```

---

## 📁 File Handling

The file-processing modules explore working with files and directories programmatically.

Topics include:

* Opening files
* Reading data
* Writing data
* Appending data
* Processing multiple files
* Directory management
* Text parsing

Example:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

---

## 🖼️ Image Processing

The `Ass_20/` module introduces image manipulation using **Pillow**.

Possible operations include:

* Opening images
* Resizing
* Cropping
* Saving
* Basic image transformations

Example:

```python
from PIL import Image

image = Image.open("input.jpg")
image = image.resize((800, 600))
image.save("output.jpg")
```

---

## 🛡️ Exception Handling

The exception-handling module focuses on writing programs that can deal with unexpected situations safely.

Topics include:

* `try`
* `except`
* `else`
* `finally`
* Built-in exceptions
* Multiple exception types
* Custom exceptions
* Defensive programming

Example:

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
```

---

# 🏗️ Object-Oriented Programming

The OOP modules introduce the fundamental concepts required to build structured Python applications.

Topics include:

* Classes
* Objects
* Constructors
* Instance methods
* Class attributes
* Encapsulation
* Inheritance
* Polymorphism
* Method overriding

Example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, I'm {self.name}."
```

---

# 🗄️ Database Programming

The `Ass_24/` module introduces relational database concepts using Python's built-in `sqlite3` library.

Topics include:

* Database creation
* Table creation
* SQL queries
* Insert operations
* Select operations
* Update operations
* Delete operations
* Parameterized queries
* Basic CRUD workflows

Example:

```python
import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

connection.commit()
connection.close()
```

---

# 🧠 Problem-Solving Approach

When approaching a programming problem, I generally follow this process:

```text
Understand the Problem
        ↓
Identify Inputs & Outputs
        ↓
Break the Problem into Smaller Steps
        ↓
Choose Appropriate Data Structures
        ↓
Design the Algorithm
        ↓
Implement the Solution
        ↓
Test Edge Cases
        ↓
Review & Refactor
```

This process helps transform a problem from an abstract requirement into a structured implementation.

---

# 📂 Directory Structure

```text
Problem Solving/
│
├── Ass_1.py
├── Ass_2.py
├── Ass_3.py
├── ...
├── Ass_13.py
│
├── Ass_14/
│
├── Ass_15.py
├── Ass_16.py
├── Ass_17.py
├── Ass_18.py
├── Ass_19.py
│
├── Ass_20/
├── Ass_21/
│
├── Ass_22.py
├── Ass_23.py
│
├── Ass_24/
├── Ass_25.py
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| **Python**              | Core programming language      |
| **Pillow**              | Image processing               |
| **SQLite3**             | Relational database management |
| **Regular Expressions** | Text pattern matching          |
| **OS / Sys**            | File and system operations     |
| **Git**                 | Version control                |

---

# 📈 Progression

The assignments are organized to gradually increase in complexity.

```text
Fundamentals
     ↓
Data Structures
     ↓
Functions
     ↓
Modules & Decorators
     ↓
File Processing
     ↓
Exception Handling
     ↓
Object-Oriented Programming
     ↓
Image Processing
     ↓
Databases
     ↓
Integrated Problem Solving
```

This progression provides a foundation for moving from isolated programming exercises toward larger practical applications.

---

# 🔗 Related Sections

For practical applications built with the concepts explored here:

**[← Back to Main Repository](../README.md)**

**[Advanced Applications →](../Advanced%20Applications/README.md)**

---

# 📌 Note

These assignments are primarily part of the learning and development process.

The code may evolve over time as concepts are revisited, improved, refactored, or implemented using alternative approaches.

> **Understand the problem. Design the solution. Write the code. Test it. Improve it.**
