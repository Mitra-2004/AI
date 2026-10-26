# Write  program to solve the tower of hanoi of using recursion.
def hanoi(n, source, auxilliary, destination):
    if n == 1:
        print("Move disk 1 from " , source , "to" , destination)
        return
    
    hanoi(n-1 , source, auxilliary , destination )
    print("Move disk " , n , "from " , source , "to " , destination )
    hanoi ( n-1 , auxilliary, source , destination )


n=int(input("Enter the number of disks:"))
hanoi(n,'A','B','C')

    
