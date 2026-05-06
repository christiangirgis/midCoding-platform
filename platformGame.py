import pgzrun

# Variables
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
player = Rect((100, 400), (40, 40))

def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")

pgzrun.go()
