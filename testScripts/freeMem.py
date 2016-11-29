import psutil

memory = psutil.virtual_memory()
free_memory = memory[4] / 1024 ** 2
print(free_memory)
