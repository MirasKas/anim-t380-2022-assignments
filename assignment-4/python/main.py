import os
import sys
import maya.cmds as mc
import maya.standalone

maya.standalone.initialize()

OriginalName = 'goldfish.model.mdk'

if mc.file(ex=(OriginalName)):
    mc.file(o=(OriginalName))

else:
    mc.file (new=True)
    mc.file(rn=(os.path.join(OriginalName + '.1')))



newName = mc.file(sn=True).split('.')
newName[3] = str(int(newName[3])+1)

mc.file(rn=((os.path.join(os.getcwd(),newName.join('.')))))

mc.file(save=True, typ=('mayaAscii'))