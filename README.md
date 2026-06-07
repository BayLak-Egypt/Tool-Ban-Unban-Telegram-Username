![Video Preview](https://raw.githubusercontent.com/BayLak-Egypt/Tool-Ban-Unban-Telegram-Username/refs/heads/main/learn.mp4)


 <td align="center">
      <a href="https://github.com/BayLak-Egypt/Tool-Ban-Unban-Telegram-Username">
        <img src="logo.png" width="20" height="20" />
      </a>
    </td>
 <td>
        <strong>  Tool-Ban-Unban-Telegram-Username V1.0</strong>
      </a>
    </td>

is a Python/Selenium suite for automating Telegram support forms. It features bulk data cycling (emails/names), dynamic JS template injection, and smart CAPTCHA detection. Efficiently manage ban reports or unban appeals via a CLI with automated form-filling and manual verification bypass.

***📝 Description***
This tool automates the process of submitting forms to Telegram support. It bridges the gap between massive data entry and human verification. It automatically fills in user details (emails, names, phones) and waits for you to solve the **CAPTCHA**. Once solved, it detects the completion and submits the form instantly.

***✨ Key Features***
Dual Mode: Supports both "Ban Reporting" for targets and "Unban Requests" for personal accounts.

Smart Detection: Real-time monitoring of the submit button after CAPTCHA solution.

Data Cycling: Automatically rotates through your lists of emails and names to ensure variety.

JS Injection: Uses external JavaScript templates for dynamic message generation.

Pre-load System: Runs a setup script (load.py) automatically to prepare the environment.

***📂 Project Structure***
main.py: The main controller and CLI.

load.py: Environment setup and data preparation.

browser_engine.py: Selenium WebDriver management.

data/: Directory for .txt files (emails, names, phone numbers).

***🚀 Installation***
Clone the repository:
```
git clone https://github.com/BayLak-Egypt/Tool-Ban-Unban-Telegram-Username.git
```
Install requirements:
```
pip install selenium
```
Configure Data:
Add your data to email-rd.txt, full-name-rd.txt, and phone-number-rd.txt.

***🚦 Usage***
Run the script:
```
python3 main.py
```
Select Task 1 for targeting a specific username or Task 2 for personal account recovery.

Solve the CAPTCHA manually when the browser opens.

The script will handle the rest!

***👨‍💻 Developer:*** **BayLak-Egypt**

[![Telegram](https://img.shields.io/badge/Telegram-@Baylaks-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Baylaks)
[![Telegram Channel](https://img.shields.io/badge/Channel-@BayLakYT-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/BayLakYT)
[![Youtube](https://img.shields.io/badge/youtube-baylak--egypt-E4405F?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@baylak-egypt)
[![Tiktok](https://img.shields.io/badge/tiktok-baylakeg-000000?style=for-the-badge&logo=fiverr&logoColor=white)](https://www.tiktok.com/@baylakeg)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-baylakeg-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send/?phone=4915510391781&text=hello&type=phone_number&app_absent=0)
[![Fiverr](https://img.shields.io/badge/Fiverr-baylakeg-1DBF73?style=for-the-badge&logo=fiverr&logoColor=white)](https://fiverr.com/baylakeg)


**Release Date: 2026/02/19**

**Disclaimer: This tool is for educational purposes only. The developer is not responsible for any misuse.**
