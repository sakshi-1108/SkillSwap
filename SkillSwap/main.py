import customtkinter as ctk
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.dashboard import DashboardScreen
from database.database import create_database
from screens.profile import ProfileScreen

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SkillSwapApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SkillSwap")
        self.geometry("1000x650")
        self.resizable(False, False)

        self.current_screen = None

        self.show_login()

    def show_login(self):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = LoginScreen(self)
        self.current_screen.pack(fill="both", expand=True)
        
    def show_register(self):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = RegisterScreen(self)
        self.current_screen.pack(fill="both", expand=True)

    def show_dashboard(self, user):

      if self.current_screen:
        self.current_screen.destroy()

      self.current_screen = DashboardScreen(self, user)
      self.current_screen.pack(fill="both", expand=True)

    def show_profile(self, current_user, selected_user):

      if self.current_screen:
        self.current_screen.destroy()

        self.current_screen = ProfileScreen(
        self,
        current_user,
        selected_user
    )

        self.current_screen.pack(fill="both", expand=True)

create_database()

app = SkillSwapApp()
app.mainloop()