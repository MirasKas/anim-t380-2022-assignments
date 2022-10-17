import os
import sys
import maya.cmds as cmds
import maya.standalone

maya.standalone.initialize()

O_Name = 'goldfish.model.mdk'

if cmds.file(ex=(fileName)):
    cmds.file(o=(fileName))

else:
    cmds.file (new=True)
    cmds.file(rn=(os.path.join(O_Name + '.1')))



newName = cmds.file(sn=True).split('.')
newName[3] = str(int(newName[3])+1)

cmds.file(rn=((os.path.join(os.getcwd(),newName.join('.')))))

cmds.file(save=True, typ=('mayaAscii'))