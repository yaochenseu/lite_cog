
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QColor

# class ColorSliderWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 400, 400)
#         self.setWindowTitle('HSV Color Slider')

#         # 创建垂直布局
#         main_layout = QVBoxLayout()

#         # 色相滑块
#         hbox_layout1 = QHBoxLayout()
#         self.slider_h = QSlider(Qt.Horizontal, self)
#         self.label_h = QLabel('H: 0', self)
#         hbox_layout1.addWidget(self.label_h)        
#         self.slider_h.setMaximum(359)
#         self.slider_h.valueChanged.connect(self.sliderValueChanged)
#         hbox_layout1.addWidget(self.slider_h)
#         main_layout.addLayout(hbox_layout1)

#         # 饱和度滑块
#         hbox_layout2 = QHBoxLayout()
#         self.label_s = QLabel('S: 0', self)
#         hbox_layout2.addWidget(self.label_s)
#         self.slider_s = QSlider(Qt.Horizontal, self)
#         self.slider_s.setMaximum(255)
#         self.slider_s.valueChanged.connect(self.sliderValueChanged)
#         hbox_layout2.addWidget(self.slider_s)
#         main_layout.addLayout(hbox_layout2)

#         # 明度滑块
#         hbox_layout3 = QHBoxLayout()
#         self.label_v = QLabel('V: 0', self)
#         hbox_layout3.addWidget(self.label_v)        
#         self.slider_v = QSlider(Qt.Horizontal, self)
#         self.slider_v.setMaximum(255)
#         self.slider_v.valueChanged.connect(self.sliderValueChanged)
#         hbox_layout3.addWidget(self.slider_v)
#         main_layout.addLayout(hbox_layout3)

#         # 创建颜色显示标签
#         self.color_label = QLabel(self)
#         main_layout.addWidget(self.color_label)

#         self.setLayout(main_layout)

#         # 初始化颜色
#         self.updateColor(0, 0, 0)

#     def sliderValueChanged(self):
#         h = self.slider_h.value()
#         s = self.slider_s.value()
#         v = self.slider_v.value()
#         self.updateColor(h, s, v)
#         self.label_h.setText(f'H: {h}')
#         self.label_s.setText(f'S: {s}')
#         self.label_v.setText(f'V: {v}')

#     def updateColor(self, h, s, v):
#         color = QColor()
#         color.setHsv(h, s, v)
#         self.color_label.setStyleSheet(f"background-color: {color.name()};")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     exe = ColorSliderWidget()
#     exe.show()
#     sys.exit(app.exec_())




import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap, QImage

class ColorSliderWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None  # 初始化 self.image
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('HSV Color Slider')

        main_layout = QVBoxLayout()

        # 色相滑块
        hbox_layout1 = QHBoxLayout()
        self.slider_h_min = QSlider(Qt.Horizontal, self)
        self.label_h_min = QLabel('H min: 0', self)
        hbox_layout1.addWidget(self.label_h_min)        
        self.slider_h_min.setMaximum(179)
        self.slider_h_min.valueChanged.connect(self.sliderValueChanged)
        hbox_layout1.addWidget(self.slider_h_min)
        main_layout.addLayout(hbox_layout1)

        self.slider_h_max = QSlider(Qt.Horizontal, self)
        self.label_h_max = QLabel('H max: 0', self)
        hbox_layout1.addWidget(self.label_h_max)        
        self.slider_h_max.setMaximum(179)
        self.slider_h_max.valueChanged.connect(self.sliderValueChanged)
        hbox_layout1.addWidget(self.slider_h_max)
        main_layout.addLayout(hbox_layout1)

        # 饱和度滑块
        hbox_layout2 = QHBoxLayout()
        self.label_s_min = QLabel('S min: 0', self)
        hbox_layout2.addWidget(self.label_s_min)
        self.slider_s_min = QSlider(Qt.Horizontal, self)
        self.slider_s_min.setMaximum(255)
        self.slider_s_min.valueChanged.connect(self.sliderValueChanged)
        hbox_layout2.addWidget(self.slider_s_min)
        main_layout.addLayout(hbox_layout2)

        self.slider_s_max = QSlider(Qt.Horizontal, self)
        self.label_s_max = QLabel('S max: 0', self)
        hbox_layout2.addWidget(self.label_s_max)
        self.slider_s_max.setMaximum(255)
        self.slider_s_max.valueChanged.connect(self.sliderValueChanged)
        hbox_layout2.addWidget(self.slider_s_max)
        main_layout.addLayout(hbox_layout2)

        # 明度滑块
        hbox_layout3 = QHBoxLayout()
        self.label_v_min = QLabel('V min: 0', self)
        hbox_layout3.addWidget(self.label_v_min)        
        self.slider_v_min = QSlider(Qt.Horizontal, self)
        self.slider_v_min.setMaximum(255)
        self.slider_v_min.valueChanged.connect(self.sliderValueChanged)
        hbox_layout3.addWidget(self.slider_v_min)
        main_layout.addLayout(hbox_layout3)

        self.slider_v_max = QSlider(Qt.Horizontal, self)
        self.label_v_max = QLabel('V max: 0', self)
        hbox_layout3.addWidget(self.label_v_max)        
        self.slider_v_max.setMaximum(255)
        self.slider_v_max.valueChanged.connect(self.sliderValueChanged)
        hbox_layout3.addWidget(self.slider_v_max)
        main_layout.addLayout(hbox_layout3)

        # 创建颜色显示标签
        self.color_label = QLabel(self)
        main_layout.addWidget(self.color_label)

        # 添加按钮以读取图片
        load_button = QPushButton('Load Image', self)
        load_button.clicked.connect(self.loadImage)
        main_layout.addWidget(load_button)

        self.setLayout(main_layout)

    def sliderValueChanged(self):
        self.updateColor()

    def loadImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        if fileName:
            self.image = cv2.imread(fileName)
            self.updateColor()

    def updateColor(self):
        if self.image is None:
            return
        
        h_min = self.slider_h_min.value()
        s_min = self.slider_s_min.value()
        v_min = self.slider_v_min.value()
        h_max = self.slider_h_max.value()
        s_max = self.slider_s_max.value()
        v_max = self.slider_v_max.value()

        self.label_h_min.setText(f'H min: {h_min}')
        self.label_h_max.setText(f'H max: {h_max}')
        self.label_s_min.setText(f'S min: {s_min}')
        self.label_s_max.setText(f'S max: {s_max}')
        self.label_v_min.setText(f'V min: {v_min}')
        self.label_v_max.setText(f'V max: {v_max}')

        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([h_min, s_min, v_min])
        upper_bound = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

        result = cv2.bitwise_and(self.image, self.image, mask=mask)

        height, width, channel = result.shape
        bytesPerLine = 3 * width
        qImg = QImage(result.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.color_label.setPixmap(QPixmap.fromImage(qImg))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = ColorSliderWidget()
    exe.show()
    sys.exit(app.exec_())
