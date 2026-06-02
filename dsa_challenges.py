def filter_and_sort_evens(numbers):
    """Takes a list of integers, filters out the odd numbers, and returns a new list sorted in ascending order."""
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_numbers.sort()
    return even_numbers


def count_character_frequency(text):
    """Takes a string, converts it to lowercase, and returns a dictionary with the frequency of each character (case-insensitive)."""

    frequency_dict = {}

    clean_text = text.lower()

    for char in clean_text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

if __name__ == "__main__":
    # Test 1: Numbers List
    task_numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
    sorted_evens = filter_and_sort_evens(task_numbers)
    print("--- Test 1: Filter and Sort Evens ---")
    print(f"Input:  {task_numbers}")
    print(f"Output: {sorted_evens}\n")

    # Test 2: Task String
    task_text = "This my task for Basic Data Structures & Algorithms"
    char_freq = count_character_frequency(task_text)
    print("--- Test 2: Character Frequency ---")
    print(f"Input Text: '{task_text}'")
    print(f"Output Dict: {char_freq}")
