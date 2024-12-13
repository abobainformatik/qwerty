import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog
from PyQt5.QtGui import QFont
from text_editor_ui import Ui_MainWindow  


class TextEditor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Текстовый редактор")

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionExit.triggered.connect(self.close)
        self.actionFont.triggered.connect(self.change_font)
        self.actionColor.triggered.connect(self.change_color)


    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt);;All Files (*)")
        if filepath:
            try:
                with open(filepath, "r") as f:
                    self.textEdit.setText(f.read())
            except Exception as e:
                print(f"Ошибка открытия файла: {e}")

    def save_file(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)")
        if filepath:
            try:
                with open(filepath, "w") as f:
                    f.write(self.textEdit.toPlainText())
            except Exception as e:
                print(f"Ошибка сохранения файла: {e}")

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())
