# Fractal Designer

An interactive desktop application built in Python to configure and draw mathematical fractals.

## Features
* **Fractal Tree:** Draws a tree pattern that splits into smaller branches using a customizable scaling factor.
* **Sierpinski Triangle:** Draws a large triangle and repeatedly removes the middle sections to create a geometric pattern.
* **Simple Navigation:** Easy screens to pick your fractal, adjust your sliders, and look at the final drawing.

### Screenshots

**1. Select a Fractal**
<img width="1366" height="768" alt="ui" src="https://github.com/user-attachments/assets/613e44da-fe1a-47e7-97dd-cd380d558764" />

**2. Adjust Settings**
<img width="1366" height="768" alt="Settings Panel" src="https://github.com/user-attachments/assets/095655eb-e447-4c7d-a94f-65a39c34acb1" />

**3. Render the Geometry**
<img width="1366" height="768" alt="Canvas Output" src="https://github.com/user-attachments/assets/3912aa05-43ac-4a71-99a2-29b6cb55a87d" />

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
