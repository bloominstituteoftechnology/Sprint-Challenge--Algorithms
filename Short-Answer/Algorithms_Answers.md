#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a). First line is setting `a` to zero. This is a constant time operation. Setting memory to some new value 0(1)

    Second Line `while  (a < n * n * n):` This while loop will continue until the condiditon is true. In this case its `a < n * n * n`. Comparing the variable a to n^3. As long as a is less than n * n * n the loop will continue giving this an operation od 0(1).

    third Line: is setting a to a new value and increasing by one. This operation is 0(1) because it pretty simular to the first line

    0(1) + 0(2) + 0(1) = 0(n2)



b) First Line: We are setting a counter called sum and equaling that to 0. We are hard coding the value and this is hapening in constant time with a operation of 0(1)
    Second line: We are traversing through the list on `n`. We are going through every single element until we get to the end. This happens more thanonces and its changing the value of n, giving this a operation of 0(n)

    third Line: once again we are setting a variable to a new value. This always will be a constant time operation of 0(1)

    forth line: here is another loop. This loop is compaing the value of j to the lenght of `n`. If this remains true the while loop will keep excuting until it is false. `while j < n:` this is an 0(Log n) operation because of the loop and compaing the values.

    fifth line is taking j and multiplying the results. This only happens if `j` is less than `n`if it is j will multiple by two(j = j * 2 ). So the data is changing as long as this condiditon remains true. 
    0(2) operation 

    six line: this is an 0(1) operation becasue we are taking the sum variable and adding one to it.

    0(1) + 0(n) * 0(1) + 0(Log n) * 0(1) = 0(log n2)

c) first line if compaing the n value and 0. 0(1) operation

    Second line: return 0 if bunnies == 0 0(1) operation

    0(1) + 0(1) = 0(2)

## Exercise II

def Min_broken(floorArr, eggs):
    1). for i in floorArr <--Length of the array
            This is 0(2) because this is a loop and 
            it has to traverse through the entire arr

    2). Set highest floor to a variable `0(1)`    
        * This is calculated to 0(1) because all we are
        doinf is setting a variable to a value. the data
        is unaffected by this and it is happening in contant time.
    
    3). if on the highest floor `f and g` break 
    eggs 
        * This is comparing to see what floor are we on
        and if we are on the highest floor and drop an egg, the egg will break. This is an 0(1) time complexity 

        * because we are just comparing two things that
        will give us one result true or false



    
    4). else dont break
        * If we are not on the highest floor then the egg doesn't break is 0(1)

        0(2) + 0(1) + 0(1) + 0(1) = 0(2) in this case Big o only cares about the biggest term here which is 0(2)

