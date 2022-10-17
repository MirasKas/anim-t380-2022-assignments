import maya.standalone
import maya.cmds as cmds
import argparse

maya.standalone.initialize()

parser = argparse.ArgumentParser(description='Creates a cube for character height reference!')
parser.add_argument('cube_h', type=int, help="Desired reference height")

args = parser.parse_args()

cubeRatio = args.cube_h // 20

cmds.polyCube (h= args.cube_h, w = 20, d = 20, sd = cubeRatio n=("charRef"))

print("Character heigh reference created")

cmds.file(save=True, typ=('mayaAscii'))

