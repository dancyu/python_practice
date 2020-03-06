# coding=UTF-8
'''
產生多個模擬資料
payload="B16880100000000100260000011111111131317B1713"
'''
import time
import random

def getdata(prefix,id,fourIMP):
    times=4
    fourV=""
    for i in range(times):
        a=random.randrange(12600,12900)
        fourV=fourV+('%x' % a)
        # print(fourV)
    tmp=('%x' % random.randrange(0,40)).zfill(2)
    # print("tmp",tmp)
    payload=prefix+id+fourIMP+fourV+tmp

    cs=0
    for a in range(21):
        b=a*2
        v=payload[b:b+2]       
        v2int=int(v,16)     #str to int (16)
        cs=v2int^cs      #xor
    checksum=('%x' % cs)
    payload=payload+checksum
    # print(payload)
    return payload.upper()

def gettimestamp(records):
    now=int(time.time()) 
    t=[]
    for i in range(records):
        t.append(now-i*10)
    t.sort()
    return t

prefix="B168"
id="8811"
fourIMP="0000000000000000"
records=5

timestamplist=gettimestamp(records)
for a in range(records):
    print(str(timestamplist[a])+"_"+getdata(prefix,id,fourIMP))