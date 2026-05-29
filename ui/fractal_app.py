import tkinter as tk
import tkinter.ttk as ttk

from fractals.fractal_tree import FractalTree
from fractals.sierpinski_triangle import SierpinskiTriangle

# This class controls the main Tkinter application
class FractalApp:
    """
    Tkinter application for choosing a fractal, changing its parameters,
    and drawing it on a canvas.
    """

    # Create the window, pages, fractal list, and input schemas
    def __init__(self):
        self.canvas = None
        self.inputs_frame = None

        self.window = tk.Tk()
        self.window.title("Fractal Designer")

        # Use most of the screen, but keep the window smaller than full screen
        screen_width = int(0.9 * self.window.winfo_screenwidth())
        screen_height = int(0.9 * self.window.winfo_screenheight())

        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.minsize(500, 500)

        self.container = tk.Frame(self.window)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.fractal_name = tk.StringVar(value="Fractal Tree")
        self.inputs = {}

        # Available fractal classes
        self.fractals = {
            "Fractal Tree": FractalTree,
            "Sierpinski Triangle": SierpinskiTriangle
        }

        # Each schema describes the inputs needed for one fractal
        self.schemas = {
            "Fractal Tree": {
                "size": {
                    "label": "Base Size",
                    "type": "int",
                    "default": 100,
                    "min": 10,
                    "max": 300
                },
                "depth": {
                    "label": "Recursion Depth",
                    "type": "int",
                    "default": 5,
                    "min": 1,
                    "max": 10
                },
                "angle": {
                    "label": "Angle",
                    "type": "int",
                    "default": 30,
                    "min": 0,
                    "max": 180
                },
                "scale": {
                    "label": "Scale",
                    "type": "float",
                    "default": 0.5,
                    "min": 0.1,
                    "max": 0.95
                },
                "color": {
                    "label": "Branch Color",
                    "type": "list",
                    "default": "green",
                    "options": ["green", "blue", "black"]
                }
            },
            "Sierpinski Triangle": {
                "side length": {
                    "label": "Side Length",
                    "type": "int",
                    "default": 100,
                    "min": 50,
                    "max": 500
                },
                "depth": {
                    "label": "Recursion Depth",
                    "type": "int",
                    "default": 5,
                    "min": 1,
                    "max": 10
                },
                "primary color": {
                    "label": "Primary Color",
                    "type": "list",
                    "default": "blue",
                    "options": ["blue", "cyan", "red"]
                },
                "secondary color": {
                    "label": "Background Color",
                    "type": "list",
                    "default": "white",
                    "options": ["white", "black"]
                }
            }
        }

        self.panels = {
            "Selecting Fractal": self.build_fractal_panel(),
            "Selecting Parameters": self.build_parameters_panel(),
            "Drawing Fractal": self.build_drawing_panel()
        }

        self.show_panel("Selecting Fractal")

    # Build the first page where user chooses the fractal type
    def build_fractal_panel(self) -> tk.Frame:
        """Builds the first page where the user selects a fractal."""
        page = tk.Frame(self.container)
        page.grid(row=0, column=0, sticky="nsew")

        tk.Label(
            page,
            text="Welcome to Fractal Designer",
            font=("Arial", 24, "bold"),
            anchor="center"
        ).pack(pady=20, fill="x")

        tk.Label(
            page,
            text="Choose a fractal to begin:",
            font=("Arial", 12),
            anchor="center"
        ).pack(pady=10, fill="x")

        dropdown = ttk.Combobox(
            page,
            textvariable=self.fractal_name,
            values=list(self.fractals.keys()),
            state="readonly",
            width=25,
            font=("Arial", 14),
            justify="center"
        )
        dropdown.pack(pady=10)

        tk.Button(
            page,
            text="Next: Adjust Settings ->",
            font=("Arial", 14),
            command=lambda: self.show_panel("Selecting Parameters")
        ).pack(pady=40)

        return page

    # Build the settings page for the selected fractal
    def build_parameters_panel(self) -> tk.Frame:
        """Builds the page where the user changes fractal settings."""
        page = tk.Frame(self.container)
        page.grid(row=0, column=0, sticky="nsew")

        top_bar = tk.Frame(page)
        top_bar.pack(fill="x", pady=5)

        tk.Button(
            top_bar,
            text="<- Back",
            command=lambda: self.show_panel("Selecting Fractal")
        ).pack(side="left", padx=10)

        tk.Button(
            top_bar,
            text="Draw Fractal",
            command=self.transition_to_drawing
        ).pack(side="right", padx=10)

        tk.Label(
            page,
            text="Adjust Parameters",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.inputs_frame = tk.Frame(page)
        self.inputs_frame.pack(pady=10)

        return page

# Build the page that contains the canvas
    def build_drawing_panel(self) -> tk.Frame:
        """Builds the canvas page where the fractal is drawn."""
        page = tk.Frame(self.container)
        page.grid(row=0, column=0, sticky="nsew")

        top_bar = tk.Frame(page)
        top_bar.pack(fill="x", pady=5)

        tk.Button(
            top_bar,
            text="<- Back to Settings",
            command=lambda: self.show_panel("Selecting Parameters")
        ).pack(side="left", padx=10)

        self.canvas = tk.Canvas(
            page,
            bg="white",
            highlightthickness=1,
            highlightbackground="black"
        )
        self.canvas.pack(padx=20, pady=20, fill="both", expand=True)

        return page

# Show the selected page
    def show_panel(self, panel_name: str):
        """Shows one page of the application."""
        if panel_name == "Selecting Parameters":
            self.generate_inputs()

        frame = self.panels[panel_name]
        frame.tkraise()

    # Create input fields based on the selected fractal
    def generate_inputs(self):
        """Creates input widgets based on the selected fractal schema."""
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        self.inputs.clear()

        # Update max values based on the current window height
        self.window.update_idletasks()
        win_height = self.window.winfo_height()

        self.schemas["Fractal Tree"]["size"]["max"] = int(win_height * 0.5)
        self.schemas["Sierpinski Triangle"]["side length"]["max"] = int(0.7 * win_height)

        fractal_name = self.fractal_name.get()
        schema = self.schemas[fractal_name]

        for row_index, (key, config) in enumerate(schema.items()):
            tk.Label(
                self.inputs_frame,
                text=config["label"] + ":",
                font=("Arial", 12)
            ).grid(row=row_index, column=0, sticky="e", padx=10, pady=5)

            if config["type"] in ["int", "float"]:
                default = min(config["default"], config["max"])
            else:
                default = config["default"]

            if config["type"] == "float":
                var = tk.DoubleVar(value=default)
                widget = tk.Scale(
                    self.inputs_frame,
                    variable=var,
                    from_=config["min"],
                    to=config["max"],
                    resolution=0.01,
                    orient="horizontal",
                    length=300
                )

            elif config["type"] == "int":
                var = tk.IntVar(value=default)
                widget = tk.Scale(
                    self.inputs_frame,
                    variable=var,
                    from_=config["min"],
                    to=config["max"],
                    orient="horizontal",
                    length=300
                )

            elif config["type"] == "list":
                var = tk.StringVar(value=default)
                widget = ttk.Combobox(
                    self.inputs_frame,
                    textvariable=var,
                    values=config["options"],
                    state="readonly",
                    width=15
                )

            widget.grid(row=row_index, column=1, sticky="w", padx=10, pady=5)
            self.inputs[key] = var

    # Go to drawing page and draw after canvas is ready
    def transition_to_drawing(self):
        """Goes to the drawing page and draws the selected fractal."""
        self.show_panel("Drawing Fractal")
        self.window.after(100, self.draw_fractal)

    def draw_fractal(self):
        """Creates the selected fractal object and draws it."""
        self.canvas.delete("all")

    # Get all user input values
        settings = {
            key: variable.get()
            for key, variable in self.inputs.items()
        }

        # We use a fixed rotation for Sierpinski in this version
        if self.fractal_name.get() == "Sierpinski Triangle":
            settings["rotation"] = -90

        # Find the selected fractal class
        fractal_class = self.fractals[self.fractal_name.get()]
        fractal_instance = fractal_class(settings=settings)
        # Draw the fractal on the canvas
        fractal_instance.draw(self.canvas)

    def run(self):
        """Starts the Tkinter app."""
        self.window.mainloop()