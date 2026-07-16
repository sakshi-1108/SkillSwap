import customtkinter as ctk
from tkinter import messagebox
from database.database import update_user, get_about
from theme import *


class EditProfileScreen(ctk.CTkFrame):

    def __init__(self, parent, user):

        super().__init__(parent)

        self.parent = parent
        self.user = user

        self.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self,
            text="Edit Profile",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        # Name
        self.name_entry = ctk.CTkEntry(
            self,
            width=400,
            height=40,
            placeholder_text="Name"
        )
        self.name_entry.insert(0, user[1])
        self.name_entry.pack(pady=10)

        # Skill
        self.skill_entry = ctk.CTkEntry(
            self,
            width=400,
            height=40,
            placeholder_text="Skill You Can Teach"
        )
        self.skill_entry.insert(0, user[4])
        self.skill_entry.pack(pady=10)

        # Learn Skill
        self.learn_entry = ctk.CTkEntry(
            self,
            width=400,
            height=40,
            placeholder_text="Skill You Want To Learn"
        )
        self.learn_entry.insert(0, user[5])
        self.learn_entry.pack(pady=10)

        # About Me
        ctk.CTkLabel(
            self,
            text="About Me",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 5))

        self.about_box = ctk.CTkTextbox(
        self,
        width=400,
        height=120
      )
        self.about_box.pack(pady=10)

        self.about_box.insert(
        "0.0",
    get_about(user[1])
    )

        # Save Button
        ctk.CTkButton(
            self,
            text="Save Changes",
            width=220,
            command=self.save_profile,
            **BUTTON
        ).pack(pady=25)

        # Back Button
        ctk.CTkButton(
            self,
            text="Back",
            width=220,
            command=lambda: parent.show_dashboard(self.user),
            **GRAY_BUTTON
        ).pack()

    def save_profile(self):

        name = self.name_entry.get().strip()
        skill = self.skill_entry.get().strip()
        learn = self.learn_entry.get().strip()
        about = self.about_box.get("0.0", "end").strip()

        if not name or not skill or not learn:
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        update_user(
            self.user[0],
            name,
            skill,
            learn,
            about
        )

        # Update current user object
        updated_user = (
            self.user[0],
            name,
            self.user[2],
            self.user[3],
            skill,
            learn,
            about
        )

        messagebox.showinfo(
            "Success",
            "Profile updated successfully!"
        )

        self.parent.show_dashboard(updated_user)
