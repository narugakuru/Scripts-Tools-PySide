import os
import shutil
import logging
import time
from datetime import datetime  # 导入datetime模块

# 设置日志配置
def setup_logging(log_file_path):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # FileHandler 用于将日志写入文件
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # StreamHandler 用于将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 日志格式
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 确保日志文件实时写入
    file_handler.flush = file_handler.stream.flush

def copy_folders_with_exclusion_and_time_check(origin_path, copy_path, exclude_exts, exclude_dirs):
    for root, dirs, files in os.walk(origin_path):
        # 忽略指定的文件夹 (在遍历子目录之前从 dirs 列表中移除)
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # 构建目标路径
        relative_path = os.path.relpath(root, origin_path)
        target_dir = os.path.join(copy_path, relative_path)

        # 创建目标目录
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # 复制文件，排除指定扩展名的文件
        for file in files:
            if not any(file.lower().endswith(ext) for ext in exclude_exts):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, file)

                if should_copy(source_file, target_file):
                    shutil.copy2(source_file, target_file)
                    logging.info(f'Copied: {source_file} to {target_file}')  # 记录日志

def should_copy(source_file, target_file):
    # 如果目标文件不存在，直接复制
    if not os.path.exists(target_file):
        return True

    # 获取文件的修改时间
    source_mtime = os.path.getmtime(source_file)
    target_mtime = os.path.getmtime(target_file)

    # 如果源文件的修改时间比目标文件新，则复制
    return source_mtime > target_mtime


if __name__ == "__main__":
    origin_path = r"Z:\ssl-htdocs"  # 源文件夹路径
    copy_path = r"E:\WorkSpace\WebKaisyu\ssl-htdocs-local"  # 目标文件夹路径

    # 设置日志输出到文件和控制台，并实时刷新日志文件
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # 获取当前日期时间
    log_file_path = f'{copy_path}/copy_log_{current_time}.txt'  # 更新日志文件路径
    setup_logging(log_file_path)
    
    exclude_exts = ['.pdf', '.PDF']  # 排除的文件扩展名
    exclude_dirs = ['.git', 'pdf']  # 排除的文件夹

    copy_folders_with_exclusion_and_time_check(origin_path, copy_path, exclude_exts, exclude_dirs)
