# 📧 Bobe's HMC - Hotmail Checker 🔥

Welcome to **Bobe's HMC** – the ultimate multithreaded Hotmail/Office365 SMTP combo checker! 🚀 This tool checks email and password combinations against the Office365 SMTP server with real-time stats, progress updates, and detailed logging. Fast, efficient, and accurate – a must-have tool for Hotmail combo checking enthusiasts! 💻

## 🔥 Features

- **Multithreaded Power** ⚡: Test combos quickly with concurrent threads.
- **Real-Time Stats** 📊: View checks per minute (CPM), progress, and elapsed time while running.
- **Progress Bar** 📈: Keep track of how far along the process is with a visual progress bar.
- **Detailed Logging** 📝:
  - **Hits** ✅: Successfully authenticated combos are saved to `hits.txt`.
  - **Bad Combos** ❌: Invalid combinations are saved to `bad.txt`.
  - **Errors** ⚠️: Any errors encountered are logged in `error.log`.

## 🚀 How to Use

1. **Install Dependencies**:
   Make sure you have the required Python packages:
   ```bash
   pip install smtplib colorama pystyle
Prepare Your Combo List: Create a combo.txt file in the root directory. Each line should contain a combo in the format:

scss
Copy code
email@example.com:password123
Run the Checker: Run the script and provide the number of threads you want to use.

bash
Copy code
python checker.py
Watch the Magic ✨:

The script will start testing the combos and display real-time stats like hits, bad combos, errors, and CPM.
Logs will be saved in hits.txt (for valid credentials), bad.txt (for invalid credentials), and error.log (for errors encountered).
🛠 Configuration
Threads: Specify the number of threads you want to run simultaneously. Higher numbers may increase speed but require more resources.
Combo File: Ensure that your combo.txt file contains valid email-password pairs in the format email:password (one pair per line).
📂 Output Files
hits.txt: Stores successfully validated email-password pairs.
bad.txt: Stores invalid combinations that failed authentication.
error.log: Logs any errors encountered during the checking process.


#⚠️ Disclaimer
# This tool is intended for educational purposes only. The creator does not condone or support illegal activities. Use it responsibly!

ignore the ai generated readme lmaooo

