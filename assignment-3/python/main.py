import os
import sys
import maya.cmds as cmds
import maya.standalone

maya.standalone.initialize()

try:
    ASSET = os.getenv('asset')
except:
    print('$asset not found')
    
if ASSET == None:
    print('$asset not set')


cwd = os.path.dirname(os.getcwd())
assetDir = 'assets\\{assetName}\\maya\scenes\\assignment-3.mb'.format(assetName=ASSET)
parentDir = os.path.join(cwd,assetDir)

os.makedirs(parentDir)

cmds.file(new=True)
cmds.file(rn=(parentDir))

cmds.group(empty=True, n=ASSET)

cmds.file(save=True, typ=('mayaAscii'))
