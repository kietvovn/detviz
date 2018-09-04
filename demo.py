from detviz import *

print (''' The determinant is the area of a unit square that you see in the plot ''')

def draw_and_show(m, plt_name = "GRAPH"):

    plot_setup(plt_name)

    draw_matrix(m, "maroon", 0.5, "-", llgram = True)

    draw_axes_for_matrix(m, "red", 0.1, "-")

    plt.show()


## main ########################################################################

# Write matrix as column vectors
I = [[1, 0], [0, 1]]

#m1 = [[3, 1], [2, 2]]
#m2 = [[2, 3], [1, 2]]
#m1xm2 = [[12, 8], [7, 5]]

m1 = [[3, 1], [2, 2]]
m2 = [[1, -1], [-1, 2]]
m1xm2 = [[1, -1], [1, 3]]

## Draw unit vectors ###########################################################
draw_and_show(I, "MATRIX - I")

## Draw matrix m1; properly scaled #############################################
# Shows how m1 modifies I
draw_and_show(m1, "MATRIX - I x M1")

## Draw matrix m2; properly scaled #############################################
# Shows how m2 modifies I
draw_and_show(m2, "MATRIX - I x M2")

## Draw matrix m1xm2; properly scaled ##########################################
# Shows how m2 modifies m1
draw_and_show(m1xm2, "MATRIX - M1 x M2")

################################################################################
