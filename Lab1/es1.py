'''
Created on Mar 21, 2015

@author: lorenzo
'''
def main ():
    n = int(raw_input("Numero: "))

    flag = True
    for i in range(2, n/2+1 ):
        if n%i == 0 and flag == True:
            print "numero non primo"
            flag = False
    if flag == True: 
        print "numero primo" 


if __name__ == '__main__':
    main()