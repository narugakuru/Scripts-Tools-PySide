from calendar import c
from utils.logger_setup import get_clear_logs
from PySide6.QtWidgets import QWidget, QFileDialog
from view.Ui_id_rules_replace import Ui_Id_Replace
from qfluentwidgets.components import (
    Flyout,
    InfoBarIcon,
    FlyoutAnimationType,
    MessageBox,
)
from utils.config_setup import ConfigManager
from PySide6.QtWidgets import (
    QHeaderView,
)
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation


from utils.all_rule_replace import CSVProcessor
from utils.config_setup import ConfigManager
import logging
from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlDatabase

# 设置日志配置
logger = logging.getLogger("GlobalLogger")

from PySide6.QtWidgets import QPushButton, QVBoxLayout
from view.Ui_add_new_row import Ui_Dialog_AddNewRow


class IdRulesReplaceInterface(QWidget, Ui_Id_Replace):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log_text = ""

        self.dialog_add_new_row = Ui_Dialog_AddNewRow()
        self.dialog_add_new_row.setupUi(self.dialog_add_new_row)
        self.PushButton_Add.clicked.connect(self.show_add_new_row)

        self.configManager = ConfigManager()
        cfg = self.configManager.config_data
        self.csvProcessor = CSVProcessor()
        self.PushButton_Select.clicked.connect(self.show_fileDialog)
        self.LineEdit_Path.setText(cfg["work_path"])
        self.PushButton_Replace.clicked.connect(self.csv_replace)
        self.bindDB()

    def bindDB(self):
        self.create_connection()
        print("绑定数据库完成")
        self.model_start = QSqlRelationalTableModel(self)
        self.model_start.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        self.model_start.setTable("start_values")
        self.model_start.select()

        self.model_cyclic = QSqlRelationalTableModel(self)
        self.model_cyclic.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        self.model_cyclic.setTable("cyclic_values")
        self.model_cyclic.select()

        self.TableView_start.setModel(self.model_start)
        self.TableView_cyclic.setModel(self.model_cyclic)

        self.TableView_start.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.TableView_start.horizontalHeader().setStretchLastSection(True)
        self.TableView_cyclic.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.TableView_cyclic.horizontalHeader().setStretchLastSection(True)

    def create_connection(self):
        print("create_connection")
        if QSqlDatabase.contains("QSQLITE"):
            QSqlDatabase.removeDatabase("QSQLITE")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(ConfigManager().SQLITE_DB_PATH)
        if not self.db.open():
            print("Unable to open database")
            return False
        print("SQLITE is open")
        return True

    def csv_replace(self):
        path = self.LineEdit_Path.text().strip()
        logger.info("替换路径：" + path)
        self.csvProcessor.process_csv(path)
        self.configManager.update_yaml("work_path", path)
        self.log_text = get_clear_logs()
        print(f"List Handle{self.log_text}")
        self.show_log()

    def msg(self):
        w = MessageBox("执行成功", self.log_text, self)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    def show_log(self):
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title="执行完毕",
            content=str(self.log_text),
            target=self.PushButton_Replace,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP,
        )

    def show_fileDialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        if folder_path:
            self.LineEdit_Path.setText(folder_path)

    def add_new_row(self):
        # Add a new row to the 'start_values' model
        row = self.model_start.rowCount()
        self.model_start.insertRow(row)
        # Optionally, set initial values for the new row here
        self.model_start.submitAll()
        # Log the action
        logger.info(f"New row added at index {row} in start_values table")

    def show_add_new_row(self):
        self.dialog_add_new_row.exec()
        # data1, data2 = dialog.get_data()
        # new_record = self.model.record()
        # new_record.setValue("column1", data1)
        # new_record.setValue("column2", data2)
        # if not self.model.insertRecord(-1, new_record):
        #     QMessageBox.critical(self, "错误", "无法新增数据。")
        # else:
        #     self.model.submitAll()  # 提交更改
