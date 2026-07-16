import customtkinter as ctk
from tkinter import messagebox
from database.database import (
    send_request,
    get_about,
    get_request_status
)
from theme import *

class ProfileScreen(ctk.CTkFrame):

    def __init__(self, parent, current_user, selected_user):

        super().__init__(parent)

        self.parent = parent
        self.current_user = current_user
        self.selected_user = selected_user

        self.pack(fill="both", expand=True)

        # ==========================
        # TITLE
        # ==========================
        ctk.CTkLabel(
            self,
            text="👤 User Profile",
            font=("Segoe UI", 32, "bold"),
            text_color="#4F46E5"
        ).pack(pady=25)

        # ==========================
        # PROFILE CARD
        # ==========================
        card = ctk.CTkFrame(
           self,
           width=750,
           corner_radius=20,
           border_width=2,
           border_color="#E5E7EB"
    )
        
        card.pack(fill="x", padx=40, pady=10)

        # Name
        ctk.CTkLabel(
            card,
            text=f"👤 {self.selected_user[0]}",
            font=("Segoe UI", 28, "bold"),
            text_color="#111827",
        ).pack(anchor="w", padx=25, pady=(20, 10))

        # Skill
        ctk.CTkLabel(
            card,
            text=f"📘 Can Teach:  {self.selected_user[1]}",
            font=("Segoe UI", 17),
            text_color="#2563EB"
        ).pack(anchor="w", padx=25, pady=5)

        # Learn Skill
        ctk.CTkLabel(
            card,
            text=f"📗 Wants to Learn:  {self.selected_user[2]}",
            font=("Segoe UI", 17),
            text_color="#16A34A" 
        ).pack(anchor="w", padx=25, pady=5)

        # About Heading
        ctk.CTkLabel(
            card,
            text="📝 About",
            font=("Segoe UI", 21, "bold"),
            text_color="#4F46E5"
        ).pack(anchor="w", padx=25, pady=(20, 5))

        # About Box
        self.about_box = ctk.CTkTextbox(
            card,
            width=650,
            height=140,
            corner_radius=12
        )
        self.about_box.pack(padx=25, pady=(0, 20))

        self.about_box.insert(
            "0.0",
                get_about(self.selected_user[0])
        )

        self.about_box.configure(state="disabled")

        # ==========================
        # SEND REQUEST BUTTON
        # ==========================
        status = get_request_status(
         self.current_user[0],
        self.selected_user[0]
        )

        if status is None:

         ctk.CTkButton(
         self,
         text="📩 Send Skill Swap Request",
         width=260,
         command=self.send_skill_request,
        **BUTTON
         ).pack(pady=20)

        elif status == "Pending":

         ctk.CTkButton(
          self,
          text="⏳ Request Pending",
          width=260,
          state="disabled"
         ).pack(pady=20)

        elif status == "Accepted":

            ctk.CTkButton(
              self,
              text="✅ Request Accepted",
              width=260,
             state="disabled"
    ).pack(pady=20)

        elif status == "Rejected":

            ctk.CTkLabel(
                self,
                text="❌ Previous request was rejected.",
                font=("Segoe UI", 15, "bold"),
                text_color="#EF4444"
            ).pack(pady=(20, 5))

            ctk.CTkButton(
                self,
                text="📩 Send Request Again",
                width=260,
                command=self.send_skill_request,
                **BUTTON
            ).pack(pady=(0, 20))

        # ==========================
        # BACK BUTTON
        # ==========================
        ctk.CTkButton(
            self,
            text="⬅ Back to Dashboard",
            width=220,
           
            command=lambda: self.parent.show_dashboard(self.current_user),
             **GRAY_BUTTON
        ).pack(pady=10)

    # ==========================
    # SEND REQUEST
    # ==========================
    def send_skill_request(self):

        success = send_request(
            self.current_user[0],
            self.selected_user[0]
        )


        if success:
            messagebox.showinfo(
                "Success",
                f"Skill Swap Request sent to {self.selected_user[0]}!"
            )
            self.parent.show_profile(self.current_user, self.selected_user)
        else:
            messagebox.showwarning(
                "Already Sent",
                f"You have already sent a request to {self.selected_user[0]}."
            )
