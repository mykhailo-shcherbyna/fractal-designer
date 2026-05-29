import math
from .fractal_base import FractalBase

# This class draws a fractal tree
class FractalTree(FractalBase):
    """
    Draws a simple fractal tree using recursion.
    Each branch creates two smaller branches until the depth becomes zero.
    """
    # This method starts drawing the tree
    def draw(self, canvas):
        # Update the canvas so we can get its real size
        canvas.update()

        # Get values from settings
        size = self.settings["size"]
        depth = self.settings["depth"]
        angle = self.settings["angle"]
        scale = self.settings["scale"]
        color = self.settings["color"]

        # Get canvas size
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # Start from the bottom middle of the canvas
        start_x = width / 2
        start_y = height - 10

        # First branch goes upward
        self.draw_branch(
            canvas,
            start_x,
            start_y,
            -90,
            depth,
            size,
            angle,
            scale,
            color
        )

    # This method draws one branch 
    # and then calls itself for smaller branches
    def draw_branch(self, canvas, start_x, start_y, current_angle,
                    depth, branch_length, angle, scale, color):
        
        # Stop drawing when depth is finished or branch is too small
        if depth == 0 or branch_length < 2:
            return

        # Calculate the end point of the branch
        end_x = start_x + branch_length * math.cos(math.radians(current_angle))
        end_y = start_y + branch_length * math.sin(math.radians(current_angle))

        # Draw the branch on the canvas
        canvas.create_line(
            start_x,
            start_y,
            end_x,
            end_y,
            fill=color,
            width=max(depth, 1)
        )

        # Draw the smaller branch on the left
        self.draw_branch(
            canvas,
            end_x,
            end_y,
            current_angle - angle,
            depth - 1,
            branch_length * scale,
            angle,
            scale,
            color
        )

        # Draw the smaller branch on the right 
        self.draw_branch(
            canvas,
            end_x,
            end_y,
            current_angle + angle,
            depth - 1,
            branch_length * scale,
            angle,
            scale,
            color
        )