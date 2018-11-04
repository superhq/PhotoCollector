from sqlalchemy import Column, String, Integer, DateTime, create_engine, MetaData, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from common import Status

Base = declarative_base()


class Res(Base):
    __tablename__ = 'res'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    fullpath = Column(String, primary_key=True)
    status = Column(Integer, default=Status.UNREADY)
    suffix = Column(String)
    datetime = Column(String)
    maker = Column(String)
    topath = Column(String)

    def __repr__(self):
        return 'fullpath=%s,status=%d,suffix=%s,datetime=%s,maker=%s,topath=%s' \
               % (self.fullpath, self.status, self.suffix, self.datetime, self.maker, self.topath)


engine = create_engine('sqlite:///rs.db', echo=False)
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
        self.session.query(Res).filter_by(fullpath=fullpath).update(values)
        self.session.commit()

    def update_uncommit(self, fullpath, **values):
        self.session.query(Res).filter_by(fullpath=fullpath).update(values)

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()

    # def add(self, res_list):
    #     self.session.add_all(res_list)
    #     self.session.commit()
    def add(self, res):
        result = self.session.query(Res).filter(Res.fullpath == res.fullpath).one_or_none()
        if result:
            pass
            # print(result)
        else:
            self.session.add(res)

    def get_all(self):
        return self.session.query(Res).all()

    def get_suffix_list(self):
        results = self.session.query(Res.suffix, func.count(Res.fullpath)).group_by(Res.suffix).all()
        return results

    def get_all_ready(self):
        return self.session.query(Res).filter_by(status=Status.REDAY)

    def count_all_ready(self):
        return self.session.query(func.count(Res.fullpath)).filter_by(status=Status.REDAY).one()[0]

    def get_all_unready(self):
        return self.session.query(Res).filter_by(status=Status.UNREADY)

    def count_all_unread(self):
        return self.session.query(func.count(Res.fullpath)).filter_by(status=Status.UNREADY).one()[0]

    def get_all_ok(self):
        return self.session.query(Res).filter_by(status=Status.OK)
