# 🔐 Password Security & Attack Simulation Tool

(Educational & Defensive Cybersecurity Project)

## Screenshots

![Screenshot 1](https://github.com/SyedShaheerHussain/Brute-Force-Attack-Simulator-on-Hashes-GUI-/blob/0e2927137ec9e4bc0d745e0659316591c886fa83/screenshots/Screenshot%20(11).png)

![Screenshot 2](https://github.com/SyedShaheerHussain/Brute-Force-Attack-Simulator-on-Hashes-GUI-/blob/0e2927137ec9e4bc0d745e0659316591c886fa83/screenshots/Screenshot%20(12).png)

![Screenshot 3](https://github.com/SyedShaheerHussain/Brute-Force-Attack-Simulator-on-Hashes-GUI-/blob/0e2927137ec9e4bc0d745e0659316591c886fa83/screenshots/Screenshot%20(13).png)

![Screenshot 4](https://github.com/SyedShaheerHussain/Brute-Force-Attack-Simulator-on-Hashes-GUI-/blob/0e2927137ec9e4bc0d745e0659316591c886fa83/screenshots/Screenshot%20(14).png)

## 📌 Overview 

### Brute-Force-Attack-Simulator-on-Hashes-GUI-

The Password Security &amp; Attack Simulation Tool is a desktop-based Python application designed to educate users about password security by visually simulating how dictionary attacks and brute-force attacks work against weak password hashes.

## Description

A Python desktop tool that educates users on password security by simulating dictionary and brute-force attacks on weak hashes.

> [!IMPORTANT]
> This project is purely educational and defensive.

It does NOT target real systems or real users and is intended to raise awareness about:

- Weak vs strong passwords

- Importance of salting

- Secure hashing algorithms

- Why brute-force attacks become impractical against strong passwords

- How rate limiting and lock mechanisms protect real-world systems

## ⚠️ Ethical Disclaimer

This tool is strictly for educational and awareness purposes only.

Using this software against real systems, accounts, or users without permission is illegal and unethical.

The goal is to understand attacker techniques so that better defenses can be designed.

## 🎯 Project Objectives

* Demonstrate how weak passwords can be cracked easily

* Show how salting changes hash behavior

* Compare hashing algorithms (MD5 → PBKDF2)

* Simulate realistic attack behavior with rate limiting

* Provide a real-world-like GUI experience

* Allow users to start, monitor, and stop attacks safely

* Educate non-technical users visually

## 🧠 Key Concepts Covered

* Password Hashing vs Encryption

* Salting & why it breaks precomputed attacks

* Dictionary attacks

* Brute-force attacks

* Password entropy & strength

* Rate limiting

* Attack monitoring & control

* Secure password practices

## 🖥️ Application Interface (GUI)

The application uses a modern, professional GUI built with CustomTkinter, featuring:

* Clean layout with panels

* Status indicators

* Progress loading animation

* Disabled controls during attacks

* Live logs for attack activity

* Real-time feedback messages

## 🔧 Features

### 🔐 Password Handling

* Password input (never stored on disk)

* Real-time password strength indicator

* Password entropy calculation (bits)

### 🔑 Hashing Algorithms

* MD5 (insecure – educational)

* SHA1 (deprecated)

* SHA256

* SHA512

* PBKDF2 (industry standard, slow hash)

### 🧂 Salting

* Optional salting toggle

* Mandatory salt enforcement for PBKDF2

* Demonstrates how salts change hash outputs

### ⚔️ Attack Simulations

* Dictionary Attack

* Uses a local wordlist (dictionary.txt)

* Simulates common password cracking

* Rate-limited to mimic real systems

* Shows success, failure, or user stop

* Brute Force Attack

* Custom character set selection

* Configurable maximum length

* Real-time attempt counting

* Rate-limited execution

* Fully stoppable by user

### ⏳ Attack Control & Feedback

* Attack start messages

* Progress bar animation (loading indicator)

* Status label: Idle / Running

* Stop attack at any time

* Clear completion, failure, or stop messages

## 🧪 Real-World Behavior Simulation
| Real System Feature | Project Implementation      |
| ------------------- | --------------------------- |
| Rate Limiting       | Attempts per second limiter |
| Lockout Control     | Stop button                 |
| Attack Visibility   | Status + progress bar       |
| Secure Hashing      | PBKDF2 support              |
| UI Feedback         | Logs + status indicators    |

## 🏗️ Project Structure

```
BruteForce-Hash-Simulator/
│
├── main.py          # Application entry point
├── gui.py           # GUI logic & event handling
├── hashing.py       # Hashing & salting functions
├── attacks.py       # Dictionary & brute-force logic
├── strength.py      # Password strength & entropy
├── rate_limit.py    # Rate-limiting simulation
├── dictionary.txt   # Sample password list
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

## ⚙️ Technologies Used

* Python 3.10+

* CustomTkinter (modern Tkinter UI)

* hashlib (cryptographic hashing)

* threading (non-blocking GUI)

* itertools (brute-force generation)

* OS / Math modules

## 📥 Installation

### Clone Repository

```
 git clone https://github.com/SyedShaheerHussain/Brute-Force-Attack-Simulator-on-Hashes-GUI-

```
```
cd Brute Force Attack Simulator on Hashes

```

## ▶️ Running the Application

```
python main.py

```

## 🧠 How It Works (High Level)

* User enters a password

* Application evaluates strength & entropy

* User selects hashing algorithm and salting

* Hash is generated internally

* Attack simulation begins

* Progress bar + status show activity

* User may stop attack anytime

* Result is displayed with attempt count

## 🔍 Core Functions & Modules

1. hashing.py

2. generate_salt()

3. hash_password(password, algorithm, salt)

4. strength.py

5. entropy(password)

6. strength(password)

7. attacks.py

8. dictionary_attack(...)

9. brute_force_attack(...)

10. rate_limit.py

11. RateLimiter.allow()

12. gui.py

13. GUI layout & controls

14. Thread-safe attack handling

15. Progress & status updates

16. Start/Stop logic

## 🧑‍🎓 Intended Audience

- Cybersecurity students

- Beginners learning password security

- Final Year Project (FYP) submissions

- Demonstrations & presentations

- Portfolio / GitHub showcase

## 🚫 What This Project Is NOT

❌ Not a hacking tool

❌ Not for real-world cracking

❌ Not designed for illegal usage

## 📈 Possible Future Enhancements

+ Attack time estimation graphs

+ PDF report generation

+ bcrypt / Argon2 support

+ Login system simulation

+ Dark/light theme toggle

+ CSV export of attack logs

## 🏆 Academic Value

This project demonstrates:

1. Secure coding practices

2. Ethical cybersecurity mindset

3. GUI design for technical tools

4. Thread-safe application logic

5. Real-world security awareness

## 📜 License & 🙌 Final Note

> [!NOTE]
> This project is released for educational use only.
> You are free to study, modify, and share it responsibly.
> Strong passwords + modern hashing = real security
> Understanding attacks is the first step to building defenses.

## ⭐ Support & Engagement

If you find this repository useful or insightful, please consider:

- ⭐ Starring the repository
- 🔁 Sharing it within your network
- 👤 Following my GitHub profile for future projects and updates

Your support helps drive continued innovation and open-source contributions.

— Syed Shaheer Hussain

[![GitHub followers](https://img.shields.io/github/followers/SyedShaheerHussain?label=Follow&style=social)](https://github.com/SyedShaheerHussain)

![Followers](https://img.shields.io/github/followers/SyedShaheerHussain?label=Followers&color=blue)

![Stars](https://img.shields.io/github/stars/SyedShaheerHussain/Brute-Force-Attack-Simulator-on-Hashes-GUI-?label=Stars&color=yellow)
