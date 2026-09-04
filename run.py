import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt
# 导入编译完成的ui生成py文件
from mainwin import Ui_MainWindow
from timerwin import Ui_TimerDialog
from alarmwin import Ui_AlarmDialog


class AlarmDialog(QDialog, Ui_AlarmDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class TimerDialog(QDialog, Ui_TimerDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 保存弹窗实例，防止局部变量回收导致窗口闪退
        self._timer_dialog = None
        self._alarm_dialog = None
        self.alarm_is_set = False  # 标记闹钟是否已经设置

    def keyPressEvent(self, event):
        """捕获键盘按下事件"""
        key = event.key()
        # a键:打开闹钟设置窗口
        if key == Qt.Key_A:
            self.open_alarm_window()
        # t键:打开计时器窗口
        elif key == Qt.Key_T:
            self.open_timer_window()
        # c键:关闭闹钟
        elif key == Qt.Key_C:
            self.close_alarm_func()
        else:
            # 其他按键交给父类处理
            super().keyPressEvent(event)

    def open_alarm_window(self):
        """按下a，打开闹钟设置弹窗"""
        if self._alarm_dialog is None:
            self._alarm_dialog = AlarmDialog(self)
        self._alarm_dialog.show()
        self._alarm_dialog.raise_()
        self._alarm_dialog.activateWindow()

    def open_timer_window(self):
        """按下t，打开计时器弹窗"""
        if self._timer_dialog is None:
            self._timer_dialog = TimerDialog(self)
        self._timer_dialog.show()
        self._timer_dialog.raise_()
        self._timer_dialog.activateWindow()

    def close_alarm_func(self):
        """按下c，关闭闹钟逻辑"""
        if self._alarm_dialog is not None:
            self._alarm_dialog.close()
        self.alarm_is_set = False
        print("闹钟已关闭")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
