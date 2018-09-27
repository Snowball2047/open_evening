from mcpi import minecraft
import time

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()

mc.setBlocks(x+5,y+5,z+5,x+10,y+10,z+10,46,1)
