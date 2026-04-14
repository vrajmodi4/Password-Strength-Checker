import tkinter as tk
from tkinter import messagebox
import re
import sys
import os

# Core Logic (Reuse from CLI version essentially)
def check_strength_logic(password):
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) < 8:
        feedback.append("• Too short: Aim for 8+ characters.")
    else:
        score += 1
        
    # Criteria 2: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add a number.")
        
    # Criteria 3: Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add an uppercase letter.")
        
    # Criteria 4: Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add a lowercase letter.")
        
    # Criteria 5: Special Characters
    if re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        feedback.append("• Add a special character (e.g., !@#).")

    # Determine Strength Label & Color
    if score == 5:
        strength = "VERY STRONG"
        color = "green"
    elif score >= 4:
        strength = "STRONG"
        color = "lightgreen"
    elif score >= 3:
        strength = "MEDIUM"
        color = "orange"
    elif score >= 2:
        strength = "WEAK"
        color = "red"
    else:
        strength = "VERY WEAK"
        color = "darkred"
        
    return strength, color, feedback

# GUI Application Class
class PasswordCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Strength Checker")
        master.geometry("400x350")
        master.resizable(False, False)

        # Title Label
        self.label = tk.Label(master, text="Check Your Password Strength", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        # Entry Widget
        self.entry = tk.Entry(master, show="*", font=("Arial", 12), width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_password)

        # Show Password Checkbox
        self.show_password_var = tk.BooleanVar()
        self.check_show = tk.Checkbutton(master, text="Show Password", variable=self.show_password_var, command=self.toggle_visibility)
        self.check_show.pack()

        # Strength Label
        self.result_label = tk.Label(master, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        # Feedback Area
        self.feedback_text = tk.Label(master, text="", font=("Arial", 10), justify="left", wraplength=350)
        self.feedback_text.pack(pady=10)

    def check_password(self, event=None):
        password = self.entry.get()
        if not password:
            self.result_label.config(text="")
            self.feedback_text.config(text="")
            return

        strength, color, feedback = check_strength_logic(password)
        
        self.result_label.config(text=f"Strength: {strength}", fg=color)
        
        feedback_str = "\n".join(feedback) if feedback else "Great job! Your password meets all criteria."
        self.feedback_text.config(text=feedback_str)

    def toggle_visibility(self):
        if self.show_password_var.get():
            self.entry.config(show="")
        else:
            self.entry.config(show="*")

if __name__ == "__main__":
    if sys.platform != 'win32' and not os.environ.get('DISPLAY'):
        print("This script requires a GUI environment. Please create a .py file and run it locally.")
    else:
        root = tk.Tk()
        app = PasswordCheckerApp(root)
        root.mainloop()
