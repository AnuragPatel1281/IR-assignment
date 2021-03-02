import numpy as np
import math
tx = 30 * math.pi / 180
ty = 30 * math.pi / 180
tz = 30 * math.pi / 180
coord = [2, 3, 0]
rotx = [[1, 0, 0],
        [0, math.cos(tx), -math.sin(tx)],
        [0, math.sin(tx), math.cos(tx)]]
roty = [[math.cos(ty), 0, math.sin(ty)],
        [0, 1, 0],
        [-math.sin(ty), 0, math.cos(ty)]]
rotz = [[math.cos(tz), -math.sin(tz), 0],
        [math.sin(tz), math.cos(tz), 0],
        [0, 0, 1]]
rotx = np.array(rotx)
roty = np.array(roty)
rotz = np.array(rotz)
rotation = ((rotx @ roty) @ rotz)
rotation = np.array(rotation)
coord = np.array(coord)
sol = rotation @ coord
print('Solution Matrix:\n')
print(sol)