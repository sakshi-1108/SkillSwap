import customtkinter as ctk
from tkinter import messagebox
from theme import *

from database.database import (
    get_requests,
    accept_request,
    reject_request
)


class RequestsScreen(ctk.CTkScrollableFrame):

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
            text="📨 Skill Swap Requests",
            font=("Segoe UI", 30, "bold"),
            text_color="#4F46E5"
        ).pack(pady=25)

        ctk.CTkLabel(
            self,
            text=f"Review your incoming requests, {user[1]}",
            font=("Segoe UI", 17),
            text_color="gray"
        ).pack(pady=(0, 25))

        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.cards_frame.pack(fill="both", expand=True, padx=20)

        self.load_requests()

        ctk.CTkButton(
            self,
            text="⬅ Back to Dashboard",
            width=220,
             command=lambda: self.parent.show_dashboard(self.user),
            **GRAY_BUTTON
        ).pack(pady=10)

    # =====================================
    # LOAD REQUESTS
    # =====================================
    def load_requests(self):

        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        requests = get_requests(self.user[1])

        if len(requests) == 0:

            ctk.CTkLabel(
                self.cards_frame,
                text="No incoming requests.",
                font=("Segoe UI", 20, "bold"),
                text_color="gray"
            ).pack(pady=50)

            return

        for request_id, sender, skill, learn, status, request_date in requests:

            card = ctk.CTkFrame(
                self.cards_frame,
                corner_radius=18,
                border_width=2,
                border_color="#E5E7EB"
            )

            card.pack(fill="x", padx=10, pady=12)

            ctk.CTkLabel(
                card,
                text=f"👤 {sender}",
                font=("Segoe UI", 22, "bold"),
                text_color="#111827"
            ).pack(anchor="w", padx=20, pady=(15, 5))

            ctk.CTkLabel(
                card,
                text=f"📘 Can Teach: {skill}",
                text_color="#2563EB"
            ).pack(anchor="w", padx=20)

            ctk.CTkLabel(
                card,
                text=f"📗 Wants to Learn: {learn}",
                text_color="#16A34A"
            ).pack(anchor="w", padx=20)

            if status == "Pending":
                status_color = "#F59E0B"      # Orange
            elif status == "Accepted":
                status_color = "#22C55E"      # Green
            else:
                status_color = "#EF4444"      # Red

            emoji = {
                "Pending": "🟠",
                "Accepted": "🟢",
                "Rejected": "🔴"
            }.get(status, "⚪")

            ctk.CTkLabel(
                card,
                text=f"{emoji} {status}",
                font=("Segoe UI", 15, "bold"),
                text_color=status_color
            ).pack(anchor="w", padx=20, pady=5)

            ctk.CTkLabel(
              card,
             text=f"📅 {request_date}",
             font=("Segoe UI", 13),
             text_color="gray"
            ).pack(anchor="w", padx=20, pady=(0, 5))

            if status == "Pending":

                buttons = ctk.CTkFrame(
                    card,
                    fg_color="transparent"
                )
                buttons.pack(pady=(12, 15))

                ctk.CTkButton(
                    buttons,
                    text="Accept",
                    width=140,
                    height=40,
                    command=lambda rid=request_id: self.accept(rid),
                    **SUCCESS_BUTTON
                ).pack(side="left", padx=10)

                ctk.CTkButton(
                    buttons,
                    text="Reject",
                    width=140,
                    height=40,
                    command=lambda rid=request_id: self.reject(rid),
                    **DANGER_BUTTON
                ).pack(side="left", padx=10)

    # =====================================
    # ACCEPT
    # =====================================
    def accept(self, request_id):

        accept_request(request_id)

        messagebox.showinfo(
            "Success",
            "Request Accepted!"
        )

        self.load_requests()

    # =====================================
    # REJECT
    # =====================================
    def reject(self, request_id):

        if not messagebox.askyesno(
            "Reject Request",
            "Are you sure you want to reject this request?"
        ):
            return

        reject_request(request_id)

        messagebox.showinfo(
            "Success",
            "Request Rejected!"
        )

        self.load_requests()
