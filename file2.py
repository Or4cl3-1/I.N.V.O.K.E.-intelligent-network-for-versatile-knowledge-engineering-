result = 0

# Rest of the code where "x" was replaced with "result"

# Unit tests
def test_result_variable():
    # Assuming the result variable is used in a function calculate_sum
    assert calculate_sum([1, 2, 3]) == 6
    assert calculate_sum([]) == 0
    assert calculate_sum([1 for _ in range(100)]) == 100
