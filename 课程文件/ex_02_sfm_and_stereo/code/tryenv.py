ans=[]
with open("environment.yml") as f:
    for a in f.readlines():
        b=a.split("=")
        if(len(b)==3):
            ans.append(b[0]+"="+b[1])
        else:
            ans.append(a)
with open("myenvironment.yml","w") as f:
    for line in ans:
        print(line,file=f)