from detviz import *

print (''' The determinant is the area of a unit square that you see in the plot ''')

def draw_and_show(m, plt_name = "GRAPH"):

    plot_setup(plt_name)

    draw_matrix(m, "maroon", 0.5, "-", llgram = True)

    draw_axes_for_matrix(m, "red", 0.1, "-")

    plt.show()


## main ########################################################################
# Rule 3; determinant is the linear function of the rows separately
# Write matrix as column vectors

# determinant of a 3x3 matrix (no easy way to visualize)
# A = 4 3 2
#     3 1 4
#     2 3 1
#
# its determinant is = 4 * | 1 4 | - 3 * | 3 4 | + 2 * | 3 1 |
#                          | 3 1 |       | 2 1 |       | 2 3 |
# fortunately we can visualize 2d determinants
C1 = [[1, 3], [4, 1]]
C2 = [[3, 2], [4, 1]]
C3 = [[3, 2], [1, 3]]

plot_setup("cofactors")

draw_matrix(C1, "maroon", 0.5, "-", llgram = True)
draw_matrix(C2, "green",  0.5, "-", llgram = True)
draw_matrix(C3, "yellow", 0.5, "-", llgram = True)


plt.show()
