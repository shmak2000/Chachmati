import numpy as np

r = int(input())
coord = np.deg2rad(np.array([
    [55.7539, 37.6208],
    [59.9398, 30.3146]
]))

x = np.sin((coord[0, 0]-coord[1, 0])/2)**2 + np.cos(coord[0, 0])*np.cos(coord[1, 0])*np.sin((coord[0, 1] - coord[1, 1])/2)**2
d = 2*r*np.arcsin(np.sqrt(x))
print(np.round(d, 2))