
import datetime

d1 = datetime.date(2022, 2, 1) #ou datetime avec les heures
d2 = datetime.date(2022, 2, 2)

if d1<d2:
    print("d1 plus vieu que d2")
else:
    print("d1 plus jeune que d2")
    
t1=datetime.time(14, 00, 00)
print(t1)

t2=datetime.date.today()
print(t2)