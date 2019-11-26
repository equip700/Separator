import json
fin=open("logins.txt","r")
# email=open("email.txt","a")
output=open("output.txt","a")
# referal=open("referal.txt","a")
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
            output.write(e+" "+str(int(times)*20)+"\n")
    print (output)
def ref():
    for i in range(len(entries)):
        # num=(2*i)
        # e=entries[num]
        # r=entries[(1+num)]
        if i%3==1 and entries[i]!="":
            r=entries[i]
            link.append(r)
            # referal.write(str(link)+"\n")
    output.write(json.dumps(link)+"\n")
    print (output)
    # print link

mail()
ref()