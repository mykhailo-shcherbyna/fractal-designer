# Fractal Designer

An interactive desktop application built in Python to configure and draw mathematical fractals.

## Features
* **Fractal Tree:** Draws a tree pattern that splits into smaller branches using a customizable scaling factor.
* **Sierpinski Triangle:** Draws a large triangle and repeatedly removes the middle sections to create a geometric pattern.
* **Simple Navigation:** Easy screens to pick your fractal, adjust your sliders, and look at the final drawing.

## Project Structure
* main.py - Starts the program.
* ui/fractal_app.py - Controls the window screens, buttons, and sliders.
* core/triangle.py - Handles the triangle shapes and math.
* fractals/fractal_base.py - The parent class configuration for the fractals.
* fractals/fractal_tree.py - The math logic that draws the tree.
* fractals/sierpinski_triangle.py - The math logic that draws the triangle.

## How to Run
1. Open your terminal or command prompt.
2. Navigate into your project folder.
3. Run this command: python main.py
