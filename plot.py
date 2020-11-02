import matplotlib.pyplot as plt 

# Process 1 points 
x1 = [0,0,20,220,420,2200] 
y1 = [0,1,2,1,0,0] 
# plotting the Process 1 points 
plt.plot(x1, y1, color='green', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 1") 

# Process 2 points 
x2 = [20,200,400,2200] 
y2 = [0,1,0,0] 
# plotting the Process 2 points 
plt.plot(x2, y2, color='yellow', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 2") 

# Process 3 points 
x3 = [200,200,200,200,400,600,2200] 
y3 = [0,1,2,3,2,1,2] 
# plotting the Process 3 points 
plt.plot(x3, y3, color='blue', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 3") 


# Process 3 points 
x4 = [220,220,1630,1660,1690,2150] 
y4 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x4, y4, color='pink', linewidth = 2, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 4") 
# Process 3 points 
x5 = [209,415,416,425,450,750] 
y5 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x5, y5, color='c', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 5") 

# Process 3 points 
x6 = [210,420,601,630,650,900] 
y6 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x6, y6, color='magenta', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 6") 

# Process 3 points 
x7 = [220,422,800,840,862,1100] 
y7 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x7, y7, color='black', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 7") 

# Process 3 points 
x8 = [216,430,1030,1050,1061,1200] 
y8 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x8, y8, color='red', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 8") 

# Process 3 points 
x9 = [219,446,1240,1250,1260,1450] 
y9 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x9, y9, color='cyan', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 9") 

# Process 3 points 
x10 = [240,460,1460,1500,1520,1600] 
y10 = [0,1,2,3,4,4] 
# plotting the Process 3 points 
plt.plot(x10, y10, color='green', linewidth = 1, 
         marker='o', markerfacecolor='black', markersize=6, label = "Process 10") 

# naming the x axis 
plt.xlabel('Time Elapsed(ticks)') 
# naming the y axis 
plt.ylabel('Queue ID') 
# giving a title to my graph 
plt.title('MLFQ for different process!') 


# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

