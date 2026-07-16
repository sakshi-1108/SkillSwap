import customtkinter as ctk
from tkinter import messagebox
from theme import *
from database.database import (
    get_all_users,
    search_users,
    get_pending_request_count,
    get_dashboard_stats,
)


class DashboardScreen(ctk.CTkScrollableFrame):

    def __init__(self, parent, user):

        super().__init__(parent)

        self.parent = parent
        self.user = user

        self.logged_name = user[1]
        self.logged_skill = user[4]
        self.logged_learn = user[5]

        self.pack(fill="both", expand=True)

        # ==========================
        # HEADER
        # ==========================
        header = ctk.CTkFrame(
            self,
            corner_radius=15
        )
        header.pack(fill="x", padx=20, pady=(20, 15))

        ctk.CTkLabel(
            header,
            text="🚀 SkillSwap",
            font=("Segoe UI", 34, "bold"),
            text_color="#4F46E5"
        ).pack(pady=(18, 5))

        ctk.CTkLabel(
            header,
            text="Connect • Learn • Grow Together",
            font=("Segoe UI", 16),
            text_color="gray"
        ).pack()

        ctk.CTkLabel(
            header,
            text=f"👋 Welcome back, {self.logged_name}",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            header,
            text="Find people who can teach you and share your own skills.",
            font=("Segoe UI", 15),
            text_color="gray"
        ).pack(pady=(0, 18))

        # ==========================
        # TOP BUTTONS
        # ==========================
        top_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        top_frame.pack(fill="x", padx=20, pady=15)

        ctk.CTkButton(
            top_frame,
            text="✏ Edit Profile",
            width=140,
            height=40,
            command=lambda: self.parent.show_edit_profile(self.user),
            **BUTTON
        ).pack(side="left", padx=10)

        total_users, pending, accepted, history = get_dashboard_stats(self.user)

        ctk.CTkButton(
            top_frame,
            text=f"📨 My Requests ({pending})",
            width=160,
            height=40,
            command=lambda: self.parent.show_requests(self.user),
            **BUTTON
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            top_frame,
            text="📜 History",
            width=140,
            height=40,
            command=lambda: self.parent.show_history(self.user),
            **BUTTON
        ).pack(side="left", padx=10)

        # ==========================
        # LOAD USERS (must happen before matches is computed)
        # ==========================
        self.users = get_all_users(self.logged_name)
        matches = self.get_recommended_matches()

        # ==========================
        # DASHBOARD STATISTICS (single block, no duplicates)
        # ==========================
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        stats_frame.pack(pady=20)

        self.total_label = self.create_stat_card(
            stats_frame,
            "👥",
            "Total Users",
            total_users,
            "#4F46E5"
        )

        self.create_stat_card(
            stats_frame,
            "📨",
            "Pending",
            pending,
            "#F59E0B"
        )

        self.create_stat_card(
            stats_frame,
            "🤝",
            "Accepted",
            accepted,
            "#22C55E"
        )

        self.create_stat_card(
            stats_frame,
            "📜",
            "History",
            history,
            "#9333EA"
        )

        self.match_label = self.create_stat_card(
            stats_frame,
            "⭐",
            "Matches",
            len(matches),
            "#4F46E5"
        )

        # ==========================
        # SEARCH
        # ==========================
        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search by Name or Skill...",
            width=450,
            height=40
        )
        self.search.pack(pady=15)

        self.search.bind("<KeyRelease>", self.filter_users)

        # ==========================
        # HEADING
        # ==========================
        ctk.CTkLabel(
            self,
            text="Recommended Skill Matches",
            font=("Segoe UI", 24, "bold"),
            text_color="#4F46E5"
        ).pack(pady=15)

        # ==========================
        # CARD AREA
        # ==========================
        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.cards_frame.pack(fill="both", expand=True, padx=20)

        self.show_recommended()

        # ==========================
        # LOGOUT
        # ==========================
        ctk.CTkButton(
            self,
            text="Logout",
            width=180,
            command=self.logout,
            **DANGER_BUTTON
        ).pack(pady=25)

    # ==========================
    # LOGOUT (with confirmation)
    # ==========================
    def logout(self):

        if messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        ):
            self.parent.show_login()

    # ==========================
    # COMPUTE RECOMMENDED MATCHES (shared by stats + show_recommended)
    # ==========================
    def get_recommended_matches(self):

        matches = []

        for name, teach, learn in self.users:

            if name.strip().lower() == self.logged_name.strip().lower():
                continue

            if teach.strip().lower() == self.logged_learn.strip().lower():
                matches.append((name, teach, learn))

        return matches

    # ==========================
    # SHOW RECOMMENDED USERS
    # ==========================
    def show_recommended(self):

        matches = self.get_recommended_matches()
        self.display_users(matches)

    # ==========================
    # DISPLAY USERS
    # ==========================
    def display_users(self, users):

        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        self.total_label.configure(
            text=str(len(self.users))
        )

        self.match_label.configure(
            text=str(len(users))
        )

        if len(users) == 0:

            ctk.CTkLabel(
                self.cards_frame,
                text="No users found.",
                font=("Arial", 18),
                text_color="gray"
            ).pack(pady=40)

            return

        for name, teach, learn in users:

            card = ctk.CTkFrame(
                self.cards_frame,
                corner_radius=15,
                border_width=2,
                border_color="#4F46E5"
            )

            card.pack(fill="x", pady=15)

            ctk.CTkLabel(
                card,
                text=f"👤 {name}",
                font=("Arial", 20, "bold"),
                text_color="#111827"
            ).pack(anchor="w", padx=20, pady=(15, 5))

            ctk.CTkLabel(
                card,
                text=f"📘 Can Teach : {teach}",
                text_color="#2563EB"
            ).pack(anchor="w", padx=20)

            ctk.CTkLabel(
                card,
                text=f"📗 Wants To Learn : {learn}",
                text_color="#16A34A"
            ).pack(anchor="w", padx=20)

            # ==========================
            # MATCH SCORE
            # ==========================
            match_score = 0

            # They teach what I want to learn
            if teach.strip().lower() == self.logged_learn.strip().lower():
                match_score += 50

            # They want to learn what I teach
            if learn.strip().lower() == self.logged_skill.strip().lower():
                match_score += 50

            # Match text
            if match_score == 100:
                match_text = "⭐⭐⭐⭐⭐ Excellent Match"
                color = "#22C55E"

            elif match_score == 50:
                match_text = "⭐⭐⭐ Good Match"
                color = "#F59E0B"

            else:
                match_text = "⭐ Low Match"
                color = "#EF4444"

            ctk.CTkLabel(
                card,
                text=f"🎯 Match Score : {match_score}%",
                font=("Segoe UI", 16, "bold"),
                text_color=color
            ).pack(anchor="w", padx=20, pady=(5, 0))

            ctk.CTkLabel(
                card,
                text=match_text,
                font=("Segoe UI", 14, "bold"),
                text_color=color
            ).pack(anchor="w", padx=20, pady=(0, 8))

            ctk.CTkButton(
                card,
                text="View Profile",
                width=140,
                command=lambda u=(name, teach, learn):
                    self.parent.show_profile(self.user, u),
                **BUTTON
            ).pack(anchor="e", padx=20, pady=(0, 15))

    # ==========================
    # SEARCH
    # ==========================
    def filter_users(self, event=None):

        text = self.search.get().strip()

        if text == "":
            self.show_recommended()
            return

        users = search_users(text)

        filtered = []

        for name, teach, learn in users:

            if name.strip().lower() == self.logged_name.strip().lower():
                continue

            filtered.append((name, teach, learn))

        self.display_users(filtered)

    # =====================================
    # CREATE STAT CARD
    # =====================================
    def create_stat_card(self, parent, icon, title, value, color):

        card = ctk.CTkFrame(
            parent,
            width=180,
            height=110,
            corner_radius=15
        )

        card.pack(side="left", padx=10)
        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI", 28)
        ).pack(pady=(10, 0))

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 15)
        ).pack()

        value_label = ctk.CTkLabel(
            card,
            text=str(value),
            font=("Segoe UI", 22, "bold"),
            text_color=color
        )
        value_label.pack()

        return value_label