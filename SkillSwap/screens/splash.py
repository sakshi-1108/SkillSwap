import customtkinter as ctk

class SplashScreen(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SkillSwap")
        self.geometry("900x600")
        self.resizable(False, False)

        title = ctk.CTkLabel(
            self,
            text="SkillSwap",
            font=("Poppins", 36, "bold")
        )

        title.pack(expand=True)