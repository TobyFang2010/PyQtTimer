import sys
import PyQt5.QtWidgets
import empty


def main():
    # 创建app实例
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # 创建主窗口对象
    main_win = PyQt5.QtWidgets.QMainWindow()
    # 实例化UI，把UI控件挂载到窗口上
    ui = empty.Ui_MainWindow()
    ui.setupUi(main_win)

    # =========在这里写你的信号、按钮事件逻辑=========
    # 示例：按钮点击
    # ui.pushButton.clicked.connect(lambda: print("按钮被点击"))

    # 显示窗口
    main_win.show()
    # 事件循环，退出程序返回码
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
