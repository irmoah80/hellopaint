import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from undo_redo import *


class Canvas(QLabel):

    is_saved = True
    first_Title = ''
    last_saved = [[] , []]
    is_projected = False

    qpixmap = None

    def __init__(self,height, width, background_color=QColor('#FFFFFF')):
        super().__init__()
        self.qpixmap = QPixmap(int(height), int(width))
        self.qpixmap.fill(background_color)
        self.setPixmap(self.qpixmap)
        self.pen_color = QColor('#000000')

        self.ur = UndoRedo()
        self.ur.push(self.pixmap().copy())


    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)

    def draw_point(self, x, y):
        painter = QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawPoint(x, y)
        painter.end()
        self.update()


    def draw_line(self, x0, y0, x1, y1):
        painter = QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(x0, y0, x1, y1)
        painter.end()
        self.update()


    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.draw_point(e.x(), e.y())
            self.prev_point = (e.x(), e.y())

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton):
            self.draw_line(self.prev_point[0], self.prev_point[1], e.x(), e.y())
            self.prev_point = (e.x(), e.y())

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.ur.push(self.pixmap().copy())
            self.prev_point = tuple()

    def clear(self):
        self.qpixmap.fill(Qt.white)
        self.setPixmap(self.qpixmap)
        self.update()
        self.ur.c_cach()
        self.ur.push(self.pixmap().copy())

    def undo(self):
        x = self.ur.undo()
        if x != False:
            self.setPixmap(x)
            self.update()

    def redo(self):
        x = self.ur.redo()
        if x != False:
            self.setPixmap(x)
            self.update()

    def save_as(self):
        filePath, format = QFileDialog.getSaveFileName(self, "Save Image", "",
                        "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.pixmap().save(filePath)
        self.setWindowTitle(self.first_Title + ' - ' + self.del_address(filePath))
        self.is_saved = True
        self.is_projected = True

    def save(self):
        if self.is_projected:
            pass

    def del_address(self , st :str):
        for i in range(len(st)):
            x = -1 * (i+1)
            if st[x] == '/':
                st = st[x+1:]
                break
        
        for i in range(len(st)):
            x = -1 * (i+1)
            if st[x] == '.':
                st = st[:x]
                break
        return st
        




class PaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(32, 32))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color + "border-radius : 15; ")


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.colors = [
            '#000002', '#868687', '#900124', '#ed2832', '#2db153', '#13a5e7', '#4951cf',
            '#fdb0ce', '#fdca0f', '#eee3ab', '#9fdde8', '#7a96c2', '#cbc2ec', '#a42f3b',
            '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#dbcfc2',
        ]
        app = QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.canvas = Canvas(geometry.width()*0.60, geometry.height()*0.7)
        w = QtWidgets.QWidget()
        w.setStyleSheet("background-color: #313234")
        l = QtWidgets.QVBoxLayout()  # vertical layout
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()  # horizontal layout
        self.add_palette_button(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

        mainMenu = self.menuBar()

        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")

        # adding brush size to main menu

        save = QAction("Save" , self)
        save.setShortcut("Ctrl+S")
        fileMenu.addAction(save)
        save.triggered.connect(self.save)

        undo = QAction("Undo" , self)
        undo.setShortcut("Ctrl+Z")
        fileMenu.addAction(undo)
        undo.triggered.connect(self.undo)

        redo = QAction("redo" , self)
        redo.setShortcut("Ctrl+Alt+Z")
        fileMenu.addAction(redo)
        redo.triggered.connect(self.redo)

        clear = QAction("clear" , self)
        fileMenu.addAction(clear)
        clear.triggered.connect(self.clear)



    def add_palette_button(self, palette):
        for c in self.colors:
            item = PaletteButton(c)
            item.pressed.connect(self.set_canvas_color)
            palette.addWidget(item)

    def set_canvas_color(self):
        sender = self.sender()
        self.canvas.set_pen_color(sender.color)

    def undo(s):
        s.canvas.undo()

    def redo(s):
        s.canvas.redo()

    def save(s):
        s.canvas.save_as()

    def clear(s):
        s.canvas.clear()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
window.show()
app.exec_()

# Window dimensions
