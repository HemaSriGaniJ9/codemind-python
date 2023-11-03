r,c = map(int,input().split())
mat=[]
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)
s=0
s1=0
for inner_list in mat:
    for every_list in inner_list:
        if every_list%2==0:
            s+=every_list
        else:
            s1+=every_list
        
print(f"{s} {s1}")
    