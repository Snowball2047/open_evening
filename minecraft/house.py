from mcpi import minecraft
import json

def getLineX(x, y, z, length):
    line = []
    for i in range(length):
        line.append(mc.getBlock(x, y, z))
        x += 1
    return line

def getAreaY(x, y, z, length):
    area = []
    for i in range(length):
        area.append(getLineX(x , y, z, 22))
        y += 1
    return area

def getVolumeZ(x, y, z, length):
    volume = []
    for i in range(length):
        volume.append(getAreaY(x, y, z, 13))
        z += 1
    return volume

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()

house = getVolumeZ(-5, y-1, -1, 15)

with open('house.json', 'w') as outfile:
    json.dump(house, outfile)
