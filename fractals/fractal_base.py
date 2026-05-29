from abc import ABC, abstractmethod

# This is the parent class for all fractals
class FractalBase(ABC):
    """
    Abstract base class for all fractal types.

    It stores the common settings dictionary and defines the draw method
    that every fractal class must implement.
    """

# Every fractal gets its own settings, like color, size, depth, etc.
    def __init__(self, settings: dict):
        self.settings = settings

# Each fractal class must implement this draw method 
# based on how it should be drawn
    @abstractmethod
    def draw(self, canvas):
        """
        Draw the fractal on the given Tkinter canvas.
        """
        pass