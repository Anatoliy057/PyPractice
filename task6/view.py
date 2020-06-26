import json

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QInputDialog

import sys

from task6.model import Game
from task6.point import Point


class CellFrame(QWidget):

    def __init__(self, size, i, j, model, parent, *args, **kwargs):
        super(CellFrame, self).__init__(*args, **kwargs)

        self.setFixedSize(QSize(size, size))

        self._is_pick = False
        self.i = i
        self.j = j
        self.game = model
        self.parent = parent

    def reset(self):
        self._is_pick = False
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        r = event.rect()

        outer = Qt.gray
        if self._is_pick:
            inner = Qt.yellow
        else:
            inner = Qt.white

        p.fillRect(r, QBrush(inner))
        pen = QPen(outer)
        pen.setWidth(1)
        p.setPen(pen)
        p.drawRect(r)

        if self.get_number() != 0:
            pen = QPen(QColor('#000000'))
            p.setPen(pen)
            f = p.font()
            f.setBold(True)
            p.setFont(f)
            p.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, str(self.get_number()))

    def click(self):
        self._is_pick = True
        self.parent.click_cell(self.i, self.j)
        self.update()

    def get_number(self):
        return self.game.get_model()[self.i][self.j]

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton and (self.get_number() != 0 or len(self.parent.clicked) == 1):
            self.click()


class GameWindow(QtWidgets.QMainWindow):

    def __init__(self, game: Game):
        super(GameWindow, self).__init__()
        self.setObjectName("Game")
        self.resize(300, 400)

        w = QWidget()

        vb = QtWidgets.QVBoxLayout()
        hb = QtWidgets.QHBoxLayout()
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        loadBtn = QtWidgets.QPushButton()
        loadBtn.setText('Load')
        loadBtn.clicked.connect(self.load)

        restartBtn = QtWidgets.QPushButton()
        restartBtn.setText('Restart')
        restartBtn.clicked.connect(self.restart)

        saveBtn = QtWidgets.QPushButton()
        saveBtn.setText('Save')
        saveBtn.clicked.connect(self.save)

        hb.addWidget(loadBtn)
        hb.addWidget(restartBtn)
        hb.addWidget(saveBtn)

        vb.addLayout(hb)
        vb.addLayout(grid)
        w.setLayout(vb)
        self.setCentralWidget(w)
        self.saveWindow = QtWidgets.QFileDialog()
        self.grid = grid
        self.clicked = []
        self.cells = []
        self.game = game
        self.init_cells()

    def click_cell(self, i: int, j: int) -> bool:
        if len(self.clicked) == 1:
            self.game.move(self.clicked[0], Point(i, j))
            if self.game.is_over():
                self.game_over()
            self.update_cells()
            self.clicked = []
        else:
            self.clicked.append(Point(i, j))

    def restart(self):
        text, ok = QInputDialog.getText(self, 'Input', 'Enter size:')
        size = self.game.size()
        if not ok:
            return
        try:
            size = int(text)
        except ValueError:
            return
        self.game.reset(size)
        self.init_cells()
        self.clicked = []

    def save(self):
        fname = QFileDialog.getSaveFileName(self, 'Save game')[0]
        if fname == '':
            return
        f = open(fname, 'w')
        f.write(json.dumps(self.game.get_model()))
        f.close()

    def load(self):
        fname = QFileDialog.getOpenFileName(self, 'Load game')[0]
        if fname == '':
            return
        f = open(fname, 'r')
        model = json.loads(f.read())
        self.game.load(model)
        self.init_cells()
        self.clicked = []

    def init_cells(self):
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)
        r = range(self.game.size())
        size = int(290 / self.game.size())
        print(self.game.size)
        for i in r:
            for j in r:
                w = CellFrame(size, i, j, self.game, self)
                self.cells.append(w)
                self.grid.addWidget(w, j, i)

    def update_cells(self):
        for c in self.cells:
            c.reset()

    def game_over(self):
        msg = "Game Over! Your score: " + str(self.game.max_cell())
        QMessageBox.about(self, "Final", msg)
        self.restart()



app = QtWidgets.QApplication([])
game = Game(5)
game.spawn(3)
application = GameWindow(game)
application.show()

sys.exit(app.exec())
