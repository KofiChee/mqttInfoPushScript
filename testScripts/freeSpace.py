import os

print("Gathering info...\n")
s = os.statvfs('/')
freeSpace = float(s.f_bavail * s.f_frsize)
freeSpace /= 1024 ** 2
print(str(freeSpace) +  " megabytes available")
