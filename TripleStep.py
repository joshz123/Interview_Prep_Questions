#A child is running up a staircase with N steps. H e can either hop up 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
values = {0:0,1:1,2:2,3:4}
def triple_step(n):
    if(n==1):
        return 1
    elif (n==2):
        return 2
    elif (n==3):
        return 4
    elif (n in values):
        return values[n]
    else:
        values[n]= triple_step(n-1)+triple_step(n-2)+triple_step(n-3)
        return values[n]


print(triple_step(110))