from utils.logger_setup import get_clear_logs
from utils import configManager
from PySide6.QtWidgets import QWidget, QFileDialog
from view.Ui_id_rules_replace import Ui_Id_Replace
from utils.all_rule_replace import CSVProcessor
import logging
from utils.config_setup import ConfigManager
from PySide6.QtWidgets import (
    QHeaderView,
)
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation


def bindDB(self):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(ConfigManager().SQLITE_DB_PATH)
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
