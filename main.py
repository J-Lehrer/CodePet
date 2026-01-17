"""
CodePet - A gamified task tracker with an evolving pixel pet companion.

Launch the application by running: python main.py
"""

import customtkinter as ctk
import tkinter as tk
from database import get_database


# Evolution stage colors for placeholder sprites
EVOLUTION_COLORS = {
    "egg": "#FFE4B5",      # Moccasin (pale yellow)
    "baby": "#98FB98",     # Pale green
    "child": "#87CEEB",    # Sky blue
    "teen": "#DDA0DD",     # Plum (purple)
    "adult": "#FFD700",    # Gold
}

# Evolution stage sprite patterns (simple pixel patterns)
# Each pattern is a list of (x, y, color_key) where coordinates are relative to center
EVOLUTION_SPRITES = {
    "egg": [
        # Simple oval egg shape
        (0, -2, "outline"), (1, -2, "outline"), (-1, -2, "outline"),
        (-2, -1, "outline"), (2, -1, "outline"),
        (-2, 0, "outline"), (2, 0, "outline"),
        (-2, 1, "outline"), (2, 1, "outline"),
        (-1, 2, "outline"), (0, 2, "outline"), (1, 2, "outline"),
        # Fill
        (0, -1, "fill"), (1, -1, "fill"), (-1, -1, "fill"),
        (0, 0, "fill"), (1, 0, "fill"), (-1, 0, "fill"),
        (0, 1, "fill"), (1, 1, "fill"), (-1, 1, "fill"),
    ],
    "baby": [
        # Small round creature
        (0, -2, "fill"), (-1, -1, "fill"), (0, -1, "fill"), (1, -1, "fill"),
        (-1, 0, "fill"), (0, 0, "fill"), (1, 0, "fill"),
        (0, 1, "fill"),
        # Eyes
        (-1, -1, "eye"), (1, -1, "eye"),
    ],
    "child": [
        # Slightly larger creature with ears
        (0, -3, "fill"), (-1, -3, "fill"), (1, -3, "fill"),
        (-2, -2, "fill"), (-1, -2, "fill"), (0, -2, "fill"), (1, -2, "fill"), (2, -2, "fill"),
        (-2, -1, "fill"), (-1, -1, "fill"), (0, -1, "fill"), (1, -1, "fill"), (2, -1, "fill"),
        (-1, 0, "fill"), (0, 0, "fill"), (1, 0, "fill"),
        (-1, 1, "fill"), (1, 1, "fill"),
        # Eyes
        (-1, -1, "eye"), (1, -1, "eye"),
    ],
    "teen": [
        # Taller creature with limbs
        (0, -4, "fill"), (-1, -4, "fill"), (1, -4, "fill"),
        (-2, -3, "fill"), (-1, -3, "fill"), (0, -3, "fill"), (1, -3, "fill"), (2, -3, "fill"),
        (-2, -2, "fill"), (-1, -2, "fill"), (0, -2, "fill"), (1, -2, "fill"), (2, -2, "fill"),
        (-1, -1, "fill"), (0, -1, "fill"), (1, -1, "fill"),
        (-1, 0, "fill"), (0, 0, "fill"), (1, 0, "fill"),
        (-2, 1, "fill"), (2, 1, "fill"),  # Arms
        (-1, 2, "fill"), (1, 2, "fill"),  # Legs
        # Eyes
        (-1, -2, "eye"), (1, -2, "eye"),
    ],
    "adult": [
        # Full-sized creature with wings/crown
        (-2, -5, "accent"), (2, -5, "accent"),  # Crown/horns
        (-1, -4, "fill"), (0, -4, "fill"), (1, -4, "fill"),
        (-2, -3, "fill"), (-1, -3, "fill"), (0, -3, "fill"), (1, -3, "fill"), (2, -3, "fill"),
        (-3, -2, "accent"), (-2, -2, "fill"), (-1, -2, "fill"), (0, -2, "fill"), (1, -2, "fill"), (2, -2, "fill"), (3, -2, "accent"),
        (-3, -1, "accent"), (-2, -1, "fill"), (-1, -1, "fill"), (0, -1, "fill"), (1, -1, "fill"), (2, -1, "fill"), (3, -1, "accent"),
        (-2, 0, "fill"), (-1, 0, "fill"), (0, 0, "fill"), (1, 0, "fill"), (2, 0, "fill"),
        (-2, 1, "fill"), (-1, 1, "fill"), (0, 1, "fill"), (1, 1, "fill"), (2, 1, "fill"),
        (-2, 2, "fill"), (2, 2, "fill"),  # Legs
        # Eyes
        (-1, -2, "eye"), (1, -2, "eye"),
    ],
}


