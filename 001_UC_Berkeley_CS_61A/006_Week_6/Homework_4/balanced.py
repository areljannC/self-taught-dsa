'''
Implement the balanced function, which returns whether m is a balanced mobile.
A mobile is balanced if both of the following conditions are met:

    1. The torque applied by its left arm is equal to the torque applied by its right arm.
       The torque of the left arm is the length of the left rod multiplied by the total mass hanging from that rod.
       Likewise for the right.
       For example, if the left arm has a length of 5, and there is a mobile hanging at the end of the left arm of total mass 10, the torque on the left side of our mobile is 50.
    2. Each of the mobiles hanging at the end of its arms is itself balanced.

Planets themselves are balanced, as there is nothing hanging off of them.
'''

from binary_mobile import Mobile, Arm, Planet
from total_mass import total_mass

# Intuition: use recursion to calculate the arm's torque 
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def balanced(m: Mobile | Arm | Planet) -> bool:
    if isinstance(m, Planet): return True # should check on initial function call
    
    # calculate and compare torque of both arms
    left_arm_torque = m.left_arm.length * total_mass(m.left_arm.attachment)
    right_arm_torque = m.right_arm.length * total_mass(m.right_arm.attachment)
    if left_arm_torque != right_arm_torque: return False

    # check if arm attachments are mobile
    if isinstance(m.left_arm.attachment, Mobile) and not balanced(m.left_arm.attachment):
        return False
    if isinstance(m.right_arm.attachment, Mobile) and not balanced(m.right_arm.attachment):
        return False

    return True

# Test cases by ChatGPT o3-mini-high
def test_balanced():
    # --- Test 1: A planet is always balanced ---
    p = Planet(10)
    assert balanced(p) is True, "A planet should be balanced by definition."

    # --- Test 2: A simple balanced mobile ---
    # Left arm: length 3, planet of mass 2 → torque = 3 * 2 = 6
    # Right arm: length 2, planet of mass 3 → torque = 2 * 3 = 6
    m1 = Mobile(Arm(3, Planet(2)), Arm(2, Planet(3)))
    assert balanced(m1) is True, "m1 should be balanced (torque 6 vs. 6)."

    # --- Test 3: A simple unbalanced mobile ---
    # Left arm: length 3, planet of mass 2 → torque = 3 * 2 = 6
    # Right arm: length 2, planet of mass 2 → torque = 2 * 2 = 4
    m2 = Mobile(Arm(3, Planet(2)), Arm(2, Planet(2)))
    assert balanced(m2) is False, "m2 should be unbalanced (torque 6 vs. 4)."

    # --- Test 4: Nested mobiles that are balanced ---
    # Create a mobile t:
    #   Left arm: length 1, planet of mass 2 → torque = 1 * 2 = 2
    #   Right arm: length 2, planet of mass 1 → torque = 2 * 1 = 2
    # Total mass of t = 3, and t is balanced.
    t = Mobile(Arm(1, Planet(2)), Arm(2, Planet(1)))

    # Create an inner mobile:
    #   Left arm: length 2, planet of mass 3 → torque = 2 * 3 = 6
    #   Right arm: length 3, planet of mass 2 → torque = 3 * 2 = 6
    # Total mass = 3 + 2 = 5, balanced.
    inner = Mobile(Arm(2, Planet(3)), Arm(3, Planet(2)))

    # Create a mobile u:
    #   Left arm: length 5, planet of mass 1 → torque = 5 * 1 = 5
    #   Right arm: length 1, attachment is the inner mobile (mass 5) → torque = 1 * 5 = 5
    # Total mass of u = 1 (from the planet) + 5 = 6, u is balanced.
    u = Mobile(Arm(5, Planet(1)), Arm(1, inner))

    # Create a larger mobile v:
    #   Left arm: length 4, attachment is mobile t (mass 3) → torque = 4 * 3 = 12
    #   Right arm: length 2, attachment is mobile u (mass 6) → torque = 2 * 6 = 12
    # v is balanced.
    v = Mobile(Arm(4, t), Arm(2, u))
    assert balanced(t) is True, "Nested mobile t should be balanced."
    assert balanced(u) is True, "Nested mobile u should be balanced."
    assert balanced(v) is True, "Nested mobile v should be balanced."

    # --- Test 5: A nested mobile that is unbalanced ---
    # Create a mobile p where the torques do not match:
    #   Left arm: length 3, attachment t (mass 3) → torque = 3 * 3 = 9
    #   Right arm: length 2, attachment u (mass 6) → torque = 2 * 6 = 12
    p = Mobile(Arm(3, t), Arm(2, u))
    assert balanced(p) is False, "Mobile p should be unbalanced (torque 9 vs. 12)."

if __name__ == '__main__':
    try:
        test_balanced()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
