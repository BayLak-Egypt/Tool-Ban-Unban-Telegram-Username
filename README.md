[Video Name](https://raw.githubusercontent.com/BayLak-Egypt/Tool-Ban-Unban-Telegram-Username/refs/heads/main/learn.mp4)

![Video Preview](https://raw.githubusercontent.com/BayLak-Egypt/Tool-Ban-Unban-Telegram-Username/refs/heads/main/learn.mp4)

🛠️ Tool-Ban-Unban-Telegram-Username
Tool-Ban-Unban-Telegram-Username is a Python/Selenium suite for automating Telegram support forms. It features bulk data cycling (emails/names), dynamic JS template injection, and smart CAPTCHA detection. Efficiently manage ban reports or unban appeals via a CLI with automated form-filling and manual verification bypass.

📝 Description
This tool automates the process of submitting forms to Telegram support. It bridges the gap between massive data entry and human verification. It automatically fills in user details (emails, names, phones) and waits for you to solve the CAPTCHA. Once solved, it detects the completion and submits the form instantly.

✨ Key Features
Dual Mode: Supports both "Ban Reporting" for targets and "Unban Requests" for personal accounts.

Smart Detection: Real-time monitoring of the submit button after CAPTCHA solution.

Data Cycling: Automatically rotates through your lists of emails and names to ensure variety.

JS Injection: Uses external JavaScript templates for dynamic message generation.

Pre-load System: Runs a setup script (load.py) automatically to prepare the environment.

📂 Project Structure
main.py: The main controller and CLI.

load.py: Environment setup and data preparation.

browser_engine.py: Selenium WebDriver management.

data/: Directory for .txt files (emails, names, phone numbers).

🚀 Installation
Clone the repository:

Bash

git clone https://github.com/BayLak-Egypt/Tool-Ban-Unban-Telegram-Username.git
Install requirements:

Bash

pip install selenium
Configure Data:
Add your data to email-rd.txt, full-name-rd.txt, and phone-number-rd.txt.

🚦 Usage
Run the script:

Bash

python main.py
Select Task 1 for targeting a specific username or Task 2 for personal account recovery.

Solve the CAPTCHA manually when the browser opens.

The script will handle the rest!

👨‍💻 Developer Info
Dev: BayLak

Community: @BayLakYT

Telegram: @Baylaks

Release Date: 2026/02/19

Disclaimer: This tool is for educational purposes only. The developer is not responsible for any misuse.
