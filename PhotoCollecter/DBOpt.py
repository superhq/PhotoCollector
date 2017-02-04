import sqlite3
class DBOpt():
    def __init__(self,name='photo.db'):
        self.db = sqlite3.connect(name)
    def __del__(self):
        print('close connection')
        self.db.close()
    def insertfile(self,path,md5=''):
        c = self.db.cursor()
        c.execute("INSERT OR REPLACE INTO files VALUES('%s','%s')"%(path,md5))
        self.db.commit()
        c.close()
    def insertfiles(self,files):
        #c = self.db.cursor()
        c = self.db.executemany("INSERT OR REPLACE INTO files(path,md5) VALUES(?,?)",files)
        self.db.commit()
        rowcount = c.rowcount
        c.close()
        return rowcount
    def updatemd5(self,file,md5):
        c = self.db.cursor()
        c.execute('UPDATE files SET md5=? WHERE path=?',(md5,file))
        self.db.commit()
        #print('row:%d'%c.rowcount)
        c.close()
    def select_unmd5_rows(self):
        c = self.db.cursor()
        c.execute("SELECT path FROM files WHERE md5=''");
        rows = c.fetchall()
        c.close()
        return rows