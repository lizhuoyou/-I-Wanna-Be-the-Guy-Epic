# interface.py
from pygame import *
import tool

# initializing font for later use
font.init()
arial_black = font.SysFont("Arial Black", 80)
comic_sans = font.SysFont("Comic Sans MS", 30)
bodoni_mt = font.SysFont("Bodoni MT Black", 40)
berlin_sans = font.SysFont("Berlin Sans FB", 20)
britannic_bold = font.SysFont("Britannic Bold", 60)

# subsurface definition for later use
red_surface = Surface((1440, 720), SRCALPHA)

# defining texts for later use
gamename_txt = arial_black.render("FINDING RICARDO", True, (139, 136, 120))
help_txt = comic_sans.render("HELP", True, (169, 169, 169))
help_greentxt = comic_sans.render("HELP", True, (0, 255, 0))
backstory_txt = bodoni_mt.render("BACKSTORY", True, (60, 60, 60))
backstory_greentxt = bodoni_mt.render("BACKSTORY", True, (0, 255, 0))
instruction_txt = bodoni_mt.render("INSTRUCTIONS", True, (60, 60, 60))
walk_txt = berlin_sans.render("Walk", True, (60, 60, 60))
jump_txt = berlin_sans.render("Jump", True, (60, 60, 60))
fire_txt = berlin_sans.render("Fire", True, (60, 60, 60))
credit_txt = bodoni_mt.render("HERE LIES", True, (60, 60, 60))
credit_greytxt = bodoni_mt.render("HERE LIES", True, (40, 40, 40))
jin_txt = berlin_sans.render("Jin Hao Dong", True, (60, 60, 60))
and_txt = berlin_sans.render("&", True, (60, 60, 60))
ricardo_txt = berlin_sans.render("Ricardo You", True, (60, 60, 60))
respawn_txt = britannic_bold.render("Respawn", True, (49, 46, 40))
return_txt = britannic_bold.render("Return", True, (49, 46, 40))
respawn_greentxt = britannic_bold.render("Respawn", True, (0, 255, 0))
return_greentxt = britannic_bold.render("Return", True, (0, 255, 0))
dead_txt = arial_black.render("DEAD", True, (255, 0, 0))

# Jin's description paragraph
jin_grave_txt1 = berlin_sans.render(
    "Here lies a generally good mastermind. Jin was", True, (60, 60, 60))
jin_grave_txt2 = berlin_sans.render(
    "the Colonel of FFF Inquisition. As the head of", True, (60, 60, 60))
jin_grave_txt3 = berlin_sans.render(
    "a secret institution, Jin should have kept silent", True, (60, 60, 60))
jin_grave_txt4 = berlin_sans.render(
    "and do nothing as Ricardo being caught by the", True, (60, 60, 60))
jin_grave_txt5 = berlin_sans.render(
    "principal. However, he was moved by Ricardo’s", True, (60, 60, 60))
jin_grave_txt6 = berlin_sans.render(
    "self-sacrifice and decided to help him escape", True, (60, 60, 60))
jin_grave_txt7 = berlin_sans.render(
    "the school’s evil claw by ordering his underlings", True, (60, 60, 60))
jin_grave_txt8 = berlin_sans.render(
    "to fight against Mr. James.", True, (60, 60, 60))
jin_grave_txt9 = berlin_sans.render(
    "May he be remembered also.", True, (60, 60, 60))

# Ricardo's description paragraph
ricardo_grave_txt1 = berlin_sans.render(
    "Here lies the hero of all youths. Ricardo could", True, (60, 60, 60))
ricardo_grave_txt2 = berlin_sans.render(
    "have been an honourable student, loved by", True, (60, 60, 60))
ricardo_grave_txt3 = berlin_sans.render(
    "teachers,, but he chose not to, because he", True, (60, 60, 60))
ricardo_grave_txt4 = berlin_sans.render(
    "realized the pains other students are suffering", True, (60, 60, 60))
ricardo_grave_txt5 = berlin_sans.render(
    "due to a simple fact – not everyone is as smart", True, (60, 60, 60))
