import customtkinter as ctk, threading
from hashing import *
from attacks import *
from rate_limit import *
from strength import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Security Simulator")
        self.geometry("1100x750")

        self.stop_attack = False
        self.attack_running = False

        self.password = ctk.StringVar()
        self.algorithm = ctk.StringVar(value="SHA256")
        self.use_salt = ctk.BooleanVar()
        self.charset = ctk.StringVar(value="abc123")
        self.max_len = ctk.IntVar(value=4)

        self.build_ui()

    def build_ui(self):
        tabs = ctk.CTkTabview(self)
        tabs.pack(fill="both", expand=True, padx=10, pady=10)

        tab = tabs.add("Attack Simulator")

        left = ctk.CTkFrame(tab, width=300)
        left.pack(side="left", fill="y", padx=10)

        # -------- INPUTS --------
        ctk.CTkLabel(left, text="Password").pack(pady=5)
        ctk.CTkEntry(left, textvariable=self.password, show="*").pack()

        self.info = ctk.CTkLabel(left, text="")
        self.info.pack(pady=5)

        self.password.trace_add(
            "write",
            lambda *_: self.info.configure(
                text=f"{strength(self.password.get())} | "
                     f"Entropy: {entropy(self.password.get())} bits"
            )
        )

        ctk.CTkCheckBox(left, text="Enable Salting", variable=self.use_salt).pack(pady=5)

        ctk.CTkOptionMenu(
            left, variable=self.algorithm,
            values=["MD5","SHA1","SHA256","SHA512","PBKDF2"]
        ).pack(pady=5)

        ctk.CTkLabel(left, text="Charset").pack()
        ctk.CTkEntry(left, textvariable=self.charset).pack()

        ctk.CTkLabel(left, text="Max Length").pack()
        ctk.CTkSlider(left, from_=1, to=6, variable=self.max_len).pack()

        # -------- BUTTONS --------
        self.btn_dict = ctk.CTkButton(left, text="Dictionary Attack", command=self.start_dict)
        self.btn_dict.pack(pady=5)

        self.btn_brute = ctk.CTkButton(left, text="Brute Force Attack", command=self.start_brute)
        self.btn_brute.pack(pady=5)

        self.btn_stop = ctk.CTkButton(left, text="STOP ATTACK", fg_color="red", command=self.stop)
        self.btn_stop.pack(pady=5)

        # -------- STATUS --------
        self.status = ctk.CTkLabel(left, text="Status: Idle")
        self.status.pack(pady=10)

        self.progress = ctk.CTkProgressBar(left, mode="indeterminate")
        self.progress.pack(fill="x", pady=5)

        # -------- OUTPUT --------
        self.output = ctk.CTkTextbox(tab)
        self.output.pack(fill="both", expand=True, padx=10)

    # ---------- HELPERS ----------
    def log(self, msg):
        self.output.insert("end", msg + "\n")
        self.output.see("end")

    def set_running(self, running):
        self.attack_running = running
        if running:
            self.progress.start()
            self.status.configure(text="Status: Attack Running...")
            self.btn_dict.configure(state="disabled")
            self.btn_brute.configure(state="disabled")
        else:
            self.progress.stop()
            self.status.configure(text="Status: Idle")
            self.btn_dict.configure(state="normal")
            self.btn_brute.configure(state="normal")

    # ---------- STOP ----------
    def stop(self):
        if self.attack_running:
            self.stop_attack = True
            self.log("Attack stopped by user.")

    # ---------- DICTIONARY ----------
    def start_dict(self):
        if self.attack_running:
            return
        self.stop_attack = False
        self.set_running(True)
        self.log("Dictionary attack started...")
        threading.Thread(target=self.dict_thread, daemon=True).start()

    def dict_thread(self):
        pwd = self.password.get()
        algo = self.algorithm.get()
        salt = generate_salt() if (self.use_salt.get() or algo == "PBKDF2") else None
        target = hash_password(pwd, algo, salt)

        limiter = RateLimiter()
        with open("dictionary.txt") as f:
            result, attempts = dictionary_attack(
                target, algo, salt, f, limiter,
                lambda: self.stop_attack
            )

        self.after(0, lambda: self.finish_attack(result, attempts, "Dictionary"))

    # ---------- BRUTE ----------
    def start_brute(self):
        if self.attack_running:
            return
        self.stop_attack = False
        self.set_running(True)
        self.log("Brute force attack started...")
        threading.Thread(target=self.brute_thread, daemon=True).start()

    def brute_thread(self):
        pwd = self.password.get()
        algo = self.algorithm.get()
        salt = generate_salt() if (self.use_salt.get() or algo == "PBKDF2") else None
        target = hash_password(pwd, algo, salt)

        limiter = RateLimiter()
        result, attempts = brute_force_attack(
            target, algo, salt,
            self.charset.get(),
            int(self.max_len.get()),
            limiter,
            lambda: self.stop_attack
        )

        self.after(0, lambda: self.finish_attack(result, attempts, "Brute Force"))

    # ---------- FINISH ----------
    def finish_attack(self, result, attempts, mode):
        self.set_running(False)

        if self.stop_attack:
            self.log(f"{mode} attack stopped. Attempts: {attempts}")
        elif result:
            self.log(f"{mode} SUCCESS → Password: {result} | Attempts: {attempts}")
        else:
            self.log(f"{mode} FAILED → Attempts: {attempts}")
