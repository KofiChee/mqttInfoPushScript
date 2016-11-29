import psutil

netInfo = psutil.net_io_counters()

mbSent = netInfo[0] / 1024 ** 2
mbRec = netInfo[1] / 1024 ** 2

print(mbSent, mbRec)
