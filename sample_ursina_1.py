from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
Sky()
player = FirstPersonController()
player.speed = 100
player.position = -100,10,-100

def box(position):
    Button(
        parent = scene,
        model="cube",
        origin=0.5,
        position = position,
        scale=(200,1,200),
        color=color.green,
        texture="grass"

    )
box((0,0,0))
app.run()
