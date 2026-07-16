import customtkinter as ctk

from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.dashboard import DashboardScreen
from screens.profile import ProfileScreen
from screens.edit_profile import EditProfileScreen
from screens.requests import RequestsScreen
from screens.history import HistoryScreen

from database.database import create_database
from theme import *


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SkillSwapApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SkillSwap")
        self.geometry("1000x650")
        self.configure(fg_color="#F5F7FA")
        self.resizable(False, False)

        self.current_screen = None

        self.show_login()

    # ==========================
    # LOGIN
    # ==========================
    def show_login(self):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = LoginScreen(self)
        self.current_screen.pack(fill="both", expand=True)

    # ==========================
    # REGISTER
    # ==========================
    def show_register(self):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = RegisterScreen(self)
        self.current_screen.pack(fill="both", expand=True)

    # ==========================
    # DASHBOARD
    # ==========================
    def show_dashboard(self, user):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = DashboardScreen(self, user)
        self.current_screen.pack(fill="both", expand=True)

    # ==========================
    # PROFILE
    # ==========================
    def show_profile(self, current_user, selected_user):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = ProfileScreen(
            self,
            current_user,
            selected_user
        )

        self.current_screen.pack(fill="both", expand=True)

    # ==========================
    # EDIT PROFILE
    # ==========================
    def show_edit_profile(self, user):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = EditProfileScreen(
            self,
            user
        )

        self.current_screen.pack(fill="both", expand=True)

    # ==========================
    # REQUESTS
    # ==========================
    def show_requests(self, user):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = RequestsScreen(
            self,
            user
        )

        self.current_screen.pack(fill="both", expand=True)

    # ==========================
    # HISTORY
    # ==========================
    def show_history(self, user):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = HistoryScreen(
            self,
            user
        )

        self.current_screen.pack(fill="both", expand=True)


create_database()

app = SkillSwapApp()
app.mainloop()