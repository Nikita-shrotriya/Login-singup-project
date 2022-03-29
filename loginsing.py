import json
print("welcome to login-signup")
user=input("1.login/2.signup")
if user=="1":
    name=input("enter name:")
    pw=input("enter password:")
    u=0
    l=0
    d=0
    s=0
    for i in pw:
        if (i.isupper()):
            u=1
        if (i.islower()):
            l=1
        if (i.isdigit()):
            d=1
        if "@" in pw or "#" in pw or "$" in pw:
            s=1
    total=u+l+d+s
    if total!=4:
        print("Password should contain atleast one uppercase, loercase, digit, and special character!")
    else:
        pw1=input("enter password for conformation:-")
        if pw==pw1:
            profile=input("enter your sub..")
            gen=input("enter gender:")
            dob=(input("enter date of birth:"))
            gmail=input("enter gmail:")
            dict1={}
            dict2={}
            dict3={}
            dict4={}
            dict5={}
            dict7={}
            dict8={}
            dict9={}
            list=[]
            dict7["name"]=name
            dict8["password"]=pw
            dict1["gen"]=gen
            dict2["dob"]=dob
            dict3["gmail"]=gmail
            dict4.update(dict7)
            dict4.update(dict8)
            dict4.update(dict3)
            dict4.update(dict1)
            dict4.update(dict2)
            dict5["profile"]=dict4
            list.append(dict5)
            with open("loginsignup.json","w") as a:
                json.dump(list,a,indent=4)
            print("your are signed up succesfully")


    
elif user=="2":
    name=input("enter name")
    password=input("enter password")
    with open("loginsignup.json","r") as file:
        a=file.read()
        if name in a:
            print("your name already is exist!")
        else:
            profile=input("enter your sub..")
            gen=input("enter gender:")
            dob=(input("enter date of birth:"))
            gmail=input("enter gmail:")
            dict1={}
            dict2={}
            dict3={}
            dict4={}
            dict5={}
            dict7={}
            dict8={}
            dict9={}
            list=[]
            dict7["name"]=name
            dict8["password"]=password
            dict1["gen"]=gen
            dict2["dob"]=dob
            dict3["gmail"]=gmail
            dict4.update(dict7)
            dict4.update(dict8)
            dict4.update(dict3)
            dict4.update(dict1)
            dict4.update(dict2)
            dict5["profile"]=dict4
            list.append(dict5)
            with open("loginsignup.json","w") as a:
                json.dump(list,a,indent=4)
            print("you are loged in succesfullly")