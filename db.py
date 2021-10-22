from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model
# 初始化数据库连接:
"""
设置数据库参数
"""
MYSQL_DB = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'pacman'
MYSQL_HOST = 'localhost'
MYSQL_POST = 3306
 
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=utf8" % (MYSQL_USER, MYSQL_PASSWD, MYSQL_HOST, MYSQL_POST, MYSQL_DB)
engine = create_engine('mysql+mysqlconnector://root:pacman@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def common_create(data):
    session = DBSession()
    session.add(data)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def query_use(id:str)-> model.User:
    session = DBSession()
    u: model.user.User = session.query(model.User).filter(model.User.id==id).one()
    return u 