import os
import collector
import res
import processor

if __name__ == '__main__':
    col = collector.Collector()
    col.collect(r"E:\\")
    # proc = processor.Processor(dest=r'C:\Users\Qun\Desktop')
    # proc.process()
    res_opt = res.ResOperator()
    suffixs = res_opt.get_suffix_list()
    for suffix in suffixs:
        print(suffix)
