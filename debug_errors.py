def calculate_average(numbers):
    """Calculates the average of a list of numbers."""

    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    # Logical Error: Incorrect average calculation for empty list
    
    try: 
        return total / len(numbers)
    except ZeroDivisionError:
        print("\n[Warning]: Attempted to calculate the average of an empty list!")
    return None
   

def get_list_element(my_list, index):
    """Attempts to return an element from a list at a given index. Catches IndexError (out of bounds) and TypeError (not a list)."""

    try:
        return my_list[index]
    except IndexError:
        print(f"[IndexError Caught]: The index {index} does not exist in this list.")
        return None
    except TypeError:
        print(f"[TypeError Caught]: Expected a list, but received a '{type(my_list).__name__}' instead.")
        return None


if __name__ == "__main__":
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15]
    data3 = []  # This will cause an error

    print(f"Average of data1: {calculate_average(data1)}")
    print(f"Average of data2: {calculate_average(data2)}")
    print(f"Average of data3: {calculate_average(data3)}")
    print("\n")

    print("--- Element Extraction ---")
    sample_list = ["Python", "Git", "VS Code"]

    print("--- Test A: Valid Input ---")
    result_a = get_list_element(sample_list, 1)
    print(f"Result: {result_a}\n")

    print("--- Test B: Out of Bounds Index ---")
    result_b = get_list_element(sample_list, 5)
    print(f"Result: {result_b}\n")

    print("--- Test C: Incorrect Data Type ---")
    result_c = get_list_element(1234567, 2)
    print(f"Result: {result_c}\n")