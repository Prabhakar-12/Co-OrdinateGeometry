import matplotlib.pyplot as plt


def plot_points(x1, y1, x2, y2, mid_x, mid_y, distance):
    """
    Visualize the two points, the line segment between them, and the midpoint.
    """
    plt.figure(figsize=(8, 6))

    # Plot points and connecting line
    plt.plot([x1, x2], [y1, y2], 'bo-', linewidth=2, markersize=8, label='Line Segment')
    plt.plot(x1, y1, 'bo', markersize=10, label=f'Point A ({x1}, {y1})')
    plt.plot(x2, y2, 'go', markersize=10, label=f'Point B ({x2}, {y2})')

    # Plot midpoint
    plt.plot(mid_x, mid_y, 'ro', markersize=12, label=f'Midpoint ({mid_x:.2f}, {mid_y:.2f})')

    # Annotate distance
    plt.annotate(f'Distance: {distance:.2f}', xy=(mid_x, mid_y), xytext=(mid_x + 0.5, mid_y + 0.5),
                 fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.7))

    # Formatting plot
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.axhline(y=0, color='black', linewidth=0.7)
    plt.axvline(x=0, color='black', linewidth=0.7)
    plt.axis('equal')
    plt.title('Distance and Midpoint Visualization')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
