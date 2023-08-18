units=int(input())
if units<200:
    uc=1.20
elif units>=200 and units<400:
    uc=1.5
elif units>=400 and units<600:
    uc=1.80
else:
    uc=2.0
bill=uc*units
if bill>400:
    sc=bill*0.15
    tb=bill+sc
    print(f"{tb:.2f}")
else:
    tb=bill+100
    print(f"{tb:.2f}")