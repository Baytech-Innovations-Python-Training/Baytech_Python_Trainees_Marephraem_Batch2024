name=input("Name of the employee:")
designation=input("designation:")
if(designation=="manager"):
    BP=16000
    HR=16000*12/100
    DA=16000*40/100
    TA=16000*9/100
    MA=3000
    LIC=1750
    PF=16000*45/100
    GP= BP + HR + DA + TA + MA
    NP= GP - (LIC + PF)
    print("GP:", GP)
    print("NP:", NP)
    print("BP:", BP)
elif(designation=="team_leader"):
    BP=14500
    HR=14500*9/100
    DA=14500*37/100
    TA=14500*6/100
    MA=2250
    LIC=1250
    PF=14500*37/100
    GP = BP + HR + DA + TA + MA
    NP = GP - (LIC + PF)
    print("GP:", GP)
    print("NP:", NP)
    print("BP:", BP)
else:
    BP=10000
    HR=10000*6/100
    DA=10000*33/100
    TA=10000*4.4/100
    MA=1800
    LIC=1000
    PF=10000*32/100
    GP = BP + HR + DA + TA + MA
    NP = GP - (LIC + PF)
    print("GP:", GP)
    print("NP:", NP)
    print("BP:", BP)