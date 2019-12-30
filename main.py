import numpy as np
class gatesvalue():
    x0=[]
    x1=[]
    output=[]
    rate=[]
print("*** Perceptron Learning ***")
print(" ")
print(" ")
print("*** Apply 1 epoch(4 iterations).Use bipolar inputs and hard limiter as the activation functions. ***")
print(" ")
print(" You have to enter 4 (X0) inputs ! ")
i=1
for x in range(4):
    i+=1
    a=input("X0 :")
    gatesvalue.x0.append(a)
print(" ")
print(gatesvalue.x0)
print(" ")
print(" You have to enter 4 (X1) inputs ! ")
i=1
for x in range(4):
    i+=1
    a=input("X1 :")
    gatesvalue.x1.append(a)
print(" ")
print(gatesvalue.x1)
print(" ")
#Now we have to take outputs from user.
print(" You have to enter 4 outputs (gates) ! ")
i=1
for x in range(4):
    i+=1
    a=input("outputs :")
    gatesvalue.output.append(a)
print(" ")
print(gatesvalue.output)
print(" ")
#we have to set w0,w1,threshould(Q) and learning rate(M)
w0=input("Enter to w0 -->  ")
w1=input("Enter to w1 -->  ")
Q=input("Enter to Thresould(Q) -->  ")
M=input("Enter to learning rate(M) -->  ")
print(" ")
print(*"************")
print(*"*** Menu ***")
print(*"************")
print("1-) Show All variables and values")
print("2-) Report the learning result in percentages ")
b=input("--> ")
if b=="1":
    print("X0 VALUES : ")
    print(gatesvalue.x0)
    print(" ")
    print("X1 VALUES : ")
    print(gatesvalue.x1)
    print(" ")
    print("OUTPUT VALUES : ")
    print(gatesvalue.output)
    print(" ")
    print("w0,w1,Q,M VALUES : ")
    print("wo :",w0," ","w1 :",w1," ","Q :",Q," ","M :",M)
elif b=="2":
    print("*** First iterations ***")
    x0=gatesvalue.x0[0]
    x0=float(x0)
    x1=gatesvalue.x1[0]
    x1=float(x1)
    output=gatesvalue.output[0]
    output=float(output)
    w0=float(w0)
    w1=float(w1)
    Q=float(Q)
    M=float(M)
    yt=(x0*w0)+(x1*w1)-(Q)
    if yt>=0:
        yt=1.0
    else:
        yt=-1.0
    print(" ")
    print("f(t) = ",yt)
    if yt==output:
        print(*"EQUAL")
        c=1
        gatesvalue.rate.append(c)
    else:
        print(*"NOT EQUAL")

    print(*"******************")
    w01=(w0)+((M*(output-yt))*x0)
    print(*"******************")
    print("w01 = ",w01)
    print(*"******************")
    print(*"******************")
    w11=(w1)+((M*(output-yt))*x1)
    print(*"******************")
    print("w11 = ",w11)
    print(*"******************")
    print(*"******************")
    print(*"******************")
    print("FIRST STEP IS FINISH ")
    print(" ")
    print("*** Second iterations ***")
    x01=gatesvalue.x0[1]
    x01=float(x01)
    x11=gatesvalue.x1[1]
    x11=float(x11)
    output1=gatesvalue.output[1]
    output1=float(output1)
    yt1=(x01*w01)+(x11*w11)-(Q)
    if yt1>=0:
        yt1=1.0
    else:
        yt1=-1.0
    print(" ")
    print("f(t) = ",yt1)
    if yt1==output1:
        print(*"EQUAL")
        c=1
        gatesvalue.rate.append(c)
    else:
        print(*"NOT EQUAL")

    print(*"******************")
    w02=(w01)+((M*(output1-yt1))*x01)
    print(*"******************")
    print("w02 = ",w02)
    print(*"******************")
    print(*"******************")
    w12=(w11)+((M*(output1-yt1))*x11)
    print(*"******************")
    print("w12 = ",w12)
    print(*"******************")
    print(*"******************")
    print(*"******************")
    print("SECOND STEP IS FINISH ")
    print(" ")
    print("*** Third iterations ***")
    x02=gatesvalue.x0[2]
    x02=float(x02)
    x12=gatesvalue.x1[2]
    x12=float(x12)
    output2=gatesvalue.output[2]
    output2=float(output2)
    yt2=(x02*w02)+(x12*w12)-(Q)
    if yt2>=0:
        yt2=1.0
    else:
        yt2=-1.0
    print(" ")
    print("f(t) = ",yt2)
    if yt2==output2:
        print(*"EQUAL")
        c=1
        gatesvalue.rate.append(c)
    else:
        print(*"NOT EQUAL")

    print(*"******************")
    w03=(w02)+((M*(output2-yt2))*x02)
    print(*"******************")
    print("w03 = ",w03)
    print(*"******************")
    print(*"******************")
    w13=(w12)+((M*(output2-yt2))*x12)
    print(*"******************")
    print("w13 = ",w13)
    print(*"******************")
    print(*"******************")
    print(*"******************")
    print("THIRD STEP IS FINISH ")
    print(" ")
    print("*** Fourth iterations ***")
    x03=gatesvalue.x0[3]
    x03=float(x03)
    x13=gatesvalue.x1[3]
    x13=float(x13)
    output3=gatesvalue.output[3]
    output3=float(output3)
    yt3=(x03*w03)+(x13*w13)-(Q)
    if yt3>=0:
        yt3=1.0
    else:
        yt3=-1.0
    print(" ")
    print("f(t) = ",yt3)
    if yt3==output3:
        print(*"EQUAL")
        c=1
        gatesvalue.rate.append(c)
    else:
        print(*"NOT EQUAL")
    print(*"******************")
    print(*"******************")
    print(*"******************")
    print("FOURTH STEP IS FINISH ")
    print(" ")
    print(" ")
    print(*"******************")
    print(*"******************")
    print(*"******************")
    print("Learning rate is : ")
    len_rate=len(gatesvalue.rate)
    rate=len_rate*25
    print("----> %",rate)


