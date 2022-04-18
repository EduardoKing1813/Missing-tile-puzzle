from msilib.schema import Font
from platform import python_branch
import pygame
import os
import sys

from config import FPS, BLOCKS_WIDTH, BLOCKS_HEIGHT, RESIZED_IMAGE_PATH
from block import swap_blocks, generate_map
from tkinter import LEFT, RIGHT, filedialog
from enum import Enum
from PIL import Image


def select_file() -> str:
    user_imgpath = filedialog.askopenfilename()
    
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
        
    img = Image.open(user_imgpath)
    resized = img.resize((800, 600))
    resized.save(RESIZED_IMAGE_PATH)
    
       
    return RESIZED_IMAGE_PATH


def main():
    pygame.init()
    pygame.display.set_caption("Missing tile!")
   
    pygame.font.init()
    font = pygame.font.SysFont('New Times Roman', 72)
    win_text = font.render('Congrats, you won!', False, (102, 178, 255))
   
    IMAGE_PATH = select_file()
    
    image = pygame.image.load(IMAGE_PATH)
    image_rect = image.get_rect()
    screen = pygame.display.set_mode( (image_rect.width + BLOCKS_WIDTH - 1, image_rect.height + BLOCKS_HEIGHT - 1) )
    fps_clock = pygame.time.Clock()
    
    image = pygame.image.load(IMAGE_PATH)
    
    game_over = False
    
    game_map, solved_map = generate_map(screen, image)
    empty_cell_index = [0, 0]

    
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN and not game_over:
                
                if event.key == pygame.K_RIGHT:
                    if empty_cell_index[0] < BLOCKS_WIDTH - 1:
                        swap_blocks(game_map, (empty_cell_index[0], empty_cell_index[1]), (empty_cell_index[0]+1, empty_cell_index[1]) )
                        empty_cell_index[0] += 1     
                                   
                elif event.key == pygame.K_LEFT:
                    if empty_cell_index[0] > 0:
                        swap_blocks(game_map, (empty_cell_index[0], empty_cell_index[1]), (empty_cell_index[0]-1, empty_cell_index[1]) )
                        empty_cell_index[0] -= 1  
                            
                elif event.key == pygame.K_UP:
                    if empty_cell_index[1] > 0:
                        swap_blocks(game_map, (empty_cell_index[0], empty_cell_index[1]), (empty_cell_index[0], empty_cell_index[1]-1) )
                        empty_cell_index[1] -= 1 
                          
                elif event.key == pygame.K_DOWN:
                    if empty_cell_index[1] < BLOCKS_HEIGHT - 1:
                        swap_blocks(game_map, (empty_cell_index[0], empty_cell_index[1]), (empty_cell_index[0], empty_cell_index[1]+1) )
                        empty_cell_index[1] += 1   

        
        
        game_over = (game_map == solved_map)
            
        for row in game_map:
            for block in row:
                block.draw()
                
            
        if game_over:
            screen.blit(win_text, (175,300))
        
        
        pygame.display.flip()
        fps_clock.tick(FPS)




if __name__ == '__main__':
    main()