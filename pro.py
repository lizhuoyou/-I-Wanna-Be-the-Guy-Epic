# pro.py
# this file is used to store the functions and pictures of Pro, the protagonist by whom the user controls.
# all the functions in this file is help to build up draw_pro function, which organize the calculations for user to
# control Pro to play the game and it also draws pro on the screen.

# import library for the pro functions
from pygame import *
import keyboard
import tool  # use the functions from our self-made tool function

# prepare pro graphics
# this library's keys are the types of motion. Its values are the lists containing pictures for one motion.
# here the mode is first we set a variable with list containing a list of names corresponding to picture files,
# then use tool.loadPics to the list consisted of pictures and put the list into the dictionary.
pro_graphics = {}

pro_walk = ["pic/pro/walk/walk_0.png",
            "pic/pro/walk/walk_1.png"]  # one is for standing, the other is for moving
pro_walk = tool.loadPics(pro_walk, 100, 100)
pro_graphics['pro_walk'] = pro_walk

pro_jump = ["pic/pro/jump/jump_0.png",
            "pic/pro/jump/jump_1.png"]  # one is for primary jump, the other is for double-jump
pro_jump = tool.loadPics(pro_jump, 100, 100)
pro_graphics['pro_jump'] = pro_jump

pro_fall = ["pic/pro/fall/fall_0.png",
            "pic/pro/fall/fall_1.png", ]  # one is for primary fall, the other is for faster-falling
pro_fall = tool.loadPics(pro_fall, 100, 100)
pro_graphics['pro_fall'] = pro_fall


def draw_pro(surface, x, y, acc, jumping, d_jump, pre_direction, ground_values, pressF, polePic, poleSet):
    """This function draws pro on the screen and returns pro's values. acc (acceleration) means the
    rate of going up/down. jumping is used to indicate if pro is jumping and d_jump is the value used for double-jump.
    pre_direction is pro's previous direction, which is for getting motion and pro's attack. ground_values is to
    calculate the region where pro can't go. pressF is pressing F key, for attacking. poleSet is the set storing pro's
    attacking values. This function uses pictures directly without calling parameter, which breaks black box but works
    efficiently."""
    walking = False  # indicate if pro is walking
    motion_direction = "none"  # indicate pro's direction

    # change pro's motion direction.
    if keyboard.is_pressed('left') and keyboard.is_pressed('right'):
        """ we want the character to change direction (motion_direction) when clicked the two arrows at once,
        so we use pre_direction to resolve it."""
        walking = True
        if pre_direction == 'left':  # if the last direction is left, the character will now move right
            motion_direction = 'right'
        else:  # vice versa
            motion_direction = 'left'
    elif keyboard.is_pressed('left'):
        walking = True
        motion_direction = 'left'
        pre_direction = 'left'
    elif keyboard.is_pressed('right'):
        walking = True
        motion_direction = 'right'
        pre_direction = 'right'

    # change pro's jumping value. Pro can double jump.
    if keyboard.is_pressed('space') and (
            d_jump == 0 or d_jump == 2):  # when d_jump = 1, space is pressed once without release; when d_jump = 2,
        jumping = True  # space is pressed and released so that pro can do the double-jump
        d_jump += 1
        acc = 40  # change acc value for going up
    elif not keyboard.is_pressed('space') and d_jump == 1:
        d_jump += 1  # enable the second jump

    # change pro's x/y values to make him move. The fist priority is jump, the second is falling, the third is walking
    # and the forth is standing still. This sequence makes pro's movement logical.
    falling, falling_acc = can_fall(x, y, acc, ground_values)  # checking if pro can fall and giving the falling acc
    if jumping:
        available, jump_acc = can_jump(x, y, acc, ground_values)  # checking if pro can fall and giving the jumping acc
        if available:
            x, y, acc = jump(x, y, jump_acc, motion_direction, ground_values)
        else:
            jumping = False

        if d_jump <= 2:  # it is used to get pro picture based on his motion
            proPic = get_pro_pic(pro_graphics, 'pro_jump', motion_direction, pre_direction, 0)
        else:
            proPic = get_pro_pic(pro_graphics, 'pro_jump',
                                 motion_direction, pre_direction, 1)

    elif falling:
        x, y, acc = fall(x, y, falling_acc, motion_direction, ground_values)

        if acc > -30:  # it is used to get pro picture based on his motion. When he is falling fast it shows the
            proPic = get_pro_pic(pro_graphics, 'pro_fall',  # second falling pic.
                                 motion_direction, pre_direction, 0)
        else:
            proPic = get_pro_pic(pro_graphics, 'pro_fall', motion_direction, pre_direction, 1)

    elif walking:
        x = walk(x, y, motion_direction, ground_values)
        d_jump = 0  # reset the jumping value
        acc = -5  # reset the falling value
        proPic = get_pro_pic(pro_graphics, 'pro_walk', motion_direction, pre_direction, 0)

    else:  # this is for standing
        proPic = get_pro_pic(pro_graphics, 'pro_walk', motion_direction, pre_direction, 1)
        d_jump = 0  # reset the jumping value
        acc = -5  # reset the falling value

    # calculates pro's attack
    if pressF and len(poleSet) < 3:  # maximum 3 poles at the same time
        poleSet = pro_attack(x, y, poleSet, pre_direction)

    # draw pro on the screen.
    surface.blit(proPic, (x, y))

    # draw pro's attacking poles
    if poleSet != set():  # checks if any pole exist
        polePic, poleSet = draw_poles(surface, polePic, poleSet)

    return x, y, acc, jumping, d_jump, pre_direction, polePic, poleSet


