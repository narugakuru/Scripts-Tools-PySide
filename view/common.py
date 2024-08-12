from logging import config
from utils.logger_setup import get_clear_logs
from utils import configManager
from PySide6.QtWidgets import QWidget, QFileDialog
from view.Ui_id_rules_replace import Ui_Id_Replace
from qfluentwidgets.components import (
    Dialog,
    Flyout,
    InfoBarIcon,
    FlyoutAnimationType,
    MessageBox,
)
from utils.all_rule_replace import CSVProcessor
from utils.configManager import (
    load_config,
    load_json_config,
    update_yaml,
    load_start_cyclic_values,
)
import logging
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTableView,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QHeaderView,
)
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation
import sys


def bindDB(self):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(configManager.load_config()["sqlite_db_path"])
    # 绑定数据库
    self.model_start = QSqlRelationalTableModel(self)
    self.model_start.setTable("start_values")
    self.model_start.select()

    self.model_cyclic = QSqlRelationalTableModel(self)
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
