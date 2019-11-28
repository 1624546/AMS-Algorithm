from AMSVariable import AMSVariable
import random
def AMS(K,Lamda,namefile):
    type = int(input("1.file\n2.keyboard\n")) #raw_input
    print(type)
    if (type == 1):
        A = open(namefile).read()
        A = A.split(",")
        length = len(A)
        print("here")
    S = AMSVariable(Lamda)
    i = 0
    while(True):
        if (type == 1):
            if (i < length):
                a = A[i]
            else:
                break;
        elif (type == 2):
            a = input("insert element\n")
            if (a<'a' or a>'z'):
                break;     
            print("at {}".format(i+1))
        if(S.isOnRecord(a)):
            S.setValue(a)
        if(i < Lamda):
            S.setElement(i, a)
            print( "in {} put {}".format(i+1,a))
            print (a)
        else:
            p = random.randrange(0, i)
            if(p<Lamda):
                p = random.randrange(0, Lamda)
                print ("in {} put {}".format(p+1,a))
                S.setElement(p, a)
            else:
                print ("toss element {}".format(a))
        S.printer()
        j = 0
        check = True
        while(j < (Lamda) and check):
            (e,v) = S.getElement(j)
            if(e == 0):
                check = False
            else:
                est = (i+1)*((v**K) - (v - 1)**K)
                print ("for {} the estimation is {}".format(e,est))
            j = j + 1
        print ("\n")
        i = i + 1

AMS(5,2,"fileAMS.txt")