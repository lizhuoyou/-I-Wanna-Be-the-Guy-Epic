# enemy.py
# this file stores functions for pro's enemies who kill pro.
# most of the following enemies have sound effects but not blade/movable blade.

# import library for enemy functions
from pygame import *
from random import randint
import math
import tool


def minion(surface, pic, horizontal_range, current_x, height, minion_dir, proX, proY, pro_alive, minionLive, poleSet,
           ripPic, minion_sound):
    """it draws a minion walking back and forth and it kill pro when they touch. horizontal_range indicates the range
    the minion can go. current_x is the minion's current x value. minion_dir is the minion's motion direction. pro_alive
    indicates if the pro is alive. minionLive indicates if the minion is still alive. poleSet is the set that contains
    poles that can kill the minion.After death, minion will reborn in about 10 seconds. ripPic is a grave picture
    indicates death. a minion's size is 60 by 50."""
    if minionLive > 0:
        min_x, max_x = horizontal_range
        # change current_x to make a minion move
        if minion_dir == "right":
            if current_x + 62 < max_x:  # check if minion gets out of its range; if so, changes direction.
                current_x += 2
            else:
                current_x -= 2
                minion_dir = 'left'
        else:  # move left
            if current_x - 2 > min_x:
                current_x -= 2
            else:
                current_x += 2
                minion_dir = 'right'

        # check if hitting pro
        if math.hypot(current_x - proX - 20, height - proY - 25) < 25:
            pro_alive = False

        # draw minion
        if minion_dir == 'right':
            surface.blit(pic, (current_x, height))
        else:
            surface.blit(transform.flip(pic, True, False), (current_x, height))

        # check if it is killed by pole
        if poleSet != set():
            for n in poleSet:
                x, y, x_change = n
                if (current_x < x + 25 < current_x + 60 or current_x < x + 75 < current_x + 60) and (height < y + 25 <
                                                                                                     height + 50 or height < y + 75 < height + 50):  # check if pole collides minion
                    minionLive -= 180  # kills minion
                    minion_sound.play()  # when minion is killed it will make a sound
                    poleSet.remove(n)  # remove the pole since it made a damage
                    break
    else:
        surface.blit(ripPic, (current_x, height))
        minionLive += 1  # when minion's live is accumulated back to 1, minion is reborn

    return current_x, minion_dir, pro_alive, minionLive, poleSet


def superMinion(surface, pic, horizontal_range, current_x, height, minion_dir, proX, proY, pro_alive, superLive,
                poleSet, ripPic, superminion_sounds):
    """it is similar to minion; however, you need to attack it 10 times to kill it. superMinion's initial life length is 10"""
    if superLive >= 1:
        min_x, max_x = horizontal_range
        # change current_x to make a minion move
        if minion_dir == "right":  # check if minion gets out of its range; if so, changes direction.
            if current_x + 62 < max_x:
                current_x += 2
            else:
                current_x -= 2
                minion_dir = 'left'
        else:  # move left
            if current_x - 2 > min_x:
                current_x -= 2
            else:
                current_x += 2
                minion_dir = 'right'

        # check if hitting pro
        if math.hypot(current_x - proX - 20, height - proY - 25) < 25:
            pro_alive = False

        # draw minion
        if minion_dir == 'right':
            surface.blit(pic, (current_x, height))
        else:
            surface.blit(transform.flip(pic, True, False), (current_x, height))

        # check if is attacked by pole
        if poleSet != set():
            for n in poleSet:
                x, y, x_change = n
                if (current_x < x + 25 < current_x + 60 or current_x < x + 75 < current_x + 60) and \
                        (height < y + 25 < height + 50 or height < y + 75 < height + 50):  # check if pole collides it
                    superLive -= 1  # be damaged by the pole
                    poleSet.remove(n)  # remove the pole since it made a damage

                    if superLive > 0:       # play sound when he's damaged
                        superminion_sounds[randint(0, 2)].play()
                    else:                   # play a special sound when he is dead
                        superminion_sounds[3].play()

                    break

    else:
        surface.blit(ripPic, (current_x, height))
        superLive += 0.01
        if superLive >= 1:
            superLive = 10  # when minion's live is accumulated back to 1, minion is reborn with 10 blood

    return current_x, minion_dir, pro_alive, superLive, poleSet


