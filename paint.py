from pathlib import Path
import tkinter as tk


def parse_command(command):
    """Parses a command byte from the AGI data.

    Args:
        command: A single byte representing a command.

    Returns:
        A tuple containing:
            - is_move (bool): True if the command represents a move, False otherwise.
            - delta_x (int): X-axis movement value (if is_move is True).
            - delta_y (int): Y-axis movement value (if is_move is True).
            - line_length (int): Length of the line to draw (if not a move).
    """

    is_move = command & 0x80
    delta_x = command & 0x7F if is_move else 0
    delta_y = (command >> 7) & 0x7F if is_move else 0
    line_length = command & 0x7F if not is_move else 0
    return is_move, delta_x, delta_y, line_length


def draw(pic_data):
    """Draws the AGI graphic based on the provided data.

    Args:
        pic_data: The byte data from the AGI graphic file.
    """

    x, y = 0, 0
    color_index = 0
    for command in pic_data[2:]:  # Skip header bytes
        is_move, delta_x, delta_y, line_length = parse_command(command)
        if is_move:
            x += delta_x
            y += delta_y
        else:
            end_x = x + line_length
            end_y = y + line_length
            draw_line((x, y), (end_x, end_y), color_index)
            x = end_x
            y = end_y
        color_index = (color_index + 1) % len(COLORS)


def draw_line(start_coords, end_coords, color_index):
    """Draws a line on the canvas.

    Args:
        start_coords: A tuple representing the starting coordinates (x, y).
        end_coords: A tuple representing the ending coordinates (x, y).
        color_index: The index of the color to use for drawing the line.
    """

    canvas.create_line(
        *[(x * SCALE_X, y * SCALE_Y) for x, y in (start_coords, end_coords)],
        fill="#%02x%02x%02x" % COLORS[color_index],
        width=4,
    )


# Define color palette (16 colors)
COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252),
]

# Adjust these values to control scaling and window size
SCALE_X = 6
SCALE_Y = 4

# Load the AGI graphic data
pic_path = Path("data/PIC_1")  # Replace with your file path
pic_data = pic_path.read_bytes()

# Create the tkinter window and canvas
root = tk.Tk()
root.title("Sierra AGI Visualizer")
canvas = tk.Canvas(root, width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()

# Draw the graphic
draw(pic_data)
tk.mainloop()