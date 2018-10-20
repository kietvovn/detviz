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
# Rule 3; determinant is the linear function of the rows separately
# Write matrix as column vectors

A = [[3, 1], [2, 2]]
B = [[4, 1], [3, 2]]
C = [[7, 1], [5, 2]]

ROTA = stick_to_x(A)
ROTB = stick_to_x(B)
ROTC = stick_to_x(C)

plot_setup("A; B; C")

draw_matrix(A, "maroon", 0.5, "-", llgram = True)
draw_matrix(B, "green",  0.5, "-", llgram = True)
draw_matrix(C, "purple", 0.5, "-", llgram = True)

print "|A| = ", 4
print "|B| = ", 5
print "|C| = ", 9

plt.show()

plot_setup("RA; RB; RC")

draw_matrix(ROTA, "maroon", 0.5, "-", llgram = True)
draw_matrix(ROTB, "green",  0.5, "-", llgram = True)
draw_matrix(ROTC, "purple", 0.5, "-", llgram = True)

plt.show()

'''
## Rule 5; subtracting a multiple of one row from another; leaves det unchanged
# Write matrix as column vectors

A = [[3, 1], [2, 2]]
B = [[3, 1 - 2*3], [2, 2 - 2*2]]

plot_setup("Rule 5")

draw_matrix(A, "maroon", 0.5, "-", llgram = True)
draw_matrix(B, "green",  0.5, "-", llgram = True)


plt.show()
'''

'''
## Rule 10: the transpose AT has the same determinant as A #####################
# Write matrix as column vectors

A = [[3, 1], [2, 2]]
AT = [[3, 2], [1, 2]]

plot_setup("Rule 10")

draw_matrix(A, "maroon", 0.5, "-", llgram = True)
draw_matrix(AT, "green",  0.5, "-", llgram = True)


plt.show()

'''
