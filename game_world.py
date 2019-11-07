
# layer 0: Background Objects
# layer 1: Hand Objects
# layer 2: Pink jelly Objects
# layer 3: Violet fish Objects
# layer 4: Balloon Objects
# layer 5: Bubble Objects
# layer 6: Krab Objects
# layer 7: Spongebob Objects
# layer 8: Patrick Objects

objects = [[],[],[],[],[],[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for i in range(len(objects)):
        for o in all_objects():
            remove_object(o)
            del o


def destroy():
    clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

