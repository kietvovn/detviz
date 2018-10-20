from detviz import *

print (''' The determinant is the area of a unit square that you see in the plot ''')

def draw_and_show(m, plt_name = "GRAPH"):

    plot_setup(plt_name)

    draw_matrix(m, "maroon", 0.5, "-", llgram = True)

    draw_axes_for_matrix(m, "red", 0.1, "-")

    plt.show()


## main ########################################################################

## I
I = [[1, 0], [0, 1]]

## A
A = [[1, 0], [5, 6]]

## S (made of eigen vectors)
S = [[1, 0], [1, 1]]

## SINV
SINV = [[1, 0], [-1, 1]]

## Diagonal L
L = [[1, 0], [0, 6]]

## S*L
SL = [[1, 0], [6, 6]]

## S*L*SINV
SLSINV = [[1, 0], [5, 6]]

plot_setup("diagonalization")

draw_matrix(A,    "maroon", 0.5, "-", llgram = True)
draw_matrix(S,    "green", 0.9, "-", llgram = True)
draw_matrix(SINV, "yellow", 0.9, "-", llgram = True)
draw_matrix(SL,   "cyan", 0.5, "-", llgram = True)

plt.show()

## Draw unit vectors ###########################################################
#draw_and_show(I, "MATRIX - I")
#
### A
#draw_and_show(A, "A")
#
### S
#draw_and_show(S, "S")
#
### SL
#draw_and_show(SL, "S*L")
#
### SLSINV
#draw_and_show(SLSINV, "SLSINV")

################################################################################
