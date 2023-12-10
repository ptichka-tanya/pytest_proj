from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 5, "word", 3, "some text"], 2, "test") == "word"
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([57, 45, 84, "cat", "dog"], 7, "test") == "test"


def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 0, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], 1, 3) == [2, 3]
    assert arrs.my_slice([51, 7, "cat", "dog", 95, 45, "horse", 3], 2, 2) == []
    assert arrs.my_slice([41, 27, 3, 17, "frog", 8, "some text", True, 56], 4, None) == ["frog", 8, "some text", True, 56]
    assert arrs.my_slice([7, 62, 5, 4, 15, 74], 1, 5) == [62, 5, 4, 15]
    assert arrs.my_slice([1, 2, 3, 4], None, 5) == [1, 2, 3, 4]
    assert arrs.my_slice([], None, 5) == []

