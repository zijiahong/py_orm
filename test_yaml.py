import yaml
import os
from  utils.config import MySQL,Config


yamlPath = os.path.join(os.path.dirname(__file__),'configs/config.yaml')
print(yamlPath)
f = open(yamlPath,'r',encoding='utf-8')
x = yaml.load(f.read(),Loader=yaml.Loader)
x = Config(x)
print(x.mySQL.DBName)