ricardo_grave_txt6 = berlin_sans.render(
    "as he is. ", True, (60, 60, 60))
ricardo_grave_txt7 = berlin_sans.render(
    "He fought, and he challenged by stealing the ", True, (60, 60, 60))
ricardo_grave_txt8 = berlin_sans.render(
    "exam answer sheet, and shared it with his", True, (60, 60, 60))
ricardo_grave_txt9 = berlin_sans.render(
    "classmates.", True, (60, 60, 60))
ricardo_grave_txt10 = berlin_sans.render(
    "May he be remembered.", True, (60, 60, 60))

date_txt = berlin_sans.render(
    "2018.05.01 - 2018.06.15", True, (60, 60, 60))

# the backstory paragraph
story_txt1 = berlin_sans.render(
    "James is a high school computer science teacher and", True, (60, 60, 60))
story_txt2 = berlin_sans.render(
    "acquires a reputation of weird humour within the school.", True, (60, 60, 60))
story_txt3 = berlin_sans.render(
    "He often tells immature jokes to his students, which is", True, (60, 60, 60))
story_txt4 = berlin_sans.render(
    "somehow receiving positive reactions. Regardless of his", True, (60, 60, 60))
story_txt5 = berlin_sans.render(
    '"image", James is having a lot of fun with his teaching', True, (60, 60, 60))
story_txt6 = berlin_sans.render(
    "career. However, his fun all turned into pains when he", True, (60, 60, 60))
story_txt7 = berlin_sans.render(
    "organized his teaching materials and realized that one of", True, (60, 60, 60))
story_txt8 = berlin_sans.render(
    "his smartest student, Ricardo, had stolen the exam sheets…", True, (60, 60, 60))

# defining Rects for later use
sign_rect = Rect(1330, 20, 100, 60)
new_account_rect = Rect(420, 450, 300, 100)
logIn_rect = Rect(720, 450, 300, 100)
chapter1_rect = Rect(50, 50, 200, 150)
chapter2_rect = Rect(50, 250, 200, 150)
chapter3_rect = Rect(50, 450, 200, 150)
backstory_rect = Rect(565, 100, 200, 40)
respawn_rect = Rect(620, 320, 200, 100)
return_rect = Rect(620, 440, 200, 100)
credit_rect = Rect(587, 450, 145, 26)

# loading pictures for later use
background_pic = transform.scale(image.load(
    "pic/intro/black_brick.jpg"), (1440, 720))
chapter1_pic = transform.scale(image.load(
    "pic/intro/chapter1.jpg"), (200, 150))
chapter2_pic = transform.scale(image.load(
    "pic/intro/chapter2.jpg"), (200, 150))
chapter3_pic = transform.scale(image.load(
    "pic/intro/chapter3.jpg"), (200, 150))
tombstone_pic = transform.scale(image.load(
    "pic/intro/tombstone.png"), (500, 700))
returnarrow_pic = transform.scale(
    image.load("pic/intro/grey_arrow.png"), (100, 50))
leftarrow_pic = transform.scale(image.load(
    "pic/intro/left_arrowkey.png"), (50, 50))
rightarrow_pic = transform.scale(image.load(
    "pic/intro/right_arrowkey.png"), (50, 50))
spacebar_pic = transform.scale(image.load("pic/intro/spacebar.png"), (150, 30))
fkey_pic = transform.scale(image.load("pic/intro/f_key.png"), (50, 50))
cemetery_pic = transform.scale(image.load(
    "pic/intro/cemetery.jpg"), (1440, 720))
jin_pic = transform.scale(image.load("pic/intro/jin.jpg"), (160, 160))
ricardo_pic = transform.scale(image.load("pic/intro/ricardo.jpg"), (160, 160))
frame_pic = transform.scale(image.load("pic/intro/frame.jpg"), (200, 200))
grass_pic = transform.scale(image.load("pic/intro/grass.png"), (1440, 300))
torch_pic = transform.scale(image.load("pic/intro/torch.png"), (200, 200))
oil_pic = transform.scale(image.load("pic/intro/oil_bucket.png"), (200, 200))
redhat_pic = transform.scale(image.load("pic/intro/red_hat.png"), (200, 160))
icon_pic = transform.scale(image.load("pic/icon.png"), (120, 120))

