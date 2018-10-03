from sqlalchemy import Column, String, Integer, DateTime, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Res(Base):
    __tablename__ = 'res'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullpath = Column(String, unique=True, nullable=False)
    suffix = Column(String)
    datetime = Column(String)
    maker = Column(String)
    topath = Column(String)

    def __repr__(self):
        return 'id=%d,fullpath=%s,suffix=%s,datetime=%s,maker=%s,topath=%s' \
               % (self.id, self.fullpath, self.suffix, self.datetime, self.maker, self.topath)


engine = create_engine('sqlite:///rs.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


class ResOperator:
    def __init__(self):
        self.session = DBSession()

    def __del__(self):
        self.session.close()

    def add_one(self, res):
        self.session.add(res)
        self.session.commit()

    def update_one(self, fullpath, **values):
        """
        问题：更新的速度太慢
        :param fullpath:
        :param values:
        :return:
        """
        print(values)
        self.session.query(Res).filter_by(fullpath=fullpath).update(values)
        self.session.commit()



    def add(self, res_list):
        self.session.add_all(res_list)
        self.session.commit()

    def get_all(self):
        return self.session.query(Res).all()
