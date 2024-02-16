import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    # Ваш код здесь:
    r1 = (x-0.5)**2 + (y-0.5)**2 < 0.1
    r2 = (x-0.55)**2 + (y-0.33)**2 < 0.003
    r3 = 0.6*x + 0.2 < y or 0.6*x+0.2 < -y+1
     
    
    return (True, True, False) if r1 and not(r2) and r3 else (False, False, False)


main(shader)