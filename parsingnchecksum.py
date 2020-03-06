'''
payload is a 44 digit
per 2 digit is 1 byte, means a payload has 22 bytes
xor the 1st byte to 21 byte should be checksum column byte22.

'''
#payload="b1680011000000000000000000000000000f15fa163e"
'''

'''
payload="6800110b860b970bc20b8931a531b031ab31b7168d00" #checksum invalid
payload="B16855110000000000000000314331F53141316DDA"

byte=[]
byte2int=[]
a=0
x=0
while a < len(payload)/2:
    b=a*2
    v=payload[b:b+2]
    byte.append(v)
    v2int=int(v,16)     #str to int (16)
    byte2int.append(v2int)
    if  a<len(payload)/2-1:        
        x=v2int^x
   
    a+=1

if x!=byte2int[21]:
    print("checksum is invalid, the last digit is %s (%s) but xor result is %s (%s)" %(byte2int[21],byte[21],x, hex(x)))
else:

    print("checksum is valid, the last digit is %s (%s)" %(byte2int[21],byte[21]))

