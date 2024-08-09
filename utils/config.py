import os
import logging
import yaml
from collections import OrderedDict

import json

logger = logging.getLogger("GlobalLogger")
# 获取项目根目录的绝对路径
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# 获取当前脚本文件所在目录的绝对路径
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
# 构造 config.yaml 的路径
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, "cfg.yaml")


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
