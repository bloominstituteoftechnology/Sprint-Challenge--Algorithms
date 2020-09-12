#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This appears to be a constant runtime as only one operation if being performed and there are no nested loops. Could be an infinite Loop

b)
I think linear for this one. There IS a nested Loop, but it will not run for the entire duration of N. 

c)
This is a linear runtime. It is a simple loop that  does 1 operation per index.

## Exercise II

This is ridiculous.

I guess what we would do isdrop an egg and if it breaks, return the floor it broke on. If it does not break, we go up a floor and chuck an egg off the side like an idiot. It will surely break, but if it doesnt we repeat the process.

    chuckEggs(f):
    if eggBreaks:
        return f
    else:
    chuckEggs(f + 1)

When turned into real code, this would give us a linear runtime. It would certainly not make it through the full lenghth of n because the egg would break on floor 0 when dropped.


