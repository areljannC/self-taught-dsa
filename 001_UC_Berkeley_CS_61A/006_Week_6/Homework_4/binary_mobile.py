'''
We are making a planetarium mobile.
A mobile is a type of hanging sculpture.
A binary mobile consists of two arms.
Each arm is a rod of a certain length, from which hangs either a planet or another mobile.
'''

from __future__ import annotations

class Mobile:
    def __init__(self, left_arm: Arm, right_arm: Arm):
        self._left_arm = left_arm
        self._right_arm = right_arm

    @property
    def left_arm(self) -> Arm:
        return self._left_arm

    @property
    def right_arm(self) -> Arm:
        return self._right_arm

class Arm:
    def __init__(self, length: int | float, attachment: Mobile | Planet):
        assert length > 0, f'Length must be greater than 0.'
        self._length = length
        self._attachment = attachment

    @property
    def length(self) -> int | float:
        return self._length

    @property
    def attachment(self) -> Mobile | Planet:
        return self._attachment

class Planet:
    def __init__(self, mass: int | float):
        assert mass > 0, f'Mass must be greater than 0.'
        self._mass = mass

    @property
    def mass(self) -> int | float:
        return self._mass

# Test cases by ChatGPT o3-mini-high
def test_planet():
    # Test: Creating a planet with valid mass
    p = Planet(10)
    assert p.mass == 10, f"Expected planet mass 10, got {p.mass}"

    # Test: Creating a planet with zero or negative mass should raise an assertion error
    try:
        Planet(0)
    except AssertionError:
        pass
    else:
        raise Exception("Planet with mass 0 should raise an error")

    try:
        Planet(-5)
    except AssertionError:
        pass
    else:
        raise Exception("Planet with negative mass should raise an error")


def test_arm():
    # Prepare an attachment for the arm: a planet.
    p = Planet(5)
    
    # Test: Creating an arm with a valid length and a planet attachment.
    arm1 = Arm(10, p)
    assert arm1.length == 10, f"Expected arm length 10, got {arm1.length}"
    assert arm1.attachment == p, "Expected the attachment of the arm to be the planet p"

    # Test: Creating an arm with a mobile attachment.
    # Create a simple mobile to attach.
    arm_left = Arm(3, p)
    arm_right = Arm(4, p)
    m = Mobile(arm_left, arm_right)
    arm2 = Arm(15, m)
    assert arm2.length == 15, f"Expected arm length 15, got {arm2.length}"
    assert arm2.attachment == m, "Expected the attachment of the arm to be the mobile m"

    # Test: Arm with zero or negative length should raise an assertion error.
    try:
        Arm(0, p)
    except AssertionError:
        pass
    else:
        raise Exception("Arm with length 0 should raise an error")

    try:
        Arm(-1, p)
    except AssertionError:
        pass
    else:
        raise Exception("Arm with negative length should raise an error")


def test_mobile():
    # Prepare planets and arms.
    p1 = Planet(3)
    p2 = Planet(4)
    arm1 = Arm(10, p1)
    arm2 = Arm(15, p2)
    
    # Test: Creating a mobile from two arms.
    m = Mobile(arm1, arm2)
    # Check that the mobile's arms match the ones provided.
    assert m.left_arm == arm1, "Mobile's left arm does not match the expected arm1"
    assert m.right_arm == arm2, "Mobile's right arm does not match the expected arm2"

if __name__ == '__main__':
    try:
        test_planet()
        test_arm()
        test_mobile()
        print('All test cases passed!')
    except AssertionError as error:
       print('A test case failed.') 
       print(error)
