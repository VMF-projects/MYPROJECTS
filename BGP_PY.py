print("""
 ██╗   ██╗███╗   ███╗███████╗
 ██║   ██║████╗ ████║██╔════╝
 ██║   ██║██╔████╔██║█████╗
 ╚██╗ ██╔╝██║╚██╔╝██║██╔══╝
  ╚████╔╝ ██║ ╚═╝ ██║██║
   ╚═══╝  ╚═╝     ╚═╝╚═╝   

Bird Guessing Program (ML/AI) v1.0
""")
print("Yes = yes / Enter = no\n")
val1=10
val2=10
val3=10
val4=10
val5=10
val6=10
val7=10
val8=10
val9=10
val10=10
while True:
    print("Choose a thing or a bird\n")
    ask1=input("Feathers?\n").lower()
    ask2=input("Beak?\n").lower()
    ask3=input("Blood?\n").lower()
    ask4=input("Wings?\n").lower()
    ask5=input("Can fly?\n").lower()
    ask6=input("Eyes?\n").lower()
    ask7=input("Legs?\n").lower()
    ask8=input("Nails?\n").lower()
    ask9=input("Has skeleton?\n").lower()
    ask10=input("Alive?\n").lower()
    tval1=ask1=="yes"
    tval2=ask2=="yes"
    tval3=ask3=="yes"
    tval4=ask4=="yes"
    tval5=ask5=="yes"
    tval6=ask6=="yes"
    tval7=ask7=="yes"
    tval8=ask8=="yes"
    tval9=ask9=="yes"
    tval10=ask10=="yes"
    result=0
    if tval1:result+=val1
    if tval2:result +=val2
    if tval3:result +=val3
    if tval4:result +=val4
    if tval5:result +=val5
    if tval6:result +=val6
    if tval7:result +=val7
    if tval8:result +=val8
    if tval9:result +=val9
    if tval10:result +=val10
    if result>50:
        print("Probably a bird\n")
    if result<50:
        print("Probably not a bird\n")
    question=input("Was it a bird?\n").lower()
    if question=="yes":
        if ask1=="yes":
            val1+=0.5
        else:
            val1-=0.5
        if ask2=="yes":
            val2+=0.5
        else:
            val2-=0.5
        if ask3=="yes":
            val3+=0.5
        else:
            val3-=0.5
        if ask4=="yes":
            val4+=0.5
        else:
            val4-=0.5
        if ask5=="yes":
            val5+=0.5
        else:
            val5-=0.5
        if ask6=="yes":
            val6+=0.5
        else:
            val6-=0.5
        if ask7=="yes":
            val7+=0.5
        else:
            val7-=0.5
        if ask8=="yes":
            val8+=0.5
        else:
            val8-=0.5
        if ask9=="yes":
            val9+=0.5
        else:
            val9-=0.5
        if ask10=="yes":
            val10+=0.5
        else:
            val10-=0.5
