from detviz import *

## main ########################################################################

m = [[3, 1], [2, 2]] # list of columns
#m = [[0, 1], [3, 0]]
munit = [[1, 0], [0, 1]]

## Draw unit vectors ###########################################################
plot_setup()

# draw matrix
draw_matrix(munit, "maroon", 0.5, "-")

plt.show()

## Draw matrix m; properly scaled ##############################################
plot_setup()

# draw matrix
draw_matrix(m, "maroon", 1, "-", llgram = False)
# draw axes alone the matrix
draw_axes_for_matrix(m, color = 'red', linewidth = 0.1, linestyle = '-')

plt.show()
