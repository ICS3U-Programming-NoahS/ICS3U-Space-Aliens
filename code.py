#!/usr/bin/env python3
#
# Created by: Noah Smith
# Created on: January 8th, 2024
# This program is the "Space Aliens" program on the PyBadge


import stage
import ugame
import time
import random
import supervisor



import constants

# Declare global variable to mute and unmute game
mute = False

def splash_scene():
    # this function is the splash scene


    # get intro sound ready
    intro_sound = open("fanfare_x.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(intro_sound)


    # an image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create a stage for the background to show up
    #   and set the frame rate to 60 FPS
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)


    # used this program to split the image into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white


    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white


    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white


    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)


    # set the layers of all sprites, items show up in order
    game.layers = [background]


    # render all sprites (background once per game scene)
    game.render_block()


    # repeat forever, game loop
    while True:
       # Wait for 2 seconds
       time.sleep(2.0)

       # go to menu scene
       menu_scene()


def menu_scene():
    # this function is the menu scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")


    # add text objects
    text = []
    text1 = stage.Text(width=50, height=40, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("SPACE ALIENS!")
    text.append(text1)


    text2 = stage.Text(width=30, height=20, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(5, 70)
    text2.text("B --> INSTRUCTIONS")
    text.append(text2)


    text3 = stage.Text(width=30, height=20, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(10, 110)
    text3.text("START --> PLAY")
    text.append(text3)


    # Set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)


    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)


    # set the layers of all sprites, items show up in order
    game.layers = text + [background]


    # render all sprites (background rendered once per game scene)
    game.render_block()


    # repeat forever, game loop
    while True:

        # Get user input
        keys = ugame.buttons.get_pressed()

        # if start is pressed, go to game scene
        if keys & ugame.K_START:
            game_scene()

        # if "B" is pressed, go to instructions scene
        if keys & ugame.K_X:
            instructions_scene()

        # Redraw Sprites
        game.tick() # wait until refresh rate finishes


def instructions_scene():
    # this function is the instructions scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")


    # add text objects
    text = []
    text1 = stage.Text(width=40, height=27, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("INSTRUCTIONS:")
    text.append(text1)


    text2 = stage.Text(width=20, height=10, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(3, 40)
    text2.text("Shoot the aliens to get points and save the universe!")
    text.append(text2)


    text3 = stage.Text(width=20, height=10, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(3, 70)
    text3.text("But don't let the    aliens get you, or you will lose!")
    text.append(text3)


    text4 = stage.Text(width=40, height=27, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text4.move(15, 110)
    text4.text("PRESS B TO RETURN")
    text.append(text4)


    # Set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)


    # Create a stage for the background to show up on
    #   and set the frame rate to  60fps
    game = stage.Stage(ugame.display, constants.FPS)


    # set the layers of all sprites, items show up in order
    game.layers = text + [background]


    # render all sprites (background once per game scene)
    game.render_block()


    # repeat forever, game loop
    while True:

        # Get user input
        keys = ugame.buttons.get_pressed()


        # if "B" is pressed, go back to menu scene
        if keys & ugame.K_X:
            menu_scene()

        # Redraw Sprites
        game.tick() # wait until refresh rate finishes


def game_scene():
    # this function is the main game scene

    # for score
    score = 0

    # Display score
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    def show_alien():
        # This function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")


    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]


    # get sounds ready
    pew_sound = open("phasers3.wav", 'rb')
    boom_sound = open("cannon_x.wav", 'rb')
    lose_sound = open("buzzer_x.wav", 'rb')
    win_sound = open("fanfare3.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    # Set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)


    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))


    # Create list of aliens to shoot at
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    # Place one alien on the screen
    show_alien()


    # Create list of lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)


    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)


    # set the layers of all sprites, items show up in order
    game.layers = [score_text] + aliens + lasers + [ship] + [background]


    # render all sprites (background once per game scene)
    game.render_block()


    # repeat forever, game loop
    while True:

        # Get user input
        keys = ugame.buttons.get_pressed()


        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
              
        # call global variable to mute game sounds
        global mute

        # Game keys in the game scene
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            if mute:
                # If game is muted and select is pressed, unmute
                ugame.audio.mute(False)
                mute = False
            else:
                # If game is unmuted and select is pressed, mute
                ugame.audio.mute(True)
                mute = True

        # move the ship left and right 
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # Update game logic
        # Play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser, if we have enough power (have not used up all of the lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # each frame move the lasers, that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # each frame move the aliens down, that are on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)

                # If an alien has reached the bottom of the screen
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score = score - 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # each frame check if any of the lasers are touching any of the aliens
        for laser_number in range(len(lasers)):
          if lasers[laser_number].x > 0:
            for alien_number in range(len(aliens)):
              if aliens[alien_number].x > 0:
                if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                               lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                               aliens[alien_number].x + 1, aliens[alien_number].y, 
                               aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                    
                    # If you hit an alien with laser
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    sound.stop()
                    sound.play(boom_sound)
                    show_alien()
                    show_alien()
                    score = score + 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # each frame check if any of the aliens are touching the ship
        for alien_number in range(len(aliens)):
          if aliens[alien_number].x > 0:

            # if the player reaches 50 points, they win and go to the win scene
            if score > 3:
                sound.stop()
                sound.play(win_sound)
                time.sleep(3.0)
                win_scene(score)
            
            # Check if the alien hit the ship
            elif stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                             aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                            ship.x, ship.y,
                            ship.x + 15, ship.y + 15):

                # alien hit the ship, so go to the game over scene
                sound.stop()
                sound.play(lose_sound)
                time.sleep(3.0)
                game_over_scene(score)

        # Redraw Sprite list
        game.render_sprites(lasers + [ship] + aliens)
        game.tick() # wait until refresh rate finishes

def game_over_scene(final_score):
    # this function is the game over scene

    # Image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER!")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    # render the background and initial location of sprite list (once per scene)
    game.render_block()

    # repeat forever, game loop
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

         # the user presses select to start the game over
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick() # wait until refresh rate finishes


def win_scene(final_score):
    # this function is the win scene

    # Image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("YOU WIN!")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    # render the background and initial location of sprite list (once per scene)
    game.render_block()

    # repeat forever, game loop
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        # the user presses select to start the game over
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    splash_scene()