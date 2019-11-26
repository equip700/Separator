import json
fin=open("logins.txt","r")
email=open("email.txt","a")
referal=open("referal.txt","a")
big_string = fin.read()
fin.close()
entries=big_string.split('\n')
link=[]
times = input("How many refs per account?")
def mail():
    for i in range(len(entries)):
        # num=(2*i)
        # e=entries[num]
        # r=entries[(1+num)]
        if i%3==0 and entries[i]!="":
            e=entries[i]
            email.write(e+" "+str(times*20)+"\n")
    print email
def ref():
    for i in range(len(entries)):
        # num=(2*i)
        # e=entries[num]
        # r=entries[(1+num)]
        if i%3==1 and entries[i]!="":
            r=entries[i]
            link.append(r)
            # referal.write(str(link)+"\n")
    referal.write(json.dumps(link)+"\n")
    print referal
    # print link

mail()
ref()