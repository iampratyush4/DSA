def rec(data1,data2):

    res=data1+data2
    
    if data1<=data2:
        return rec(data1+1,data2)
    return res



if __name__=="__main__":

    res=0

    print(rec(1,4))

    