def MrBanana(surface, MrBananaPics, BananaPic, BXY, BananaXY, BananaXYchange,
             proX, proY, MrBananaLive, pro_alive, firing, poleSet, banana_sounds):
    """it is an enemy who attacks pro by throwing bananas or kill pro when they collide together.MrBananaLive is how
    much blood he has."""
    MrBX, MrBY = BXY
    if MrBananaLive > 0:
        x1, x2 = MrBX - 240, MrBX + 360  # x1 and x2 defines MrBanana's x-detecting range
        y1, y2 = MrBY - 240, MrBY + 360  # y1 and y2 defines MrBanana's y-detecting range
        bananaX, bananaY = BananaXY
        if (x1 < proX + 50 < x2 or x1 < proX < x2) and (y1 < proY + 50 < y2 or y1 < proY < y2):  # check if pro is in
            # detecting range
            # draw a translucent circle behind MrBanana to show his attacking range.
            MrBanana_energy = Surface((120, 120), SRCALPHA)
            draw.circle(MrBanana_energy, (255, 225, 0, 200), (60, 60), 60)
            draw.circle(MrBanana_energy, (255, 102, 0, 200), (60, 60), 45)
            surface.blit(MrBanana_energy, (MrBX, MrBY))

            surface.blit(MrBananaPics[1], (MrBX, MrBY))

            if math.hypot(MrBX - proX + 10, MrBY - proY + 10) < 80:  # kills pro when they collide
                pro_alive = False

            elif not firing:  # make sure there is only one flying banana on the screen
                bananaX = MrBX + 35  # reset banana's x/y values
                bananaY = MrBY + 35

                distance = math.hypot(MrBX - proX + 10, MrBY - proY + 10)  # use the distance between pro and
                x_distance = MrBX - proX + 10  # MrBanana to find the banana's x/y
                y_distance = MrBY - proY + 10  # change
                BananaXYchange = -round(10 * x_distance / distance), -round(
                    10 * y_distance / distance)  # ball moves 10 units/update. since using the vector from pro
                # to MrBanana and banana goes from MrBanana to pro, we use negative value so banana flies to pro

                banana_sounds[randint(0, 1)].play()  # play a sound when he shoots a new banana
                firing = True
        else:
            surface.blit(MrBananaPics[0], (MrBX, MrBY))  # another appearance for when pro is farther away.

        if firing:  # MrBanana's attacking banana
            # change banana's x/y to make it fly to pro's position when the banana starts flying
            xChange, yChange = BananaXYchange
            bananaX += xChange
            bananaY += yChange
            BananaXY = bananaX, bananaY
            BananaPic = tool.rotate90(BananaPic)
            surface.blit(BananaPic, BananaXY)

            if math.hypot(bananaX - proX - 25,  # check if pro is attacked by the banana by finding the distance
                          bananaY - proY - 25) < 50:  # between their centers
                pro_alive = False

            if bananaX > 1440 or bananaX < 0 or bananaY < 0 or bananaY > 720:  # check if banana is out screen.
                firing = False

        # check if MrBanana is attacked by pro's poles
        if poleSet != set():
            for n in poleSet:
                x, y, x_change = n
                if (MrBX < x + 25 < MrBX + 120 or MrBX < x + 75 < MrBX + 120) and \
                        (MrBY < y + 25 < MrBY + 120 or MrBY < y + 75 < MrBY + 120):  # check if pole collides MrBanana
                    MrBananaLive -= 1
                    if MrBananaLive > 0:    # play sound when he's damaged
                        banana_sounds[2].play()
                    else:                   # play a special sound when he is dead
                        banana_sounds[3].play()
                    poleSet.remove(n)  # remove the pole since it made a damage
                    break

    else:  # after death MrBanana becomes a rotating banana which kills Pro when they collide
        if math.hypot(MrBX - proX + 10, MrBY - proY + 10) < 80:  # kills pro when they collide
            pro_alive = False

        BananaPic = tool.rotate90(BananaPic)
        surface.blit(transform.scale(BananaPic, (120, 120)), (MrBX, MrBY))

    return BananaPic, BananaXY, BananaXYchange, MrBananaLive, pro_alive, firing, poleSet


