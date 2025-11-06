world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def add_objects(ol, depth = 0):
    world[depth] += ol


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
            remove_colision_object(o)
            return
    # collision_pairs에서도 제거를 해줘야됨~~

    raise ValueError('Cannot delete non existing object')

def remove_colision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def clear():
    global world

    for layer in world:
        layer.clear()


def collide(a,b):
    #get_bb의 리턴값이 튜플이여서.
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

collision_pairs = {} # key: 충돌종류, value: [[a] , [b]]

def addcollide_pairs(group, a, b):
    if group not in collision_pairs:
        print('새로운 그룹 추가')
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)
    #boy:ball: [[]],[[]]





def handle_collision():
    for group, pairs in collision_pairs.items(): # pairs: [[a],[b]] 키하고 밸류하고 분류가 됨 item 이
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    a.handle_collision(group,b)
                    b.handle_collision(group,a)
    pass
