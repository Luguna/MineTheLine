import math
from mcpi import minecraft

HALF_LENGTH_OF_CUBE_EDGE = 80

mc = minecraft.Minecraft.create()
player_x, player_y, player_z = mc.player.getPos()
player_x = math.ceil(player_x)
player_y = math.ceil(player_y)
player_z = math.ceil(player_z)

min_x = player_x - HALF_LENGTH_OF_CUBE_EDGE
max_x = player_x + HALF_LENGTH_OF_CUBE_EDGE
min_y = player_y
max_y = player_y + (2 * HALF_LENGTH_OF_CUBE_EDGE)
min_z = player_z - HALF_LENGTH_OF_CUBE_EDGE
max_z = player_z + HALF_LENGTH_OF_CUBE_EDGE

mc.setBlocks(min_x, min_y, min_z, max_x, max_y, max_z, 0)
mc.postToChat("Land cleared!")