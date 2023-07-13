ManagerBP=16000
TeamLeaderBP=14500
ExecutiveBP=10000
Name=input("Enter Your Name:")
print("Designation\n1.Manager\n2.Team Leader\n3.Executive")
Designation=int(input("Select your Designation:"))
if Designation==1:
    HR=(12/100)*ManagerBP
    DA=(40/100)*ManagerBP
    TA=(9/100)*ManagerBP
    MA=3000
    LIC=1750
    PF=(45/100)*ManagerBP
    GP=ManagerBP+HR+DA+TA+MA
    print("Name:",Name)
    print("Designation:Manager")
    print("Basic Pay:",ManagerBP)
    print("Gross Pay:",GP)
    print("Net Pay:",GP-(LIC+PF))
elif Designation==2:
    HR=(9/100)*TeamLeaderBP
    DA=(37/100)*TeamLeaderBP
    TA=(6/100)*TeamLeaderBP
    MA=2250
    LIC=1250
    PF=(37/100)*TeamLeaderBP
    GP=TeamLeaderBP+HR+DA+TA+MA
    print("Name:",Name)
    print("Designation:Team Leader")
    print("Basic Pay:",TeamLeaderBP)
    print("Gross Pay:",GP)
    print("Net Pay:",GP-(LIC+PF))
elif Designation==3:
    HR=(6/100)*ExecutiveBP
    DA=(33/100)*ExecutiveBP
    TA=(4.5/100)*ExecutiveBP
    MA=1800
    LIC=1000
    PF=(32/100)*ExecutiveBP
    GP=ExecutiveBP+HR+DA+TA+MA
    print("Name:",Name)
    print("Designation:Executive")
    print("Basic Pay:",ExecutiveBP)
    print("Gross Pay:",GP)
    print("Net Pay:",GP-(LIC+PF))
else:
    print("Your option is invalid!")
    

    
