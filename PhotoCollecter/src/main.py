import os
import collector
import res
import processor

if __name__ == '__main__':
    # col = collector.Collector()
    # col.collect(r"E:\20160610")
    proc = processor.Processor(dest=r'C:\Users\Qun\Desktop')
    proc.process_dest_path()
    proc.copy_read_files()
    res_opt = res.ResOperator()
    items = res_opt.get_all_unready()
    for item in items:
        print(item)
