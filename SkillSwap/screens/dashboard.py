import customtkinter as ctk
from database.database import get_all_users, search_users

class DashboardScreen(ctk.CTkScrollableFrame):

    def __init__(self, parent, user):
        super().__init__(parent)

        self.parent = parent
        self.user = user

        # Logged-in user information
        self.logged_name = user[1]
        self.logged_skill = user[4]
        self.logged_learn = user[5]

        self.pack(fill="both", expand=True)

        # ==========================
        # TITLE
        # ==========================
        title = ctk.CTkLabel(
            self,
            text="SkillSwap",
            font=("Arial", 34, "bold")
        )
        title.pack(pady=(20, 5))

        welcome = ctk.CTkLabel(
            self,
            text=f"👋 Welcome, {self.logged_name}",
            font=("Arial", 24, "bold")
        )
        welcome.pack()

        # ==========================
        # SEARCH BAR
        # ==========================
        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search by Skill...",
            width=450,
            height=40
        )
        self.search.pack(pady=20)
        #self.search.bind("<KeyRelease>", self.filter_users)
        # ==========================
        # GET USERS
        # ==========================
        self.users = get_all_users()
        users = self.users

        total_users = len(users)

        matches = []

        for name, teach, learn in users:

            # Don't show yourself
            if name.strip().lower() == self.logged_name.strip().lower():
    
                continue

            # Match users who teach what I want
            if teach.strip().lower() == self.logged_learn.strip().lower():
                matches.append((name, teach, learn))

        # ==========================
        # STATS
        # ==========================
        stats = ctk.CTkFrame(self)
        stats.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            stats,
            text=f"👥 Total Users : {total_users}",
            font=("Arial", 15, "bold")
        ).pack(side="left", padx=20, pady=10)

        ctk.CTkLabel(
            stats,
            text=f"⭐ Matches Found : {len(matches)}",
            font=("Arial", 15, "bold")
        ).pack(side="right", padx=20)

        # ==========================
        # HEADING
        # ==========================
        heading = ctk.CTkLabel(
            self,
            text="Recommended Skill Matches",
            font=("Arial", 22, "bold")
        )
        heading.pack(pady=15)

        # ==========================
        # USER CARDS
        # ==========================
        if len(matches) == 0:

            ctk.CTkLabel(
                self,
                text="No matching users found.",
                font=("Arial", 18),
                text_color="gray"
            ).pack(pady=30)

        else:

            for name, teach, learn in matches:

                card = ctk.CTkFrame(
                    self,
                    corner_radius=15,
                    border_width=2,
                    border_color="#4F46E5"
                )

                card.pack(fill="x", padx=20, pady=12)

                ctk.CTkLabel(
                    card,
                    text=f"👤 {name}",
                    font=("Arial", 20, "bold")
                ).pack(anchor="w", padx=20, pady=(15, 5))

                ctk.CTkLabel(
                    card,
                    text=f"📘 Can Teach : {teach}",
                    font=("Arial", 15)
                ).pack(anchor="w", padx=20)

                ctk.CTkLabel(
                    card,
                    text=f"📗 Wants To Learn : {learn}",
                    font=("Arial", 15)
                ).pack(anchor="w", padx=20)

                ctk.CTkLabel(
                    card,
                    text="⭐⭐⭐⭐⭐ Skill Match",
                    text_color="green",
                    font=("Arial", 14, "bold")
                ).pack(anchor="w", padx=20, pady=8)

                ctk.CTkButton(
    card,
    text="View Profile",
    width=120,
    command=lambda u=(name, teach, learn):
        self.parent.show_profile(self.user, u)
).pack(anchor="e", padx=20, pady=(0,15))

        # ==========================
        # LOGOUT BUTTON
        # ==========================
        logout = ctk.CTkButton(
            self,
            text="Logout",
            width=180,
            command=self.parent.show_login
        )
        logout.pack(pady=25)