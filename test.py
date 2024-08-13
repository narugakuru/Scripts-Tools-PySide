from peewee import PostgresqlDatabase
from urllib.parse import urlparse, parse_qs


def create_db_connection(url):
    # 解析 URL
    parsed_url = urlparse(url)

    # 提取数据库连接参数
    database = parsed_url.path.lstrip("/")
    user = parsed_url.username
    password = parsed_url.password
    host = parsed_url.hostname
    port = parsed_url.port

    # 解析查询参数（用于选项）
    query_params = parse_qs(parsed_url.query)
    options = (
        query_params.get("options", [])[0]
        if "options" in query_params
        else "-csearch_path=takusai_tanntai"
    )

    # 创建数据库连接
    db = PostgresqlDatabase(
        database, user=user, password=password, host=host, port=port, options=options
    )

    return db


# 示例 URL
db_url = "postgresql+psycopg2://postgres:rootroot@localhost:5432/postgre"

# 使用函数创建数据库连接
db = create_db_connection(db_url)

# 测试连接
try:
    db.connect()
    print("数据库连接成功")
except Exception as e:
    print(f"数据库连接失败: {e}")
