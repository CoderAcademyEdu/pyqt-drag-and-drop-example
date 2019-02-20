from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from drag_drop_container import *


class DDExample():

    def __init__(self):

        self.app = QApplication([])

        # create 3 labels
        # give each one a tag that we can access later to determine order

        label1 = QLabel('Hello world')
        label1.tag = 'hello'

        label2 = QLabel('You can reorder us')
        label2.tag = 'reorder'

        label3 = QLabel('I am the last one')
        label3.tag = 'last'

        # create a DragDropContainer which is a widget that 
        # can have a number of child widgets added to it
        dd_container = DragDropContainer()

        # add the labels to the container
        # (these can be any widget not just labels)
        dd_container.add_child(label1)
        dd_container.add_child(label2)
        dd_container.add_child(label3)

        # this creates a main window out of the container
        dd_container.show()

        # store the container in an attribute for later use
        self.dd_container = dd_container


    def run(self):

        # start main loop
        self.app.exec_()

        # when event loop ends, app has quit
        # so print out final list order
        for widget in self.dd_container.list_widgets():
            print(widget.tag)

ui = DDExample()
ui.run()
