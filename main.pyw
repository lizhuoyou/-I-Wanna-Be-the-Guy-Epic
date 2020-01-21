# game name: FINDING RICARDO
# game type: Mario or I Wanna Be the Guy
# Header comments
# individual features
"""
1. Gravity effecting player's movement
2. Player's ability to move horizontally
3. Player's ability to double jump
4. Player's ability to throw staff to kill mobs
5. Maps made up of 2D lists
6. Player is able to walk on and interact with blocks of the maps
7. Interactive traps that are able to kill the player
8. Interactive mobs that are able to kill the player
9. Player is able to travel from one map to another through in-game portals
10. Player's movement are all animated
11. Secret chapters are hidden within the three chapters
12. Secret easteregg is hidden within the three chapters
13. Multiple easteregg is hidden within the menu screen
14. Player's movements all acquire sound effects
15. Mobs' movement all acquire sound effects
16. Background music is acquired
17. Additional sound effects such as completing a level are included
18. Multiple backgrounds are displayed
19. More than 10 different blocks are displayed
20. Instructions and guidelines are displayed in the menu
21. A background story is displayed in the menu
22. Additional control bar is displayed when the player is inside of a chapter
23. The user is able to create and login into multiple accounts, each with a name and a password
24. The accounts record data about the game experience (e.g. number of chapters unlocked, total death)
25. Total death of the current account is displayed on the control bar and is constantly updating
26. A save option is provided on the control bar
27. The user is able to turn on or off the background music using the control bar
28. All mobs and traps are animated
29. The user is able to return to the menu using the control bar
30. The user is able to either re-attempt the current chapter or return to the menu when the player dies
31. The user, with no existing account, can only start from chapter 1, with rest being locked
32. The user, with account, choose between different chapters depending on the account's status
33. The control bar displays the player's current health (which is 1)
"""
# attention to details
"""
1. It is made sure that the player cannot move out of the map except vertically up (which is on purpose)
2. It is made sure that the player's hitbox is at the center of the player's picture
3. It is made sure that all chapters are playable and is kept at a challenging difficulty (make the game fun)
4. It is made sure that all audios are set with appropriate volume, not conflicting with each other
5. It is made sure that all pressable buttons chances colour when the mouse collide with them
6. It is made sure that all instructions are easy to understand
7. The menu is made with multiple surfaces which keeps the game clean
8. It is made sure that the control bar is clear and concise
9. Codes and functions are organized into different files base on their functionality
10. Most functions are black-boxed which prevents conflicts
11. It is made sure that there is no bug in the game.
12. It is made sure that the chapters are positioned in an increasing order of difficulty
"""
# Reminding: 1. various functions with comments are distributed to sub files (tool.py, pro.py, enemy.py, interface.py).
#            2. userData.txt contains players' account and their account information. When do testing I suggest using
#               the account with name 1 and password 1
#            3. to make testing even easier, please go to line 1155 and uncomment "pro_alive = True" to be invincible


# main.py
from pygame import *
from random import *
import os

# import from my files
import pro
import tool
import enemy
import interface

# Here is to initializing the program set up the screen and frame.
init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
display.set_caption('FINDING RICARDO')
iconPic = image.load("pic/icon.png")
display.set_icon(iconPic)
mouse.set_cursor(*cursors.broken_x)  # reset cursor's picture
screen = display.set_mode((1440, 720))
surface = 'intro'  # is to change the interfaces

# show icon while the program is being processed
screen.fill((224, 224, 224))
screen.blit(transform.scale(iconPic, (500, 500)), (470, 110))
display.update()

# preserve pro's basic info
pro_alive = True
polePic = transform.scale(image.load('pic/pro/staff/pole.png'), (100, 100))
userMaxChap = 1  # defines which chapter pro can get to.
userName = ''  # it defines who the user is by storing user's name
deathTimes = 0  # this is checking how many times pro has been died

# preserve background pictures
backPics = ['pic/background/0.jpg', 'pic/background/1.jpg', 'pic/background/2.jpg',
            "pic/background/sky.jpg", "pic/background/system_failure.jpg", "pic/background/classroom.jpg"]
backPics = tool.loadPics(backPics, 1440, 720)

# preserve lava pic which is used to indicate the region where pro can't go
lavaPic = transform.scale(image.load("pic/background/lava.jpg"), (1440, 100))
nmlX1 = 0
nmlX2 = -1440
nmlY = 705

# preserve ground pics
groundPics = ["pic/blocks/0.png", "pic/blocks/1.png", "pic/blocks/2.png",
              "pic/blocks/3.png", "pic/blocks/4.png", "pic/blocks/5.png",
              "pic/blocks/6.png", "pic/blocks/7.png", "pic/blocks/8.png",
              "pic/blocks/9.png", "pic/blocks/10.png"]
groundPics = tool.loadPics(groundPics, 60, 60)

# preserve enemy pics
minionPics = ["pic/enemy/bat.png", "pic/enemy/minionB.png", "pic/enemy/minionR.png", "pic/enemy/alpaca.png",
              "pic/enemy/red_bird.png", "pic/enemy/blue_bird.png", "pic/enemy/yellow_bird.png",
              "pic/enemy/superMinion.png"]

minionPics = tool.loadPics(minionPics, 60, 50)
ripPic = transform.scale(image.load('pic/enemy/rip.png'), (50, 50))  # when a minion is dead it shows a grave stone

MrBananaPics = ['pic/enemy/MrBanana0.png', 'pic/enemy/MrBanana1.png']
MrBananaPics = tool.loadPics(MrBananaPics, 120, 120)
BananaPic = transform.scale(image.load('pic/enemy/banana.png'), (50, 50))  # the banana thrown by MrBanana
BananaPic1 = BananaPic  # in each chapter, there are maximum 4 banana pictures being used.
BananaPic2 = BananaPic
BananaPic3 = BananaPic
BananaPic4 = BananaPic

FFFPics = ['pic/enemy/MrFFF0.png', 'pic/enemy/MrFFF1.png']
FFFPics = tool.loadPics(FFFPics, 120, 120)
fireBallPic = transform.scale(image.load('pic/enemy/fireBall.png'), (50, 50))  # the fire ball thrown by MrFFF
fireBallPic1 = fireBallPic  # in each chapter, there are maximum 3 fireball pictures being used.
fireBallPic2 = fireBallPic
fireBallPic3 = fireBallPic

