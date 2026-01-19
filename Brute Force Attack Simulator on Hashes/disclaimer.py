import customtkinter as ctk
import sys

def show_disclaimer():
    app = ctk.CTk()
    app.geometry("600x400")
    app.title("Educational Disclaimer")

    text = (
        "⚠️ DISCLAIMER ⚠️\n\n"
        "This application is strictly for EDUCATIONAL purposes.\n\n"
        "It demonstrates how weak passwords and unsalted hashes "
        "can be cracked easily.\n\n"
        "Using this tool on real systems or real users is illegal.\n\n"
        "Click 'I Agree' to continue."
    )

    label = ctk.CTkLabel(app, text=text, wraplength=520)
    label.pack(pady=40)

    def accept():
        app.destroy()

    btn = ctk.CTkButton(app, text="I Agree", command=accept)
    btn.pack(pady=20)

    app.mainloop()
