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

# Write matrix as column vectors
I = [[1, 0], [0, 1]]

M = [[2, 3], [3, 1]]

plot_setup("ROTATE")

draw_matrix(I, "maroon", 0.5, "-", llgram = True)

Irot = rotate(I, 90.0)

draw_matrix(Irot, "red", 0.5, "-", llgram = True)

####

draw_matrix(M, "green", 0.5, "-", llgram = True)

Mrot = rotate(M, 90.0)

draw_matrix(Mrot, "purple", 0.5, "-", llgram = True)

plt.show()

###

plot_setup("STICK TO FLOOR")

draw_matrix(M, "green", 0.5, "-", llgram = True)

Mstickx = stick_to_x(M, 1)

draw_matrix(Mstickx, "purple", 0.5, "-", llgram = True)

plt.show()
