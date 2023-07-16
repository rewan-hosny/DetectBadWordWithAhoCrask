
from threading import *
import pandas as pd
import time
import csv
import re
from collections import defaultdict
import timeit
import queue
import producer
import consumer



class ConsumerTh(Thread):
    def __init__(self,STOP,sharedDic, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerTh, self).__init__()
        self.target = target
        self.name = name
        self.STOP=STOP
        self.sharedDic=sharedDic
        return

    def run(self):
        Flag1 = True

        timeList1 = []
        start = time.time()
        while True:

                item = consumer.healthy.get()
                if(item is self.STOP):
                    consumer.healthy.queue.clear()
                    break
                else:
                    if Flag1:
                        pd.concat(item).to_csv('C:\ofile\\healty_aho.csv', mode="w", header=False)
                        Flag1 = False
                    else:
                       pd.concat(item).to_csv('C:\ofile\\healty_aho.csv', mode="a", header=False)
                    stop =time.time()
                    writeTime1=stop-start
                    timeList1.append(writeTime1)




        totalWriteTime1 = sum(timeList1)

        if("write" in self.sharedDic):
            self.sharedDic["write"]+=totalWriteTime1
        else:

            self.sharedDic["write"]=totalWriteTime1
        return




class Consumerunhealthy(Thread):
    def __init__(self,STOP,sharedDic, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(Consumerunhealthy, self).__init__()
        self.target = target
        self.name = name
        self.STOP=STOP
        self.sharedDic=sharedDic
        return

    def run(self):
        Flag2 = True
        timeList2 = []
        start = time.time()
        while True:

                item1 = consumer.unhealthy.get()
                if(item1 is self.STOP):
                    consumer.unhealthy.queue.clear()
                    break
                else:
                    if Flag2:

                        pd.concat(item1).to_csv('C:\ofile\\unhealty_aho.csv', mode="w", header=False)
                        Flag2 = False
                    else:
                       pd.concat(item1).to_csv('C:\ofile\\unhealty_aho.csv', mode="a", header=False)
                    stop = time.time()
                    writeTime2 = stop - start
                    timeList2.append(writeTime2)


        totalWriteTime2 = sum(timeList2)

        if ("write" in self.sharedDic):
            self.sharedDic["write"] += totalWriteTime2

        else:

            self.sharedDic["write"] = totalWriteTime2

        return






