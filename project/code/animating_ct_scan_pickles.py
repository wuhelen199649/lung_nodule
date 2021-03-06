from __future__ import print_function
from matplotlib.pyplot import figure, show, gray
import cPickle as pickle


# first_ten = pickle.load(open("../data/first_ten.p", "rb" ))
# X = first_ten[0]

class IndexTracker(object):
    '''
    Creates a matplotlib object in which you can scroll through the
    Z-axis of a three-dimensional array 
    '''
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices/2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = np.clip(self.ind + 1, 0, self.slices - 1)
        else:
            self.ind = np.clip(self.ind - 1, 0, self.slices - 1)

        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()

fig = figure()
ax = fig.add_subplot(111)

tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.onscroll)

#CT Scan in Grayscale
#ax.imshow(visu_base, cmap=mpl.cm.gray)
show()
