import os

print("PID of current process is :",os.getpid())
print("PID of parent process is :",os.getppid())



"""
1st time run:
PID of current process is : 15348
PID of parent process is : 9140

2nd time run:
PID of current process is : 9532
PID of parent process is : 9140
"""