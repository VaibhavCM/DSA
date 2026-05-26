# we convert m to cm and cm to m and we store in the dictionary
n=int(input("enter the n value: "))
for i in range(1,n+1):
    m_cm={i:i*100}

    cm_m={i:i/100}

    print("we converting meter to centi meter: ",m_cm)
    print("we converting centi_meter to meter: ",cm_m)