# Sprint Challenge: Algorithms

In this week's Sprint you explored and implemented some classic algorithmic
approaches and used them to solve novel problems. You also implemented some
classic and fundamental sorting algorithms and learned about how to go about
evaluating their respective runtimes and performance. This Sprint Challenge aims
to assess your comfort with these topics through exercises that build on the
data structures you implemented and the algorithmic intuition you've started to
build up.

## Instructions

**Read these instructions carefully. Understand exactly what is expected
_before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your Challenge
score is a measure of your ability to work independently using the material
covered throughout this sprint. You need to demonstrate proficiency in the
concepts and objectives that were introduced and that you practiced in the
preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are
encouraged to follow the twenty-minute rule and seek support from your PM and
Instructor in your cohort help channel on Slack. Your submitted work reflects
your proficiency in the concepts and topics that were covered this week.

You have three hours to complete this Sprint Challenge. Plan your time
accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you
ever need to return to old code for any number of reasons) and it also helps
your project manager to more thoroughly assess your work.

## Description

This Sprint Challenge is split into two separate parts that test your ability to
write and analyze algorithms.

### 1. Self-Study/Essay Questions (20% of your score)

For this portion of the sprint challenge, you'll be answering questions posed in
the `Algorithms_Questions.md` document inside the `Self-Study` directory. Write
down your answer and also write down a justification for _why_ you put down that
answer. This could net you some partial credit if your justification is sound
but the answer you put down turns out to not be correct. Add your answers to the
questions in the `Algorithms_Answers.md` file.

### 2. Implement Heapsort (65% of your score)

Inside the `task1` directory you'll find the `heap.py` file with a working
implementation of the heap class--the heap is already written for you.

A heap is a tree-like data structure that can rapidly tell you what the largest
or smallest number is within that set of data.

You have to figure out how to use the heap to implement heapsort.

Some hints:

* Initially when you make a new `Heap` data structure, it is empty.

* You can insert values into the heap with its `insert()` method.

* This is a _max heap_. That is, the `get_max()` and `delete()` methods will
  return the maximum value stored in the heap. In addition `delete()` also
  removes the value from the heap.

* Pseudocode in Wikipedia or elsewhere will be of little use here. Think
  conceptually at first; how could you use this information to sort a list of
  numbers? Then code.

Your `heapsort` function should return a new list containing all of the sorted
data.

Run `python test_heap.py` to run the tests for your `heapsort` function to
ensure that your implementation is correct.

### 3. Analyze some runtimes (15% of your score)

Open up the `Analysis_Answers.md` file. This is where you'll jot down your
answers for the runtimes of the functions you just implemented.

### Stretch Problem: Min versus Max

The heap presented in the code is called a _max heap_, because `delete()` always
returns the maximum value in the heap.

Modify it to be a _min heap_, so that `delete()` always returns the _minimum_
value in the heap. Also change `get_max()` to `get_min()`.

Your heapsort probably broke after you did this. What did you have to modify to
fix it?

How does the time complexity change?

In terms of wall clock time, is the min heap version faster or slower?

### Stretch Problem

Modify the `Heap` class and your `heapsort()` algorithm to run in `O(1)` space.