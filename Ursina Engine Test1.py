from ursina import *
from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45, 45, 45)
            )

class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.pink
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('button pressed')

def update():
    if held_keys['a']:
        test1.x -= 4 * time.dt
    if held_keys['s']:
        test1.y -= 4 * time.dt
    if held_keys['d']:
        test1.x += 4 * time.dt
    if held_keys['w']:
        test1.y += 4 * time.dt

app = Ursina()

test1 = Entity(model = 'quad', color = color.red, scale = (1, 3), position = (1,5))

test_cube = Test_button()

app.run()
