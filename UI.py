from appJar import gui
import random


def gen_rand():
    x = random.randint(1, 101)
    a = [random.randint(1, 11) for _ in range(x)]
    b = [random.randint(1, 11) for _ in range(x)]
    return list(zip(a, b))


def draw():
    app = gui()
    points = []

    def press(btn):
        nonlocal points
        if btn == "Done":
            app.stop()
        elif btn == "Random":
            points = gen_rand()
            app.stop()
        elif btn == "Submit":
            points.append(tuple(map(int, app.getEntry('points').split(','))))

    app.addLabel("title", "Введіть точки вигляду: 1,1 ", 0, 0, 2)  # Row 0,Column 0,Span 2
    app.addEntry("points", 1, 0, 2)                           # Row 1,Column 1
    app.addButtons(["Submit", "Done"], press, 3, 0, 2)  # Row 3,Column 0,Span 2
    app.addButton("Random", press, 4, 1, 2)
    app.setEntryFocus("points")
    app.go()
    return points


