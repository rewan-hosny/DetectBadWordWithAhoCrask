
from threading import *
import pandas as pd
import logging
import random
import queue
import time
import csv
import re
from collections import defaultdict
import timeit

import consumer




BUF_SIZE = 10
q = queue.Queue(10)


class ProducerThread (Thread):
    def __init__(self,sharedDic,STOP,Nrows, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super (ProducerThread, self).__init__ ()
        self.target = target
        self.name = name
        self.STOP = STOP
        self.Nrows = Nrows
        self.sharedDic=sharedDic

    def run(self):


        if not q.full ():
            chunksize =100000


            with pd.read_csv("C:\ofile\\2.csv", chunksize=chunksize,nrows=self.Nrows, on_bad_lines="skip",dtype='unicode',na_filter=False,
                             encoding="ISO-8859-1",
                             low_memory=False) as reader:                        #O(n)
                start = time.time()
                for chunk in reader:  #O(n)
                    q.put (chunk)

            stop = time.time()
            readTime=stop - start

            print("time read",stop - start)

            self.sharedDic["read"]=readTime
            q.put(self.STOP)
            return


