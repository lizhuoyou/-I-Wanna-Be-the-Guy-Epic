# tool.py
# this file stores the functions for loading multiple pictures, rotate pictures, draw blocks on the screen, background
# music, save/load user account information, and some sub functions.

from pygame import *


def loadPics(pic_names, leng, heigh):
    """It is used to load a bunch of pictures by getting the input of the pictures' names and size"""
    pic_list = []

    for name in pic_names:      # add pictures to the list based on the pictures' name
        pic_list.append(transform.scale(image.load(name), (leng, heigh)))

    return pic_list


def rotate90(picture):
    """it rotates a picture 90 degreess"""
    return transform.rotate(picture, 90)


def make_ground(surface, twoDL, pics):
    """Tt requires a surface and a 2 two-dimension list to draw the ground(block) pictures.pics stores a picture list
    consisted of various types of blocks"""
    for x in range(12):  # find the x/y index of each block as their locations
        for y in range(24):
            if twoDL[x][y] == 1:  # based on the specific value of the key of the 2d list, select different block
                surface.blit(pics[0], (60 * y, 60 * x))  # pictures
            elif twoDL[x][y] == 2:
                surface.blit(pics[1], (60 * y, 60 * x))
            elif twoDL[x][y] == 3:
                surface.blit(pics[2], (60 * y, 60 * x))
            elif twoDL[x][y] == 4:
                surface.blit(pics[3], (60 * y, 60 * x))
            elif twoDL[x][y] == 5:
                surface.blit(pics[4], (60 * y, 60 * x))
            elif twoDL[x][y] == 6:
                surface.blit(pics[5], (60 * y, 60 * x))
            elif twoDL[x][y] == 7:
                surface.blit(pics[6], (60 * y, 60 * x))
            elif twoDL[x][y] == 8:
                surface.blit(pics[7], (60 * y, 60 * x))
            elif twoDL[x][y] == 9:
                surface.blit(pics[8], (60 * y, 60 * x))
            elif twoDL[x][y] == 10:
                surface.blit(pics[9], (60 * y, 60 * x))
            elif twoDL[x][y] == 11:
                surface.blit(pics[10], (60 * y, 60 * x))


def no_man_land(surface, pic, nmlX1, nmlX2, nmlY, moveSpeed):
    """it draws a moving picture to show the ground which pro couldn't touch. nm1X1 is the first x value to be used to
     draw the picture. the pic goes right"""
    surface.blit(pic, (nmlX1, nmlY))
    surface.blit(pic, (nmlX2, nmlY))

    if nmlX1 + moveSpeed < 1440:  # check if nmlx is too close to left
        nmlX1 += moveSpeed
    else:
        nmlX1 = -1440  # if so, rest  the nmlx

    if nmlX2 + moveSpeed < 1440:  # check if nml is too close to left
        nmlX2 += moveSpeed
    else:
        nmlX2 = -1440

    return nmlX1, nmlX2  # if so, rest  the nmlx


def background_music(playIt, musicName):
    "it is to play background music"
    if playIt:
        mixer.music.stop()  # reset music
        mixer.music.load(musicName)
        mixer.music.play(-1)  # play the music forever.


def saveFile(surface, chapter, deathTimes, userName):
    '''it adds a new user account or update the current using account.'''
    userFile = open("userData.txt").read().strip().split('\n')  # read the file for checking and editing
    comicFont = font.SysFont("Comic Sans MS", 28)  # preserve the font for later use

    if userName == '':  # when user name is '', that means he/she is new.
        name = getName(surface)
        if name != '':
            for line in userName:  # check if the userName had been used.
                n, p, c, d = line.split('\t')  # name, passWord, chapter, deathTimes
                if n == name:
                    txtPic = comicFont.render("Sorry,the user name has existed.", True, (204, 255, 51))  # add reminder
                    surface.blit(txtPic, (300, 266))
                    display.update()
                    time.wait(1000)
                    break
            else:
                file = open("userData.txt", 'a')
                passWord = getPassword(surface)

                while passWord == '':  # ensure the password is valid
                    txtPic = comicFont.render("There is no password!", True, (204, 255, 51))  # reminds user the invalid
                    surface.blit(txtPic, (300, 266))  # password
                    display.update()
                    time.wait(1000)

                    passWord = getPassword(surface)  # ask the password again.

                file.write(name + '\t' + passWord + '\t' + str(chapter) + '\t' + str(deathTimes) + '\n')
                file.close()

    else:
        file = open("userData.txt", 'w')  # rewrite the file to change the info
        txtPic = comicFont.render("It is saved!", True, (204, 255, 51))  # add a notification
        surface.blit(txtPic, (300, 266))
        display.update()
        time.wait(1000)

        for line in userFile:
            n, p, c, d = line.split('\t')  # name, passWord, chapter, deathTimes
            if n == userName and chapter > int(c):  # change maximum chapter and death times
                file.write(n + '\t' + p + '\t' + str(chapter) + '\t' + str(deathTimes) + '\n')

            elif n == userName and deathTimes >= int(c):        # only change death times as max_chapter isn't changed
                file.write(n + '\t' + p + '\t' + c + '\t' + str(deathTimes) + '\n')

            else:  # write other users' data to the updated file as well
                file.write(n + '\t' + p + '\t' + c + '\t' + d + '\n')
        file.close()


