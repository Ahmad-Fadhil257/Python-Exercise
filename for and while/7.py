total = 0
for a in range(1,6,2):
     print (a,end= " ")# kaya no 5, + nya bermasalah
     total = total + a
     if a < 5:
          print(end="+ ")
print("=",total)