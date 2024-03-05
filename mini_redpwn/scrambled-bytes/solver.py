from scapy.all import rdpcap
import random

packets = rdpcap('capture.pcapng')
data = [ord(bytes(p["UDP"].payload)) for p in packets
        if p.haslayer("UDP")
        and len(p["UDP"].payload)==1
        and p.haslayer("IP")
        and p["IP"].src=="172.17.0.2"
        and p["IP"].dst=="172.17.0.3"
        ]

random.seed(1614044650)
location = [i for i in range(len(data))]
random.shuffle(location)
res = bytearray([0]*len(data))

for i in range(len(data)):
    random.randrange(65536)
    r = random.randrange(256)
    res[location[i]] = data[i]^r


open("out.png", "wb").write(res)
