import math
import pygame
import random

from config import EMPTY_CELL_IMAGE_PATH, BLOCKS_WIDTH, BLOCKS_HEIGHT, SHUFFLE_RATE



def swap_blocks(game_map, block1_pos, block2_pos):
    block1_x, block1_y = block1_pos
    block2_x, block2_y = block2_pos
    
    block1 = game_map[block1_y][block1_x]
    block2 = game_map[block2_y][block2_x]
    
    game_map[block1_y][block1_x] = block2
    game_map[block2_y][block2_x] = block1
    
    Block.swap(block1, block2)
    
    
def generate_blocks(screen, image) -> list:
    image_rect = image.get_rect()
    size_x = math.floor(image_rect.width / BLOCKS_WIDTH)
    size_y = math.floor(image_rect.height / BLOCKS_HEIGHT)
    
    blocks_list = []
    

    for i in range(0, image_rect.height, size_y):
        for j in range(0, image_rect.width, size_x):
            
            if i == 0 and j == 0:
                cropped_image = pygame.Surface.subsurface(pygame.image.load(EMPTY_CELL_IMAGE_PATH) , (j, i, size_x, size_y) )
            else:
                cropped_image = pygame.Surface.subsurface(image, (j, i, size_x, size_y) )
                
            left_corner_pos = [j, i]
            
            if i > 0:
                left_corner_pos[1] += i / size_y
                    
            if j > 0:
                left_corner_pos[0] += j / size_x
                
            block = Block(screen, cropped_image, tuple(left_corner_pos))
            blocks_list.append(block)
    
    return blocks_list


def generate_map(screen, image) -> tuple:
    blocks_list = generate_blocks(screen, image)
    
    game_map = [ list() for _ in range(BLOCKS_HEIGHT) ]
    
    for i in range(BLOCKS_HEIGHT):
        for j in range(BLOCKS_WIDTH):
            game_map[i].append( blocks_list[i * BLOCKS_WIDTH + j] )
    
    #Saving solved state
    solved = game_map.copy()
    
    for i in range(len(game_map)):
        solved[i] = game_map[i].copy()
    
    #Shuffling blocks
    for _ in range(SHUFFLE_RATE):
        block1_x, block1_y = random.randint(0, BLOCKS_WIDTH - 1), random.randint(0, BLOCKS_HEIGHT - 1)
        block2_x, block2_y = random.randint(0, BLOCKS_WIDTH - 1), random.randint(0, BLOCKS_HEIGHT - 1)
        
        if block1_x == block1_y:
            block1_x = (block1_x + 1) % BLOCKS_WIDTH
        
        if block2_x == block2_y:
            block2_x = (block2_x + 1) % BLOCKS_WIDTH
        
        swap_blocks(game_map, (block1_x, block1_y), (block2_x, block2_y))
        
    
        
    return (game_map, solved)


class Block:
    def __init__(self, screen, image, left_corner_pos : tuple):
        self.screen = screen
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = left_corner_pos[0]
        self.rect.y = left_corner_pos[1] 
        
        self.swap = self._swap
        
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
        
    def _swap(self, other_block):
        self_coordinates = (self.rect.x, self.rect.y)
        
        self.rect.x = other_block.rect[0]
        self.rect.y = other_block.rect[1]
        
        other_block.rect.x = self_coordinates[0]
        other_block.rect.y = self_coordinates[1]
        
    
    def get_position(self) -> tuple:
        return (self.rect.x, self.rect.y)
        
        
    @staticmethod
    def swap(block1, block2):
        block1_coord = (block1.rect.x, block1.rect.y)
        
        block1.rect.x = block2.rect.x
        block1.rect.y = block2.rect.y
        
        block2.rect.x = block1_coord[0]
        block2.rect.y = block1_coord[1]