import tkinter as tk

BOARD_SIZE = 8
CELL = 70      # taille d'une case en pixels
MARGIN = 30    # marge pour les numéros de lignes / colonnes
DELAY = 150    # millisecondes entre deux déplacements (animation)


def valid_prefix(path):
    """Garde les cases du chemin jusqu'à la première case invalide
    (hors échiquier ou déjà visitée)."""
    valid = []
    for (x, y) in path:
        if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
            break
        if (x, y) in valid:
            break
        valid.append((x, y))
    return valid


def center(x, y):
    """Centre (en pixels) de la case (x, y)."""
    return MARGIN + x * CELL + CELL // 2, MARGIN + y * CELL + CELL // 2


def show_solution(path, generation):
    # accepte aussi bien une liste de positions qu'un objet Knight
    if hasattr(path, "path"):
        path = path.path
    valid_path = valid_prefix(path)

    root = tk.Tk()
    root.title(f"Knight's Tour - génération {generation}")
    size = BOARD_SIZE * CELL + 2 * MARGIN
    canvas = tk.Canvas(root, width=size, height=size,
                       bg="#eeeed2", highlightthickness=0)
    canvas.pack()

    # numéros des colonnes et des lignes (1 à 8), comme dans la Figure 2
    for i in range(BOARD_SIZE):
        c = MARGIN + i * CELL + CELL // 2
        for pos in (MARGIN // 2, MARGIN + BOARD_SIZE * CELL + MARGIN // 2):
            canvas.create_text(c, pos, text=str(i + 1), fill="#769656")
            canvas.create_text(pos, c, text=str(i + 1), fill="#769656")

    # échiquier
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            color = "#eeeed2" if (x + y) % 2 == 0 else "#769656"
            canvas.create_rectangle(MARGIN + x * CELL, MARGIN + y * CELL,
                                    MARGIN + (x + 1) * CELL,
                                    MARGIN + (y + 1) * CELL,
                                    fill=color, outline=color)

    # le cavalier, créé une seule fois sur la case de départ
    start_x, start_y = center(*valid_path[0])
    knight_id = canvas.create_text(start_x, start_y, text="♞",
                                   font=("Arial", 36), fill="black")

    def step(i):
        """Affiche le déplacement numéro i (0 = case de départ)."""
        x, y = valid_path[i]
        cx, cy = center(x, y)
        canvas.create_text(cx, cy, text=str(i + 1), font=("Arial", 16))
        canvas.coords(knight_id, cx, cy)       # déplace le cavalier
        canvas.tag_raise(knight_id)            # le garde au-dessus des numéros
        if i + 1 < len(valid_path):
            root.after(DELAY, step, i + 1)     # prochain déplacement

    step(0)
    root.mainloop()