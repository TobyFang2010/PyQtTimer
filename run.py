import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, QTimer, QTime, QDate

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

        # 弹窗实例，防止局部变量回收窗口闪退
        self._timer_dialog = None
        self._alarm_dialog = None
        self.alarm_is_set = False

        # 1秒刷新一次时钟
        self.clock_timer = QTimer(self)
        self.clock_timer.setInterval(1000)
        self.clock_timer.timeout.connect(self.update_clock_display)
        self.clock_timer.start()

    def update_clock_display(self):
        """更新时钟显示，数字交给QLCDNumber，中文用Label"""
        now = QDate.currentDate()
        now_time = QTime.currentTime()

        self.lcdYear.display(now.year())
        self.lcdMonth.display(now.month())
        self.lcdDay.display(now.day())
        self.lcdWeek.display(now.dayOfWeek())
        self.lcdHMS.display(now_time.toString("HH:mm:ss"))

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.open_alarm_window()
        elif key == Qt.Key_T:
            self.open_timer_window()
        elif key == Qt.Key_C:
            self.close_alarm_func()
        else:
            super().keyPressEvent(event)

    def open_alarm_window(self):
        if self._alarm_dialog is None:
            self._alarm_dialog = AlarmDialog(self)
        self._alarm_dialog.show()
        self._alarm_dialog.raise_()
        self._alarm_dialog.activateWindow()

    def open_timer_window(self):
        if self._timer_dialog is None:
            self._timer_dialog = TimerDialog(self)
        self._timer_dialog.show()
        self._timer_dialog.raise_()
        self._timer_dialog.activateWindow()

    def close_alarm_func(self):
        if self._alarm_dialog is not None:
            self._alarm_dialog.close()
        self.alarm_is_set = False
        print("闹钟已关闭")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
