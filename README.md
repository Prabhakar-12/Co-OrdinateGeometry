# Distance & Midpoint Calculator (Flask + Python)

A simple web application that calculates the distance and midpoint between two points in a 2D coordinate system. Built using Python, Flask, HTML/CSS, and Matplotlib.

## Features

- Input two points: \((x_1, y_1)\) and \((x_2, y_2)\).
- Compute:
  - Distance: \(\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\).
  - Midpoint: \(\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)\).
- Visualize the two points, the line segment, and the midpoint on a graph.
- Clean, beginner-friendly code structure using separate modules.

## Project Structure

distance_midpoint_calculator/
├── app.py
├── README.md
├── requirements.txt
├── src/
│ ├── calculator.py
│ └── plotter.py
├── templates/
│ └── index.html
└── static/
└── style.css