# for login and use new account
new_account_rect = Rect(420, 450, 300, 100)
logIn_rect = Rect(720, 450, 300, 100)

new_account_pic = transform.scale(
    image.load("pic/intro/newHere.jpg"), (300, 100))
logIn_pic = transform.scale(image.load("pic/intro/logIn.jpg"), (300, 100))


def intro_screen(screen, mx, my, press, showChaps, userMaxChap, userName, deaths):
    "this function is used to draw introduction screen and redirect user to the interface they wanna go"
    surface = 'intro'   # when it is in intro screen, it's always initially 'intro'

    screen.blit(background_pic, (0, 0))  # blit the background picture

    # draw the game title
    draw.rect(screen, (56, 56, 56), (300, 200, 840, 180))
    draw.rect(screen, (180, 180, 180), (300, 200, 840, 180), 10)
    screen.blit(gamename_txt, (315, 230))

    # draw circles to fill the gaps
    draw.circle(screen, (180, 180, 180), (300, 200), 5)
    draw.circle(screen, (180, 180, 180), (1140, 200), 5)
    draw.circle(screen, (180, 180, 180), (300, 380), 5)
    draw.circle(screen, (180, 180, 180), (1140, 380), 5)

    # this is the button that allows the user to move between different subsurfaces within "intro"
    draw.rect(screen, (56, 56, 56), sign_rect)
    draw.rect(screen, (180, 180, 180), sign_rect, 4)

    # go to guide screen if the button is pressed
    if sign_rect.collidepoint(mx, my):
        screen.blit(help_greentxt, (1340, 30))
        if press:
            surface = 'guide'
    else:
        screen.blit(help_txt, (1340, 30))

    # displays the three chapters for the user to select
    if showChaps:  # chapter bar is hide before an account is selected
        screen.blit(chapter1_pic, (50, 50))
        screen.blit(chapter2_pic, (50, 250))
        screen.blit(chapter3_pic, (50, 450))

        # a shadow shows the chapter being locked
        # meaning that the user cannot select this chapter
        alpha = Surface((200, 150), SRCALPHA)
        draw.rect(alpha, (0, 0, 0, 130), (0, 0, 200, 150))
        if userMaxChap < 2:
            screen.blit(alpha, (50, 250))
            screen.blit(alpha, (50, 450))
        elif userMaxChap < 3:
            screen.blit(alpha, (50, 450))

        if chapter1_rect.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), chapter1_rect, 3)
            if press:
                surface = "chapter1"
        elif chapter2_rect.collidepoint(mx, my) and userMaxChap > 1:
            draw.rect(screen, (0, 255, 0), chapter2_rect, 3)
            if press:
                surface = "chapter2"
        elif chapter3_rect.collidepoint(mx, my) and userMaxChap > 2:
            draw.rect(screen, (0, 0, 255), chapter3_rect, 3)
            if press:
                surface = "chapter3"

        # user can switch to another account or make a new account
        screen.blit(new_account_pic, (420, 450))
        screen.blit(logIn_pic, (720, 450))
        draw.rect(screen, (211, 211, 211), (420, 450, 600, 100), 3)
        if logIn_rect.collidepoint(mx, my):
            draw.rect(screen, (153, 0, 0), logIn_rect, 3)
            if press:
                if userName != "":          # save previous account's values when switch accounts
                    tool.saveFile(screen, userMaxChap, deaths, userName)

                userMaxChap, deaths, userName = tool.loadFile(
                    screen, userMaxChap, deaths, userName)

        elif new_account_rect.collidepoint(mx, my):       # use new account
            draw.rect(screen, (153, 0, 0), new_account_rect, 3)
            if press:
                if userName != "":          # save previous account's values when switch accounts
                    tool.saveFile(screen, userMaxChap, deaths, userName)

                # reset user's information to get a new account.
                userMaxChap = 0
                deaths = 0
                userName = ""

    else:       # users need to choose account and then select chapter to play
        screen.blit(new_account_pic, (420, 450))
        screen.blit(logIn_pic, (720, 450))
        draw.rect(screen, (211, 211, 211), (420, 450, 600, 100), 3)

        if new_account_rect.collidepoint(mx, my):       # use new account
            draw.rect(screen, (153, 0, 0), new_account_rect, 3)
            if press:
                showChaps = True

        elif logIn_rect.collidepoint(mx, my):           # login to saved account
            draw.rect(screen, (153, 0, 0), logIn_rect, 3)
            if press:
                userMaxChap, deaths, userName = tool.loadFile(
                    screen, userMaxChap, deaths, userName)
                if userName != '':
                    showChaps = True

    return surface, showChaps, userMaxChap, userName, deaths


