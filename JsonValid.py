import json
import re
import sys
import os

# JSON validator by check objects (default)
def json_resource_validator_obj(path: str) -> bool:
    with open(path, 'r') as file:
        data = json.load(file)

    if 'PolicyDocument' in data:
        if 'Statement' in data['PolicyDocument']:
            for state in data['PolicyDocument']['Statement']:
                if 'Resource' in state:
                    if isinstance(state['Resource'], list):
                        for res in state['Resource']:
                            if res == '*':
                                return False
                    else:
                        if state['Resource'] == '*':
                            return False
    return True

# JSON validator by check regex
def json_resource_validator_regex(path: str) -> bool:
    with open(path, 'r') as file:
        data = file.read()

    if re.search(r'\s*"Resource"\s*:\s*"\*"\s*', data):
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No file. Use command with argument like ~", sys.argv[0], "<path/to/file.json>")
        sys.exit(0)
    if not os.path.isfile(sys.argv[1]):
        print(sys.argv[1],"is not a file!")
        sys.exit(0)

    if len(sys.argv) >= 3 and sys.argv[2] == "--regex":
        func = json_resource_validator_regex
    else:
        func = json_resource_validator_obj

    if func(sys.argv[1]):
        print("File is valid")
    else:
        print("File is invalid!")
