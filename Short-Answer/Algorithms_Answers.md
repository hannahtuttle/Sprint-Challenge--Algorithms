#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0                   
    while (a < n * n * n):  O(n) - its a loop that is true wile a is less than n^3, n does not change only a does
      a = a + n * n         O(1) 

maybe O(n)

b)  sum = 0
    for i in range(n): # O(n)
      j = 1            # O(1)
      while j < n:     # O(n)
        j *= 2         # O(nk) or O(1)?
        sum += 1       # O(1)


answer: maybe O(n)?

c)  def bunnyEars(bunnies):             
      if bunnies == 0:                         
        return 0

      return 2 + bunnyEars(bunnies-1)

    maybe O(n) 

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.


Create a function that takes in an n number of building stories.
    floor zero does not exist, so you have to stop function at 0
find the middle in n and drop an egg and see if it breaks (true/false)
    if true (broken), then you know you are two high
        take the lower half and break it in a half again
        check to see if the egg breaks if true do the same as above
    if false (not broken) the you are too low to find at what floor the egg breaks go high
        take the upper half and split that again. check that floor, based on your results true/false repeat the steps above
    do this until the nth floor == true and nth floor -1 == false

    n = 10
        floor 10
        floor 9 - third test if 2nd test false
        floor 8
        floor 7 - second test if 1st test false
        floor 6
        floor 5 - first test here true/false
        floor 4
        floor 3
        floor 2 - second test if 1st test true
        floor 1

    since i am splitting this and testing just the half i need based on the responces would this be linear? O(n)

