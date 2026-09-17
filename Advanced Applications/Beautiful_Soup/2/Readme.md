# 🕷️ Web Scraping & Data Extraction

The `Beautiful_Soup/` directory contains Python projects focused on **web scraping, HTML parsing, structured data extraction, and data storage**.

These projects demonstrate how Python can be used to collect information from web pages, process the extracted content, and transform it into structured datasets.

---

## 🎯 Objectives

The main objectives of these projects are to practice:

* HTTP requests
* HTML parsing
* DOM navigation
* Data extraction
* Text processing
* Data cleaning
* CSV generation
* Automating repetitive data collection tasks

---

## 🛠️ Technologies

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| **Python**         | Core programming language |
| **Requests**       | Sending HTTP requests     |
| **BeautifulSoup4** | Parsing HTML documents    |
| **CSV**            | Storing structured data   |

---

## 📂 Projects

### 📋 Project 1 — Job Data Scraper

Located in:

```text
Beautiful_Soup/1/
```

This project focuses on extracting job-related information from web pages and storing the collected information in a CSV file.

**Output:**

```text
Jobs.csv
```

See the dedicated documentation:

**[Project 1 README →](1/README.md)**

---

### 📚 Project 2 — Book Catalog Scraper

Located in:

```text
Beautiful_Soup/2/
```

This project demonstrates extracting book-related information from an online catalog and storing the resulting dataset in:

```text
books_data.csv
```

See the dedicated documentation:

**[Project 2 README →](2/README.md)**

---

## 🔄 Scraping Workflow

```text
Target Website
      ↓
HTTP Request
      ↓
HTML Response
      ↓
BeautifulSoup Parser
      ↓
Locate Required Elements
      ↓
Extract Data
      ↓
Clean / Transform Data
      ↓
Save Structured Dataset
```

---

## 🧠 Core Concepts

The projects in this directory provide practical experience with:

### HTTP Communication

Sending requests to web pages and processing their responses.

### HTML Parsing

Using BeautifulSoup to navigate HTML documents and locate required elements.

### Data Extraction

Selecting specific elements and attributes from a web page.

### Data Processing

Cleaning and organizing extracted information before storing it.

### Structured Output

Converting scraped information into CSV datasets that can be processed later.

---

## ⚡ Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Running a Project

Navigate to the desired project directory.

For example:

```bash
cd "Beautiful_Soup/1"
```

Then run:

```bash
python Project.py
```

For the second project:

```bash
cd "../2"
python Project.py
```

> The exact entry-point filename may vary if the project structure changes.

---

## 📁 Directory Structure

```text
Beautiful_Soup/
│
├── README.md
│
├── 1/
│   ├── README.md
│   ├── Project.py
│   └── Jobs.csv
│
└── 2/
    ├── README.md
    ├── Project.py
    └── books_data.csv
```

---

## 📌 Notes

These projects are primarily intended for learning and practicing web scraping and data extraction techniques.

When scraping websites, always respect the target website's terms of service, robots policies where applicable, rate limits, and applicable laws.

---

**[Project 1 →](1/README.md)**

**[Project 2 →](2/README.md)**
