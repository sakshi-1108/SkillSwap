import customtkinter as ctk


class ProfileScreen(ctk.CTkFrame):

    def __init__(self, parent, current_user, selected_user):

        super().__init__(parent)

        self.parent = parent
        self.current_user = current_user
        self.selected_user = selected_user

        self.pack(fill="both", expand=True)

        # ==========================
        # HEADING
        # ==========================
        ctk.CTkLabel(
            self,
            text="User Profile",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=20)

        # ==========================
        # NAME
        # ==========================
        ctk.CTkLabel(
            self,
            text=f"👤 Name : {selected_user[0]}",
            font=("Segoe UI", 18)
        ).pack(anchor="w", padx=40, pady=10)

        # ==========================
        # SKILL
        # ==========================
        ctk.CTkLabel(
            self,
            text=f"📘 Can Teach : {selected_user[1]}",
            font=("Segoe UI", 18)
        ).pack(anchor="w", padx=40)

        # ==========================
        # LEARNING
        # ==========================
        ctk.CTkLabel(
            self,
            text=f"📗 Wants To Learn : {selected_user[2]}",
            font=("Segoe UI", 18)
        ).pack(anchor="w", padx=40, pady=(0, 20))

        # ==========================
        # ABOUT
        # ==========================
        ctk.CTkLabel(
            self,
            text="About",
            font=("Segoe UI", 20, "bold")
        ).pack(anchor="w", padx=40)

        self.about_box = ctk.CTkTextbox(
            self,
            width=600,
            height=120
        )
        self.about_box.pack(padx=40, pady=10)

        self.about_box.insert(
            "0.0",
            "This user hasn't added an introduction yet."
        )

        self.about_box.configure(state="disabled")

        # ==========================
        # BACK BUTTON
        # ==========================
        ctk.CTkButton(
            self,
            text="⬅ Back to Dashboard",
            width=220,
            command=lambda: parent.show_dashboard(current_user)
        ).pack(pady=25)