def guide_screen(screen, mx, my, press):
    "the guide screen that shows the control keys and other information"

    # draws a tombstone and instruction menu
    screen.blit(background_pic, (0, 0))
    screen.blit(tombstone_pic, (400, 50))
    screen.blit(leftarrow_pic, (500, 300))
    screen.blit(rightarrow_pic, (560, 300))
    screen.blit(spacebar_pic, (620, 320))
    screen.blit(fkey_pic, (780, 300))

    draw.rect(screen, (56, 56, 56), sign_rect)
    draw.rect(screen, (180, 180, 180), sign_rect, 4)
    screen.blit(returnarrow_pic, (1330, 30))

    # return to intro screen if pressed this button
    if press and sign_rect.collidepoint(mx, my):
        return "intro"

    # go to backstory if the word backstory is pressed
    if backstory_rect.collidepoint(mx, my):
        screen.blit(backstory_greentxt, (580, 110))
        if press:
            return "backstory"
    else:
        screen.blit(backstory_txt, (580, 110))

    if credit_rect.collidepoint(mx, my):
        if press:
            return "credit"
        screen.blit(credit_greytxt, (590, 450))
    else:
        screen.blit(credit_txt, (590, 450))

    # blit the instruction texts
    screen.blit(instruction_txt, (570, 220))
    screen.blit(walk_txt, (530, 360))
    screen.blit(jump_txt, (680, 360))
    screen.blit(fire_txt, (790, 360))
    screen.blit(jin_txt, (600, 510))
    screen.blit(and_txt, (650, 540))
    screen.blit(ricardo_txt, (600, 570))

    return "guide"


def credit_screen(screen, mx, my, press):
    "shows the developer credits"
    # basic picture setup
    screen.blit(cemetery_pic, (0, 0))
    screen.blit(tombstone_pic, (150, 50))
    screen.blit(tombstone_pic, (750, 50))
    screen.blit(frame_pic, (330, 150))
    screen.blit(frame_pic, (930, 150))
    screen.blit(jin_pic, (350, 170))
    screen.blit(ricardo_pic, (950, 170))

    # Jin's character description
    screen.blit(jin_grave_txt1, (225, 360))
    screen.blit(jin_grave_txt2, (225, 380))
    screen.blit(jin_grave_txt3, (225, 400))
    screen.blit(jin_grave_txt4, (225, 420))
    screen.blit(jin_grave_txt5, (225, 440))
    screen.blit(jin_grave_txt6, (225, 460))
    screen.blit(jin_grave_txt7, (225, 480))
    screen.blit(jin_grave_txt8, (235, 500))
    screen.blit(jin_grave_txt9, (245, 520))
    screen.blit(date_txt, (235, 560))

    # Ricardo's character description
    screen.blit(ricardo_grave_txt1, (825, 360))
    screen.blit(ricardo_grave_txt2, (825, 380))
    screen.blit(ricardo_grave_txt3, (825, 400))
    screen.blit(ricardo_grave_txt4, (825, 420))
    screen.blit(ricardo_grave_txt5, (825, 440))
    screen.blit(ricardo_grave_txt6, (835, 460))
    screen.blit(ricardo_grave_txt7, (825, 480))
    screen.blit(ricardo_grave_txt8, (825, 500))
    screen.blit(ricardo_grave_txt9, (845, 520))
    screen.blit(ricardo_grave_txt10, (835, 540))
    screen.blit(date_txt, (835, 580))

    # more background decorations
    screen.blit(grass_pic, (0, 490))
    screen.blit(oil_pic, (420, 520))
    screen.blit(torch_pic, (430, 500))
    screen.blit(redhat_pic, (1000, 550))

    if press:
        return "guide"

    return "credit"


