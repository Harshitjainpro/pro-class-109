import random
import csv
import plotly.figure_factory as pff
import statistics
count = []
sumResult = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    count.append(i)
    sumResult.append(dice1+dice2)
mean = sum(sumResult)/len(sumResult)
std_dve = statistics.stdev(sumResult)
median = statistics.median(sumResult)
mode = statistics.mode(sumResult)
print("mean", mean)
print("std_dev", std_dve)
print("median", median)
print("mode", mode)
first_std_dev_start, first_std_dev_end = mean-std_dve, mean+std_dve
second_std_dev_start, second_std_dev_end = mean-(2*std_dve), mean+(2*std_dve)
third_std_dev_start, third_std_dev_end = mean-(3*std_dve), mean+(3*std_dve)
list_of_data_1_std_dev = [
    result for result in sumResult if result > first_std_dev_start
    and
    result < first_std_dev_end
]

list_of_data_2_std_dev = [
    result for result in sumResult if result > second_std_dev_start
    and
    result < second_std_dev_end
]

list_of_data_3_std_dev = [
    result for result in sumResult if result > third_std_dev_start
    and
    result < third_std_dev_end
]
print("per of data within 1 std_dev",format(len(list_of_data_1_std_dev)*100.0/len(sumResult)))
print("per of data within 2 std_dev",format(len(list_of_data_2_std_dev)*100.0/len(sumResult)))
print("per of data within 3 std_dev",format(len(list_of_data_3_std_dev)*100.0/len(sumResult)))
fig = pff.create_distplot([sumResult], ["sum"])
fig.show()
