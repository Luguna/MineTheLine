import math
from mcpi import block
from mcpi import minecraft
from PIL import Image

mc = minecraft.Minecraft.create()

player_x, player_y, player_z = mc.player.getPos()

img = Image.open("track5.jpg")
width, height = img.size
px = img.load()

start_x = math.ceil(player_x) - math.ceil(width/2)
start_y = math.ceil(player_y)
start_z = math.ceil(player_z) - math.ceil(height/2)

for x_offset in range(width):
    for z_offset in range(height):
        px_r, px_g, px_b = px[x_offset, z_offset]
        block_x = start_x + x_offset
        block_y = start_y - 3
        block_z = start_z + z_offset
        if(px_r + px_g + px_b < 255):
            block_type = block.GOLD_BLOCK
        else:
            block_type = block.IRON_BLOCK
        #mc.postToChat(f"({block_x}, {block_y}, {block_z}) = {block_type.id}")
        mc.setBlock(block_x, block_y, block_z, block_type.id)

mc.postToChat("Track spawned!")