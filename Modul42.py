result=[]
def main():#code that will determine the number of module
    for i in range(0,10):
        x=int(input())
        y=x%42
        result.append(y)
    print(len(set(result)))
main()
