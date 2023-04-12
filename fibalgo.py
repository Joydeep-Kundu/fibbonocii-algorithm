def fibonacii(num,lis):
    if num==1:
        return lis[1]
    return fibonacii(num-1,[lis[1],lis[0]+lis[1]])

def main():
    print(fibonacii(8,[0,1]))

if __name__=='__main__':
    main()
