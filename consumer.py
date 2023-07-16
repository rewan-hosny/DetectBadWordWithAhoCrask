
from threading import *
import pandas as pd
import time
import csv
import re
from collections import defaultdict
import timeit
import queue
import producer
import write
import ahocorasick

healthy = queue.Queue(10)
unhealthy= queue.Queue (10)

class ConsumerThread (Thread):
    def __init__(self,sharedDic,STOP,n, target=None, name=None):
        super (ConsumerThread, self).__init__ ()
        self.target = target
        self.name = name
        self.STOP=STOP
        self.n=n
        self.sharedDic=sharedDic
        self.badWords = pd.read_csv("C:\ofile\\badWords.csv",header=None)
        self.A = ahocorasick.Automaton()
        for word in self.badWords[0]:
            self.A.add_word(word.lower(), word.lower())
        self.A.make_automaton()
        return

    def run(self):
        timeList = []
        while True:
            chunk = producer.q.get()
            if (chunk is self.STOP):
                healthy.put(self.STOP)
                unhealthy.put(self.STOP)
                break
            else:
                start =time.time()
                unhealth=chunk[chunk.apply(lambda columncontent: len(list(self.A.iter(
                            str(
                                str(columncontent[0]) + " " +
                                str(columncontent[2]) + " " +
                                str(columncontent[6])
                            ).lower()
                        )))!= 0, raw=True, axis=1)]

                health = chunk[chunk.apply(lambda columncontent: len(list(self.A.iter(
                    str(
                        str(columncontent[0]) + " " +
                        str(columncontent[2]) + " " +
                        str(columncontent[6])
                    ).lower()
                ))) == 0, raw=True, axis=1)]

                stop = time.time()
                processTime1 = stop - start
                timeList.append(processTime1)

                N=self.n
                listunhealthy=[unhealth[i:i+N] for i in range(0,unhealth.shape[0],N)]
                unhealthy.put(listunhealthy)
                listhealty= [health[i:i+N] for i in range(0,health.shape[0],N)]
                healthy.put(listhealty)




            totaltime=sum(timeList)
            print("time process", totaltime)
            self.sharedDic["process"]=totaltime


        producer.q.queue.clear()
        return

