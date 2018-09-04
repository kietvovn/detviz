# visualize determinants
# inspired by 3BLUE1BROWN youtube
# Works only for a 2x2 matrix

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

XMIN = -3
XMAX = 20
YMIN = -3
YMAX = 20

class Point:

    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

## Check if the matrix is 2x2
def is_2x2(m):
    return (len(m) == 2 and len(m[0]) == 2 and len(m[1]) == 2)

## plot bounds getter [xmin, xmax, ymin, ymax]
def plot_bounds():
    # get x bounds
    xmin, xmax = plt.gca().get_xbound()
    # get y bounds
    ymin, ymax = plt.gca().get_ybound()

    #return [xmin, xmax, ymin, ymax]
    return [XMIN, XMAX, YMIN, YMAX]

## Setup the plot before drawing matrices and vectors
def plot_setup(plt_name = "GRAPH"):
    plt.subplot(1, 1, 1)
    plt.title(plt_name)
    plt.axis('equal')
    plt.xticks(range(XMIN, XMAX, 1))
    plt.yticks(range(YMIN, YMAX, 1))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(color='gray', linestyle = '-', linewidth=0.1)

    # draw axes
    draw_axes()

    ## Full screen plot always
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

## draw a line on to the plt
def draw_line(pt1, pt2, color_ = "r", linewidth_ = 1, linestyle_ = "-"):

    l = mlines.Line2D([pt1.x, pt2.x],
                      [pt1.y, pt2.y],
                      color = color_,
                      linewidth = linewidth_,
                      linestyle = linestyle_)
    plt.gca().add_line(l)

## draw line on to the plot given the slope of a line and a point that it passes thru
def draw_line_slope_point(slope, pt, color = "r", linewidth = 1, linestyle = "-"):

    # line equation y = mx + c

    # y intercept
    c = float(pt.y) - (float(slope) * float(pt.x))

    xmin, xmax, ymin, ymax = plot_bounds()

    # line end points
    pt1 = Point(float(xmin), slope * float(xmin) + c)
    pt2 = Point(float(xmax), slope * float(xmax) + c)

    draw_line(pt1, pt2, color, linewidth, linestyle)

## draw the given vector on to the plot
def draw_vector(v, color_ = "r", linewidth_ = 1, linestyle_ = "-", srcx = 0, srcy = 0):

    plt.arrow(srcx, srcy, v[0], v[1],
              head_width = 0.05,
              head_length = 0.070,
              color = color_,
              linewidth = linewidth_,
              linestyle = linestyle_)

## draw the given matrix on to the plot
def draw_matrix(m, color_ = "r", linewidth_ = 1, linestyle_ = "-", llgram = False):

    # only 2x2 matrix supported
    if (not is_2x2(m)):
        print ("ERROR: Can draw only 2x2 matrix")
        return

    # m is a list of column vectors
    for cv in m:
        draw_vector(cv, color_, linewidth_, linestyle_)

    # draw the parallelogram if llgram is true
    if llgram:
        draw_vector(m[0], "blue", linewidth_, linestyle_, m[1][0], m[1][1])
        draw_vector(m[1], "blue", linewidth_, linestyle_, m[0][0], m[0][1])

## draw axes on to the current plot
def draw_axes():

    ax = plt.gca()

    xmin, xmax, ymin, ymax = plot_bounds()

    # x axis
    ptx1 = Point(xmin, 0)
    ptx2 = Point(xmax, 0)
    # y axis
    pty1 = Point(0, ymin)
    pty2 = Point(0, ymax)

    draw_line(ptx1, ptx2, "green", "0.3", "-")
    draw_line(pty1, pty2, "green", "0.3", "-")

## draw a vertical line at given x
def draw_vertical(x, color = 'r', linewidth = 1, linestyle = "-"):

    xmin, xmax, ymin, ymax = plot_bounds()

    pt1 = Point(x, ymin)
    pt2 = Point(x, ymax)

    draw_line(pt1, pt2, color, linewidth, linestyle)

## draw a horizontal line at given y
def draw_horizontal(y, color, linewidth, linestyle):

    xmin, xmax, ymin, ymax = plot_bounds()

    pt1 = Point(xmin, y)
    pt2 = Point(xmax, y)

    draw_line(pt1, pt2, color, linewidth, linestyle)

## draw line perpendicular to the given vector
def draw_perp(v, color = "r", linewidth = 1, linestyle = "-"):

    if v[0] == 0 or v[1] == 0:
        # gotta draw vertical/horizontal line where the vector is pointing at
        if v[0] == 0:
            draw_horizontal(v[1], color, linewidth, linestyle)
        if v[1] == 0:
            draw_vertical(v[0], color, linewidth, linestyle)
        return

    slope = float(v[1]) / float(v[0])
    slope_perp = -(1.0/slope)

    # equation of line y = mx + c;
    # we know line passes thru (v[0], v[1])
    # we know m (slope)
    c = float(v[1]) - (float(slope_perp) * float(v[0]))

    xmin, xmax, ymin, ymax = plot_bounds()

    pt1 = Point(xmin, slope_perp * xmin + c)
    pt2 = Point(xmax, slope_perp * xmax + c)

    draw_line(pt1, pt2, color, linewidth, linestyle)


## draw axes on to the current plot based on the vector ticks
def draw_axes_for_vector(v, color = "r", linewidth = 1, linestyle = "-"):

    xmin, xmax, ymin, ymax = plot_bounds()

    for i in range(xmin, xmax, 1):
        if i == 0:
            continue
        #draw_perp([v[0] * i, v[1] * i], color, linewidth, linestyle)

## draw axes on to the current plot based on the matrix ticks
def draw_axes_for_matrix(m, color = "r", linewidth = 1, linestyle = "-"):

    if (not is_2x2(m)):
        print ("ERROR : Matrix dims not 2x2")
        return

    v1 = m[0]
    v2 = m[1]

    xmin, xmax, ymin, ymax = plot_bounds()

    if v1[0] == 0:
        # v1 is pointing up!!
        for i in range(10*xmin, 10*xmax, 1):
            draw_vertical(v1[0] + v2[0] * i, color, linewidth, linestyle)

    else:
        slope_v1 = float(v1[1]) / float(v1[0])
        # all lines along v1
        for i in range(10*xmin, 10*xmax, 1):
            V = [v1[0] + v2[0] * i, v1[1] + v2[1] * i]
            pt = Point(V[0], V[1])
            draw_line_slope_point(slope_v1, pt, color, linewidth, linestyle)

    if v2[0] == 0:
        # v2 is pointing up !!
        for i in range(10*xmin, 10*xmax, 1):
            draw_vertical(v2[0] + v1[0] * i, color, linewidth, linestyle)

    else:
        slope_v2 = float(v2[1]) / float(v2[0])
        # all lines along v2
        for i in range(10*xmin, 10*xmax, 1):
            V = [v2[0] + v1[0] * i, v2[1] + v1[1] * i]
            pt = Point(V[0], V[1])
            draw_line_slope_point(slope_v2, pt, color, linewidth, linestyle)

################################################################################
