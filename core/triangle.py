import math


# This class represents a normal triangle
class Triangle:

   # Create a triangle with 3 points and a color
    def __init__(self, vertices: list | tuple, color: str = "lightblue"):
        # A triangle must have exactly 3 point
        if len(vertices) != 3:
            raise ValueError("Triangle must have exactly 3 vertices.")

        self.vertices = tuple(vertices)
        self.color = color

    # Draw the triangle on the canvas
    def draw(self, canvas):
        canvas.create_polygon(self.vertices, fill=self.color)

    # Calculate the middle point between two points
    @staticmethod
    def calculate_midpoint(p1: tuple, p2: tuple) -> tuple:
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2
        return mid_x, mid_y


# This class represents an equilateral triangle
class EquilateralTriangle(Triangle):

    # Create the triangle from vertices or from center and side length
    def __init__(
        self,
        vertices: tuple | list = None,
        centroid: tuple = None,
        side_length: float | int = None,
        rotation: float | int = 90,
        color: str = "lightblue"
    ):
        # uer the vertices directly if they're given
        if vertices is not None:
            super().__init__(vertices=vertices, color=color)
            return

        # If center and side length are given, calculate the vertices
        if centroid is not None and side_length is not None:
            if side_length <= 0:
                raise ValueError("Side length must be positive.")

            rotation_in_radians = math.radians(rotation)

            # These are the three angles for the triangle points
            angles = (
                rotation_in_radians,
                rotation_in_radians + 2 * math.pi / 3,
                rotation_in_radians + 4 * math.pi / 3
            )

            # This radius helps us find the points from the center
            radius = side_length / math.sqrt(3)
            centroid_x, centroid_y = centroid

            # Calculate all three vertices
            vertices = [
                (
                    centroid_x + radius * math.cos(angle),
                    centroid_y + radius * math.sin(angle)
                )
                for angle in angles
            ]                

            super().__init__(vertices=vertices, color=color)
            return

        # If the needed values are missing, show an error
        raise ValueError("Provide either vertices or both centroid and side_length.")

# Remove the middle part and return the three outer triangles
    def remove_central(self, canvas, color: str = "white") -> tuple:
        # Find the middle point of each side
        m01 = Triangle.calculate_midpoint(self.vertices[0], self.vertices[1])
        m12 = Triangle.calculate_midpoint(self.vertices[1], self.vertices[2])
        m02 = Triangle.calculate_midpoint(self.vertices[0], self.vertices[2])

        # Draw the middle triangle with background color
        central_triangle = EquilateralTriangle(
            vertices=(m01, m12, m02),
            color=color
        )
        central_triangle.draw(canvas)

        # Create the three smaller outer triangles
        outer_triangles = (
            EquilateralTriangle(
                vertices=(self.vertices[0], m01, m02),
                color=self.color
            ),
            EquilateralTriangle(
                vertices=(m01, self.vertices[1], m12),
                color=self.color
            ),
            EquilateralTriangle(
                vertices=(m02, m12, self.vertices[2]),
                color=self.color
            )
        )

        # Return these triangles for the next step
        return outer_triangles