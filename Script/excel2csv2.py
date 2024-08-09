import pandas as pd
import os


def is_numeric(value):
    """检查值是否为纯数字"""
    try:
        # 转换为字符串后检查是否为数字
        return str(value).isdigit()
    except ValueError:
        return False


def clean_sheet(sheet_data):
    """移除非数据行和空数据列，并清理数据"""
    # 删除空数据列
    sheet_data.dropna(axis=1, how="all", inplace=True)

    # 仅保留第一列是纯数字的行
    sheet_data_cleaned = sheet_data[sheet_data.iloc[:, 0].apply(is_numeric)]

    # 清理数据：去除每个单元格两边的空格
    sheet_data_cleaned = sheet_data_cleaned.applymap(
        lambda x: x.strip() if isinstance(x, str) else x
    )

    return sheet_data_cleaned


def excel_to_csv(excel_file):
    # 读取Excel文件
    excel_data = pd.ExcelFile(excel_file)

    # 获取Excel文件的路径和文件名（不包括扩展名）
    file_path, file_name = os.path.split(excel_file)
    output_path = os.path.join(file_path, "output")
    os.makedirs(output_path, exist_ok=True)

    # 遍历每个sheet
    for sheet_name in excel_data.sheet_names:
        # 读取当前sheet的数据
        sheet_data = pd.read_excel(excel_file, sheet_name=sheet_name)

        # 清理数据
        cleaned_data = clean_sheet(sheet_data)

        # 构建CSV文件名
        csv_file = os.path.join(output_path, f"{sheet_name}.csv")

        # 将数据保存到CSV文件中
        cleaned_data.to_csv(
            csv_file, index=False, sep=",", quoting=0
        )  # quoting=0 对应 csv.QUOTE_MINIMAL

        print(f"Sheet '{sheet_name}' has been saved to '{csv_file}'")


# 示例调用
excel_file = "D:\\WorkSpace\\データ_羅さん.xlsx"
excel_to_csv(excel_file)
