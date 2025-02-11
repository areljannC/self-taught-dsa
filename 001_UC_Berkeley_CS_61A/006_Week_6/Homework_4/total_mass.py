'''
Implement total_mass which returns the total mass of attachment, a planet or mobile.
'''

from binary_mobile import Mobile, Arm, Planet

# Intuition: use recursion to calculate the mass of a planet; recurse until attachment is a planet
# Implementation: recursion
# Time complexity: O(n)
# Space complexity: O(n)
def total_mass(attachment: Mobile | Planet) -> int | float:
    if isinstance(attachment, Planet): return attachment.mass
    return (total_mass(attachment.left_arm.attachment) +
            total_mass(attachment.right_arm.attachment))

# Test cases by ChatGPT o3-mini-high
def test_total_mass():
    # Test 1: A single planet.
    p = Planet(5)
    # For a planet, total_mass should simply be its mass.
    assert total_mass(p) == 5, f"Expected total mass 5 for planet with mass 5, got {total_mass(p)}"

    # Test 2: A simple mobile with two arms, each holding a planet.
    # left arm holds a planet of mass 2; right arm holds a planet of mass 1.
    m1 = Mobile(Arm(1, Planet(2)), Arm(2, Planet(1)))
    # Total mass should be 2 + 1 = 3.
    assert total_mass(m1) == 3, f"Expected total mass 3, got {total_mass(m1)}"

    # Test 3: A mobile with a nested mobile as an attachment.
    # Construct a mobile whose:
    #   - left arm holds a planet of mass 1.
    #   - right arm holds another mobile that has two arms:
    #         left arm with a planet of mass 3, and
    #         right arm with a planet of mass 2.
    inner_mobile = Mobile(Arm(2, Planet(3)), Arm(3, Planet(2)))
    m2 = Mobile(Arm(5, Planet(1)), Arm(1, inner_mobile))
    # Total mass for m2 should be:
    #   left arm: mass 1;
    #   right arm: mass (3 + 2) = 5;
    # so overall 1 + 5 = 6.
    assert total_mass(m2) == 6, f"Expected total mass 6, got {total_mass(m2)}"

    # Test 4: A more complex mobile combining previous ones.
    # Let m1 be the simple mobile (total mass 3) and m2 be the nested mobile (total mass 6).
    # Create a mobile whose left arm holds m1 and right arm holds m2.
    m3 = Mobile(Arm(4, m1), Arm(2, m2))
    # Total mass for m3 should be total_mass(m1) + total_mass(m2) = 3 + 6 = 9.
    assert total_mass(m3) == 9, f"Expected total mass 9, got {total_mass(m3)}"

if __name__ == '__main__':
    try:
        test_total_mass()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
