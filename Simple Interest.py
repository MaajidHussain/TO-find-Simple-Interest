def SimpleInterest(P,T,R):
    print("Principal is: ",P)
    print("Time is: ",T)
    print("Rate is: ",R)
    SimpleInterest=(P*T*R)/100
    print("Simple for given P,T,R is: ",SimpleInterest)
P=int(input("Enter the principal amount: "))
T=int(input("Enter the Time: "))
R=int(input("Enter the Rate: "))
SimpleInterest(P,T,R)