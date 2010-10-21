#!/usr/bin/env python
# vi: set et:ts=4:sw=4
import pygame
import sys
import os
import dircache

       
def main(screen):
    bgimage = pygame.image.load("gfx/menu.png")
    main = ["New game", "Custom Level", "Level Editor", "Quit."]
    levels = dircache.listdir('levels/')
    buttons = main
    dircache.annotate('levels/', levels)
    button_height = 37
    menu_margin = 30

    offset = 0
    clevel = False
    edit = False
    update = True

    fgcolor = 255, 255, 255
    #bgcolor = 0, 0, 0

    menuhover = -1

    font = pygame.font.SysFont("Bitstream Vera Sans", 24)

    labels = []
    for button in buttons:
        labels.append(font.render(button, 1, fgcolor))

    while True:
        event = pygame.event.wait()
        if update:
            update = False
            labels = []
            if clevel:
                i = offset*8
                labels.append(font.render("Return to main menu", 1, fgcolor))
                labels.append(font.render("Previous page", 1, fgcolor))
                while i < (1+offset)*8:
                    if i < len(levels):
                        labels.append(font.render(levels[i], 1, fgcolor))
                    else:
                        labels.append(font.render("(empty)", 1, fgcolor))
                    i += 1
                labels.append(font.render("Next page", 1, fgcolor))
            else:
                for choices in main:
                    labels.append(font.render(choices, 1, fgcolor))

        if event.type == pygame.VIDEOEXPOSE:
            screen.blit(bgimage, (0,0))

            for i in range(len(labels)):
                screen.blit(labels[i], (menu_margin, i * button_height + menu_margin))
            if menuhover != -1:
                rect = labels[menuhover].get_rect()
                rect[0] += menu_margin - 4
                rect[1] += menu_margin + menuhover * button_height - 3
                rect[2] += 8
                rect[3] += 6
                pygame.draw.rect(screen, (255,0,0), rect, 3)

            pygame.display.update()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(labels)):
                rect = labels[i].get_rect()
                if (event.pos[0] < rect[2] + menu_margin and event.pos[0] > menu_margin and event.pos[1] > menu_margin + i*button_height and event.pos[1] < menu_margin + (i+1)*button_height):
                    if clevel:
                        if i == 0:
                            clevel = False
                            update = True
                        elif i == 1:
                            if offset != 0:
                                offset -= 1
                                update = True
                        elif i == 10:
                            update = True
                            offset += 1
                        else:
                            if i+offset*6 - 2 < len(levels):
                                if "/" in levels[offset*6+i-2]:
                                    returnlist = []
                                    for level in dircache.listdir('levels/' + levels[offset*6+i-2]):
                                        returnlist.append("levels/" + levels[offset*6+i-2] + level)
                                else:
                                    returnlist = ["levels/" + levels[offset*6+i-2]]
                                return edit, returnlist
                    else:
                        if i == 0:
                            return False, dircache.listdir("levels/campaign/")
                        elif i == 1:
                            clevel = True
                            edit = False
                            update = True
                        elif i == 2:
                            edit = True
                            clevel = True
                            update = True
                        elif i == 3:
                            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            menuhover = -1
            for i in range(len(labels)):
                rect = labels[i].get_rect()
                if (event.pos[0] < rect[2] + menu_margin and event.pos[0] > menu_margin and event.pos[1] > menu_margin + i*button_height and event.pos[1] < menu_margin + (i+1)*button_height):
                    menuhover = i
if (__name__ == '__main__'):
    import os
    import sys
    import pygame
    pygame.init()
    window_width = 640
    window_height = 480
    screen = pygame.display.set_mode((window_width, window_height))
    main(screen)
