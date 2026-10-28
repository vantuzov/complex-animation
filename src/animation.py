import math


def get_shape_points(width: int, height: int, progress: float) -> list[float]:
    center_x = width / 2
    center_y = height / 2
    size = min(width, height) * 0.35
    points = []

    for i in range(120):
        angle = 2 * math.pi * i / 120
        delta = (angle + math.pi / 2) % (2 * math.pi / 3) - math.pi / 3
        triangle_radius = size * math.cos(math.pi / 3) / math.cos(delta)
        radius = size + (triangle_radius - size) * progress
        points.extend(
            (
                center_x + radius * math.cos(angle),
                center_y + radius * math.sin(angle),
            )
        )

    return points