potPic = transform.scale(image.load('pic/enemy/pot.png'), (70, 70))  # for the piranha flower
flowerPic = transform.scale(image.load('pic/enemy/flower.png'), (70, 70))

bladePic = transform.scale(image.load('pic/enemy/blade.png'), (100, 100))  # for the rotating blade
bladePic1 = bladePic  # in each chapter, there are maximum 5 blade pictures being used.
bladePic2 = bladePic
bladePic3 = bladePic
bladePic4 = bladePic
bladePic5 = bladePic

facePics = ["pic/enemy/face0.png", "pic/enemy/face1.png", "pic/enemy/face2.png"]
facePics = tool.loadPics(facePics, 60, 60)

explosionPic = image.load('pic/enemy/explosion.png')  # this is for TNT

# the ending picture
end_pic = transform.scale(image.load('pic/ricardo&mckenzie.jpg'), (500, 720))

# preserve music
# background music
mixer.music.load("sound/background_music.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)
music_pause = False

# sound effects
click_sound = mixer.Sound("sound/click.wav")

pro_sounds = [mixer.Sound("sound/pro/jump1.wav"), mixer.Sound("sound/pro/jump2.wav"),
              mixer.Sound("sound/pro/woosh.wav"), mixer.Sound("sound/pro/dies.wav")]

fff_sounds = [mixer.Sound("sound/fff/fireball1.wav"), mixer.Sound("sound/fff/fireball2.wav"),
              mixer.Sound("sound/fff/ow.wav"), mixer.Sound("sound/fff/rah.wav")]

banana_sounds = [mixer.Sound("sound/banana/banana1.wav"), mixer.Sound("sound/banana/banana2.wav"),
                 mixer.Sound("sound/banana/ow.wav"), mixer.Sound("sound/banana/rah.wav")]

happysad_sounds = [mixer.Sound("sound/happysad/laugh1.wav"), mixer.Sound("sound/happysad/laugh2.wav"),
                   mixer.Sound("sound/happysad/laugh3.wav"), mixer.Sound("sound/happysad/explosion.wav")]

minion_sound = mixer.Sound("sound/fff/ow.wav")

superminion_sounds = [mixer.Sound("sound/superminion/laugh1.wav"), mixer.Sound("sound/superminion/laugh2.wav"),
                      mixer.Sound("sound/superminion/laugh3.wav"), mixer.Sound("sound/superminion/rah.wav")]

flower_sound = mixer.Sound("sound/flower/flower_bump.wav")

stage_clear_sound = mixer.Sound("sound/stage_clear.wav")

world_clear_sound = mixer.Sound("sound/world_clear.wav")

special_block_sound = mixer.Sound("sound/coin.wav")

just_died = False  # a variable used to activate death music

# preserve ground lists to draw the ground blocks
showChaps = False  # this is used to show chapter bar which directs user to chapters

chapter1_ground = [[4, 7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 7, 0, 7, 0, 7, 0, 0],
                   [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [7, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 7, 0, 7, 0, 7, 0, 7, 0],
                   [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 7, 0, 7, 0, 7, 0, 0],
                   [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 7, 9, 0, 7, 0, 7, 0, 7, 0, 7, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 7, 0, 9, 0, 0, 7, 0, 7, 0, 7, 0, 0],
                   [0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 8, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 7, 7, 9, 0, 7, 0, 7, 0, 8, 0, 8, 0],
                   [8, 8, 0, 0, 7, 0, 7, 0, 0, 0, 7, 0, 7, 9, 9, 0, 0, 0, 0, 0, 8, 8, 8, 0]]

easteregg_ground = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                    [6, 6, 6, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

chapter2_ground = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [3, 2, 3, 3, 2, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 3, 3, 2, 3, 2],
                   [5, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 5, 5, 5],
                   [5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5],
                   [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 1, 5, 5, 5, 1, 1]]

chapter3_ground = [[0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0, 0, 6, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 11, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 11, 11, 11, 11, 11, 11, 4],
                   [0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 10, 0, 11, 11, 11, 11, 11, 11, 11, 11, 0, 10, 0, 11, 11, 11, 11, 0, 10, 0],
                   [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 10, 0, 0, 0, 0, 11, 0, 10, 0],
                   [0, 0, 0, 0, 10, 11, 11, 11, 11, 11, 11, 11, 0, 11, 0, 10, 10, 10, 10, 0, 11, 0, 10, 0],
                   [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 11, 0, 10, 0],
                   [10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 10, 10]]

easteregg2_ground = [[0, 0, 4, 0, 4, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 4, 4, 0, 0, 0],
                     [0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0],
                     [0, 0, 4, 4, 4, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0],
                     [0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0],
                     [0, 0, 4, 0, 4, 0, 4, 4, 4, 0, 4, 4, 4, 0, 4, 4, 4, 0, 4, 4, 4, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 4, 0, 0, 0, 4, 0, 4, 4, 4, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4, 4, 0, 0],
                     [0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0],
                     [0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0],
                     [0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0],
                     [0, 0, 0, 4, 0, 4, 0, 0, 4, 4, 4, 0, 4, 0, 4, 0, 4, 4, 4, 0, 4, 4, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# preserve portal image. portal is where pro gonna finish each chapter
portal_pic = transform.scale(image.load("pic/portal.png"), (60, 120))


# this game is distributed in 3 chapters. Each chapter has is own value. we use surface to display chapters
def set_chapter(chap):
    """this function is used to set up chapters.It takes in a chapter's name and use glob to set up.It is not a black
    box function but it is extraordinary efficient for this game"""
    # first we use global to enable this function to change the variables in this program to set up the game
    global pro_alive, jumping, pro_direction, d_jump, acc, poleSet, pro_x, pro_y, portal1_rect, portal2_rect, minion1Dir, minion1X, \
        minion2X, minion2Dir, minion1Live, minion2Live, minion3X, minion3Dir, minion3Live, upBallXY1, downBallXY1, upXYchange1, \
        downXYchange1, MrFFF_alive1, upFiring1, downFiring1, upBallXY2, downBallXY2, upXYchange2, downXYchange2, \
        MrFFF_alive2, upFiring2, downFiring2, upBallXY3, downBallXY3, upXYchange3, downXYchange3, MrFFF_alive3, \
        upFiring3, downFiring3, blade1Y, blade1X, blade1_dir, blade1_start, blade1_end, blade2Y, blade2X, blade2_dir, \
        blade2_start, blade2_end, blade3Y, blade3X, blade3_dir, blade3_start, blade3_end, blade4X, blade4Y, blade4_dir, \
        blade4_start, blade4_end, blade5X, blade5Y, blade5_dir, blade5_start, blade5_end, potXY, flowerXY, piranhaMode, \
        alpaca1X, alpaca1Dir, alpaca1Live, alpaca2X, alpaca2Dir, alpaca2Live, alpaca3X, alpaca3Dir, alpaca3Live, \
        alpaca4X, alpaca4Dir, alpaca4Live, alpaca5X, alpaca5Dir, alpaca5Live, Banana1XY, Banana1XYchange, MrBanana1Live, \
        firing1, Banana2XY, Banana2XYchange, MrBanana2Live, firing2, Banana3XY, Banana3XYchange, MrBanana3Live, firing3, \
        Banana4XY, Banana4XYchange, MrBanana4Live, firing4, potXY1, flowerXY1, piranhaMode1, potXY2, flowerXY2, \
        piranhaMode2, potXY3, flowerXY3, piranhaMode3, potXY4, flowerXY4, piranhaMode4, potXY5, flowerXY5, piranhaMode5, \
        potXY6, flowerXY6, piranhaMode6, potXY7, flowerXY7, piranhaMode7, potXY8, flowerXY8, piranhaMode8, potXY9, \
        flowerXY9, piranhaMode9, potXY10, flowerXY10, piranhaMode10, potXY11, flowerXY11, piranhaMode11, potXY12, \
        flowerXY12, piranhaMode12, potXY13, flowerXY13, piranhaMode13, special_block_count, superMinionX, superMinionDir, \
        superMinionLive, triggerTNT, letGO

    # secondly we reset Pro's universal motion variables
    pro_alive = True
    jumping = False
    pro_direction = "right"  # initial direction is right.
    d_jump = 0
    acc = -5
    poleSet = set()  # when pro get to the next chapter, poleSet has to be reset
    mixer.music.unpause()

    # then we set the variable based on different chapters
    if chap == "chapter1":  # chapter 1.
        # preparing for pro
        pro_x, pro_y = -20, 520

        # portals.
        portal1_rect = Rect(1240, 540, 80, 120)
        portal2_rect = Rect(1300, 420, 80, 120)

        # enemies
        minion1X = 620
        minion1Dir = 'left'
        minion2X = 0
        minion2Dir = 'right'
        minion1Live = 1
        minion2Live = 1
        minion3X = 70
        minion3Dir = 'right'
        minion3Live = 1

        upBallXY1 = -100, -100  # make sure it is not shown in the screen when the game starts
        downBallXY1 = -100, -100
        upXYchange1 = 0, 0
        downXYchange1 = 0, 0
        MrFFF_alive1 = 9
        upFiring1 = False
        downFiring1 = False

        upBallXY2 = -100, -100  # make sure it is not shown in the screen when the game starts
        downBallXY2 = -100, -100
        upXYchange2 = 0, 0
        downXYchange2 = 0, 0
        MrFFF_alive2 = 9
        upFiring2 = False
        downFiring2 = False

        upBallXY3 = -100, -100  # make sure it is not shown in the screen when the game starts
        downBallXY3 = -100, -100
        upXYchange3 = 0, 0
        downXYchange3 = 0, 0
        MrFFF_alive3 = 9
        upFiring3 = False
        downFiring3 = False

        blade3Y = 200
        blade3X = 400
        blade3_dir = "up"
        blade3_start = -50
        blade3_end = 500

        blade4X = 800
        blade4Y = 100
        blade4_dir = "down"
        blade4_start = -50
        blade4_end = 500

        blade5X = 200
        blade5Y = 400
        blade5_dir = "up"
        blade5_start = -50
        blade5_end = 500

        potXY = (775, 350)
        flowerXY = (775, 320)
        piranhaMode = 0

    elif chap == "chapter2":
        # set portal
        portal1_rect = Rect(1360, 60, 80, 120)

        # reset pro's x,y value
        pro_x, pro_y = (600, 160)

        # minions
        alpaca1X = 620
        alpaca1Dir = 'left'
        alpaca1Live = 1

        alpaca2X = 100
        alpaca2Dir = 'right'
        alpaca2Live = 1

        alpaca3X = 150
        alpaca3Dir = 'left'
        alpaca3Live = 1

        alpaca4X = 200
        alpaca4Dir = 'right'
        alpaca4Live = 1

        alpaca5X = 250
        alpaca5Dir = 'left'
        alpaca5Live = 1

        # Mr. Banana
        Banana1XY = -100, -100
        Banana1XYchange = 0, 0
        MrBanana1Live = 7
        firing1 = False

        Banana2XY = -100, -100
        Banana2XYchange = 0, 0
        MrBanana2Live = 7
        firing2 = False

        Banana3XY = -100, -100
        Banana3XYchange = 0, 0
        MrBanana3Live = 7
        firing3 = False

        Banana4XY = -100, -100
        Banana4XYchange = 0, 0
        MrBanana4Live = 7
        firing4 = False

        blade3Y = 500
        blade3X = 400
        blade3_dir = "left"
        blade3_start = 400
        blade3_end = 900

        blade4Y = 610
        blade4X = 400
        blade4_dir = "right"
        blade4_start = 200
        blade4_end = 600

        blade5Y = 300
        blade5X = 1030
        blade5_dir = "up"
        blade5_start = -50
        blade5_end = 400

        # flower
        potXY = (1140, 650)
        flowerXY = (1140, 620)
        piranhaMode = 0

    elif chap == 'chapter3':
        # reset pro's x,y value
        pro_x, pro_y = -20, 400

        # portal
        portal1_rect = Rect(240, 550, 80, 120)

        # special_block
        chapter3_ground[5][23] = 4

        # minions
        minion1X = 600
        minion1Dir = 'left'
        minion1Live = 10

        minion2X = 800
        minion2Dir = 'right'
        minion2Live = 1

        minion3X = 1000
        minion3Dir = 'right'
        minion3Live = 1

        superMinionX = 350
        superMinionDir = 'left'
        superMinionLive = 10

        # Mr. FFF
        upBallXY1 = -100, -100
        downBallXY1 = -100, -100
        upXYchange1 = 0, 0
        downXYchange1 = 0, 0
        MrFFF_alive1 = 9
        upFiring1 = False
        downFiring1 = False

        # Mr. Banana
        Banana1XY = -100, -100
        Banana1XYchange = 0, 0
        MrBanana1Live = 7
        firing1 = False

        # pic
        blade1Y = 260
        blade1X = 302
        blade1_dir = "right"
        blade1_start = 300
        blade1_end = 900

        blade2Y = 402
        blade2X = 200
        blade2_dir = "down"
        blade2_start = 400
        blade2_end = 620

        blade3Y = 620
        blade3X = 1378
        blade3_dir = "left"
        blade3_start = 1280
        blade3_end = 1380

        # flower
        potXY1 = (55, 690)
        flowerXY1 = (55, 660)
        piranhaMode1 = 0

        potXY2 = (175, 690)
        flowerXY2 = (175, 660)
        piranhaMode2 = 0

        potXY3 = (175, 690)
        flowerXY3 = (175, 660)
        piranhaMode3 = 0

        potXY4 = (295, 690)
        flowerXY4 = (295, 660)
        piranhaMode4 = 0

        potXY5 = (415, 690)
        flowerXY5 = (415, 660)
        piranhaMode5 = 0

        potXY6 = (535, 690)
        flowerXY6 = (535, 660)
        piranhaMode6 = 0

        potXY7 = (655, 690)
        flowerXY7 = (655, 660)
        piranhaMode7 = 0

        potXY8 = (775, 690)
        flowerXY8 = (775, 660)
        piranhaMode8 = 0

        potXY9 = (895, 690)
        flowerXY9 = (895, 660)
        piranhaMode9 = 0

        potXY10 = (1015, 690)
        flowerXY10 = (1015, 660)
        piranhaMode10 = 0

        potXY11 = (1135, 690)
        flowerXY11 = (1135, 660)
        piranhaMode11 = 0

        potXY12 = (1255, 690)
        flowerXY12 = (1255, 660)
        piranhaMode12 = 0

        potXY13 = (1375, 690)
        flowerXY13 = (1375, 660)
        piranhaMode13 = 0

        triggerTNT = False
        letGO = False

        # it is for a special block which will break after pro standing on it for certain amount of time
        special_block_count = 0


# for circumstance bar.
# circumstance bar enable user to save, check death times, open/close background music, go back to menu and so on.
# for save during the middle of the game
save_rect = Rect(1300, 725, 120, 40)
save_pic = transform.scale(image.load("pic/save.png"), (120, 40))

font.init()
arial_black = font.SysFont("Arial Black", 30)
comic_sans = font.SysFont("Comic Sans MS", 80)
health_txt = arial_black.render("lim x → ∞ 1000^10000/x+1", True, (40, 40, 40))
no_health_txt = arial_black.render("0", True, (40, 40, 40))

# return to intro
menu_rect = Rect(40, 725, 120, 40)
menu_txt = arial_black.render("Menu", True, (40, 40, 40))

# bgm
music_on = True
bgm_rect = Rect(180, 725, 120, 40)
bgm_txt = arial_black.render("BGM", True, (40, 40, 40))

# the ending text
end_txt = comic_sans.render("MISSION COMPLETE", True, (255, 255, 255))

# start!
clock = time.Clock()        # to make the game run smoothly
running = True
while running:
    # exiting
    press = False  # this is used to count clicking
    pressF = False  # this is checking if f key is pressed
    for e in event.get():
        if e.type == QUIT:
            running = False
            if userName != '':  # auto-save user's information if he/she had log in.
                tool.saveFile(screen, userMaxChap, deathTimes, userName)
        if e.type == MOUSEBUTTONUP:  # make testing easier
            press = True  # this means the mouse is clicked
            click_sound.play()
        if e.type == KEYDOWN:
            if e.key == K_f:
                pressF = True
                pro_sounds[2].play()  # throwing sound is played when the user press f (which throws a stick)
            if e.key == K_SPACE:
                pro_sounds[randint(0, 1)].play()  # a jumping sound (randomly selected) is played when the player jumps

    mx, my = mouse.get_pos()

    if surface == "intro":  # go to intro screen
        mixer.music.pause()
        surface, showChaps, userMaxChap, userName, deathTimes = interface.intro_screen(screen, mx, my, press, showChaps,
                                                                                       userMaxChap, userName,
                                                                                       deathTimes)
        if surface == 'chapter1':  # set values for each chapter
            set_chapter(surface)
            screen = display.set_mode((1440,
                                       770))  # when player is playing the game, the screen's size will be changed with some extened features
        elif surface == 'chapter2':
            set_chapter(surface)  # values of variables are different depending on the chapter
            screen = display.set_mode((1440, 770))
        elif surface == 'chapter3':
            set_chapter(surface)
            screen = display.set_mode((1440, 770))

    elif surface == "guide":
        surface = interface.guide_screen(screen, mx, my, press)

    elif surface == "credit":
        surface = interface.credit_screen(screen, mx, my, press)

    elif surface == "backstory":
        surface = interface.story_screen(screen, mx, my, press)

    else:           # the flowing surfaces are the surfaces user actually play the game.
        if surface == "easteregg":
            screen.blit(backPics[3], (0, 0))
            tool.make_ground(screen, easteregg_ground, groundPics)
            pro_x, pro_y, acc, jumping, d_jump, pro_direction, polePic, poleSet = pro.draw_pro(screen, pro_x,
                                                                                               pro_y, acc, jumping,
                                                                                               d_jump,
                                                                                               pro_direction,
                                                                                               easteregg_ground,
                                                                                               pressF, polePic,
                                                                                               poleSet)

            if pro_y == 640:  # if the player drops to the "ground",
                surface = "chapter1"  # it then drops down (since this map is directly above chapter 1)
                pro_y = -80  # to the top of chapter 1

            # a portal is set on the map, and if player enters the portal, the player is transported
            # directly to chapter 3
            screen.blit(portal_pic, (1320, 420))
            if portal2_rect.collidepoint(pro_x, pro_y):
                surface = "chapter3"
                set_chapter(surface)
                userMaxChap = 3

        elif surface == 'chapter1':
            if pro_alive:
                # background
                screen.blit(backPics[0], (0, 0))

                # here we add the ground
                tool.make_ground(screen, chapter1_ground, groundPics)

                # draw the pro
                pro_x, pro_y, acc, jumping, d_jump, pro_direction, polePic, poleSet = pro.draw_pro(screen, pro_x,
                                                                                                   pro_y, acc,
                                                                                                   jumping, d_jump,
                                                                                                   pro_direction,
                                                                                                   chapter1_ground,
                                                                                                   pressF, polePic,
                                                                                                   poleSet)
                # draw the minions
                minion1X, minion1Dir, pro_alive, minion1Live, poleSet = enemy.minion(screen, minionPics[2],
                                                                                     (80, 660), minion1X, 300,
                                                                                     minion1Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     minion1Live, poleSet,
                                                                                     ripPic, minion_sound)

                minion2X, minion2Dir, pro_alive, minion2Live, poleSet = enemy.minion(screen, minionPics[1],
                                                                                     (0, 820), minion2X, 460,
                                                                                     minion2Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     minion2Live, poleSet,
                                                                                     ripPic, minion_sound)
                minion3X, minion3Dir, pro_alive, minion3Live, poleSet = enemy.minion(screen, minionPics[0], (70, 1350),
                                                                                     minion3X, 60, minion3Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     minion3Live, poleSet, ripPic,
                                                                                     minion_sound)

                # draw the stationary blades
                bladePic1, pro_alive = enemy.blade(screen, bladePic1, 130, 600, pro_x, pro_y, pro_alive)

                bladePic2, pro_alive = enemy.blade(screen, bladePic2, 590, 480, pro_x, pro_y, pro_alive)

                # the other 3 blades move upside down
                bladePic3, pro_alive, blade3X, blade3Y, blade3_dir = enemy.movable_blade(screen, bladePic3,
                                                                                         blade3X,
                                                                                         blade3Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         10, blade3_dir,
                                                                                         blade3_start,
                                                                                         blade3_end)

                bladePic4, pro_alive, blade4X, blade4Y, blade4_dir = enemy.movable_blade(screen, bladePic4,
                                                                                         blade4X,
                                                                                         blade4Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         10, blade4_dir,
                                                                                         blade4_start,
                                                                                         blade4_end)

                bladePic5, pro_alive, blade5X, blade5Y, blade5_dir = enemy.movable_blade(screen, bladePic5,
                                                                                         blade5X,
                                                                                         blade5Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         10, blade5_dir,
                                                                                         blade5_start,
                                                                                         blade5_end)

                # draws the three MR.FFF mob
                fireBallPic1, upBallXY1, downBallXY1, upXYchange1, downXYchange1, MrFFF_alive1, pro_alive, upFiring1, downFiring1, poleSet = enemy.MrFFF(
                    screen, FFFPics, fireBallPic1, (1120, 120), upBallXY1, downBallXY1, upXYchange1,
                    downXYchange1,
                    pro_x, pro_y, MrFFF_alive1, pro_alive, upFiring1, downFiring1, poleSet, fff_sounds)
                fireBallPic2, upBallXY2, downBallXY2, upXYchange2, downXYchange2, MrFFF_alive2, pro_alive, upFiring2, downFiring2, poleSet = enemy.MrFFF(
                    screen, FFFPics, fireBallPic2, (1000, 360), upBallXY2, downBallXY2, upXYchange2,
                    downXYchange2,
                    pro_x, pro_y, MrFFF_alive2, pro_alive, upFiring2, downFiring2, poleSet, fff_sounds)

                fireBallPic3, upBallXY3, downBallXY3, upXYchange3, downXYchange3, MrFFF_alive3, pro_alive, upFiring3, downFiring3, poleSet = enemy.MrFFF(
                    screen, FFFPics, fireBallPic3, (1240, 360), upBallXY3, downBallXY3, upXYchange3,
                    downXYchange3,
                    pro_x, pro_y, MrFFF_alive3, pro_alive, upFiring3, downFiring3, poleSet, fff_sounds)

                # draws the flower and the pipe
                piranhaMode, flowerXY, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY,
                                                                       flowerXY, pro_x,
                                                                       pro_y, piranhaMode, pro_alive, flower_sound)

                # blit a lava pic to indicate the pro can't touch the ground
                nmlX1, nmlX2 = tool.no_man_land(screen, lavaPic, nmlX1, nmlX2, nmlY, 2)

                # if player notice the question mark block and go up there by jumping out of screen, he'll see easteregg
                if pro_y == -80 and -40 < pro_x < -20:
                    surface = "easteregg"
                    set_chapter(surface)

                # use portal so user can go to next chapter
                screen.blit(portal_pic, (1260, 540))
                if portal1_rect.collidepoint(pro_x, pro_y):
                    surface = "chapter2"        # setup for next chapter.
                    set_chapter(surface)
                    userMaxChap = 2
                    stage_clear_sound.play()

                # if pro falls on the very bottom of the screen, he will die
                if pro_y == 640:
                    pro_alive = False

                if not pro_alive:  # this will later be stored on the users file (counting the death in total)
                    deathTimes += 1

            else:  # the "death" surface will be displayed if the character dies
                surface, pro_alive = interface.death_screen(screen, mx, my, press, "chapter1")
                if pro_alive:  # reset the game when restart
                    set_chapter(surface)

        elif surface == "chapter2":
            if pro_alive:
                screen.blit(backPics[1], (0, 0))

                # here we add the ground
                tool.make_ground(screen, chapter2_ground, groundPics)

                # draw the pro
                pro_x, pro_y, acc, jumping, d_jump, pro_direction, polePic, poleSet = pro.draw_pro(screen, pro_x,
                                                                                                   pro_y, acc,
                                                                                                   jumping, d_jump,
                                                                                                   pro_direction,
                                                                                                   chapter2_ground,
                                                                                                   pressF, polePic,
                                                                                                   poleSet)
                # minions
                alpaca1X, alpaca1Dir, pro_alive, alpaca1Live, poleSet = enemy.superMinion(screen, minionPics[3],
                                                                                          (600, 600), alpaca1X, -50,
                                                                                          alpaca1Dir,
                                                                                          pro_x, pro_y, pro_alive,
                                                                                          alpaca1Live, poleSet,
                                                                                          ripPic, superminion_sounds)

                alpaca2X, alpaca2Dir, pro_alive, alpaca2Live, poleSet = enemy.minion(screen, minionPics[3],
                                                                                     (100, 350), alpaca2X, 370,
                                                                                     alpaca2Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     alpaca2Live, poleSet,
                                                                                     ripPic, minion_sound)

                alpaca3X, alpaca3Dir, pro_alive, alpaca3Live, poleSet = enemy.minion(screen, minionPics[3],
                                                                                     (100, 350), alpaca3X, 370,
                                                                                     alpaca3Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     alpaca3Live, poleSet,
                                                                                     ripPic, minion_sound)

                alpaca4X, alpaca4Dir, pro_alive, alpaca4Live, poleSet = enemy.minion(screen, minionPics[3],
                                                                                     (100, 350), alpaca4X, 370,
                                                                                     alpaca4Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     alpaca4Live, poleSet,
                                                                                     ripPic, minion_sound)

                alpaca5X, alpaca5Dir, pro_alive, alpaca5Live, poleSet = enemy.minion(screen, minionPics[3],
                                                                                     (100, 350), alpaca5X, 370,
                                                                                     alpaca5Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     alpaca5Live, poleSet,
                                                                                     ripPic, minion_sound)

                # Mr. Banana
                BananaPic1, Banana1XY, Banana1XYchange, MrBanana1Live, pro_alive, firing1, poleSet = enemy.MrBanana(
                    screen,
                    MrBananaPics,
                    BananaPic1,
                    (0, 125),
                    Banana1XY,
                    Banana1XYchange,
                    pro_x, pro_y,
                    MrBanana1Live,
                    pro_alive,
                    firing1, poleSet, banana_sounds)

                BananaPic2, Banana2XY, Banana2XYchange, MrBanana2Live, pro_alive, firing2, poleSet = enemy.MrBanana(
                    screen,
                    MrBananaPics,
                    BananaPic2,
                    (100, 125),
                    Banana2XY,
                    Banana2XYchange,
                    pro_x, pro_y,
                    MrBanana2Live,
                    pro_alive,
                    firing2, poleSet, banana_sounds)

                BananaPic3, Banana3XY, Banana3XYchange, MrBanana3Live, pro_alive, firing3, poleSet = enemy.MrBanana(
                    screen,
                    MrBananaPics,
                    BananaPic3,
                    (200, 125),
                    Banana3XY,
                    Banana3XYchange,
                    pro_x, pro_y,
                    MrBanana3Live,
                    pro_alive,
                    firing3, poleSet, banana_sounds)

                BananaPic4, Banana4XY, Banana4XYchange, MrBanana4Live, pro_alive, firing4, poleSet = enemy.MrBanana(
                    screen,
                    MrBananaPics,
                    BananaPic4,
                    (1280, 365),
                    Banana4XY,
                    Banana4XYchange,
                    pro_x, pro_y,
                    MrBanana4Live,
                    pro_alive,
                    firing4, poleSet, banana_sounds)

                # blade
                bladePic1, pro_alive = enemy.blade(
                    screen, bladePic1, 930, 580, pro_x, pro_y, pro_alive)

                bladePic2, pro_alive = enemy.blade(
                    screen, bladePic2, 910, 320, pro_x, pro_y, pro_alive)

                # movable blades
                bladePic3, pro_alive, blade3X, blade3Y, blade3_dir = enemy.movable_blade(screen, bladePic3,
                                                                                         blade3X,
                                                                                         blade3Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         11, blade3_dir,
                                                                                         blade3_start,
                                                                                         blade3_end)

                bladePic4, pro_alive, blade4X, blade4Y, blade4_dir = enemy.movable_blade(screen, bladePic4,
                                                                                         blade4X,
                                                                                         blade4Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         11, blade4_dir,
                                                                                         blade4_start,
                                                                                         blade4_end)

                bladePic5, pro_alive, blade5X, blade5Y, blade5_dir = enemy.movable_blade(screen, bladePic5,
                                                                                         blade5X,
                                                                                         blade5Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         10, blade5_dir,
                                                                                         blade5_start,
                                                                                         blade5_end)

                # flower
                piranhaMode, flowerXY, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY,
                                                                       flowerXY, pro_x, pro_y, piranhaMode,
                                                                       pro_alive, flower_sound)

                # portal
                screen.blit(portal_pic, (1380, 60))
                if portal1_rect.collidepoint(pro_x, pro_y):
                    surface = "chapter3"
                    set_chapter(surface)
                    userMaxChap = 3
                    stage_clear_sound.play()

                if not pro_alive:       # accumulate death times
                    deathTimes += 1

            else:
                surface, pro_alive = interface.death_screen(screen, mx, my, press, "chapter2")
                if pro_alive:  # reset the game when restart
                    set_chapter(surface)

        elif surface == "chapter3":
            # the following will be used for chapter 3
            if pro_alive:
                screen.blit(backPics[2], (0, 0))

                # here we add the ground
                tool.make_ground(screen, chapter3_ground, groundPics)

                # draw the pro
                pro_x, pro_y, acc, jumping, d_jump, pro_direction, polePic, poleSet = pro.draw_pro(screen, pro_x,
                                                                                                   pro_y, acc,
                                                                                                   jumping, d_jump,
                                                                                                   pro_direction,
                                                                                                   chapter3_ground,
                                                                                                   pressF, polePic,
                                                                                                   poleSet)

                # draw minions
                minion1X, minion1Dir, pro_alive, minion1Live, poleSet = enemy.minion(screen, minionPics[4],
                                                                                     (180, 600), minion1X, 60,
                                                                                     minion1Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     minion1Live, poleSet,
                                                                                     ripPic, minion_sound)

                minion2X, minion2Dir, pro_alive, minion2Live, poleSet = enemy.minion(screen, minionPics[5],
                                                                                     (500, 1100), minion2X, 0,
                                                                                     minion2Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     minion2Live, poleSet,
                                                                                     ripPic, minion_sound)

                minion3X, minion3Dir, pro_alive, minion3Live, poleSet = enemy.minion(screen, minionPics[6],
                                                                                     (900, 1400), minion3X, 120,
                                                                                     minion3Dir,
                                                                                     pro_x, pro_y, pro_alive,
                                                                                     minion3Live, poleSet,
                                                                                     ripPic, minion_sound)

                superMinionX, superMinionDir, pro_alive, superMinionLive, poleSet = enemy.superMinion(screen,
                                                                                                      minionPics[7],
                                                                                                      (300, 720),
                                                                                                      superMinionX, 610,
                                                                                                      superMinionDir,
                                                                                                      pro_x, pro_y,
                                                                                                      pro_alive,
                                                                                                      superMinionLive,
                                                                                                      poleSet,
                                                                                                      ripPic,
                                                                                                      superminion_sounds)

                # Mr. FFF
                fireBallPic1, upBallXY1, downBallXY1, upXYchange1, downXYchange1, MrFFF_alive1, pro_alive, upFiring1, downFiring1, poleSet = enemy.MrFFF(
                    screen, FFFPics, fireBallPic1, (
                        600, 180), upBallXY1, downBallXY1, upXYchange1,
                    downXYchange1,
                    pro_x, pro_y, MrFFF_alive1, pro_alive, upFiring1, downFiring1, poleSet, fff_sounds)

                # Mr. Banana
                BananaPic1, Banana1XY, Banana1XYchange, MrBanana1Live, pro_alive, firing1, poleSetf = enemy.MrBanana(
                    screen, MrBananaPics, BananaPic1, (240, 280), Banana1XY, Banana1XYchange, pro_x, pro_y,
                    MrBanana1Live,
                    pro_alive, firing1, poleSet, banana_sounds)

                # blade
                # this if-elif statements are made so the movable blades can turn and change their moving directions
                if (blade1X, blade1Y) == (898, 260) and blade1_dir == "right":
                    blade1_dir = "down"
                    blade1X, blade1Y = 900, 262
                    blade1_start, blade1_end = (260, 600)

                elif (blade1X, blade1Y) == (900, 498) and blade1_dir == "down":
                    blade1_dir = "right"
                    blade1X, blade1Y = 902, 500
                    blade1_start, blade1_end = (900, 1100)

                elif (blade1X, blade1Y) == (902, 500) and blade1_dir == "left":
                    blade1_dir = "up"
                    blade1X, blade1Y = 900, 498
                    blade1_start, blade1_end = (260, 500)

                elif (blade1X, blade1Y) == (900, 262) and blade1_dir == "up":
                    blade1_dir = "left"
                    blade1X, blade1Y = 898, 260
                    blade1_start, blade1_end = (300, 900)

                bladePic1, pro_alive, blade1X, blade1Y, blade1_dir = enemy.movable_blade(screen, bladePic1,
                                                                                         blade1X,
                                                                                         blade1Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         2, blade1_dir,
                                                                                         blade1_start,
                                                                                         blade1_end)

                # this if-elif statements are made so the movable blades can turn and change their moving directions
                if (blade2X, blade2Y) == (200, 618) and blade2_dir == "down":
                    blade2_dir = "left"
                    blade2X, blade2Y = 198, 620
                    blade2_start, blade2_end = (0, 200)

                elif (blade2X, blade2Y) == (198, 620) and blade2_dir == "right":
                    blade2_dir = "up"
                    blade2X, blade2Y = 200, 618
                    blade2_start, blade2_end = (400, 620)

                bladePic2, pro_alive, blade2X, blade2Y, blade2_dir = enemy.movable_blade(screen, bladePic2,
                                                                                         blade2X,
                                                                                         blade2Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         2, blade2_dir,
                                                                                         blade2_start,
                                                                                         blade2_end)

                # this if-elif statements are made so the movable blades can turn and change their moving directions
                if (blade3X, blade3Y) == (1282, 620) and blade3_dir == "left":
                    blade3_dir = "up"
                    blade3X, blade3Y = 1280, 618
                    blade3_start, blade3_end = (360, 620)

                elif (blade3X, blade3Y) == (1280, 618) and blade3_dir == "down":
                    blade3_dir = "right"
                    blade3X, blade3Y = 1282, 620
                    blade3_start, blade3_end = (1280, 1380)

                bladePic3, pro_alive, blade3X, blade3Y, blade3_dir = enemy.movable_blade(screen, bladePic3,
                                                                                         blade3X,
                                                                                         blade3Y, pro_x,
                                                                                         pro_y, pro_alive,
                                                                                         2, blade3_dir,
                                                                                         blade3_start,
                                                                                         blade3_end)

                # draw piranha flower
                piranhaMode1, flowerXY1, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY1,
                                                                         flowerXY1, pro_x,
                                                                         pro_y, piranhaMode1, pro_alive, flower_sound)

                piranhaMode2, flowerXY2, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY2,
                                                                         flowerXY2, pro_x,
                                                                         pro_y, piranhaMode2, pro_alive, flower_sound)

                piranhaMode3, flowerXY3, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY3,
                                                                         flowerXY3, pro_x,
                                                                         pro_y, piranhaMode3, pro_alive, flower_sound)

                piranhaMode4, flowerXY4, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY4,
                                                                         flowerXY4, pro_x,
                                                                         pro_y, piranhaMode4, pro_alive, flower_sound)

                piranhaMode5, flowerXY5, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY5,
                                                                         flowerXY5, pro_x,
                                                                         pro_y, piranhaMode5, pro_alive, flower_sound)

                piranhaMode6, flowerXY6, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY6,
                                                                         flowerXY6, pro_x,
                                                                         pro_y, piranhaMode6, pro_alive, flower_sound)

                piranhaMode7, flowerXY7, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY7,
                                                                         flowerXY7, pro_x,
                                                                         pro_y, piranhaMode7, pro_alive, flower_sound)

                piranhaMode8, flowerXY8, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY8,
                                                                         flowerXY8, pro_x,
                                                                         pro_y, piranhaMode8, pro_alive, flower_sound)

                piranhaMode9, flowerXY9, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY9,
                                                                         flowerXY9, pro_x,
                                                                         pro_y, piranhaMode9, pro_alive, flower_sound)

                piranhaMode10, flowerXY10, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY10,
                                                                           flowerXY10, pro_x,
                                                                           pro_y, piranhaMode10, pro_alive,
                                                                           flower_sound)

                piranhaMode11, flowerXY11, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY11,
                                                                           flowerXY11, pro_x,
                                                                           pro_y, piranhaMode11, pro_alive,
                                                                           flower_sound)

                piranhaMode12, flowerXY12, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY12,
                                                                           flowerXY12, pro_x,
                                                                           pro_y, piranhaMode12, pro_alive,
                                                                           flower_sound)

                piranhaMode13, flowerXY13, pro_alive = enemy.piranhaFlower(screen, potPic, flowerPic, potXY13,
                                                                           flowerXY13, pro_x,
                                                                           pro_y, piranhaMode13, pro_alive,
                                                                           flower_sound)

                # draws a semi-happy semi-sad face mob
                triggerTNT = enemy.face(screen, facePics, (960, 300), pro_x, pro_y, letGO, happysad_sounds)
                if triggerTNT:
                    pro_alive = enemy.TNT(screen, facePics[2], explosionPic, (960, 300), pro_x, pro_y)

                    # this can change the surface to show the TNT works when pro is set to be invincible
                    # surface = 'intro'

                # display the "health" of the block so that the user will know when the block will break
                if 70 - special_block_count > 9:
                    special_block_txt = arial_black.render(str(70 - special_block_count), True, (255, 255, 0))
                    screen.blit(special_block_txt, (1390, 310))
                elif 70 - special_block_count > 0:
                    special_block_txt = arial_black.render("0" + str(70 - special_block_count), True, (255, 255, 0))
                    screen.blit(special_block_txt, (1390, 310))

                if 1348 <= pro_x <= 1370 and pro_y == 220:  # if the player is stepping on top of the question block
                    special_block_count += 1  # the block will count up to 70 and when it reaches, it dissappears
                    special_block_sound.play()  # play the sound so the user will know that they are activating the code

                    if special_block_count == 70:  # if the block dissappears, the TNT mob will not explode when
                        chapter3_ground[5][23] = 0  # the player collide with it
                        letGO = True

                # another easter egg is triggered if the player steps in this area
                if 1230 <= pro_x <= 1250 and 630 <= pro_y <= 640:
                    pro_x, pro_y = (760, 400)
                    surface = "easteregg2"

                # portal
                screen.blit(portal_pic, (300, 570))
                if portal1_rect.collidepoint(pro_x, pro_y):
                    surface = "ending picture"
                    mixer.music.pause()
                    world_clear_sound.play()

                if not pro_alive:  # count how many deaths.
                    deathTimes += 1
            else:
                surface, pro_alive = interface.death_screen(screen, mx, my, press, "chapter3")
                if pro_alive:  # reset the game when restart
                    set_chapter(surface)

        elif surface == "easteregg2":
            # this easteregg is a deadend and does not do anything
            # the user can only close the game after that (but hey! it is an EASTEREGG!)
            screen.blit(backPics[4], (0, 0))

            # here we add the ground
            tool.make_ground(screen, easteregg2_ground, groundPics)

            # draw the pro
            pro_x, pro_y, acc, jumping, d_jump, pro_direction, polePic, poleSet = pro.draw_pro(screen, pro_x,
                                                                                               pro_y, acc,
                                                                                               jumping, d_jump,
                                                                                               pro_direction,
                                                                                               easteregg2_ground,
                                                                                               pressF, polePic,
                                                                                               poleSet)

        elif surface == "ending picture":
            screen.blit(backPics[5], (0, 0))
            screen.blit(end_pic, (470, 0))
            screen.blit(end_txt, (300, 600))
            if press:
                surface = "intro"

        # this is for testing. we leave it just in case you need it (you'll probably need it)
        # pro_alive = True  # temporarily disable pro to die

        # these codes make sure the death sound will be played and only play once when player dies
        if not pro_alive and just_died:
            pro_sounds[3].play()
            just_died = False

        if pro_alive:
            just_died = True

        # here we draw a control bar
        # this is an additional space that allows the user to perform several commands when playing inside of a chapter
        draw.rect(screen, (192, 192, 192), (0, 720, 1440, 50))
        draw.rect(screen, (179, 0, 0), (0, 720, 1440, 50), 4)

        # show pro's status
        screen.blit(transform.scale(iconPic, (40, 40)), (400, 725))  # draws the player's icon/head

        if pro_alive:  # draws a full health bar if the player is alive
            draw.rect(screen, (255, 0, 0), (450, 725, 460, 40))
            screen.blit(health_txt, (460, 725))
        else:  # draws a grey bar representing player's death
            draw.rect(screen, (160, 160, 160), (450, 725, 460, 40))
            screen.blit(no_health_txt, (660, 725))

        # display the number of deaths
        death_number_txt = arial_black.render("TOTAL DEATH: " + str(deathTimes), True, (255, 0, 0))
        screen.blit(death_number_txt, (950, 725))

        # for saving
        # draws a save button that allows the user to save their progress
        draw.rect(screen, (0, 0, 0), save_rect, 4)
        screen.blit(save_pic, (1300, 725))

        # allows the user to enter their username and password to save
        if save_rect.collidepoint(mx, my):
            draw.rect(screen, (0, 255, 0), save_rect, 4)
            if press:
                tool.saveFile(screen, userMaxChap, deathTimes, userName)

        if surface == 'intro':
            # set screen back to smaller size it is not inside of a chapter
            screen = display.set_mode((1440, 720))

        # return to menu (intro screen)
        draw.rect(screen, (168, 168, 168), menu_rect)

        # allows the user to return to the intro screen if the button is pressed
        if menu_rect.collidepoint(mx, my):
            draw.rect(screen, (108, 108, 108), menu_rect)
            draw.rect(screen, (0, 255, 0), menu_rect, 4)
            if press:
                surface = "intro"
        else:
            draw.rect(screen, (0, 0, 0), menu_rect, 4)

        screen.blit(menu_txt, (58, 723))

        # allows the user to turn on or off the background music during gaming
        draw.rect(screen, (0, 255, 0), bgm_rect)
        if music_on:
            draw.rect(screen, (0, 255, 0), bgm_rect)
        else:
            draw.rect(screen, (255, 0, 0), bgm_rect)
        if bgm_rect.collidepoint(mx, my):
            draw.rect(screen, (0, 0, 255), bgm_rect, 4)
            if press:
                if music_on:
                    music_on = False
                    mixer.music.pause()
                else:
                    music_on = True
                    mixer.music.unpause()
        else:
            draw.rect(screen, (0, 0, 0), bgm_rect, 4)

        if surface == 'intro':  # when the surface became intro, the screen size should change as well
            screen = display.set_mode((1440, 720))

        screen.blit(bgm_txt, (200, 723))

    clock.tick(50)
    display.flip()

quit()
