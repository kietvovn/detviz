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


A    = [[3, 1], [2, 2]]
A_3row1 = [[9, 1], [6, 2]]
ARowEx = [[1, 3], [2, 2]]
Ainv = [[2, -1], [-2, 3]] # chuck divide by det for now
AAinv = [[4, 0], [0, 4]]

## Draw unit vectors ###########################################################
draw_and_show(I, "MATRIX - I")

## Draw matrix A ; properly scaled #############################################
# Shows how A modifies I
draw_and_show(A, "A")

## Draw matrix A_3row1 ; properly scaled #######################################
# Shows how A_3row1 modifies I
draw_and_show(A_3row1, "A : 3 x row1")

## Draw row exchanged matrix A ; properly scaled ###############################
# Shows how row exchanged A modifies I
draw_and_show(ARowEx, "ARowEx")

## Draw matrix Ainv; properly scaled ###########################################
# Shows how Ainv modifies I
draw_and_show(Ainv, "Ainv")

## Draw matrix AAINV; properly scaled ##########################################
# Shows how A modifies AINV
draw_and_show(AAinv, "MATRIX - AAINV")

################################################################################