def walk(x, y, motion_direction, ground_values):
    """use pro's existed x,y values and acceleration rate to return pro's new x,y values after walking"""
    # move left
    if motion_direction == "left":
        if in_map(x - 10, y, ground_values):  # checks if pro can walk.
            return x - 10
        else:
            return x
    # move right
    else:
        if in_map(x + 10, y, ground_values):
            return x + 10
        else:
            return x


def can_jump(x, y, acc, ground_values):
    """this function tests if pro can jump and return jumping acceleration value"""
    if in_map(x, y - acc, ground_values):  # checks if pro movement is applicable
        return True, acc
    elif acc < 0:  # it is for the case that acceleration is too large  (going up)
        for distance in range(acc, 0):
            if in_map(x, y - distance, ground_values):
                return True, distance
    elif acc > 0:  # it is for the case that acceleration is too large  (going down)
        possible_dis = [x for x in range(0, acc)]  # checks if any smaller change of distance is applicable
        distances = possible_dis[::-1]
        for distance in distances:
            if in_map(x, y - distance, ground_values):
                return True, distance

    return False, 0


def jump(x, y, acc, direction, ground_values):
    """use pro's x,y values and acceleration rate to return pro's new x,y after falling.When pro's jumping, his
    x/y change will be relatively smaller"""
    # jump left
    if direction == "left":
        if in_map(x - 7, y - acc, ground_values):  # checks if pro can jump left
            return x - 7, y - acc, acc - 5
        else:
            return x, y - acc, acc - 5
    # jump right
    elif direction == "right":
        if in_map(x + 7, y - acc, ground_values):  # checks if pro can jump right
            return x + 7, y - acc, acc - 5
        else:
            return x, y - acc, acc - 5
    # jump straight
    else:
        return x, y - acc, acc - 5


def can_fall(x, y, acc, ground_values):
    """this tests if pro can fall down and give the falling acceleration value"""
    if in_map(x, y - acc, ground_values):  # checks if pro movement is applicable
        return True, acc
    elif acc < 0:  # this is for the case that acceleration is too large
        for distance in range(acc, 0):
            if in_map(x, y - distance, ground_values):  # checks if any smaller change of distance is applicable
                return True, distance

    return False, 0


def fall(x, y, acc, direction, ground_values):
    """use pro's x,y values and acceleration rate to return pro's new x,y after falling. When pro's falling, his
    x/y change will be relatively smaller"""
    # fall left
    if direction == "left":  # checks if pro can fall left
        if in_map(x - 7, y - acc, ground_values):
            return x - 7, y - acc, acc - 5
        elif in_map(x, y - acc, ground_values):
            return x, y - acc, acc - 5
    # fall right
    elif direction == "right":  # checks if pro can fall right
        if in_map(x + 7, y - acc, ground_values):
            return x + 7, y - acc, acc - 5
        elif in_map(x, y - acc, ground_values):
            return x, y - acc, acc - 5
    # fall straight
    else:
        return x, y - acc, acc - 5


def in_map(proX, proY, ground_values):
    """it is to check pro's movement is applicable by checking if he will get into blocks or out of the map. it take in
    environment value and the pro's x/y values and output boolean to indicate if pro's movement is applicable. Because
    pro's picture is not perfectly filled png, so we don't use the picture's size which is 100*100"""
    h_w_values = set()  # height-width values for the blocks
    for y in range(12):
        for x in range(24):
            if ground_values[y][x] != 0:
                h_w_values.add((60 * y, 60 * x))  # use ground_values to find h_w_values for blocks
    for n in h_w_values:
        y, x = n  # box's x,y value
        if x < proX + 70 < x + 60 or x < proX + 30 < x + 60:  # check if pro's next movement will get him into blocks
            if y < proY + 80 < y + 60 or y < proY + 25 < y + 60:
                return False

    if proY > 640:  # check if pro will touch the ground
        return False
    if proX > 1370 or proX < -30:  # check if pro will touch the left/right side.
        return False

    return True


def pro_attack(proX, proY, poleSet, direction):
    """it changes the pole set to accomplish an attack."""
    if direction == "right":  # attacks towards right
        poleSet.add((proX, proY, 200))  # a pole can travel far as 200 pixels.
    else:  # attacks towards left
        poleSet.add((proX, proY, -200))

    return poleSet


def draw_poles(surface, polePic, poleSet):
    """this function shows the pole and adapt poles' values by changing poleSet and change polePic.It returns rotated
    pole picture and new pole set"""
    new_set = set()
    polePic = tool.rotate90(polePic)

    for n in poleSet:  # changing pole set
        x, y, x_change = n  # a pole's x value, y value and the rest of x's distance to go.
        surface.blit(polePic, (x, y))
        if x_change > 0:  # a pole goes towards right
            x += 10  # change pole's x value
            x_change -= 10  # reduce the rest distance for x value's change
            new_set.add((x, y, x_change))
        elif x_change < 0:  # a pole goes towards left
            x -= 10
            x_change += 10
            new_set.add((x, y, x_change))

    return polePic, new_set


def get_pro_pic(pic_dict, pic_type, current_dir, pre_dir, pic_num):
    """this function is used to get the appearance for Pro,by using the picture's type and number and Pro's direction.
    pic_dict is picture dictionary storing pro's pictures. pic_type is a string telling the type of picture, is the key.
    pic_num indicates the specific picture being used, is the index for list that is the value of the dictionary."""
    if current_dir == 'right':
        return pic_dict[pic_type][pic_num]

    elif current_dir == 'left':
        return transform.flip(pic_dict[pic_type][pic_num], True, False)  # flip the picture when pro is moving left

    else:  # if pro currently doesn't have any direction then we use the pre-used direction for his direction
        if pre_dir == 'right':
            return pic_dict[pic_type][pic_num]
        elif pre_dir == 'left':
            return transform.flip(pic_dict[pic_type][pic_num], True, False)  # flip the picture when pro is moving left
