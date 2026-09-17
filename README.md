# 🐍 Advanced Python Engineering & Problem-Solving Ecosystem

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg?style=for-the-badge)]()
[![Architecture](https://img.shields.io/badge/Architecture-OOP%20%26%20Modular-orange.svg?style=for-the-badge)]()

Welcome to my primary **Python Engineering & Problem-Solving Repository**.

This repository documents my journey in Python development through a combination of **algorithmic problem solving, software engineering, web development, automation, web scraping, database management, and API integration**.

The goal is to build a strong foundation in computer science concepts while applying those concepts to practical, real-world projects.

---

## 🎯 Repository Goals

This repository focuses on developing and demonstrating the following skills:

* 🧠 Problem-solving and algorithmic thinking
* 🐍 Python programming and language fundamentals
* 🏗️ Object-Oriented Programming and modular architecture
* 📊 Data structures and data processing
* 📁 File handling and data manipulation
* 🗄️ Database integration with SQLite
* 🌐 Web development with Flask
* 🕷️ Web scraping and data extraction
* 🤖 Browser automation with Selenium and Playwright
* 🔌 REST API integration
* 🖼️ Image processing with Pillow
* 🛡️ Exception handling and defensive programming
* 🧪 Writing maintainable and reusable code

---

## 💡 Engineering Philosophy

My approach to software development is built around four main principles:

### 1. Clean & Maintainable Code

I aim to write code that is:

* Readable
* Modular
* Reusable
* Easy to maintain
* Organized around clear responsibilities

Where appropriate, projects use **Object-Oriented Programming (OOP)** and modular design to keep components separated and manageable.

### 2. Problem-Solving First

Every programming challenge is an opportunity to improve:

* Logical thinking
* Algorithm design
* Data structure usage
* Edge-case handling
* Code optimization

The objective is not only to make a solution work, but also to understand **why it works and how it can be improved**.

### 3. Reliability & Error Handling

Real-world software needs to handle unexpected situations.

Projects in this repository explore techniques such as:

* Exception handling
* Input validation
* Defensive programming
* Handling missing or invalid data
* Managing automation failures
* Separating error-prone operations into clear boundaries

### 4. Practical Automation

Python becomes especially powerful when combined with automation.

This repository contains projects involving:

* Browser automation
* Web scraping
* Data extraction
* File processing
* API communication
* Repetitive workflow automation

---

# 📂 Repository Structure

```text
.
├── Problem Solving/
│   ├── Ass_1.py
│   ├── Ass_2.py
│   ├── ...
│   ├── Ass_13.py
│   ├── Ass_14/
│   ├── Ass_15.py
│   ├── ...
│   ├── Ass_19.py
│   ├── Ass_20/
│   ├── Ass_21/
│   ├── Ass_22.py
│   ├── Ass_23.py
│   ├── Ass_24/
│   ├── Ass_25.py
│   └── README.md
│
└── Advanced Applications/
    ├── Beautiful_Soup/
    │   ├── 1/
    │   └── 2/
    │
    ├── Flask/
    │   ├── Flask_Full_Project.py
    │   ├── static/
    │   └── templates/
    │
    ├── Selenium/
    │   ├── Bot_With_OOP/
    │   ├── Hack_Swing/
    │   └── Simple_Automation/
    │
    ├── Playwright/
    │
    ├── Requests/
    │
    └── README.md
```

---

# 🧩 Problem Solving

The `Problem Solving/` directory contains a structured collection of Python exercises and assignments focused on strengthening programming fundamentals and problem-solving abilities.

The modules progressively cover topics such as:

* Python syntax and fundamentals
* Data types
* Conditions and loops
* Lists, tuples, sets, and dictionaries
* Functions
* Lambda expressions
* `*args` and `**kwargs`
* Modules and packages
* Decorators
* File handling
* Exception handling
* Object-Oriented Programming
* Image processing
* SQLite databases
* Integrated programming challenges

👉 See the dedicated documentation:

**[Problem Solving README](Problem%20Solving/README.md)**

---

# 🚀 Advanced Applications

The `Advanced Applications/` directory contains practical Python projects that apply programming concepts to real-world use cases.

The main areas include:

### 🕷️ Web Scraping

Projects using tools such as:

* BeautifulSoup
* Requests
* HTML parsing
* CSV processing

Examples include extracting information from websites and transforming it into structured datasets.

---

### 🌐 Flask Web Development

The Flask section demonstrates web application development using:

* Flask
* Jinja2
* HTML5
* CSS3
* JavaScript
* jQuery

The projects explore concepts such as:

* Routing
* Templates
* Static files
* Dynamic pages
* Form handling
* Application structure

---

### 🤖 Browser Automation

Automation projects using:

* Selenium WebDriver
* Playwright

The Selenium projects also explore organizing automation code using **Object-Oriented Programming** and separating configuration, automation logic, and application entry points.

---

### 🔌 API & HTTP Requests

The `Requests/` section contains experiments and projects involving HTTP communication and external services.

Topics include:

* HTTP requests
* REST APIs
* JSON responses
* Authentication
* Query parameters
* API data processing

---

👉 See the dedicated documentation:

**[Advanced Applications README](Advanced%20Applications/README.md)**

---

# 🛠️ Technology Stack

| Category               | Technologies                                            |
| ---------------------- | ------------------------------------------------------- |
| **Language**           | Python 3.10+                                            |
| **Problem Solving**    | Python Data Structures, Algorithms, Regular Expressions |
| **Data Processing**    | CSV, Pandas                                             |
| **Web Scraping**       | BeautifulSoup4, Requests                                |
| **Browser Automation** | Selenium, Playwright                                    |
| **Web Development**    | Flask, Jinja2                                           |
| **Frontend**           | HTML5, CSS3, JavaScript, jQuery                         |
| **Database**           | SQLite3                                                 |
| **Image Processing**   | Pillow                                                  |
| **Development Tools**  | Virtual Environments, Git                               |

---

# ⚡ Getting Started

## 1. Prerequisites

Make sure Python 3.10 or newer is installed.

```bash
python --version
```

On some Linux/macOS systems:

```bash
python3 --version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/your-username/python-problem-solving-apps.git
cd python-problem-solving-apps
```

Replace `your-username` with your GitHub username.

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, the main dependencies used across the projects can be installed with:

```bash
pip install flask beautifulsoup4 selenium playwright requests pillow pandas
```

For Playwright:

```bash
playwright install
```

> Some individual projects may require additional dependencies.

---

# ▶️ Running Projects

## Selenium Booking Bot

```bash
python "Advanced Applications/Selenium/Bot_With_OOP/run.py"
```

## Flask Application

```bash
python "Advanced Applications/Flask/Flask_Full_Project.py"
```

## BeautifulSoup Scraper

```bash
python "Advanced Applications/Beautiful_Soup/1/Project.py"
```

## Problem-Solving Module

```bash
python "Problem Solving/Ass_24/Python/index.py"
```

> File names and entry points may vary depending on the specific project.

---

# 📚 Learning Roadmap

The repository follows a progressive learning path:

```text
Python Fundamentals
        ↓
Data Structures
        ↓
Problem Solving
        ↓
Functions & Functional Programming
        ↓
File Handling
        ↓
Exception Handling
        ↓
Object-Oriented Programming
        ↓
Databases
        ↓
Web Scraping
        ↓
API Integration
        ↓
Web Development
        ↓
Browser Automation
        ↓
Larger Practical Applications
```

This structure allows theoretical knowledge to be reinforced through practical implementation.

---

# 📈 Continuous Learning

This repository is continuously evolving as I improve my skills in:

* Python development
* Software architecture
* Algorithm design
* Automation
* Web development
* Data extraction
* Database management
* Testing and debugging

Each project represents a step toward writing software that is more **efficient, maintainable, reusable, and reliable**.

---

# 📌 Notes

This repository is primarily a learning and development portfolio.

Some projects are educational exercises, while others are practical implementations designed to explore specific technologies or engineering concepts.

The structure and codebase will continue to evolve as new concepts and projects are added.

---

# 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

## ❤️ Author

Built with Python, curiosity, and a continuous commitment to learning and improving.

> **Learn → Build → Break → Debug → Improve → Repeat.**
