def count_occurrences(lst, value):
    """
    Count the number of occurrences of a value in a list.

    :param lst: List of elements
    :param value: Value to count in the list
    :return: Number of occurrences of the value in the list
    """
    return lst.count(value)

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 2, 2, 5, 2]
    value_to_count = 2
    print(f"The value {value_to_count} occurs {count_occurrences(sample_list, value_to_count)} times in the list.")