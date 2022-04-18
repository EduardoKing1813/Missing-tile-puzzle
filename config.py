#Difficulty of the game
DIFFICULTY = 1
#Possible options: 1-Easy, 2-Normal, 3-HARD


#-------------------------------------------------------------------
#SYSTEM_VALUES
EMPTY_CELL_IMAGE_PATH = 'empty.png'
RESIZED_IMAGE_PATH = './tmp/resized_image.png'
FPS = 30

match DIFFICULTY:
    
    case 1:
        BLOCKS_WIDTH = 4
        BLOCKS_HEIGHT = 4
        
    case 2:
        BLOCKS_WIDTH = 8
        BLOCKS_HEIGHT = 8

    case 3:
        BLOCKS_WIDTH = 20
        BLOCKS_HEIGHT = 20


    case _:
        BLOCKS_WIDTH = 4
        BLOCKS_HEIGHT = 4
    


#How many time blocks will be swapped
SHUFFLE_RATE = (BLOCKS_WIDTH * BLOCKS_HEIGHT)**2