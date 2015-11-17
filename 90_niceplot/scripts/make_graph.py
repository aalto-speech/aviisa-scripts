#!/usr/bin/env python3
import itertools
from matplotlib.markers import MarkerStyle
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

import os
import sys
import glob
#
# plt.style.use('ggplot')
#
# fig, axes = plt.subplots(ncols=2, nrows=2)
# ax1, ax2, ax3, ax4 = axes.ravel()
#
# # scatter plot (Note: `plt.scatter` doesn't use default colors)
# x, y = np.random.normal(size=(2, 200))
# ax1.plot(x, y, 'o')
# ax1.plot([1,2], [2,3], '-')
#
# # sinusoidal lines with colors from default color cycle
# L = 2*np.pi
# x = np.linspace(0, L)
# ncolors = len(plt.rcParams['axes.color_cycle'])
# shift = np.linspace(0, L, ncolors, endpoint=False)
# for s in shift:
#     ax2.plot(x, np.sin(x + s), '-')
# ax2.margins(0)
#
# # bar graphs
# x = np.arange(5)
# y1, y2 = np.random.randint(1, 25, size=(2, 5))
# width = 0.25
# ax3.bar(x, y1, width)
# ax3.bar(x+width, y2, width, color=plt.rcParams['axes.color_cycle'][2])
# ax3.set_xticks(x+width)
# ax3.set_xticklabels(['a', 'b', 'c', 'd', 'e'])
#
# # circles with colors from default color cycle
# for i, color in enumerate(plt.rcParams['axes.color_cycle']):
#     xy = np.random.normal(size=2)
#     ax4.add_patch(plt.Circle(xy, radius=0.3, color=color))
# ax4.axis('equal')
# ax4.margins(0)
#
# plt.show()


def extract_x(pattern, file_name):
    pi = pattern.index('*')
    si = file_name.index(pattern[:pi]) + pi
    ei = file_name.index(pattern[pi+1:])
    return int(file_name[si:ei])


def extract_error(f):
    return float([l.split()[-3] for l in open(f, encoding='utf-8').readlines() if "Sum/Av" in l][0])


def main(out_dir, config):
    rc('font',**{'family':'serif','serif':['Libertine']})
    rc('text', usetex=True)
    BD = os.path.join(os.environ['GROUP_DIR'], 'p', 'sami', 'recog_tests')

    config_name = os.path.basename(config)
    config = [l.strip() for l in open(config, encoding='utf-8').readlines() if len(l.strip()) > 0]
    title = config[0]
    ylabel = config[1]
    xlabel = config[2]
    line_configs = config[3:]

    plt.style.use('ggplot')
    fig = plt.figure(figsize=(7,5))

    plt.ylim([10,30])
    plt.xlim([0,10])

    marker = itertools.cycle(('x', '+', 'o', '*'))

    for lc in line_configs:
        p = lc.split(None, 1)
        files = sorted(glob.glob(os.path.join(BD, p[0])))
        x = [extract_x(p[0], f) for f in files]
        y = [extract_error(f) for f in files]
        x, y = zip(*sorted(zip(x,y)))


        print(x)
        print(y)

        plt.plot(x, y, linestyle='solid', marker=next(marker), label=p[1])

    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    plt.savefig("{}/{}.pdf".format(out_dir, config_name), format='pdf')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])