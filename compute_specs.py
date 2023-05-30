import numpy as np
import matplotlib.pyplot as plt


file = open("log.txt", "r")
data = file.readlines()
file.close()

data_splitted = [line.split("/") for line in data]
print(data_splitted)