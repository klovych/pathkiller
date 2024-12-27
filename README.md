# Pathkiller 🕵️‍♂️🔍

Pathkiller is a directory brute-forcing tool for web servers. It uses wordlists to guess paths and identify hidden directories and files.

> by @kloveyzstd | Tbilisian Coder 🇬🇪

## 📦 Installation:
#### **1. Clone the repository:**

You can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/klovych/pathkiller.git
cd pathkiller
```
#### **2. To install all dependencies, use `pip` and the `requirements.txt` file:**

```bash
pip install -r requirements.txt
```
📝 Usage:
Run the program with Python:
```
python pathkiller.py
```
You will be prompted to select a wordlist, provide the website URL, and set other parameters.

![image](https://github.com/user-attachments/assets/098d24dd-83a4-4fc6-ba3e-0f2eefa44e67)
![image](https://github.com/user-attachments/assets/40f3e80a-e175-443e-a9f3-16b161de52cf)
![image](https://github.com/user-attachments/assets/4644325f-2ca4-488a-a794-23bd58cd1365)
![image](https://github.com/user-attachments/assets/e066b5c0-b018-4240-8eb4-6d7350761d6f)
![image](https://github.com/user-attachments/assets/3ba0421f-8bd9-446f-8737-266e81a0f296)
![image](https://github.com/user-attachments/assets/ac84bfaf-2fb6-4a2e-8ea7-757a36200a1c)




🚀 How It Works:

Pathkiller sends HTTP requests to the provided URL with each path from the wordlist, appending the specified extensions. It uses multithreading to speed up the process and displays results with HTTP status codes 200 and 301.

If you wish to configure custom headers for requests, you can specify them via the command line.

🔧 Configuration:
You can specify the wordlist, URL, number of threads, and file extensions you want to test. Pathkiller will automatically perform all the requests and display the results.

Project Structure:
```
pathkiller/
├── pathkiller.py        # Main program script
├── README.md            # Project description and usage
├── requirements.txt     # List of dependencies
└── LICENSE              # License file (MIT License)
```
