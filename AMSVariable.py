class AMSVariable:
    
    def __init__(self,Length):
        global element
        global value
        element = [0] * Length
        value = [0] * Length

    def setValue(self,e):
        for i in range(len(element)):
            if (element[i] is (e)):
                value[i] = value[i] + 1


    def getElement(self,i):
        return element[i],value[i]

    def setElement(self,i,e):
        element[i] = e
        value[i] = 1

    def isOnRecord(self,e):
        for i in range(len(element)):
            if (element[i] is (e)):
                return True
        return False

    def printer(self):
        print (element,value)
