from detviz import *
import math

print (''' The determinant is the area of a unit square that you see in the plot ''')

def draw_and_show(m, plt_name = "GRAPH"):

    plot_setup(plt_name)

    draw_matrix(m, "maroon", 0.5, "-", llgram = True)

    draw_axes_for_matrix(m, "red", 0.1, "-")

    plt.show()

def rotate_vector(v, rad):

    assert (len(v) == 2)

    return [v[0] * math.cos(rad) + v[1] * (-math.sin(rad)),
            v[0] * math.sin(rad) + v[1] * math.cos(rad)]

def rotate(m, deg):

    # sanity check
    assert (len(m) == 2 or len(m) == 1)
    assert (len(m[0]) == 2)
    if len(m) == 2:
        assert (len(m[1]) == 2)

    ret = []

    for i in range(0, len(m)):
        ret.append(rotate_vector(m[i], math.radians(deg)))

    return ret

def stick_to_x(m, vidx = 0):

    # sanity check
    assert (len(m) == 2 or len(m) == 1)
    assert (len(m[0]) == 2)
    if len(m) == 2:
        assert (len(m[1]) == 2)

    assert (vidx < len(m))

    # calculate the degrees of the first vector off the x axis
    deg = math.degrees(math.atan2(m[vidx][1], m[vidx][0]))

    return rotate(m, -deg)

## main ########################################################################

## A
A = [[2, 1], [1, 2]]

## L
L = [[1, -0.5], [0, 1]]

## U
U = [[2, 0], [1, 1.5]]

## ROT A
ROTA = stick_to_x(A)

print "A ", A
print "ROTA", ROTA

plot_setup("A = LU")

draw_matrix(A,    "maroon", 0.5, "-", llgram = True)
draw_matrix(L,    "green", 0.5, "-", llgram = True)
draw_matrix(U,   "cyan", 0.9, "-", llgram = True)
draw_matrix(ROTA, "red", 0.9, "--", llgram = True)

#draw_matrix(stick_to_x(A), "red", 0.5, "--", llgram = True)

plt.show()

################################################################################
