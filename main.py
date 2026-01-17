"""
CodePet - A gamified task tracker with an evolving pixel pet companion.

Launch the application by running: python main.py
"""

import customtkinter as ctk
from database import get_database


class CodePetApp(ctk.CTk):
    """Main application window for CodePet."""

    def __init__(self):
        super().__init__()

        # Initialize database
        self.db = get_database()

        # Window configuration
        self.title("CodePet")
        self.geometry("900x700")
        self.minsize(600, 400)

        # Configure grid for responsive layout
        # Row 0 takes all vertical space
        self.grid_rowconfigure(0, weight=1)
        # Column 0 (sidebar) fixed width, column 1 (content) expands
        self.grid_columnconfigure(0, weight=0, minsize=200)
        self.grid_columnconfigure(1, weight=1)

        # Create main layout components
        self._create_sidebar()
        self._create_content_area()

    def _create_sidebar(self):
        """Create the left sidebar for pet display and stats."""
        self.sidebar = ctk.CTkFrame(
            self,
            width=200,
            corner_radius=0,
            fg_color=("gray90", "gray17")  # Light mode, Dark mode colors
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        # Prevent sidebar from shrinking
        self.sidebar.grid_propagate(False)

        # Configure sidebar internal grid
        self.sidebar.grid_columnconfigure(0, weight=1)

        # Sidebar title
        self.sidebar_title = ctk.CTkLabel(
            self.sidebar,
            text="CodePet",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.sidebar_title.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Placeholder for pet display (will be implemented in US-004)
        self.pet_frame = ctk.CTkFrame(
            self.sidebar,
            height=150,
            fg_color=("gray85", "gray20")
        )
        self.pet_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.pet_frame.grid_propagate(False)

        self.pet_placeholder = ctk.CTkLabel(
            self.pet_frame,
            text="🥚\nPet Area",
            font=ctk.CTkFont(size=14)
        )
        self.pet_placeholder.place(relx=0.5, rely=0.5, anchor="center")

        # Placeholder for stats (will be expanded in US-004)
        self.stats_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color=("gray85", "gray20")
        )
        self.stats_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.stats_label = ctk.CTkLabel(
            self.stats_frame,
            text="Level: 1\nXP: 0",
            font=ctk.CTkFont(size=12),
            justify="left"
        )
        self.stats_label.grid(row=0, column=0, padx=10, pady=10)

    def _create_content_area(self):
        """Create the main content area for task list."""
        self.content_area = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=("gray95", "gray13")  # Light mode, Dark mode colors
        )
        self.content_area.grid(row=0, column=1, sticky="nsew")

        # Configure content area internal grid
        self.content_area.grid_rowconfigure(1, weight=1)
        self.content_area.grid_columnconfigure(0, weight=1)

        # Header for task list
        self.content_header = ctk.CTkLabel(
            self.content_area,
            text="Tasks",
            font=ctk.CTkFont(size=24, weight="bold"),
            anchor="w"
        )
        self.content_header.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Task list container (will be populated in US-005)
        self.task_container = ctk.CTkFrame(
            self.content_area,
            fg_color="transparent"
        )
        self.task_container.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.task_container.grid_rowconfigure(0, weight=1)
        self.task_container.grid_columnconfigure(0, weight=1)

        # Placeholder for empty state
        self.empty_state = ctk.CTkLabel(
            self.task_container,
            text="No tasks yet.\nAdd a task to get started!",
            font=ctk.CTkFont(size=14),
            text_color=("gray50", "gray60")
        )
        self.empty_state.grid(row=0, column=0, pady=50)


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
