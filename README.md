# Recursion Review

## What is recursion?
Solving a problem by solving smaller versions of the same problem. A recursive function is one that calls itself.

One mathematical practice that mirrors the structure of a recursive function is an inductive proof. If you've used this, a lot of these concepts may be familiar to you.

In an inductive proof, you can prove that something is true for all natural numbers _N_ by proving that:

* It is true for the first natural number (0 or 1) (this is called the **basis** or **base case**)
* It is true for arbitrary natural number _n_ and _n_ + 1 (this is called the **inductive step**)

By the same token, a recursive function has:

* A **base case**. This is a defined solution that will not call the function again. (This is where the function stops.)
* A **reduction step**. This relates the problem to a smaller subproblem of the same function. (Converges to the base case enventually)

Let's think about writing a recursive program that performs a simple countdown.

What is the base case?
What is the reduction step?

###Method signature:
```
def countdown(n):
  # method body goes here
```

10 minutes for working.
Want to use Python? Try http://www.skulpt.org/

###Desired output
```
countdown(10)
10
9
8
7
6
5
4
3
2
1
BLASTOFF!
```

Go over the solutions together.

##Pitfalls

* Make sure that you have a base case and that you will always hit it. Otherwise the program will loop infinitely.
  * What's wrong here?
  ```
    def countdown(n):
      if n == 0:
        print "BLASTOFF!"
      else:
        print n
        countdown(n-1)
  ```
* Make sure that your problem is actually getting smaller each time.

##Next problem: Factorial
Remember these? https://en.wikipedia.org/wiki/Factorial
> 3! = 3 * 2 * 1
> 5! = 5 * 4 * 3 * 2 * 1

And so on...

Let's write it.
What is the base case?
What is the reduction step?

###Method signature:
```
def countdown(n):
  # method body goes here
```

Need that site again? It's http://www.skulpt.org/
