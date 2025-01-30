"""
Towers of Hanoi A classic puzzle called the Towers of Hanoi is a game that consists
of three rods, and a number of disks of different sizes which can slide onto any rod.

The puzzle starts with n disks in a neat stack in ascending order of size on a start
rod, the smallest at the top, forming a conical shape.

Towees of Hanoi The objective of the puzzle is to move the entire stack to an end rod, obeying the following rules:

  - Only one disk may be moved at a time.
  - Each move consists of taking the top (smallest) disk from one of the rods and sliding it onto another rod, on top of the other disks that may already be present on that rod.
  - No disk may be placed on top of a smaller disk.
    
Complete the definition of move_stack, which prints out the steps required to move n disks from the start rod to the end rod without violating the rules.
The provided print_move function will print out the step to move a single disk from the given origin to the given destination.

  n:     number of disks
  start: a pole position, either 1, 2, or 3
  end:   a pole position, either 1, 2, or 3

There are exactly three poles, and start and end must be different.
Assume that the start pole has at least n disks of increasing size,
and the end pole is either empty or has a top disk larger than the top n start disks.
"""
def print_move(origin: int, destination: int):
    print(f"Move the top stack from rod {origin} to rod {destination}.")

# Comments: I was really close to solving this one. The only thing missing was the usage of aux.
#   This basically dictates which pole stacks move to for the time being.
#   I literally asked ChatGPT about my implementation and it only added the aux variable.
#   The function structure was the exact same so I'm very happy with my improvements in
#   algorithmic thinking approach and implementation to problems I've never seen before.
def move_stack(n: int, start: int, end: int):
    if n == 0: return
    aux = 6 - start - end
    move_stack(n - 1, start, aux)
    print_move(start, end)
    move_stack(n - 1, aux, end)

print("n = 1")
move_stack(1, 1, 3)
print("=======================================")

print("n = 2")
move_stack(2, 1, 3)
print("=======================================")

print("n = 3")
move_stack(3, 1, 3)
print("=======================================")

print("n = 5")
move_stack(5, 1, 3)
print("=======================================")