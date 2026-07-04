import customtkinter as ctk
from tkinter import messagebox
from database.database import register_user


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

        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        skill = self.skill.get()
        learn_skill = self.learn_skill.get()

        if not name or not email or not password:
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
            return

        try:
            register_user(
                name,
                email,
                password,
                skill,
                learn_skill
            )

            messagebox.showinfo(
                "Success",
                "Account created successfully!"
            )

            self.parent.show_login()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def go_back(self):
        self.parent.show_login()