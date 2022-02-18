def solve(heads,legs):
    error="No solution"
    chicken=0
    rabbit=0
    
    if(heads>=legs):
        print(error)
    elif(legs%2!=0):
        print(error)
    else:
        rabbit=(legs-2*heads)/2
        chicken=heads-rabbit
        print(int(chicken),int(rabbit))
solve(35,94)
