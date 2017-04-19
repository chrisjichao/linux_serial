#! /usr/bin/env python
#coding=utf-8

import pty
import os
import select
import time

def mkpty():
    # ´ò¿ªÎ±ÖÕ¶Ë
    master1, slave = pty.openpty()
    slaveName1 = os.ttyname(slave)
    print '\nslave device names: ', slaveName1
    return master1

if __name__ == "__main__":

    mkpty()
    while True:
        print "串口"
        time.sleep(5)
