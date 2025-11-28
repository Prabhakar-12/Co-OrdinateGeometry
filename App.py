from flask import Flask, render_template, request, redirect, url_for
from src.calculator import calculate_distance, calculate_midpoint
from src.plotter import plot_points
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def create_plot_image(x1, y1, x2, y2, mid_x, mid_y, distance):
    # Create plot in memory and return base64 string to embed in HTML
    fig = plt.figure(figsize=(6,5))
    plt.plot([x1, x2], [y1, y2], 'bo-', linewidth=2, markersize=8, label='Line Segment')
    plt.plot(x1, y1, 'bo', markersize=10, label=f'Point A ({x1}, {y1})')
    plt.plot(x2, y2, 'go', markersize=10, label=f'Point B ({x2}, {y2})')
    plt.plot(mid_x, mid_y, 'ro', markersize=12, label=f'Midpoint ({mid_x:.2f}, {mid_y:.2f})')
    plt.annotate(f'Distance: {distance:.2f}', xy=(mid_x, mid_y), xytext=(mid_x + 0.5, mid_y + 0.5),
                 fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.7))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.axhline(y=0, color='black', linewidth=0.7)
    plt.axvline(x=0, color='black', linewidth=0.7)
    plt.axis('equal')
    plt.title('Distance and Midpoint Visualization')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.legend(loc='best')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    img_data = base64.b64encode(buf.read()).decode('utf-8')
    return img_data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            x1 = float(request.form.get("x1"))
            y1 = float(request.form.get("y1"))
            x2 = float(request.form.get("x2"))
            y2 = float(request.form.get("y2"))

            distance = calculate_distance(x1, y1, x2, y2)
            mid_x, mid_y = calculate_midpoint(x1, y1, x2, y2)
            plot_img = create_plot_image(x1, y1, x2, y2, mid_x, mid_y, distance)

            return render_template("index.html",
                                   x1=x1, y1=y1, x2=x2, y2=y2,
                                   distance=round(distance, 4),
                                   midpoint=(round(mid_x, 4), round(mid_y, 4)),
                                   plot_img=plot_img)
        except ValueError:
            error = "Please enter valid numeric coordinates."
            return render_template("index.html", error=error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