def MrFFF(surface, FFFPics, fireBallPic, FXY, upBallXY, downBallXY, upXYchange, downXYchange,
          proX, proY, MrFFFLive, pro_alive, upFiring, downFiring, poleSet, fff_sounds):
    """it is an enemy who attacks pro by throwing fireballs or kill pro when they collide together.MrBananaLive is how
    much blood he has. this is similar to MrBanana. however, MrFFF shoots 2 fireballs simultaneously and has 9 bloods"""
    FFFX, FFFY = FXY
    if MrFFFLive > 0:
        x1, x2 = FFFX - 240, FFFX + 360  # x1 and x2 defines MrFFF's x-detecting range
        y1, y2 = FFFY - 240, FFFY + 360  # y1 and y2 defines MrFFF's y-detecting range
        upBallX, upBallY = upBallXY
        downBallX, downBallY = downBallXY
        if (x1 < proX + 50 < x2 or x1 < proX < x2) and (y1 < proY + 50 < y2 or y1 < proY < y2):  # check if pro is in
            # detecting range
            # draw a translucent circle behind MrBanana to show his attacking range.
            FFF_energy = Surface((120, 120), SRCALPHA)
            draw.circle(FFF_energy, (255, 26, 26, 200), (60, 60), 60)
            draw.circle(FFF_energy, (153, 0, 0, 200), (60, 60), 45)
            surface.blit(FFF_energy, (FFFX, FFFY))

            surface.blit(FFFPics[1], (FFFX, FFFY))

            if math.hypot(FFFX - proX + 10, FFFY - proY + 10) < 80:  # kills pro when they collide
                pro_alive = False
            elif not upFiring and not downFiring:  # make sure there are only 1 pair(or 1 from the pair) fireballs on
                # the screen
                # reset banana's x/y values
                upBallX = FFFX + 35
                upBallY = FFFY + 35
                downBallX = FFFX + 35
                downBallY = FFFY + 35

                distance = math.hypot(FFFX - proX + 10, FFFY - proY + 10)  # use the distance between pro and
                x_distance = FFFX - proX + 10  # MrBanana to find the banana's x/y
                y_distance = FFFY - proY + 10  # change
                upXYchange = -round(10 * x_distance / distance), -round(
                    7 * y_distance / distance)  # 2 firs balls go towards pro
                downXYchange = -round(7 * x_distance / distance), -round(
                    10 * y_distance / distance)  # but not exactly at pro's position

                fff_sounds[randint(0, 1)].play()  # play a sound when he shoots a pair of fireballs
                upFiring = True
                downFiring = True
        else:
            surface.blit(FFFPics[0], (FFFX, FFFY))  # another appearance for when pro is farther away.

        if upFiring or downFiring:
            fireBallPic = tool.rotate90(fireBallPic)

        # MrFFF's attacting fireballs
        # checking two fireballs respectively.
        if upFiring:
            xChange, yChange = upXYchange
            upBallX += xChange  # reset fireball's x/y values
            upBallY += yChange
            upBallXY = upBallX, upBallY
            surface.blit(fireBallPic, upBallXY)

            if math.hypot(upBallX - proX - 25, upBallY - proY - 25) < 50:  # check if pro is attacked by fireball by
                pro_alive = False  # finding the distance between their centers

            if upBallX > 1440 or upBallX < 0 or upBallY < 0 or upBallY > 720:  # check if fireball is out screen.
                upFiring = False

        # same as upFiring
        if downFiring:
            xChange, yChange = downXYchange
            downBallX += xChange
            downBallY += yChange
            downBallXY = downBallX, downBallY
            surface.blit(fireBallPic, downBallXY)

            if math.hypot(downBallX - proX - 25,
                          downBallY - proY - 25) < 50:
                pro_alive = False

            if downBallX > 1440 or downBallX < 0 or downBallY < 0 or downBallY > 720:
                downFiring = False

        # check if it is damaged by pole
        if poleSet != set():
            for n in poleSet:
                x, y, x_change = n
                if (FFFX < x + 25 < FFFX + 120 or FFFX < x + 75 < FFFX + 120) \
                        and (FFFY < y + 25 < FFFY + 120 or FFFY < y + 75 < FFFY + 120):  # check if pole collides MrFFF
                    MrFFFLive -= 1
                    if MrFFFLive > 0:
                        fff_sounds[2].play()  # play sound when he's damaged
                    else:
                        fff_sounds[3].play()  # play a special sound when he is dead

                    poleSet.remove(n)  # remove the pole since it made a damage
                    break

    else:  # after death MrFFF becomes a rotating fireball which kills Pro when they collide
        if math.hypot(FFFX - proX + 10, FFFY - proY + 10) < 80:  # kills pro when they collide
            pro_alive = False

        fireBallPic = tool.rotate90(fireBallPic)
        surface.blit(transform.scale(fireBallPic, (120, 120)), (FFFX, FFFY))

    return fireBallPic, upBallXY, downBallXY, upXYchange, downXYchange, MrFFFLive, pro_alive, upFiring, downFiring, poleSet


