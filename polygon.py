import math

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    angle_x = math.radians(360 / (number_of_sides * 2))
    height = math.cos(angle_x) * circle_radius
    base = math.sin(angle_x) * circle_radius
    triangle_area = 0.5 * base * height
    print(f"angle x: {angle_x}, height: {height}, base: {base}, triangle area: {triangle_area}")
    return round(triangle_area * (number_of_sides * 2), 3)