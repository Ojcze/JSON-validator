import JsonValid


def test_function(func, n_files=5):
    filename_json_template = "testdata{}.json"
    print("Testing validation by function", func.__name__ + "...")
    test_function_correct_results = [
        False,
        True,
        False,
        True,
        False
    ]
    for i in range(n_files):
        print("test", i, end='')
        file_to_test = filename_json_template.format(i)
        assert (func(file_to_test) == test_function_correct_results[i])
        print(" - passed")
    print("Tests passed")


if __name__ == '__main__':
    test_function(JsonValid.json_resource_validator_obj)
    test_function(JsonValid.json_resource_validator_regex)
