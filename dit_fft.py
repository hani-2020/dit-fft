import numpy as np
import matplotlib.pyplot as plt
import math
def bitsize(x):
    return int(math.log(len(x),2))
def bitrev(x,size):
    binary=bin(x)
    reverse=binary[-1:1:-1]
    reverse=reverse+'0'*(size-len(reverse))
    return int(reverse,2)
def mfft(x):
    l=bitsize(x)
    xrev=[0]*len(x)
    X=[0]*len(x)
    #X1=[0]*len(x)
    #X2=[0]*len(x)
    arr1=[0]*int(len(x)/2)
    arr2=[0]*int(len(x)/2)
    stage=int(math.log(len(x),2))
    for i in range(len(x)):
        xrev[i]=x[bitrev(i,l)]
    for i in range(stage):
        sum=0
        for n in range(2**i):
            arr1[n]=sum
            sum=sum+1
        for n in range(2**i,int(len(x)/2)):
            arr1[n]=arr1[n-(2**i)]+2**(i+1)
        for n in range(int(len(x)/2)):
            arr2[n]=arr1[n]+2**i
        #print(f"{i+1}th stage addition indexes={arr1}")
        #print(f"{i+1}th stage subtraction indexes={arr2}")
        k=0
        w=np.exp(-1j*2*np.pi/2**(i+1))
        for n in range(int(len(x)/2)):
            if k<2**i:
                X[arr1[n]]=xrev[arr2[n]]*(w**k)+xrev[arr1[n]]
                #X1[arr1[n]]=xrev[arr2[n]]*(w**k)+xrev[arr1[n]]
                #print(f"{i+1}th stage addition portion w**k={np.round(w**k,3)}")
                k=k+1
            else:
                k=0
                X[arr1[n]]=xrev[arr2[n]]*(w**k)+xrev[arr1[n]]
                #X1[arr1[n]]=xrev[arr2[n]]*(w**k)+xrev[arr1[n]]
                #print(f"{i+1}th stage addition portion w**k={np.round(w**k,3)}")
                k=k+1
        #print(f"{i+1}th stage addition portion={np.round(X1)}")
        k=0
        for n in range(int(len(x)/2)):
            if k<2**i:
                X[arr2[n]]=xrev[arr1[n]]-(w**k)*xrev[arr2[n]]
                #X2[arr2[n]]=xrev[arr1[n]]-(w**k)*xrev[arr2[n]]
                #print(f"{i+1}th stage subtraction portion w**k={np.round(w**k,3)}")
                k=k+1
            else:
                k=0
                X[arr2[n]]=xrev[arr1[n]]-(w**k)*xrev[arr2[n]]
                #X2[arr2[n]]=xrev[arr1[n]]-(w**k)*xrev[arr2[n]]
                #print(f"{i+1}th stage subtraction portion w**k={np.round(w**k,3)}")
                k=k+1
        #print(f"{i+1}th stage subtraction portion={np.round(X2)}")
        for n in range(len(x)):
            xrev[n]=X[n]
    return np.round(X)
x=[1,2,4,8,16,32,64,128] #Input    
print(mfft(x))
