import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy


    zombies = [Zombie() for i in range(4)]
    game_world.add_objects(zombies, 1)


    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.addcollide_pairs('grass:ball', grass, None) # 충돌검사에 잔디 등록

    boy = Boy()
    game_world.add_object(boy, 1)

    global balls
    balls = [Ball(random.randint(300,1600) , 60 , 0) for i in range(20)]
    game_world.add_objects(balls, 1)


#    충돌검사가 필요한 페어를 등록
    game_world.addcollide_pairs('boy:ball', boy , None)

    for ball in balls:
        game_world.addcollide_pairs('boy:ball',None, ball)
        game_world.addcollide_pairs('zombie:ball', None, ball)

    for zombie in zombies:
        game_world.addcollide_pairs('zombie:ball', zombie, None)



def update():
    game_world.update()
    game_world.handle_collision()
    # for ball in balls.copy():
    #     if game_world.collide(boy,ball):
    #         print('COLLISION!')
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

