# 🚀 Advanced Python Applications

The `Advanced Applications/` directory contains practical Python projects that apply programming concepts to real-world development scenarios.

While the `Problem Solving/` section focuses primarily on programming foundations and algorithmic thinking, this section focuses on **building applications, automating workflows, interacting with external services, extracting data, and developing web-based systems**.

---

# 🎯 Main Objectives

The projects in this directory are designed to explore:

* 🌐 Web application development
* 🕷️ Web scraping and data extraction
* 🤖 Browser automation
* 🔌 API and HTTP communication
* 🗄️ Data processing
* 🏗️ Modular application architecture
* 🧱 Object-Oriented Programming in practical projects
* 🧪 Automation and testing workflows
* 🔄 Integration between different technologies

---

# 🏗️ Application Architecture

```text
Advanced Applications/
│
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

# 🕷️ 1. Web Scraping & Data Extraction

## BeautifulSoup

The `Beautiful_Soup/` directory contains projects focused on extracting structured information from web pages.

The projects demonstrate concepts such as:

* HTTP requests
* HTML parsing
* DOM navigation
* Data extraction
* Text cleaning
* Structured output
* CSV generation

### Example Projects

#### 📋 Job Data Extraction

A scraper designed to collect job-related information from web pages and store the extracted data in a structured format.

Typical output:

```text
Jobs.csv
```

Possible data fields include:

* Job title
* Company
* Location
* Description
* Other available metadata

---

#### 📚 Book Catalog Extraction

A scraping project focused on extracting information from an online book catalog.

Typical output:

```text
books_data.csv
```

The project demonstrates extracting and organizing information such as:

* Book title
* Price
* Availability
* Rating
* Product metadata

> The exact fields depend on the implementation of each scraper.

---

# 🌐 2. Flask Web Development

The `Flask/` directory contains a complete web application project built with the Flask framework.

### Main Components

```text
Flask/
│
├── Flask_Full_Project.py
│
├── static/
│   ├── CSS/
│   └── JavaScript/
│
└── templates/
    ├── base.html
    ├── homepage.html
    ├── about.html
    ├── add.html
    └── skills.html
```

### Technologies

* Flask
* Jinja2
* HTML5
* CSS3
* JavaScript
* jQuery

### Concepts Demonstrated

* Application routing
* URL handling
* Template rendering
* Template inheritance
* Static assets
* HTML forms
* Dynamic content
* Frontend/backend integration

The project demonstrates how Python can be used to build a dynamic web application rather than standalone scripts.

---

# 🤖 3. Browser Automation

The `Selenium/` directory contains browser automation projects using **Selenium WebDriver**.

---

## Selenium Bot with OOP

### Location

```text
Selenium/Bot_With_OOP/
```

The project organizes browser automation logic using an Object-Oriented structure.

Example structure:

```text
Bot_With_OOP/
│
├── booking/
│   ├── booking.py
│   └── constants.py
│
└── run.py
```

### Concepts

* Selenium WebDriver
* Browser configuration
* Page interaction
* Element selection
* Form automation
* Dropdown interaction
* Explicit waits
* OOP architecture
* Separation of configuration and application logic

The purpose of the project is to demonstrate how browser automation can be organized into reusable components instead of relying on a single large script.

---

## Simple Automation

```text
Selenium/Simple_Automation/
```

Contains smaller automation experiments designed to explore:

* WebDriver configuration
* Browser interaction
* Element locating
* Basic automated workflows

---

## Automation Experiments

```text
Selenium/Hack_Swing/
```

Contains experimental automation scripts used to explore browser interaction and automation techniques.

---

# 🎭 4. Playwright

The `Playwright/` directory contains projects and experiments using the modern **Playwright browser automation framework**.

Topics include:

* Browser automation
* Page navigation
* Element interaction
* Automated workflows
* Code generation
* End-to-end testing concepts

Playwright provides another approach to browser automation and complements the Selenium projects in this repository.

---

# 🔌 5. HTTP Requests & APIs

The `Requests/` directory focuses on communicating with external web services using Python.

Main concepts include:

* HTTP requests
* GET and POST requests
* Query parameters
* Headers
* JSON responses
* API authentication
* Response handling
* External service integration

Example:

```python
import requests

response = requests.get("https://api.example.com/data")

if response.ok:
    data = response.json()
    print(data)
```

---

# 🧱 Engineering Concepts

Across these projects, I focus on applying software engineering principles to practical problems.

## Modular Design

Large tasks are divided into smaller components with clear responsibilities.

```text
Application
    │
    ├── Configuration
    │
    ├── Core Logic
    │
    ├── External Services
    │
    └── Entry Point
```

---

## Object-Oriented Design

Where appropriate, OOP is used to organize related data and behavior into reusable components.

Key concepts include:

* Classes
* Objects
* Encapsulation
* Composition
* Inheritance
* Reusable methods

---

## Error Handling

Practical applications need to account for unexpected situations.

Projects may include techniques such as:

* Exception handling
* Input validation
* Response validation
* Missing-element handling
* Browser automation safeguards
* Controlled failure handling

---

# 🛠️ Technology Stack

| Category                 | Technologies                    |
| ------------------------ | ------------------------------- |
| **Programming Language** | Python 3.10+                    |
| **Web Scraping**         | BeautifulSoup4, Requests        |
| **Web Development**      | Flask, Jinja2                   |
| **Browser Automation**   | Selenium, Playwright            |
| **Data Processing**      | CSV, Pandas                     |
| **Image Processing**     | Pillow                          |
| **Database**             | SQLite3                         |
| **Frontend**             | HTML5, CSS3, JavaScript, jQuery |
| **Version Control**      | Git                             |

---

# ⚡ Getting Started

From the root directory, create and activate a virtual environment:

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

Install the required packages:

```bash
pip install flask beautifulsoup4 selenium playwright requests pillow pandas
```

For Playwright:

```bash
playwright install
```

---

# ▶️ Running Applications

## Flask

```bash
python Flask/Flask_Full_Project.py
```

---

## Selenium Bot

```bash
python Selenium/Bot_With_OOP/run.py
```

---

## BeautifulSoup Scraper

Example:

```bash
python Beautiful_Soup/1/Project.py
```

> Entry-point filenames may differ between projects.

---

# 📚 Practical Learning Path

The applications in this directory build upon the fundamentals developed in the problem-solving section.

```text
Python Fundamentals
        ↓
Problem Solving
        ↓
Functions & OOP
        ↓
File & Data Processing
        ↓
HTTP Requests
        ↓
Web Scraping
        ↓
Flask Web Development
        ↓
Browser Automation
        ↓
Integrated Applications
```

---

# 🔗 Related Sections

**[← Back to Main Repository](../README.md)**

---

# 📈 Continuous Development

This directory will continue to grow as new technologies, projects, and engineering concepts are explored.

The focus is on moving from simple scripts toward applications that are:

* Modular
* Maintainable
* Reusable
* Testable
* Practical

> **Learn the technology → Build with it → Understand the limitations → Improve the implementation.**
