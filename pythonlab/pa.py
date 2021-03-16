#write a python program to convert seconds to day,hour,minutes
second=float(input("enter second"))
minute=second//60
hours=((second//60)//60)
day=(((second//60)//60)//24)
print(f"total minute for given second  is{minute}")
print(f"total hour for given second is{hours}")
print(f"total day for given second is{day}")
