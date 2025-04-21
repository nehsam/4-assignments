import tkinter as tk

# Canvas size
CANVAS_SIZE = 400
CELL_SIZE = 40

def toggle_cell(event):
    """ Toggle cell color between blue and white. """
    x, y = event.x, event.y
    row, col = y // CELL_SIZE, x // CELL_SIZE
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        current_color = canvas.itemcget(grid[row][col], "fill")
        new_color = "white" if current_color == "blue" else "blue"
        canvas.itemconfig(grid[row][col], fill=new_color)

def main():
    global canvas, grid, GRID_SIZE

    GRID_SIZE = CANVAS_SIZE // CELL_SIZE
    root = tk.Tk()
    root.title("Grid Toggle Game")

    canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
    canvas.pack()

    # Create grid
    grid = [[canvas.create_rectangle(
        col * CELL_SIZE, row * CELL_SIZE,
        (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE,
        fill="blue", outline="black") for col in range(GRID_SIZE)]
        for row in range(GRID_SIZE)]

    # Bind mouse click to toggle
    canvas.bind("<Button-1>", toggle_cell)

    root.mainloop()

if __name__ == '__main__':
    main()
