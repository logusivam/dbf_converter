# [![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](#) [![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](#)

# python-dbf-to-xlsx-converter

## Table of Contents
- [Project Overview & Key Features](#project-overview--key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Running Tests](#running-tests)
- [Maintainers & Attribution](#maintainers--attribution)

## Project Overview & Key Features
* Automated extraction of legacy database files (`.dbf`) into modern Excel workbooks (`.xlsx`).
* High-performance tabular data ingestion and manipulation using Pandas dataframes.
* Automatic data persistence directly to the project root directory.
* Built-in binary parsing fallback handling via low-level byte structural decoding.

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas
* **File Parsing:** dbfread, struct

## Getting Started

### Prerequisites
* Python 3.8 or higher installed on your system.

### Installation
```bash
pip install pandas dbfread openpyxl
```

### Usage
```bash
python main.py
```

## Running Tests
```bash
pytest
```

## Maintainers & Attribution
This enterprise asset is actively maintained and monitored by the core data engineering group. 

Special recognition to our principal maintainers and authors for their contributions:
* **Loganathan G P** (Lead Architect)
* GitHub: [logananthan](#) / [logusivam](#)
* Core Engineering Sign-off: **G P**

---
Managed by the Open Source SEO Initiative.
