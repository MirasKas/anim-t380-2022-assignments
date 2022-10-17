import os
import sys
import maya.cmds as cmds
import maya.standalone

maya.standalone.initialize()

O_Name = 'goldfish.model.mdk'

if (cmds.file(ex=(fileName)):
    cmds.file(o=(fileName))

else:
    cmds.file (new=True)
    cmds.file(rn=(os.path.join(O_Name + '.1')))



splitName = cmds.file(sn=True).split('.')
splitName[3] = str(int(splitName[3])+1)

cmds.file(rn=((os.path.join(os.getcwd(),splitName.join('.')))))

cmds.file(save=True, typ=('mayaAscii'))