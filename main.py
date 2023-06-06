import pygame #you should add "Lambda's Pygame Interface Utilities (LPIU)" library to this list
import utils
from utils import (
    dir_path,
    window,
    center,
    text
)
running = True

fps = 60

clock = pygame.time.Clock()

visible = False

########################
# SCENES
########################

scene = None

class hi:
    def handle():
        window.fill((50,50,50))


#    lambda : (
 #       window.fill((50,50,50)),
  #      msg := utils.text(10,"I'm tired of tools only having typed out docs..."),
   #     msg.render(10,10),
    #    hover_button := utils.button("Hover over me!", 32, (255, 255, 255)),
     #   (hover_button := utils.button("So mine is interactive...", 32, (255, 255, 255))) if hover_button.hover() else None
      #  hover_button.render()

scene = None

class game:
    def handle():
        window.fill((50,50,50)),
        msg = utils.text(32,"I'm tired of tools only having typed out docs...",thicc=2)
        msg.render(center.x(msg.w),1 * 100)
        hover_button = utils.button("Hover over me!", 32, (255, 255, 255))
        if hover_button.hover(center.x(hover_button.txt.w), 2 * 100):
            hover_button = utils.button("So mine is interactive...", 32, (255, 255, 255))
            msg = utils.text(32,"I would say now let\'s check out the code!",thicc=2)
            msg.render(center.x(msg.w),3 * 100)
            msg = utils.text(32,"But I haven't added the comments to guide you...",thicc=2)
            msg.render(center.x(msg.w),(3 * 100) + msg.h)
            msg = utils.text(32,"...and it's a bit of a mess right now.",thicc=2) 
            msg.render(center.x(msg.w),((3 * 100) + (msg.h * 2)))
        hover_button.render(center.x(hover_button.txt.w), 2 * 100)



########################
# GAME LOOP
########################

scene = game

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit