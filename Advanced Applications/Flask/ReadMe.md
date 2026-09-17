# 🌐 Flask Full-Stack Web Application

A Python web application built with the **Flask framework**, demonstrating how Python can be used to create dynamic web applications with server-side routing, templates, static assets, and frontend interactions.

This project combines a Python backend with HTML, CSS, JavaScript, and Jinja2 templates to create a structured web application.

---

## 🎯 Project Objectives

The project focuses on practicing:

* Flask application structure
* URL routing
* Dynamic page rendering
* Jinja2 templating
* Template inheritance
* Static assets
* HTML forms
* Frontend/backend integration
* Organizing a web application into separate components

---

## 🛠️ Technology Stack

| Technology     | Purpose                  |
| -------------- | ------------------------ |
| **Python**     | Backend programming      |
| **Flask**      | Web framework            |
| **Jinja2**     | Server-side templating   |
| **HTML5**      | Page structure           |
| **CSS3**       | Styling                  |
| **JavaScript** | Client-side interactions |
| **jQuery**     | Frontend scripting       |

---

## 🏗️ Project Structure

```text id="q3u8k1"
Flask/
│
├── README.md
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

> The exact contents of `static/` and `templates/` may vary as the project evolves.

---

## 🔄 Application Flow

```text id="6p3j2d"
Browser
   ↓
HTTP Request
   ↓
Flask Application
   ↓
Route Handler
   ↓
Business Logic
   ↓
Jinja2 Template
   ↓
Rendered HTML
   ↓
Browser
```

---

## 🧩 Main Components

### Flask Application

The main Python file contains the application logic and Flask configuration.

```text id="j6h8tq"
Flask_Full_Project.py
```

It is responsible for defining routes and handling incoming requests.

---

### Templates

The `templates/` directory contains the HTML pages rendered by Flask.

```text id="f7m0w3"
templates/
├── base.html
├── homepage.html
├── about.html
├── add.html
└── skills.html
```

Using a base template makes it possible to reuse common page elements across multiple pages.

---

### Static Assets

The `static/` directory contains frontend resources such as:

* CSS
* JavaScript
* Images or other static files

These assets are served separately from the dynamic Flask routes.

---

# 🧠 Concepts Demonstrated

## Routing

Flask routes connect URLs to Python functions.

Example:

```python id="y0e4rm"
@app.route("/")
def home():
    return render_template("homepage.html")
```

---

## Template Rendering

Jinja2 allows Python-generated data to be passed into HTML templates.

Example:

```python id="6w8v0j"
return render_template(
    "skills.html",
    skills=skills
)
```

---

## Template Inheritance

A shared base template can be used to avoid duplicating common HTML structures.

Example:

```html id="s6h1rv"
{% extends "base.html" %}

{% block content %}
    <h1>Skills</h1>
{% endblock %}
```

---

# ⚡ Installation

Create a virtual environment:

```bash id="0u0qhl"
python -m venv venv
```

### Windows

```bash id="b5a7pu"
venv\Scripts\activate
```

### Linux / macOS

```bash id="2q0p3c"
source venv/bin/activate
```

Install Flask:

```bash id="a9l7do"
pip install flask
```

---

# ▶️ Running the Application

From the `Flask/` directory:

```bash id="l0g6di"
python Flask_Full_Project.py
```

Flask will start the development server.

Open the local address displayed in the terminal in your browser.

---

# 🧪 Development

During development, Flask's development server can be used to quickly test application changes.

A typical development workflow is:

```text id="f3p7ku"
Modify Code
    ↓
Run Application
    ↓
Open Browser
    ↓
Test Route
    ↓
Check Template
    ↓
Debug
    ↓
Refactor
```

---

# 🔮 Possible Improvements

Future improvements could include:

* Application factory pattern
* Blueprints
* Environment-based configuration
* Form validation
* Database integration
* Authentication
* Automated testing
* Better separation between routes and business logic
* Production WSGI configuration

---

# 📌 Notes

This project is primarily intended for learning and practicing Flask web development concepts.

The architecture can be extended as the application grows.

---
