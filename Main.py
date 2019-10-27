import Enter, Register, Lobby, Rank, Record,Reminder
import sys,requests,json
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import api,Judge
token,status,id=0,0,0


class ENTER(QMainWindow, Enter.Ui_MainWindow):  # 登录页面
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.Register.clicked.connect(self.for_register)
        self.Enter.clicked.connect(self.for_enter)
    def for_register(self):
        w = REGISTER(window)
        w.show()
    def for_enter(self):
        User_account='041702215'
        User_password='zxcvbnm.'
        #User_account=self.account.text()
        #User_password=self.password.text()
        if User_account == "":
            self.reminder.setText("请输入账号!")
        elif User_password == "":
            self.reminder.setText("请输入密码!")
        else:#上传信息
            status=api.login(User_account,User_password)
            if(status==3002):
                self.reminder.setText("该账号不存在，请注册！")
            elif(status==1005):
                self.reminder.setText("用户名或密码错误，请重试！")
            else:
                #进入大厅
                token=status
                self.close()
                w = LOBBY(window)
                w.show()

class REGISTER(QtWidgets.QDialog, Register.Ui_Dialog):  # 注册页面
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.Register.clicked.connect(self.for_register)
    def for_register(self):
        user_account = self.account.text()
        user_password = self.password_1.text()
        student_number = self.number.text()
        student_password = self.password_2.text()
        if user_account == "":
            self.reminder.setText("请输入账号!")
        elif user_password == "":
            self.reminder.setText("请输入密码!")
        elif student_number == "":
            self.reminder.setText("请输入学号!")
        elif student_password == "":
            self.reminder.setText("请输入教务处密码!")
        else:        #上传信息
            status=api.register(user_account, user_password, student_number, student_password)
            judge=Judge.judge(status)
            if(judge):
                self.reminder.setText(judge)
            else:
                self.close()

class LOBBY(QMainWindow, Lobby.Ui_MainWindow): # 游戏大厅
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.Begin.clicked.connect(self.for_begin)
        self.Enterroom.clicked.connect(self.for_enterroom)
        self.Rank.clicked.connect(self.for_rank)
        self.Record.clicked.connect(self.for_record)
    def for_begin(self):
        #id,card=api.begin_game(token)
        self.close()
        w = RECORD(window)
        w.show()
        w.number.setText(str(id))
        w.for_details()
    def for_enterroom(self):
        w=REMINDER(window)
        w.Text.setText("此功能尚待开发，敬请期待")
        w.show()
    def for_rank(self):
        # 进入排行榜
        self.close()
        w = RANK(window)
        w.show()
    def for_record(self):
        # 进入对战记录
        self.close()
        w = RECORD(window)
        w.show()

class RANK(QMainWindow, Rank.Ui_MainWindow): # 排行榜
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.turnback.clicked.connect(self.for_turnback)
        self.setTable()
    def for_turnback(self):
        self.close()
        w = LOBBY(window)
        w.show()
    def setTable(self):
        re_js=api.get_ranking()
        if(re_js):
            for i in range(10):
                #item=self.tableWidget.item(i, 1)
                #item.setText(QtCore.QCoreApplication.translate("MainWindow", re_js[i]["player_id"]))
                # 为每个表格内添加数据
                Item = QtWidgets.QTableWidgetItem(re_js[i]["player_id"])
                print(Item)
                self.tableWidget.setItem(i, 0, Item)
                #self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(re_js[i]["player_id"]))
                #self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(re_js[i]["score"]))
                self.show()
        else:
            w = REMINDER(window)
            w.Text.setText("出现未知错误")
            w.show()




class RECORD(QMainWindow, Record.Ui_MainWindow):  # 对战记录
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.turnback.clicked.connect(self.for_turnback)
        self.Search.clicked.connect(self.for_details)
        self.last.clicked.connect(self.for_last)
        self.next.clicked.connect(self.for_next)
    def for_turnback(self):
        self.close()
        w = LOBBY(window)
        w.show()
    def for_details(self):
        id = self.number.text()
        re_js = api.get_detail(token, id)
        if (re_js):
            self.shape.setText(re_js["card"])
            self.change.setText(re_js["score"])
        else:
            w = REMINDER(window)
            w.Text.setText("该场号不存在")
            w.show()
    def for_next(self):
        w=REMINDER(window)
        w.Text.setText("此功能尚待开发，敬请期待")
        w.show()
    def for_last(self):
        w=REMINDER(window)
        w.Text.setText("此功能尚待开发，敬请期待")
        w.show()

class REMINDER(QtWidgets.QDialog, Reminder.Ui_Dialog):  # 提示页面
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.Yes.clicked.connect(self.for_yes)
    def for_yes(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    window = ENTER()
    # 显示
    window.show()
    sys.exit(app.exec_())
