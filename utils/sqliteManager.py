import sqlite3
import json
from utils import configManager


class SQLiteManager:
    def __init__(self, db_path=None):
        """初始化 SQLiteManager，连接到指定的 SQLite 数据库文件。"""
        self.db_path = configManager.load_config()["sqlite_db_path"]
        self.connection = None
        self.cursor = None

    def connect(self):
        """连接到 SQLite 数据库。"""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

    def disconnect(self):
        """断开与 SQLite 数据库的连接。"""
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=()):
        """执行查询操作并返回结果。"""
        self.connect()
        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        self.disconnect()
        return results

    def execute_update(self, query, params=()):
        """执行更新操作（插入、删除、更新）。"""
        self.connect()
        self.cursor.execute(query, params)
        self.connection.commit()
        self.disconnect()

    def create_table(self, table_name, columns):
        """创建一个新表。"""
        columns_def = ", ".join([f"{name} {dtype}" for name, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def});"
        self.execute_update(query)

    def insert_data(self, table_name, data):
        """插入数据到表中。"""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
        self.execute_update(query, tuple(data.values()))

    def update_data(self, table_name, data, condition):
        """更新表中的数据。"""
        set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition};"
        self.execute_update(query, tuple(data.values()))

    def delete_data(self, table_name, condition):
        """删除表中的数据。"""
        query = f"DELETE FROM {table_name} WHERE {condition};"
        self.execute_update(query)

    def fetch_all(self, table_name):
        """从表中获取所有数据。"""
        query = f"SELECT * FROM {table_name};"
        return self.execute_query(query)

    def fetch_one(self, table_name, condition):
        """从表中获取符合条件的单条数据。"""
        query = f"SELECT * FROM {table_name} WHERE {condition};"
        results = self.execute_query(query)
        return results[0] if results else None

    def insert_or_update(self, table_name, data, unique_column):
        """插入或更新数据。"""
        existing_data = self.fetch_one(
            table_name, f"{unique_column} = '{data[unique_column]}'"
        )
        if existing_data:
            self.update_data(
                table_name, data, f"{unique_column} = '{data[unique_column]}'"
            )
        else:
            self.insert_data(table_name, data)


# 示例使用
if __name__ == "__main__":
    db_manager = SQLiteManager()
    # 查询数据
    print(db_manager.fetch_all("id_values")[:5])
    print(db_manager.fetch_all("cyclic_values")[:5])

"""     # 创建表
    db_manager.create_table(
        "start_values", {"key": "TEXT PRIMARY KEY", "value": "INTEGER"}
    )

    db_manager.create_table(
        "cyclic_values", {"key": "TEXT PRIMARY KEY", "values": "TEXT"}
    )

    # 插入数据
    db_manager.insert_data("start_values", {"key": "seq_id", "value": 10000})

    # 更新数据
    db_manager.update_data("start_values", {"value": 20000}, 'key = "seq_id"')

    # 删除数据
    db_manager.delete_data("start_values", 'key = "seq_id"') 
    """
