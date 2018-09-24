import sqlite3


class DbOpt():

    def __init__(self, name='photo.db'):
        self.db = sqlite3.connect(name)

    def __del__(self):
        #print('close connection')
        self.db.close()

    def create_table(self):
        c = self.db.cursor()
        c.execute("CREATE TABLE `files` (\
            `path`    TEXT NOT NULL,\
            `suffix` TEXT,\
            `md5`    TEXT,\
            PRIMARY KEY(`path`)\
            );")
        
    def drop_table(self):
        c = self.db.cursor()
        c.execute("DROP TABLE `files`")

    def insertfile(self, path, suffix, md5=''):
        c = self.db.cursor()
        c.execute("INSERT OR REPLACE INTO files VALUES('%s','%s','%s')" % (path, suffix, md5))
        self.db.commit()
        c.close()

    def insertfiles(self, files):
        # c = self.db.cursor()
        c = self.db.executemany("INSERT OR REPLACE INTO files(path,suffix,md5) VALUES(?,?,?)", files)
        self.db.commit()
        rowcount = c.rowcount
        c.close()
        return rowcount

    def updatemd5(self, file, md5):
        c = self.db.cursor()
        c.execute('UPDATE files SET md5=? WHERE path=?', (md5, file))
        self.db.commit()
        # print('row:%d'%c.rowcount)
        c.close()

    def select_unmd5_rows(self):
        c = self.db.cursor()
        c.execute("SELECT path FROM files WHERE md5=''")
        rows = c.fetchall()
        c.close()
        return rows
    
    def sum_rows(self):
        c = self.db.cursor()
        c.execute("SELECT count(path) FROM files;")
        sum = c.fetchone()
        c.close()
        return sum

    def sum_by_suffix(self):
        c = self.db.cursor()
        c.execute("SELECT suffix,count(path) FROM files group by suffix")
        rows = c.fetchall()
        c.close()
        return rows
