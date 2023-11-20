import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys

argv = sys.argv
name = 'radomKegel' + (argv[1] if len(argv) > 1 else '')
plt.figure(name)
plt.clf()
fig, ax = plt.subplots()


def plotRectangle(x, y, d1, d2, edgeColor, fill=False, faceColor=None):
    rect = patches.Rectangle((x - d1//2, y-d2//2), d1, d2, edgecolor=edgeColor, facecolor=faceColor, fill=fill)
    ax.add_patch(rect)


def plotCircle(x, y, d, color, fill=True):
    circle = plt.Circle((x, y), d, color=color, fill=fill)
    ax.set_aspect(1)
    ax.add_artist(circle)


def plotField():
    plotCircle(0, 0, 775, color='k')
    plotCircle(0, 0, 750, color='w')
    plotRectangle(0, 0, 200, 200, 'y')


def randomKegelAndPlot():
    randomCount = np.random.randint(3, size=16)
    while True:
        if np.count_nonzero(randomCount == 2) == 4 and np.count_nonzero(randomCount == 1) == 4:
            cb = 0
            cw = 0
            for i in range(0, 16, 2):
                if randomCount[i] == 1:
                    cw += 1
                elif randomCount[i] == 2:
                    cb += 1
            if cb == 2 and cw == 2:
                pos = 0
                for i in range(16):
                    if randomCount[i] != 0:
                        pos = i
                        break
                for i in range(pos + 1, 16):
                    if randomCount[i] != 0:
                        if randomCount[i] != randomCount[pos]:
                            pos = i
                        else:
                            break
                else:
                    break

        randomCount = np.random.randint(3, size=16)
    plotCircle(400, 0, 30, color=('y' if randomCount[0] == 0 else ('#E7E4DA' if randomCount[0] == 1 else 'k')), fill=True)
    plotCircle(675*math.cos(math.radians(22.5)), -675*math.sin(math.radians(22.5)), 30, color=('y' if randomCount[1] == 0 else ('#E7E4DA' if randomCount[1] == 1 else 'k')), fill=True)
    plotCircle(400*math.cos(math.pi/4), -400*math.sin(math.pi/4), 30, color=('y' if randomCount[2] == 0 else ('#E7E4DA' if randomCount[2] == 1 else 'k')), fill=True)
    plotCircle(675*math.cos(math.radians(67.5)), -675*math.sin(math.radians(67.5)), 30, color=('y' if randomCount[3] == 0 else ('#E7E4DA' if randomCount[3] == 1 else 'k')), fill=True)
    plotCircle(0, -400, 30, color=('y' if randomCount[4] == 0 else ('#E7E4DA' if randomCount[4] == 1 else 'k')), fill=True)
    plotCircle(-675*math.cos(math.radians(67.5)), -675*math.sin(math.radians(67.5)), 30, color=('y' if randomCount[5] == 0 else ('#E7E4DA' if randomCount[5] == 1 else 'k')), fill=True)
    plotCircle(-400*math.cos(math.pi/4), -400*math.sin(math.pi/4), 30, color=('y' if randomCount[6] == 0 else ('#E7E4DA' if randomCount[6] == 1 else 'k')), fill=True)
    plotCircle(-675*math.cos(math.radians(22.5)), -675*math.sin(math.radians(22.5)), 30, color=('y' if randomCount[7] == 0 else ('#E7E4DA' if randomCount[7] == 1 else 'k')), fill=True)
    plotCircle(-400, 0, 30, color=('y' if randomCount[8] == 0 else ('#E7E4DA' if randomCount[8] == 1 else 'k')), fill=True)
    plotCircle(-675*math.cos(math.radians(22.5)), 675*math.sin(math.radians(22.5)), 30, color=('y' if randomCount[9] == 0 else ('#E7E4DA' if randomCount[9] == 1 else 'k')), fill=True)
    plotCircle(-400*math.cos(math.pi/4), 400*math.sin(math.pi/4), 30, color=('y' if randomCount[10] == 0 else ('#E7E4DA' if randomCount[10] == 1 else 'k')), fill=True)
    plotCircle(-675*math.cos(math.radians(67.5)), 675*math.sin(math.radians(67.5)), 30, color=('y' if randomCount[11] == 0 else ('#E7E4DA' if randomCount[11] == 1 else 'k')), fill=True)
    plotCircle(0, 400, 30, color=('y' if randomCount[12] == 0 else ('#E7E4DA' if randomCount[12] == 1 else 'k')), fill=True)
    plotCircle(675*math.cos(math.radians(67.5)), 675*math.sin(math.radians(67.5)), 30, color=('y' if randomCount[13] == 0 else ('#E7E4DA' if randomCount[13] == 1 else 'k')), fill=True)
    plotCircle(400*math.cos(math.pi/4), 400*math.sin(math.pi/4), 30, color=('y' if randomCount[14] == 0 else ('#E7E4DA' if randomCount[14] == 1 else 'k')), fill=True)
    plotCircle(675*math.cos(math.radians(22.5)), 675*math.sin(math.radians(22.5)), 30, color=('y' if randomCount[15] == 0 else ('#E7E4DA' if randomCount[15] == 1 else 'k')), fill=True)

    plotCircle(400, 0, 30, color=('y' if randomCount[0] == 0 else 'k'), fill=False)
    plotCircle(675 * math.cos(math.radians(22.5)), -675 * math.sin(math.radians(22.5)), 30, color=('y' if randomCount[1] == 0 else 'k'), fill=False)
    plotCircle(400 * math.cos(math.pi / 4), -400 * math.sin(math.pi / 4), 30, color=('y' if randomCount[2] == 0 else 'k'), fill=False)
    plotCircle(675 * math.cos(math.radians(67.5)), -675 * math.sin(math.radians(67.5)), 30, color=('y' if randomCount[3] == 0 else 'k'), fill=False)
    plotCircle(0, -400, 30, color=('y' if randomCount[4] == 0 else 'k'), fill=False)
    plotCircle(-675 * math.cos(math.radians(67.5)), -675 * math.sin(math.radians(67.5)), 30, color=('y' if randomCount[5] == 0 else 'k'), fill=False)
    plotCircle(-400 * math.cos(math.pi / 4), -400 * math.sin(math.pi / 4), 30, color=('y' if randomCount[6] == 0 else 'k'), fill=False)
    plotCircle(-675 * math.cos(math.radians(22.5)), -675 * math.sin(math.radians(22.5)), 30, color=('y' if randomCount[7] == 0 else 'k'), fill=False)
    plotCircle(-400, 0, 30, color=('y' if randomCount[8] == 0 else 'k'), fill=False)
    plotCircle(-675 * math.cos(math.radians(22.5)), 675 * math.sin(math.radians(22.5)), 30, color=('y' if randomCount[9] == 0 else 'k'), fill=False)
    plotCircle(-400 * math.cos(math.pi / 4), 400 * math.sin(math.pi / 4), 30, color=('y' if randomCount[10] == 0 else 'k'), fill=False)
    plotCircle(-675 * math.cos(math.radians(67.5)), 675 * math.sin(math.radians(67.5)), 30, color=('y' if randomCount[11] == 0 else 'k'), fill=False)
    plotCircle(0, 400, 30, color=('y' if randomCount[12] == 0 else 'k'), fill=False)
    plotCircle(675 * math.cos(math.radians(67.5)), 675 * math.sin(math.radians(67.5)), 30, color=('y' if randomCount[13] == 0 else 'k'), fill=False)
    plotCircle(400 * math.cos(math.pi / 4), 400 * math.sin(math.pi / 4), 30, color=('y' if randomCount[14] == 0 else 'k'), fill=False)
    plotCircle(675 * math.cos(math.radians(22.5)), 675 * math.sin(math.radians(22.5)), 30, color=('y' if randomCount[15] == 0 else 'k'), fill=False)


plotField()
randomKegelAndPlot()
ax.fill([-900, -900, -800], [800, 900, 900], color='r')

plotCircle(950, 900, 30, color='y', fill=True)
ax.text(1000, 880, 'empty kegel pos', color='k', fontsize=9)

plotCircle(950, 800, 30, color='k', fill=True)
ax.text(1000, 780, 'black kegel pos', color='k', fontsize=9)

plotCircle(950, 700, 30, color='#E7E4DA', fill=True)
plotCircle(950, 700, 30, color='k', fill=False)
ax.text(1000, 680, 'white kegel pos', color='k', fontsize=9)

ax.fill([930, 930, 980], [580, 630, 630], color='r')
ax.text(1000, 580, 'orientate mark', color='k', fontsize=9)

plotRectangle(950, 500, 50, 50, 'y')
ax.text(1000, 480, 'robot starting pos', color='k', fontsize=9)


plt.xlim(-1000, 1000)
plt.ylim(-950, 950)

plt.axis('off')
plt.savefig(str(name) + ".png", dpi=500)


