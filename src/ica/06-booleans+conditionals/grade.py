def percent_to_letter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    assert percent_to_letter(90) == "A"
    assert percent_to_letter(80) == "B"
    assert percent_to_letter(70) == "C"
    assert percent_to_letter(60) == "D"
    assert percent_to_letter(40) == "F"
    print("All tests passed!")