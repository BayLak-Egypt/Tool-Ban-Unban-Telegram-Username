import os
def load_text_list(file_name):
    if not os.path.exists(file_name): return []
    with open(file_name, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]
def load_js_templates(file_name, choice):
    if not os.path.exists(file_name): return []
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
    ban_list, unban_list = [], []
    current_mode = None
    for line in content:
        line = line.strip()
        if "BAN" in line: current_mode = "ban"
        elif "UNBAN" in line: current_mode = "unban"
        if '"' in line and current_mode:
            text = line.split('"')[1]
            if current_mode == "ban": ban_list.append(text)
            else: unban_list.append(text)
    return ban_list if choice == "1" else unban_list