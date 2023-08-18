basic=float(input())
if basic<=10000:
    hra=0.8*basic
    da=0.2*basic
elif basic<=20000:
    hra=0.9*basic
    da=0.25*basic
else:
    hra=0.95*basic
    da=0.3*basic
gs=basic+hra+da
print(f"{gs:.2f}")