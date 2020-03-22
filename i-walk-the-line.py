import math
import time
from mcpi import block
from mcpi import minecraft

mc = minecraft.Minecraft.create()

def StandingOnWalkTile():
    x, y, z = mc.player.getPos()
    if(mc.getBlock(x, y-1, z) == block.GOLD_BLOCK.id):
        return True
    return False

def NextMove(current_position, last_position):
    print(f"Looking for next move - Cur {current_position}")
    for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
        x = current_position.x + i
        z = current_position.z + j
        print(f"Checking {x},{z} --- Last {last_position.x},{last_position.z}")
        if(mc.getBlock(x, y-1, z) == block.GOLD_BLOCK.id):
            print(f"{x},{z} --- Gold!")
            if(PositionMatches(minecraft.Vec3(x, y, z), last_position)):
                print(f"{x},{z} --- Failure - Position matches last")
            else:
                print(f"{x},{z} --- Success")
                return (x, y, z)
        else:
            print(f"{x},{z} --- Failure - No gold")
    return None

def PositionMatches(posA, posB):
    if(posA.x == posB.x and
       posA.y == posB.y and
       posA.z == posB.z):
        return True
    else:
        return False

# Center player on tile
x, y, z = mc.player.getPos()
mc.player.setPos(math.floor(x)+0.5, y, math.floor(z)+0.5)

if(StandingOnWalkTile()):
    start_position = mc.player.getPos()
    current_position = start_position
    last_position = start_position

while(StandingOnWalkTile()):
    current_position = mc.player.getPos()
    (x, y, z) = NextMove(current_position, last_position)
    last_position = current_position
    print(f"Moving to {x}{z}")
    mc.player.setPos(x, y, z)
    current_position = mc.player.getPos()
    if(PositionMatches(current_position, start_position)):
        mc.postToChat(f"Completed lap!")

mc.postToChat("Not standing on the track... =(")