URL = "https://neetcode.io/problems/duplicate-integer/question?list=neetcode150"

def solution(nums: list[int]) -> bool:
    assert len(nums) >= 0
    assert len(nums) <= 10**5
    assert min(nums) >= -10**9
    assert max(nums) <= 10**9
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

assert solution([1,2,3,3])
assert not solution([1,2,3,4])

# NOTE: Analogs of this problem: changing `int` to other primitive types.
# NOTE: Analogs of this problem: changing `int` to non-primitive types.
# NOTE: Analogs of this problem: changing `list` to other compound types.
# e.g. what if the data container is not ordered? Or not iterable?
