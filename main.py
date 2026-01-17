"""
CodePet - A gamified task tracker with an evolving pixel pet companion.

Launch the application by running: python main.py
"""

import customtkinter as ctk


class CodePetApp(ctk.CTk):
    """Main application window for CodePet."""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("CodePet")
        self.geometry("900x700")
        self.minsize(600, 400)
        
        # Configure grid for responsive layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Placeholder label (will be replaced with actual UI in later user stories)
        self.placeholder = ctk.CTkLabel(
            self,
            text="🥚 CodePet\n\nYour coding companion is hatching soon...",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.placeholder.grid(row=0, column=0, padx=20, pady=20)


def main():
    """Entry point for the application."""
    # Set appearance mode and color theme
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    
    # Create and run the application
    app = CodePetApp()
    app.mainloop()


if __name__ == "__main__":
    main()
