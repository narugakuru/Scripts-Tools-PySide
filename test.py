from backup import configManager
from utils import all_rule_replace
from utils import *
from view import *

cp = all_rule_replace.CSVProcessor()
path = configManager.load_config()["work_path"]
cp.process_csv(path)
