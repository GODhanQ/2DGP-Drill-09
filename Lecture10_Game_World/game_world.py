# world[0] : lower layer    | background
# world[1] : upper layer    | objects
# world[2] : ceiling layer  | ceiling elements
world = [[], [], []]

def add_object(o, layer=0):
    world[layer].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    else:
        print('\033[95m' + "Object not found in game world. can't remove." + '\033[0m')