from colorpalette import Ui_MainWindow
from sys import exit, argv
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtCore import Qt, QRect, QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class ColorPalette(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ColorPalette, self).__init__()
        self.setupUi(self)
        intreg = QRegExp("^[0-9]{11}$")
        integervalidator = QRegExpValidator(intreg, self)
        self.redline.setValidator(integervalidator)
        self.greenline.setValidator(integervalidator)
        self.blueline.setValidator(integervalidator)
        self.redline.setText("255")
        self.greenline.setText("0")
        self.blueline.setText("0")
        self.hexline.setText("ff0000")
        self.slider2Frame.setStyleSheet(
            "#slider2Frame{"
            + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({255},{0},{0},255))"
            + "}"
        )
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.close)
        self.pallete1slider.valueChanged.connect(self.slidervalues)
        self.redline.textChanged.connect(self.search)
        self.blueline.textChanged.connect(self.search)
        self.greenline.textChanged.connect(self.search)
        self.hexline.textChanged.connect(self.search)

        def moveWindow(event):
            if self.isMaximized() == False:
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()

        self.frame_4.mouseMoveEvent = moveWindow

        def colorWindow(event):
            if event.buttons() == Qt.LeftButton:
                if (
                    event.x() > 35
                    and event.y() > 22
                    and event.x() < 315
                    and event.y() < 305
                ):
                    self.clickPosition = event.globalPos()
                    pixMap = QPixmap(316, 306)
                    self.colortracker.setStyleSheet(
                        "#colortracker{border:2px solid white;background-color:transparent;}"
                    )
                    self.colortracker.setGeometry(
                        QRect(event.x() - 13, event.y() - 13, 26, 26)
                    )
                    self.palletesFrame.render(pixMap)
                    image = pixMap.toImage()
                    color = image.pixelColor(event.x(), event.y())
                    r = color.toRgb().red()
                    g = color.toRgb().green()
                    b = color.toRgb().blue()
                    self.showcolor.setStyleSheet(f"background-color:{color.name()};")
                    self.redline.setText(f"{r}")
                    self.greenline.setText(f"{g}")
                    self.blueline.setText(f"{b}")
                    self.hexline.setText(str(self.rgb_to_hex((r, g, b))))

        self.palletesFrame.mouseMoveEvent = colorWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def slidervalues(self):
        val = self.pallete1slider.value()
        self.colortracker.setGeometry(302, 12, 26, 26)

        if val >= 0 and val < 256:
            r = 255
            g = val
            b = 0
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.slider2Frame.setStyleSheet(
                "#slider2Frame{"
                + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({r},{g},{b},255))"
                + "}"
            )
            self.redline.setText(f"{r}")
            self.greenline.setText(f"{g}")
            self.blueline.setText(f"{b}")
            self.hexline.setText(str(self.rgb_to_hex((r, g, b))))
        if val >= 256 and val < 512:
            r = 511 - val
            g = 255
            b = 0
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.slider2Frame.setStyleSheet(
                "#slider2Frame{"
                + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({r},{g},{b},255))"
                + "}"
            )
            self.redline.setText(f"{r}")
            self.greenline.setText(f"{g}")
            self.blueline.setText(f"{b}")
            self.hexline.setText(str(self.rgb_to_hex((r, g, b))))
        if val >= 512 and val < 768:
            r = 0
            g = 255
            b = val - 512
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.slider2Frame.setStyleSheet(
                "#slider2Frame{"
                + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({r},{g},{b},255))"
                + "}"
            )
            self.redline.setText(f"{r}")
            self.greenline.setText(f"{g}")
            self.blueline.setText(f"{b}")
            self.hexline.setText(str(self.rgb_to_hex((r, g, b))))
        if val >= 768 and val < 1024:
            r = 0
            g = 1023 - val
            b = 255
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.slider2Frame.setStyleSheet(
                "#slider2Frame{"
                + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({r},{g},{b},255))"
                + "}"
            )
            self.redline.setText(f"{r}")
            self.greenline.setText(f"{g}")
            self.blueline.setText(f"{b}")
            self.hexline.setText(str(self.rgb_to_hex((r, g, b))))
        if val >= 1024 and val < 1280:
            r = val - 1024
            g = 0
            b = 255
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.slider2Frame.setStyleSheet(
                "#slider2Frame{"
                + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({r},{g},{b},255))"
                + "}"
            )
            self.redline.setText(f"{r}")
            self.greenline.setText(f"{g}")
            self.blueline.setText(f"{b}")
            self.hexline.setText(str(self.rgb_to_hex((r, g, b))))
        if val >= 1280 and val < 1536:
            r = 255
            g = 0
            b = 1535 - val
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.slider2Frame.setStyleSheet(
                "#slider2Frame{"
                + f"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 rgba(255,255,255,255) stop: 1.0 rgba({r},{g},{b},255))"
                + "}"
            )
            self.redline.setText(f"{r}")
            self.greenline.setText(f"{g}")
            self.blueline.setText(f"{b}")
            self.hexline.setText(str(self.rgb_to_hex((r, g, b))))

    def search(self):
        try:
            r = self.redline.text()
            g = self.greenline.text()
            b = self.blueline.text()
            if int(r) > 255:
                self.redline.setText("255")
            if int(r) < 0:
                self.redline.setText("0")
            if int(g) > 255:
                self.greenline.setText("255")
            if int(g) < 0:
                self.greenline.setText("0")
            if int(b) > 255:
                self.blueline.setText("255")
            if int(b) < 0:
                self.blueline.setText("0")
            if int(r) == 255 and int(g) >= 0 and int(g) < 255 and int(b) == 0:
                self.pallete1slider.setSliderPosition(int(g))
            if int(r) <= 255 and int(g) == 255 and int(b) == 0:
                self.pallete1slider.setSliderPosition(511 - int(r))
            if int(r) == 0 and int(g) == 255 and int(b) >= 0:
                self.pallete1slider.setSliderPosition(512 + int(b))
            if int(r) == 0 and int(g) <= 255 and int(b) == 255:
                self.pallete1slider.setSliderPosition(1023 - int(g))
            if int(r) >= 0 and int(g) == 0 and int(b) == 255:
                self.pallete1slider.setSliderPosition(1024 + int(r))
            if int(r) == 255 and int(g) == 0 and int(b) <= 255:
                self.pallete1slider.setSliderPosition(1535 - int(b))
            self.pallete1slider.setStyleSheet(
                "QSlider::handle:horizontal{"
                + f"background-color:rgb({r},{g},{b})"
                + "}"
            )
            self.showcolor.setStyleSheet(f"background-color:rgb({r},{g},{b})")
            self.hexline.setText(str(self.rgb_to_hex((int(r), int(g), int(b)))))
        except:
            QMessageBox.about(
                self,
                "Warning",
                '<p><div style="font-size:15pt; color:black; font-weight:600;">The input value must be between 0 and 255.</div></p>',
            )

    def rgb_to_hex(self, rgb):
        return "%02x%02x%02x" % rgb


if __name__ == "__main__":
    app = QApplication(argv)
    Form = ColorPalette()
    Form.show()
    exit(app.exec_())