class CodePetApp(ctk.CTk):
    """Main application window for CodePet."""

    def __init__(self):
        super().__init__()

        # Initialize database
        self.db = get_database()

        # Load pet state from database
        self.pet_state = self._load_pet_state()

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

    def _load_pet_state(self) -> dict:
        """Load pet state from database."""
        cursor = self.db.execute("SELECT * FROM pet_state WHERE id = 1")
        row = cursor.fetchone()
        return dict(row) if row else {
            "name": "Pet",
            "level": 1,
            "current_xp": 0,
            "evolution_stage": "egg"
        }

    def _calculate_xp_for_level(self, level: int) -> int:
        """Calculate XP needed to reach a given level (polynomial curve)."""
        # XP = 50 * level^1.5 (rounded)
        return int(50 * (level ** 1.5))

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

        # Pet display frame
        self.pet_frame = ctk.CTkFrame(
            self.sidebar,
            height=150,
            fg_color=("gray85", "gray20")
        )
        self.pet_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.pet_frame.grid_propagate(False)
        self.pet_frame.grid_columnconfigure(0, weight=1)
        self.pet_frame.grid_rowconfigure(0, weight=1)

        # Canvas for pet sprite
        self.pet_canvas = tk.Canvas(
            self.pet_frame,
            width=160,
            height=120,
            bg="#333333",
            highlightthickness=0
        )
        self.pet_canvas.grid(row=0, column=0, padx=10, pady=10)

        # Draw initial pet sprite
        self._draw_pet_sprite()

        # Pet name label
        self.pet_name_label = ctk.CTkLabel(
            self.sidebar,
            text=self.pet_state["name"],
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.pet_name_label.grid(row=2, column=0, padx=10, pady=(5, 0))

        # Stats frame with level and XP
        self.stats_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color=("gray85", "gray20")
        )
        self.stats_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.stats_frame.grid_columnconfigure(0, weight=1)

        # Level display
        self.level_label = ctk.CTkLabel(
            self.stats_frame,
            text=f"Level {self.pet_state['level']}",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.level_label.grid(row=0, column=0, padx=10, pady=(10, 5))

        # XP bar frame
        self.xp_frame = ctk.CTkFrame(
            self.stats_frame,
            fg_color="transparent"
        )
        self.xp_frame.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")
        self.xp_frame.grid_columnconfigure(0, weight=1)

        # XP label
        xp_needed = self._calculate_xp_for_level(self.pet_state["level"] + 1)
        current_xp = self.pet_state["current_xp"]
        self.xp_label = ctk.CTkLabel(
            self.xp_frame,
            text=f"XP: {current_xp}/{xp_needed}",
            font=ctk.CTkFont(size=11)
        )
        self.xp_label.grid(row=0, column=0, sticky="w")

        # XP progress bar
        xp_progress = current_xp / xp_needed if xp_needed > 0 else 0
        self.xp_bar = ctk.CTkProgressBar(
            self.stats_frame,
            width=160,
            height=15
        )
        self.xp_bar.set(xp_progress)
        self.xp_bar.grid(row=2, column=0, padx=10, pady=(0, 10))

        # Evolution stage label
        self.evolution_label = ctk.CTkLabel(
            self.stats_frame,
            text=f"Stage: {self.pet_state['evolution_stage'].capitalize()}",
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60")
        )
        self.evolution_label.grid(row=3, column=0, padx=10, pady=(0, 10))

    def _draw_pet_sprite(self):
        """Draw the pet sprite on the canvas based on evolution stage."""
        self.pet_canvas.delete("all")

        stage = self.pet_state["evolution_stage"]
        base_color = EVOLUTION_COLORS.get(stage, "#FFFFFF")
        sprite = EVOLUTION_SPRITES.get(stage, EVOLUTION_SPRITES["egg"])

        # Calculate center of canvas
        canvas_width = 160
        canvas_height = 120
        center_x = canvas_width // 2
        center_y = canvas_height // 2

        # Pixel size
        pixel_size = 8

        # Draw each pixel
        for px, py, color_type in sprite:
            x1 = center_x + px * pixel_size
            y1 = center_y + py * pixel_size
            x2 = x1 + pixel_size
            y2 = y1 + pixel_size

            if color_type == "fill":
                color = base_color
            elif color_type == "outline":
                color = self._darken_color(base_color, 0.3)
            elif color_type == "eye":
                color = "#000000"
            elif color_type == "accent":
                color = self._lighten_color(base_color, 0.3)
            else:
                color = base_color

            self.pet_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def _darken_color(self, hex_color: str, factor: float) -> str:
        """Darken a hex color by a factor (0-1)."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        r = int(r * (1 - factor))
        g = int(g * (1 - factor))
        b = int(b * (1 - factor))

        return f"#{r:02x}{g:02x}{b:02x}"

    def _lighten_color(self, hex_color: str, factor: float) -> str:
        """Lighten a hex color by a factor (0-1)."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))

        return f"#{r:02x}{g:02x}{b:02x}"

    def update_pet_display(self):
        """Update the pet display with current state."""
        # Reload pet state from database
        self.pet_state = self._load_pet_state()

        # Update pet name
        self.pet_name_label.configure(text=self.pet_state["name"])

        # Update level
        self.level_label.configure(text=f"Level {self.pet_state['level']}")

        # Update XP bar
        xp_needed = self._calculate_xp_for_level(self.pet_state["level"] + 1)
        current_xp = self.pet_state["current_xp"]
        self.xp_label.configure(text=f"XP: {current_xp}/{xp_needed}")
        xp_progress = current_xp / xp_needed if xp_needed > 0 else 0
        self.xp_bar.set(xp_progress)

        # Update evolution stage
        self.evolution_label.configure(
            text=f"Stage: {self.pet_state['evolution_stage'].capitalize()}"
        )

        # Redraw sprite
        self._draw_pet_sprite()

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
