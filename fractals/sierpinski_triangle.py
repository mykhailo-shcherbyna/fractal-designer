from fractals.fractal_base import FractalBase
from core.triangle import EquilateralTriangle


# This class draws a Sierpinski triangle fractal
class SierpinskiTriangle(FractalBase):
    """
    Draws a Sierpinski triangle fractal.
    It starts from one big triangle and removes the middle part step by step.
    """

    # This method starts drawing the Sierpinski triangle
    def draw(self, canvas):
        # Update the canvas so we can get the correct size
        canvas.update()

        # get values from settings
        side_length = self.settings["side length"]
        depth = self.settings["depth"]
        primary_color = self.settings["primary color"]
        secondary_color = self.settings["secondary color"]
        rotation = self.settings.get("rotation", -90)

        #  Get canvas size
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # Put the first big triangle in the middle of the canvas
        center_x = width / 2
        center_y = height / 2

        # Create the first big triangle
        base_triangle = EquilateralTriangle(
            centroid=(center_x, center_y),
            side_length=side_length,
            rotation=rotation,
            color=primary_color
        )

         # Draw the first triangle
        base_triangle.draw(canvas)

        # This list stores the triangles for the current step
        triangles = [base_triangle]

        # Repeat this process based on the selected depth
        for _ in range(depth):
            # we needs a list to stores the new smaller triangles
            next_triangles = []

            # Divide each triangle into smaller triangles
            for triangle in triangles:
                smaller_triangles = triangle.remove_central(
                    canvas,
                    color=secondary_color
                )

                # Add the smaller triangles for the next round
                next_triangles.extend(smaller_triangles)
            # Move to the next level of triangles
            triangles = next_triangles