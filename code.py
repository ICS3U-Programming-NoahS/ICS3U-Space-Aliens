#!/usr/bin/env python3
#
# Created by: Noah Smith
# Created on: January 8th, 2024
# This program is the "Space Aliens" program on the PyBadge

import stage
import ugame


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp]")

    # Set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order
    game.layers = [background]

    # render all sprites (background once per game scene)
    game.render_block()

    # repeat forever, game loop
    while True:
        
        # Get user input

        # Update game logic

        # Redraw Sprites
        game.render_Sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()