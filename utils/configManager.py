import os, sys
import logging
import yaml

from utils import sqliteManager
import json

logger = logging.getLogger("GlobalLogger")
# 获取项目根目录的绝对路径
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# 获取当前脚本文件所在目录的绝对路径
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
# 构造 config.yaml 的路径
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, "cfg.yaml")

# 获取临时目录路径
if getattr(sys, "frozen", False):
    # 如果是打包后的执行文件
    bundle_dir = sys._MEIPASS
else:
    # 如果是源代码运行
    bundle_dir = os.path.abspath(os.path.dirname(__file__))

# 加载配置文件和数据库文件
CONFIG_PATH = os.path.join(bundle_dir, "cfg.yaml")
SQLITE_DB_PATH = os.path.join(bundle_dir, "rePlaceRule.db")


def load_config():
    with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    return config


def load_json_config():
    config = load_config()
    json_str = json.dumps(config, separators=(",", ":"))
    return format_json(json_str)


def format_json(json_str):
    formatted_str = ""
    in_string = False
    indent_level = 0
    last_char = ""

    for char in json_str:
        if char == '"':
            in_string = not in_string

        if char in "{[" and not in_string:
            formatted_str += char + "\n" + " " * (indent_level + 1)
            indent_level += 1
        elif char in "}]" and not in_string:
            indent_level -= 1
            formatted_str += "\n" + " " * indent_level + char
        elif char == "," and not in_string:
            formatted_str += char + "\n" + " " * indent_level
        elif char == " " and last_char in "[]" and not in_string:
            continue
        else:
            formatted_str += char

        last_char = char

    return formatted_str


def update_yaml(field, new_value):
    # 读取 YAML 文件
    with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)

    # 更新指定字段
    if field in data:
        data[field] = new_value
    else:
        print(f"字段 '{field}' 不存在于 YAML 文件中。")
        return

    # 写入更新后的 YAML 文件
    with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as file:
        yaml.dump(
            data, file, default_flow_style=False, allow_unicode=True, sort_keys=False
        )

    logger.info(f"字段 '{field}' 已更新为 '{new_value}'")


def save_config(config):
    """保存配置文件."""
    with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as file:
        yaml.dump(
            config, file, allow_unicode=True, sort_keys=False, default_flow_style=False
        )


def get_values():
    """从配置文件中提取start_values和cyclic_values."""
    config = load_config()

    # 提取start_values和cyclic_values
    start_values = config.get("start_values", {})
    cyclic_values = config.get("cyclic_values", {})

    return start_values, cyclic_values


def load_start_cyclic_values():
    db = sqliteManager.SQLiteManager()
    start_values = db.fetch_all("start_values")
    cyclic_values = db.fetch_all("cyclic_values")
    # Convert lists to dictionaries
    start_values = {item[0]: item[1] for item in start_values}
    cyclic_values = {
        item[0]: eval(item[1]) for item in cyclic_values
    }  # Convert string to list

    return start_values, cyclic_values


class ConfigManager:
    def __init__(self):
        self.db = sqliteManager.SQLiteManager()
        self.start_values = self.db.fetch_all("start_values")
        self.cyclic_values = self.db.fetch_all("cyclic_values")

    def load_start_cyclic_values(self):
        db = sqliteManager.SQLiteManager()
        self.start_values = db.fetch_all("start_values")
        self.cyclic_values = db.fetch_all("cyclic_values")
        # Convert lists to dictionaries
        start_values = {item[0]: item[1] for item in self.start_values}
        cyclic_values = {
            item[0]: eval(item[1]) for item in self.cyclic_values
        }  # Convert string to list

        return start_values, cyclic_values
import yaml
import sqlite3
import os

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, cfg_file='cfg.yaml', db_file='rule.db'):
        self.cfg_file = cfg_file
        self.db_file = db_file
        self._load_config()
        self._load_database()

    def _load_config(self):
        with open(self.cfg_file, 'r') as f:
            self.config_data = yaml.safe_load(f)

    def _load_database(self):
        self.db_conn = sqlite3.connect(self.db_file)
        self.db_cursor = self.db_conn.cursor()

    def get_config_value(self, key):
        return self.config_data.get(key)

    def query_db(self, query, params=()):
        self.db_cursor.execute(query, params)
        return self.db_cursor.fetchall()

    def __del__(self):
        if hasattr(self, 'db_conn'):
            self.db_conn.close()