def blade(surface, bladePic, bladeX, bladeY, proX, proY, proLive):
    """this is a stationary blade which rotates and kills Pro when they collide. it can't be broke"""
    nBladePic = tool.rotate90(bladePic)
    surface.blit(nBladePic, (bladeX, bladeY))

    if math.hypot(bladeX - proX, bladeY - proY) < 50:  # kills pro when they collide
        proLive = False

    return nBladePic, proLive


def movable_blade(surface, bladePic, bladeX, bladeY, proX, proY, proLive, speed, direction, start_range, end_range):
    """this is a movable blade that can move vertically and horizontally at any speed and range. it kills pro when they
    collide"""
    # call blade function to draw blade and return if pro is killed.
    pic, pro_alive = blade(surface, bladePic, bladeX, bladeY, proX, proY, proLive)

    # detecting movable_blade's direction and then change its x/y values to make it move
    if direction == "up":
        if start_range < bladeY < end_range:  # check if blade should change direction
            bladeY -= speed
        else:
            bladeY += speed
            direction = "down"

    elif direction == "down":
        if start_range < bladeY < end_range:  # check if blade should change direction
            bladeY += speed
        else:
            bladeY -= speed
            direction = "up"

    elif direction == "left":
        if start_range < bladeX < end_range:  # check if blade should change direction
            bladeX -= speed
        else:
            bladeX += speed
            direction = "right"

    elif direction == "right":
        if start_range < bladeX < end_range:  # check if blade should change direction
            bladeX += speed
        else:
            bladeX -= speed
            direction = "left"

    return pic, pro_alive, bladeX, bladeY, direction


