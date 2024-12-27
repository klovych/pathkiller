# Pathkiller 🕵️‍♂️🔍

Pathkiller is a directory brute-forcing tool for web servers. It uses wordlists to guess paths and identify hidden directories and files.

> by @kloveyzstd | Tbilisian Coder 🇬🇪

## 📦 Installation

To install all dependencies, use `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
📝 Usage
Run the program with Python:
```
python pathkiller.py
```
You will be prompted to select a wordlist, provide the website URL, and set other parameters.

🚀 How It Works
Pathkiller sends HTTP requests to the provided URL with each path from the wordlist, appending the specified extensions. It uses multithreading to speed up the process and displays results with HTTP status codes 200 and 301.

If you wish to configure custom headers for requests, you can specify them via the command line.

🔧 Configuration
You can specify the wordlist, URL, number of threads, and file extensions you want to test. Pathkiller will automatically perform all the requests and display the results.

Project Structure:
```
pathkiller/
├── pathkiller.py        # Main script of the program
├── README.md            # Project description
├── requirements.txt     # List of dependencies
└── LICENSE              # Project license
```
