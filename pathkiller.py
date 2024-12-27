import argparse
import requests
import inquirer
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to perform HTTP request
def scan_path(base_url, path, extensions, headers, total_paths, index):
    found = False  # Flag to track if we've found any valid URLs
    for ext in extensions:
        url = f"{base_url.rstrip('/')}/{path.strip()}{ext}"
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code in [200, 301]:
                if not found:  # Print the first found URL and status
                    print(f"{Fore.GREEN}[+] Found: {url} ({response.status_code})")
                    found = True
        except requests.exceptions.RequestException:
            continue  # Skip errors without printing anything

        # Output the progress
        progress = (index + 1) / total_paths * 100
        sys.stdout.write(f"\r[+] Scanning {index + 1}/{total_paths} ({progress:.2f}%)")  # Print on the same line
        sys.stdout.flush()

# Load paths from a wordlist
def load_wordlist(wordlist_path):
    if not os.path.isfile(wordlist_path):
        print(f"{Fore.RED}[!] Wordlist file not found: {wordlist_path}")
        return []
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            return [line.strip() for line in f]
    except UnicodeDecodeError:
        print(f"{Fore.RED}[!] Failed to decode {wordlist_path} with UTF-8. Trying Latin-1...")
        try:
            with open(wordlist_path, "r", encoding="latin-1", errors="ignore") as f:
                return [line.strip() for line in f]
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to load wordlist: {e}")
            return []

# Main scanning function
def start_scan(base_url, wordlist, extensions, threads, headers):
    paths = load_wordlist(wordlist)
    if not paths:
        return

    total_paths = len(paths)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for index, path in enumerate(paths):
            futures.append(executor.submit(scan_path, base_url, path, extensions, headers, total_paths, index))
        
        try:
            # Wait for all futures to complete
            for future in as_completed(futures):
                future.result()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted. Closing threads...")
            sys.exit(0)

    print("\n[+] Scan completed.")

# Function to display a simple menu to select wordlist and website URL
def select_inputs():
    # List of common wordlist paths available in Kali Linux
    wordlist_options = [
        '/usr/share/wordlists/rockyou.txt', 
        '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt',
        '/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt',
        '/usr/share/wordlists/dirbuster/directory-list-2.3-big.txt',
        '/usr/share/wordlists/dirbuster/directory-list-2.3-merged.txt',
        '/usr/share/wordlists/seclists/Discovery/Web-Content/common.txt',
        '/usr/share/wordlists/seclists/Discovery/Web-Content/big.txt',
        '/usr/share/wordlists/seclists/Discovery/Web-Content/raft-large-directories.txt'
    ]
    
    questions = [
        inquirer.List('wordlist',
                      message="Select a wordlist",
                      choices=wordlist_options,
                      default=wordlist_options[0]),
        inquirer.Text('url', message="Enter the website URL (e.g., http://example.com)", validate=lambda _, x: x.startswith("http"))
    ]
    
    answers = inquirer.prompt(questions)
    return answers['url'], answers['wordlist']

# Main function
def main():
    # Print program title and author info
    print(f"{Fore.RED}{Style.BRIGHT}Pathkiller{Style.RESET_ALL}")
    print(f"{Fore.WHITE}by {Fore.RED}@kloveyzstd {Fore.WHITE}| Tbilisian Coder{Style.RESET_ALL}\n")

    # Get URL and wordlist selection from user input
    base_url, wordlist_path = select_inputs()

    # Ask for optional extensions
    extensions = input("Enter comma-separated file extensions to test (e.g., .php,.html,.txt) or press Enter for default: ").split(",")
    
    # Ask for number of threads
    threads = int(input("Enter the number of threads to use (default 10): ") or 10)

    # Ask for custom headers if needed
    headers = {}
    add_headers = input("Do you want to add custom headers? (y/n): ").lower()
    if add_headers == 'y':
        while True:
            header = input("Enter a header (e.g., 'User-Agent: custom') or press Enter to stop: ")
            if not header:
                break
            try:
                key, value = header.split(":", 1)
                headers[key.strip()] = value.strip()
            except ValueError:
                print(f"{Fore.RED}[!] Invalid header format. Please use 'key: value' format.")
    
    # Start the scan
    start_scan(base_url, wordlist_path, extensions, threads, headers)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Program interrupted. Exiting gracefully...")
        sys.exit(0)
