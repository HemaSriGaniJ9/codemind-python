seconds=int(input())
hours=(seconds//3600)
minutes=(seconds-(3600*hours))//60
seconds=(seconds-(3600*hours)-(minutes*60))
print(f"H:M:S-{hours}:{minutes}:{seconds}")