def piranhaFlower(surface, potPic, flowerPic, potXY, flowerXY, proX, proY, piranhaMode, pro_alive, flower_sound):
    """it is a piranha flower which kills pro by collide him. The vat is safe and it contains the flower.
    piranhaMode indicates what stage the flower is at:hiding, show the flower, ready to fly, flyingUp/down. Also, if pro
    is far above it, the flower will fly when pro is right above it"""

    # unpack pot and flower's x/y values for later use.
    potX, potY = potXY
    flowerX, flowerY = flowerXY

    # draw piranhaFlower and calculate damages based on its stage.
    if piranhaMode == 0:  # hiding
        if potX < proX + 70 < potX + 60 or potX < proX + 30 < potX + 60:  # check if pro's x value enter its range.
            if potY - 120 < proY + 80 < potY + 60:  # check if pro is above it
                piranhaMode = 1  # change stage
                surface.blit(flowerPic, (flowerX, flowerY))
                flower_sound.play()  # made sound to indicate showing flower

            if potY - 20 < proY + 80 < potY + 60:  # detecting if pro is close enough to be devoured by the flower.
                pro_alive = False
        surface.blit(potPic, (potX, potY))

    elif piranhaMode == 1:  # show the flower
        surface.blit(flowerPic, (flowerX, flowerY))
        surface.blit(potPic, (potX, potY))

        if proX + 30 > potX + 60 or proX + 70 < potX:  # enable flower to fly after pro is out of its range
            piranhaMode = 2

        elif potY - 20 < proY + 80 < potY + 60:  # detecting if pro is close enough to be devoured by the flower.
            pro_alive = False

    elif piranhaMode == 2:  # ready to fly
        surface.blit(flowerPic, (flowerX, flowerY))
        surface.blit(potPic, (potX, potY))

        if potX < proX + 70 < potX + 60 or potX < proX + 30 < potX + 60:  # check if pro is in its range again
            piranhaMode = 3

    elif piranhaMode == 3:  # flower flies up
        flowerY -= 12  # change flower's y value to make it move
        surface.blit(flowerPic, (flowerX, flowerY))
        surface.blit(potPic, (potX, potY))

        if flowerY < proY + 80 < flowerY + 60 or flowerY < proY + 25 < flowerY + 60:  # it kills pro if the flower
            if flowerX < proX + 70 < flowerX + 60 or potX < proX + 30 < flowerX + 60:  # collides him
                pro_alive = False

        if flowerY < -60:  # check if the flower is high enough to go back to the vat.
            piranhaMode = 4

    else:  # flower flies up
        flowerY += 12  # change flower's y value to make it move
        surface.blit(transform.flip(flowerPic, False, True), (flowerX, flowerY))
        surface.blit(potPic, (potX, potY))

        if flowerY < proY + 80 < flowerY + 60 or flowerY < proY + 25 < flowerY + 60:  # it kills pro if the flower
            if flowerX < proX + 70 < flowerX + 60 or potX < proX + 30 < flowerX + 60:  # collides him
                pro_alive = False

        if flowerY >= potY:  # when the flower drop back to the pot, the stage becomes back to 0(hiding)
            flowerY = potY - 30
            flower_sound.play()
            piranhaMode = 0

    # if pro is far above it, the flower will turn to mode 2 to fly.
    if proY < potY - 120 and (potX < proX + 70 < potX + 60 or potX < proX + 30 < potX + 60) and piranhaMode == 0:
        piranhaMode = 2

    return piranhaMode, (flowerX, flowerY), pro_alive


def face(surface, facepicLis, faceXY, proX, proY, letGO, happysad_sounds):
    """it is a face block which kills pro by calling TNT if letGo value is False. Normally it is a half-happy-half-sad
    face; if letGo is true and pro go through it, it will a smile face; if letGo is false and pro go through it it will
    be a sad face and explode"""
    surface.blit(facepicLis[0], faceXY)
    x, y = faceXY

    if (x < proX + 70 < x + 60 or x < proX + 30 < x + 60) \
            and (y < proY + 80 < y + 60 or y < proY + 25 < y + 60):  # check if pro collide the face.
        if letGO:
            surface.blit(facepicLis[1], faceXY)  # shows a happy face to indicate pro will be safe
            happysad_sounds[randint(0, 2)].play()
            return False  # it does not trigger the TNT
        else:
            surface.blit(facepicLis[2], faceXY)  # shows a sad face to indicate pro will be killed
            happysad_sounds[3].play()
            return True  # here it triggers the TNT
    return False


def TNT(surface, TNTblockPic, explosionPic, TNTxy, proX, proY):
    """it is a TNT block which will explode and kill pro when pro collides it."""
    surface.blit(TNTblockPic, TNTxy)
    x, y = TNTxy

    if (x < proX + 70 < x + 60 or x < proX + 30 < x + 60) \
            and (y < proY + 80 < y + 60 or y < proY + 25 < y + 60):  # check if pro collide the TNT.

        picSize = 60

        # expending the explosionPic to show the explosion is happening
        while picSize < 2000:
            surface.blit(transform.scale(explosionPic, (picSize, picSize)), (
                int(x + 30 - picSize / 2), int(y + 30 - picSize / 2)))  # keeps the explosion center the same
            picSize += 10
            display.update()
            time.wait(10)
        return False

    return True
