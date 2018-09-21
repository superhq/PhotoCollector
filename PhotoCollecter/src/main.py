import os
from src import DBOpt
from src import CalMd5
class PhotoCollecter():
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest
        self.count = 0
        self.dbopt = DBOpt.DBOpt()
        self.files=[]
        self.md5 = CalMd5.CalMd5()
    def walkdir(self,path):
        try:
            for name in os.listdir(path):
                filepath = os.path.join(path,name)
                if os.path.isdir(filepath):
                    self.walkdir(filepath)
                else:
                    #print(filepath)
                    #self.dbopt.insertfile(filepath)
                    self.files.append((filepath,''))
                    self.count += 1
        except Exception as e:
            print(e)
    def writedb(self):
        return self.dbopt.insertfiles(self.files)
    def calmd5(self):
        rows = self.dbopt.select_unmd5_rows()
        for item in rows:
            file = item[0]
            md5 = self.md5.getmd5(file)
            self.dbopt.updatemd5(file, md5)
            print(file,md5)
    
if __name__ == '__main__':
    collector = PhotoCollecter(r'E:\\',r'.\test')
    #collector.walkdir(collector.src)
    #insertcount = collector.writedb()
    #print('total photos:%d'%collector.count)
    #print('insert count%d'%insertcount)
    collector.calmd5()
    