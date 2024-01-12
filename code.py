#!/usr/bin/env python3
#
# Created by: Noah Smith
# Created on: January 8th, 2024
# This program is the "Space Aliens" program on the PyBadge

import stage
import ugame

import constants


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]

    # render all sprites (background once per game scene)
    game.render_block()

    # repeat forever, game loop
    while True:
        
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
            
        # Update game logic
 
        # Redraw Sprites
        game.render_sprites([ship])
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()