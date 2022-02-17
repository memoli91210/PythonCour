

"""
timestanp(mktime) <===> structure (localtime)

strftime:
%d=> jour (01 a 31)
%m => mois (01 a 12)
%Y => annee (ex 2018)  %y(00 a 99)
%H => heures (00 a 23)
%I => minutes (00 a 59)
%S => secondes (00 a 59)
%p => am/pm

%A (jour semaine)  %a(jour abrege)
%B (mois) %b (mois abrege)

%Z : fuseau horaire
"""




import time

# begin=time.time()
# print("le premier text")

# time.sleep(5)

# print("le premier text")
# end=time.time()

# print(f"temp ecouler: {end-begin}")

#print(time.localtime())

# tps = time.localtime()
# print(tps)

# tps=time.mktime(tps)
# print(tps)


my_time=time.strftime("%d/%m/%y")
print(my_time)