def loadFile(surface, userMaxChap, deaths, oldName):
    """attract a saved user's account information into the game to resume the game"""
    userFile = open("userData.txt").read().strip().split('\n')
    userName = getName(surface)
    comicFont = font.SysFont("Comic Sans MS", 28)
    for line in userFile:  # check if the userName had been used
        n, p, c, d = line.split('\t')  # name, passWord, chapter, deathTimes
        if n == userName:
            password = getPassword(surface)
            if p == password:
                return int(c), int(d), userName  # return user's max chapter and death times.
            else:
                txtPic = comicFont.render("Sorry,I'm afraid that the password is wrong.",
                                          True, (204, 255, 51))  # tells the user the password is wrong
                surface.blit(txtPic, (300, 266))
                display.update()
                time.wait(1000)
                return userMaxChap, deaths, oldName
    else:
        txtPic = comicFont.render("Sorry,I'm afraid that the user name doesn't exist.",
                                  True, (204, 255, 51))  # tells the user name does not exist
        surface.blit(txtPic, (300, 266))
        display.update()
        time.wait(1000)

        return userMaxChap, deaths, oldName


getNameBack = transform.scale(image.load("pic/getNameBackground.jpg"), (800, 30))
getPassBack = transform.scale(image.load("pic/getPassBackground.jpg"), (800, 30))


def getName(surface):
    '''it gets the user name by asking the user to type it and return a string of the name'''
    ans = ""

    arialFont = font.SysFont("Arial Black", 21)  # set up font for input text
    back = surface.copy()
    textArea = Rect(300, 300, 800, 30)

    # instructs user to input name
    surface.blit(getNameBack, (300, 270))
    draw.rect(surface, (211, 211, 211), (300, 270, 800, 30), 2)
    comicFont = font.SysFont("Comic Sans MS", 28)
    txtPic = comicFont.render("What your name?(Press enter to continue)", True, (204, 255, 51))
    surface.blit(txtPic, (300, 266))

    cursorShow = 0  # used to indicate if to show cursor
    myclock = time.Clock()
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""

            if e.type == KEYDOWN:  # checking which key user has pressed.
                if e.key == K_BACKSPACE:  # delete the last letter
                    if len(ans) > 0:
                        ans = ans[:-1]

                elif e.key == K_KP_ENTER or e.key == K_RETURN:  # finish typing
                    typing = False

                elif e.key < 256:  # get typed letter
                    ans += e.unicode

        txtPic = arialFont.render(ans, True, (0, 0, 0))  # show the input on the screen
        draw.rect(surface, (220, 255, 220), textArea)
        draw.rect(surface, (211, 211, 211), textArea, 2)
        surface.blit(txtPic, (textArea.x + 3, textArea.y + 2))

        if cursorShow // 50 % 2 == 1:  # show the cursor periodically
            cx = textArea.x + txtPic.get_width() + 3
            cy = textArea.y + 3
            draw.rect(surface, (255, 0, 0), (cx, cy, 2, textArea.height - 6))
        cursorShow += 1

        myclock.tick(100)
        display.flip()

    surface.blit(back, (0, 0))  # redraw the screen before asking name

    return ans


def getPassword(surface):
    '''it gets the password for the user and return a string of the name'''

    ans = ""

    arialFont = font.SysFont("Arial Black", 21)  # set up font for input text
    back = surface.copy()
    textArea = Rect(300, 300, 800, 30)

    # instructs user to input name
    surface.blit(getPassBack, (300, 270))
    draw.rect(surface, (211, 211, 211), (300, 270, 800, 30), 2)
    comicFont = font.SysFont("Comic Sans MS", 28)
    txtPic = comicFont.render("What is your password?(press enter to finish)", True, (204, 255, 51))
    surface.blit(txtPic, (300, 266))

    cursorShow = 0  # used to indicate if to show cursor
    myclock = time.Clock()
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""

            if e.type == KEYDOWN:  # checking which key user has pressed.
                if e.key == K_BACKSPACE:  # delete the last letter
                    if len(ans) > 0:
                        ans = ans[:-1]

                elif e.key == K_KP_ENTER or e.key == K_RETURN:  # finish typing
                    typing = False

                elif e.key < 256:  # get typed letter
                    ans += e.unicode

        txtPic = arialFont.render(ans, True, (0, 0, 0))  # show the input on the screen
        draw.rect(surface, (220, 255, 220), textArea)
        draw.rect(surface, (211, 211, 211), textArea, 2)
        surface.blit(txtPic, (textArea.x + 3, textArea.y + 2))

        if cursorShow // 50 % 2 == 1:  # show the cursor periodically
            cx = textArea.x + txtPic.get_width() + 3
            cy = textArea.y + 3
            draw.rect(surface, (255, 0, 0), (cx, cy, 2, textArea.height - 6))
        cursorShow += 1

        myclock.tick(100)       # make the function go stationary and affluent
        display.flip()

    surface.blit(back, (0, 0))  # redraw the screen before asking name

    return ans
