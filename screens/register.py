import re
import customtkinter as ctk
from tkinter import messagebox
from database.database import register_user
from theme import *

class RegisterScreen(ctk.CTkFrame):

    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        # Title
        title = ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(40, 20))

        # Name
        self.name = ctk.CTkEntry(
            self,
            placeholder_text="Full Name",
            width=350,
            height=45
        )
        self.name.pack(pady=10)

        # Email
        self.email = ctk.CTkEntry(
            self,
            placeholder_text="Email",
            width=350,
            height=45
        )
        self.email.pack(pady=10)

        # Password
        self.password = ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*",
            width=350,
            height=45
        )
        self.password.pack(pady=10)

        # Skill You Can Teach
        self.skill = ctk.CTkEntry(
            self,
            placeholder_text="Skill You Can Teach",
            width=350,
            height=45
        )
        self.skill.pack(pady=10)

        # Skill You Want To Learn
        self.learn_skill = ctk.CTkEntry(
            self,
            placeholder_text="Skill You Want To Learn",
            width=350,
            height=45
        )
        self.learn_skill.pack(pady=10)

        # Register Button
        self.register_btn = ctk.CTkButton(
            self,
            text="Register",
            width=350,
            height=45,
            command=self.register
        )
        self.register_btn.pack(pady=20)

        # Back Button
        self.back_btn = ctk.CTkButton(
            self,
            text="Back to Login",
            width=350,
            height=45,
            fg_color="gray",
            command=self.go_back
        )
        self.back_btn.pack()

    def register(self):

        name = self.name.get().strip()
        email = self.email.get().strip()
        password = self.password.get()
        skill = self.skill.get().strip()
        learn_skill = self.learn_skill.get().strip()

        # Empty Field Validation
        if not name or not email or not password or not skill or not learn_skill:
            messagebox.showerror(
                "Error",
                "All fields are required."
            )
            return

        # Name Validation
        if len(name) < 2:
            messagebox.showerror(
                "Error",
                "Name must contain at least 2 characters."
            )
            return

        # Email Validation
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.match(email_pattern, email):
            messagebox.showerror(
                "Error",
                "Enter a valid email address."
            )
            return

        # Password Validation
        if len(password) < 4:
            messagebox.showerror(
                "Error",
                "Password must be at least 4 characters long."
            )
            return

        # Skill Validation
        if len(skill) < 2:
            messagebox.showerror(
                "Error",
                "Please enter a valid skill."
            )
            return

        # Learn Skill Validation
        if len(learn_skill) < 2:
            messagebox.showerror(
                "Error",
                "Please enter the skill you want to learn."
            )
            return

        try:
            success = register_user(
                name,
                email,
                password,
                skill,
                learn_skill
            )

            if success:
                messagebox.showinfo(
                    "Success",
                    "Registration Successful!"
                )
                self.parent.show_login()

            else:
                messagebox.showerror(
                    "Registration Failed",
                    "An account with this email already exists."
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def go_back(self):
        self.parent.show_login()