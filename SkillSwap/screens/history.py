import customtkinter as ctk
from database.database import get_history
from theme import *


class HistoryScreen(ctk.CTkScrollableFrame):

    def __init__(self, parent, user):

        super().__init__(parent)

        self.parent = parent
        self.user = user

        self.pack(fill="both", expand=True)

        # ==========================
        # TITLE
        # ==========================
        ctk.CTkLabel(
            self,
            text="📜 Request History",
            font=("Segoe UI", 30, "bold"),
            text_color="#4F46E5"
        ).pack(pady=25)

        ctk.CTkLabel(
            self,
            text=f"View all the requests you've sent and received, {self.user[1]}",
            font=("Segoe UI", 16),
            text_color="gray"
        ).pack(pady=(0, 20))

        received, sent = get_history(user[1])

        # ==========================
        # RECEIVED REQUESTS
        # ==========================
        ctk.CTkLabel(
            self,
            text="📥 Requests Received",
            font=("Segoe UI", 22, "bold"),
            text_color="#2563EB"
        ).pack(anchor="w", padx=20, pady=(15, 10))

        if len(received) == 0:

            ctk.CTkLabel(
                self,
                text="📭 No requests found yet.",
                font=("Segoe UI", 20, "bold"),
                text_color="gray"
            ).pack(anchor="w", padx=30, pady=(0, 20))

        else:

            for name, skill, learn, status, request_date in received:
                self.create_history_card(
                    name,
                    skill,
                    learn,
                    status,
                    request_date  
                )

        # ==========================
        # SENT REQUESTS
        # ==========================
        ctk.CTkLabel(
            self,
            text="📤 Requests Sent",
            font=("Segoe UI", 22, "bold"),
            text_color="#16A34A"
        ).pack(anchor="w", padx=20, pady=(25, 10))

        if len(sent) == 0:

            ctk.CTkLabel(
                self,
                text="📭 No requests found yet.",
                font=("Segoe UI", 20, "bold"),
                text_color="gray"
            ).pack(anchor="w", padx=30, pady=(0, 20))

        else:

            for name, skill, learn, status, request_date in sent:
                self.create_history_card(
                    name,
                    skill,
                    learn,
                    status,
                    request_date
                )

        # ==========================
        # BACK BUTTON
        # ==========================
        ctk.CTkButton(
            self,
            text="⬅ Back to Dashboard",
            width=200,
            command=lambda: parent.show_dashboard(user),
            **GRAY_BUTTON
        ).pack(pady=30)

    # =====================================
    # REUSABLE HISTORY CARD
    # =====================================
    def create_history_card(
        self,
        name,
        skill,
        learn,
        status,
        request_date
    ):

        card = ctk.CTkFrame(
            self,
            corner_radius=18,
            border_width=2,
            border_color="#E5E7EB",
            fg_color="#F9FAFB"
        )

        card.pack(
            fill="x",
            padx=25,
            pady=10
        )

        ctk.CTkLabel(
            card,
            text=f"👤 {name}",
            font=("Segoe UI", 22, "bold"),
            text_color="#111827"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            card,
            text=f"📘 Can Teach: {skill}",
            font=("Segoe UI", 16),
            text_color="#2563EB"
        ).pack(
            anchor="w",
            padx=20
        )

        ctk.CTkLabel(
            card,
            text=f"📗 Wants to Learn: {learn}",
            font=("Segoe UI", 16),
            text_color="#16A34A"
        ).pack(
            anchor="w",
            padx=20
        )

        if status == "Pending":
            status_color = "#F59E0B"
            emoji = "🟠"

        elif status == "Accepted":
            status_color = "#22C55E"
            emoji = "🟢"

        else:
            status_color = "#EF4444"
            emoji = "🔴"

        
        ctk.CTkLabel(
            card,
            text=f"📅 {request_date}",
            font=("Segoe UI", 13),
            text_color="gray"
        ).pack(
    anchor="w",
    padx=20,
    pady=(0, 15)
)
