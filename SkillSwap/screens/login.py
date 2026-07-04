import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from database.database import login_user


class LoginScreen(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.pack(fill="both", expand=True)

        # ==========================
        # LEFT PANEL
        # ==========================
        self.left_frame = ctk.CTkFrame(
            self,
            width=400,
            fg_color="#4F46E5",
            corner_radius=0
        )
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.pack_propagate(False)

        # ==========================
        # RIGHT PANEL
        # ==========================
        self.right_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=0
        )
        self.right_frame.pack(side="right", fill="both", expand=True)

        # ==========================
        # LOGO
        # ==========================
        self.logo_image = ctk.CTkImage(
            light_image=Image.open("assets/icons/people.png"),
            dark_image=Image.open("assets/icons/people.png"),
            size=(100, 100)
        )

        ctk.CTkLabel(
            self.left_frame,
            image=self.logo_image,
            text=""
        ).pack(pady=(80, 20))

        ctk.CTkLabel(
            self.left_frame,
            text="SkillSwap",
            font=("Arial", 34, "bold"),
            text_color="white"
        ).pack()

        ctk.CTkLabel(
            self.left_frame,
            text="Exchange Skills.\nGrow Together.\n\nLearn anything by\nsharing what you know.",
            font=("Arial", 18),
            justify="center",
            text_color="white"
        ).pack(pady=20)

        ctk.CTkLabel(
            self.left_frame,
            text='"Knowledge grows\nwhen shared."',
            font=("Arial", 14, "italic"),
            text_color="#DDE6FF"
        ).pack()

        # ==========================
        # RIGHT PANEL CONTENT
        # ==========================
        ctk.CTkLabel(
            self.right_frame,
            text="Welcome Back!",
            font=("Arial", 30, "bold"),
            text_color="black"
        ).pack(pady=(90, 10))

        ctk.CTkLabel(
            self.right_frame,
            text="Sign in to continue your learning journey.",
            font=("Arial", 15),
            text_color="gray"
        ).pack(pady=(0, 30))

        self.email_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="Email",
            width=350,
            height=45
        )
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="Password",
            show="*",
            width=350,
            height=45
        )
        self.password_entry.pack(pady=10)

        self.show_password = False

        self.show_btn = ctk.CTkButton(
            self.right_frame,
            text="Show Password",
            width=350,
            height=35,
            fg_color="transparent",
            text_color="#4F46E5",
            hover=False,
            command=self.toggle_password
        )
        self.show_btn.pack()

        self.login_button = ctk.CTkButton(
            self.right_frame,
            text="Sign In",
            width=350,
            height=45,
            fg_color="#4F46E5",
            hover_color="#4338CA",
            command=self.login
        )
        self.login_button.pack(pady=(20, 15))

        self.register_button = ctk.CTkButton(
            self.right_frame,
            text="Create Account",
            width=350,
            height=45,
            fg_color="gray",
            hover_color="#666666",
            command=self.open_register
        )
        self.register_button.pack()

    # ==========================
    # SHOW / HIDE PASSWORD
    # ==========================
    def toggle_password(self):

        self.show_password = not self.show_password

        if self.show_password:
            self.password_entry.configure(show="")
            self.show_btn.configure(text="Hide Password")
        else:
            self.password_entry.configure(show="*")
            self.show_btn.configure(text="Show Password")

        # ==========================
    # LOGIN
    # ==========================
    def login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        print("Email entered:", email)
        print("Password entered:", password)

        user = login_user(email, password)

        print("User found:", user)

        if user:
            self.parent.show_dashboard(user)
        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Email or Password."
            )

    # ==========================
    # OPEN REGISTER
    # ==========================
    def open_register(self):
        self.parent.show_register()