import time
import sys
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browser_engine import BrowserManager
from data_loader import load_text_list, load_js_templates
from config import TARGET_URL, TIMEOUT, CAPTCHA_WAIT
def run_load_script():
    """Runs the load.py script and waits for it to finish"""
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    load_path = os.path.join(current_dir, "load.py")
    print(f"⏳ Running: {load_path}")
    try:
        subprocess.run([sys.executable, load_path], check=True)
        print("✅ load.py finished successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error while running load.py: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
def print_ascii_art():
    """Prints a cool ASCII art banner with colored side info"""
    BLUE = "\033[94m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    art_lines = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⣿⡄",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⡿⠿⠛⢙⣿⣿⠃",
        "⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣾⣿⣿⠿⠛⠋⠁⠀⠀⠀⣸⣿⣿⠀",
        "⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⡿⠟⠛⠉⠀⠀⣠⣤⠞⠁⠀⠀⣿⣿⡇",
        "⠀⣴⣾⣿⣿⡿⠿⠛⠉⠀⠀⠀⢀⣠⣶⣿⠟⠁⠀⠀⠀⢸⣿⣿",
        "⠸⣿⣿⣿⣧⣄⣀⠀⠀⣀⣴⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⣼⣿⡿",
        "⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⠇",
        "⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡇⠀⣀⣄⡀⠀⠀⠀⠀⢸⣿⣿",
        "⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣠⣾⣿⣿⣿⣦⡀⠀⠀⣿⣿⡏",
        "⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡿⠋⠈⠻⣿⣿⣦⣸⣿⣿⠁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⠏"
    ]
    side_text = [
        f"{YELLOW}Ban/Unban Tool v1.0{RESET}",
        f"{RED}2026/2/19{RESET}",
        f"{GREEN}Made by BayLak{RESET}",
        f"{GREEN}MyGroup: @BayLakYT{RESET}",
        f"{GREEN}MyTelegram: @Baylaks{RESET}"
    ]
    for i, line in enumerate(art_lines):
        if i < len(side_text):
            print(f"{BLUE}{line}{RESET}  {side_text[i]}")
        else:
            print(f"{BLUE}{line}{RESET}")
def run_task():
    print_ascii_art()
    run_load_script()
    print("="*50)
    print(" 🛠️  MAIN CONFIGURATION")
    print("="*50)
    print("1. Task One (dec.js + Replace [x] + Phone List)")
    print("2. Task Two (dec01.js + Personal Phone)")
    task_choice = input("Select Task (1 or 2): ")
    print("\n1. Ban Report | 2. Unban Request")
    type_choice = input("Select Type (1 or 2): ")
    emails = load_text_list("email-rd.txt")
    names = load_text_list("full-name-rd.txt")
    if not emails or not names:
        print("❌ Error: Email or Name files are empty!"); return
    if task_choice == "1":
        target_user = input("Enter target username to replace [x]: ")
        templates = load_js_templates("dec.js", type_choice)
        phones = load_text_list("phone-number-rd.txt")
        data_cycle_limit = min(len(emails), len(names), len(phones), len(templates))
    else:
        target_user = ""
        my_private_phone = input("Enter your personal phone number: ")
        templates = load_js_templates("dec01.js", type_choice)
        data_cycle_limit = min(len(emails), len(names), len(templates))
    print(f"\n📊 Unique records found: {data_cycle_limit}")
    try:
        total_to_run = int(input("How many operations total? (0 for cycle unique records only): "))
        if total_to_run <= 0:
            total_to_run = data_cycle_limit
    except ValueError:
        total_to_run = data_cycle_limit
    print(f"🚀 Starting {total_to_run} operations...")
    driver = BrowserManager.get_driver()
    for i in range(total_to_run):
        idx = i % data_cycle_limit
        final_desc = templates[idx].replace("[x]", target_user) if task_choice == "1" else templates[idx]
        current_email = emails[idx % len(emails)]
        current_name = names[idx % len(names)]
        current_phone = phones[idx % len(phones)] if task_choice == "1" else my_private_phone
        print(f"\n[{i+1}/{total_to_run}] Current Session: {current_email}")
        driver.get(TARGET_URL)
        try:
            wait = WebDriverWait(driver, TIMEOUT)
            wait.until(EC.presence_of_element_located((By.ID, "support_problem"))).send_keys(final_desc)
            driver.find_element(By.ID, "support_email").send_keys(current_email)
            driver.find_element(By.ID, "support_phone").send_keys(current_phone)
            try:
                driver.find_element(By.ID, "support_legal_name").send_keys(current_name)
            except: pass
            print(f"⚠️  WAITING: Solve the CAPTCHA in the browser.")
            submitted = False
            for sec in range(CAPTCHA_WAIT, 0, -1):
                sys.stdout.write(f"\r⏱️  Monitor: {sec}s left... ")
                sys.stdout.flush()
                is_ready = driver.execute_script("""
                    var btn = document.querySelector('div.support_submit > button');
                    var success = document.querySelector('#success');
                    var isVisible = success && success.style.display !== 'none';
                    return (btn && !btn.disabled) || isVisible;
                """)
                if is_ready:
                    print(f"\n✨ Solution detected! Submitting...")
                    driver.execute_script("""
                        var btn = document.querySelector('div.support_submit > button');
                        if(btn) {
                            btn.disabled = false;
                            btn.click();
                            var form = btn.closest('form');
                            if(form) form.submit();
                        }
                    """)
                    submitted = True
                    break
                time.sleep(1)
            if submitted:
                print(f"✅ Operation {i+1} completed.")
                time.sleep(2)
            else:
                print(f"\n❌ Operation {i+1} timed out.")
        except Exception as e:
            print(f"\n❌ Script Error: {str(e)[:50]}")
if __name__ == "__main__":
    try:
        run_task()
    finally:
        print("\n" + "="*50)
        print("🏁 WORKFLOW FINISHED")
        print("="*50)
        BrowserManager.quit_driver()