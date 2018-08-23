import pandas as pd
t=pd.read_excel("C:/Users/abc/Downloads/dataset(1).xlsx")
List=[]
for x in t.values.tolist():
    if x[2]=='3rd' or x[2]=='4th' :
        flag=True
        for y in x[0].split():
            if y.lower() in x[1].split('@')[0]:
                flag=False
                break
        if flag:
            List.append(x)
    else:
        List.append(x)
newD=pd.DataFrame(List,columns=["Name","Email","Year","Department"])
newD.to_excel("C:/Users/abc/Desktop/test.xlsx")

x=newD.iloc[:,3].tolist().count("ME")+newD.iloc[:,3].tolist().count("ME")
if(x<(0.1*len(newD))):
    print("Sorry but the Towering Constraints cannot be satisfied!")
else:
    print("AI it is !!")
import pandas as pd
t=pd.read_excel("C:/Users/abc/Downloads/dataset(1).xlsx")
List=[]
for x in t.values.tolist():
    if x[2]=='3rd' or x[2]=='4th' :
        flag=True
        for y in x[0].split():
            if y.lower() in x[1].split('@')[0]:
                flag=False
                break
        if flag:
            List.append(x)
    else:
        List.append(x)
newD=pd.DataFrame(List,columns=["Name","Email","Year","Department"])
newD.to_excel("C:/Users/abc/Desktop/test.xlsx")

x=newD.iloc[:,3].tolist().count("ME")+newD.iloc[:,3].tolist().count("ME")
if(x<(0.1*len(newD))):
    print("Sorry but the Towering Constraints cannot be satisfied!")
else:
    print("AI it is !!")
import pandas as pd
t=pd.read_excel("C:/Users/abc/Downloads/dataset(1).xlsx")
List=[]
for x in t.values.tolist():
    if x[2]=='3rd' or x[2]=='4th' :
        flag=True
        for y in x[0].split():
            if y.lower() in x[1].split('@')[0]:
                flag=False
                break
        if flag:
            List.append(x)
    else:
        List.append(x)
newD=pd.DataFrame(List,columns=["Name","Email","Year","Department"])
newD.to_excel("C:/Users/abc/Desktop/test.xlsx")

x=newD.iloc[:,3].tolist().count("ME")+newD.iloc[:,3].tolist().count("ME")
if(x<(0.1*len(newD))):
    print("Sorry but the Towering Constraints cannot be satisfied!")
else:
    print("AI it is !!")