def story_screen(screen, mx, my, press):
    "shows the backstory of the game"

    # same thing as guide screen, only to move everything to the left
    screen.blit(background_pic, (0, 0))
    screen.blit(tombstone_pic, (100, 50))
    screen.blit(leftarrow_pic, (200, 300))
    screen.blit(rightarrow_pic, (260, 300))
    screen.blit(spacebar_pic, (320, 320))
    screen.blit(fkey_pic, (480, 300))
    screen.blit(backstory_txt, (880, 110))
    screen.blit(instruction_txt, (270, 220))
    screen.blit(walk_txt, (230, 360))
    screen.blit(jump_txt, (380, 360))
    screen.blit(fire_txt, (490, 360))
    screen.blit(credit_txt, (290, 450))
    screen.blit(jin_txt, (300, 510))
    screen.blit(and_txt, (350, 540))
    screen.blit(ricardo_txt, (300, 570))

    draw.rect(screen, (56, 56, 56), sign_rect)
    draw.rect(screen, (180, 180, 180), sign_rect, 4)
    screen.blit(returnarrow_pic, (1330, 30))

    # set up the backstory frame
    draw.rect(screen, (180, 180, 180), (700, 100, 500, 600))
    draw.rect(screen, (56, 56, 56), (700, 100, 500, 600), 5)
    screen.blit(backstory_txt, (860, 120))
    screen.blit(icon_pic, (890, 150))

    # blit the story paragraph
    screen.blit(story_txt1, (720, 270))
    screen.blit(story_txt2, (720, 320))
    screen.blit(story_txt3, (720, 370))
    screen.blit(story_txt4, (720, 420))
    screen.blit(story_txt5, (720, 470))
    screen.blit(story_txt6, (720, 520))
    screen.blit(story_txt7, (720, 570))
    screen.blit(story_txt8, (720, 620))

    # return to guide screen if this button is pressed
    if press and sign_rect.collidepoint(mx, my):
        return "guide"

    return "backstory"


def death_screen(screen, mx, my, press, chapter_num):
    "shows a red blood-ish stain after the player dies"
    # and gives the user the options to respawn or return to intro screen

    # draws the red stain
    draw.rect(red_surface, (255, 0, 0, 1), (0, 0, 1440, 720))
    screen.blit(red_surface, (0, 0))

    # set up the two buttons
    draw.rect(screen, (80, 80, 80), (570, 160, 300, 400))
    draw.rect(screen, (40, 40, 40), (570, 160, 300, 400), 10)
    screen.blit(dead_txt, (600, 180))
    draw.rect(screen, (140, 140, 140), respawn_rect)
    draw.rect(screen, (40, 40, 40), respawn_rect, 5)
    draw.rect(screen, (140, 140, 140), return_rect)
    draw.rect(screen, (40, 40, 40), return_rect, 5)
    screen.blit(respawn_txt, (625, 350))
    screen.blit(return_txt, (650, 470))

    # restart this chapter if the button is pressed
    if respawn_rect.collidepoint(mx, my):
        screen.blit(respawn_greentxt, (625, 350))
        if press:
            return chapter_num, True
    # return to intro screen if the button is pressed
    if return_rect.collidepoint(mx, my):
        screen.blit(return_greentxt, (650, 470))
        if press:
            return "intro", True

    return chapter_num, False
