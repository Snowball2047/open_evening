from mcpi import minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()

mc.player.setPos(0,y,0)
mc.setBlocks(-50, y-1, -50, 50, y-1, 50, 2)
mc.setBlocks(-50, y, -50, 50, y+100, 50, 0)
#mc.setBlocks(-5, y-1, 1, 17, y-1, 17, 1)
#mc.setBlocks(2, y-1, 2, 10, y-1, 10, 4)
