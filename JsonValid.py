import json
import re


# JSON validator by check regex
def jason_aws_validator_regex(path: str) -> bool:
    with open(path, 'r') as file:
        data = file.read()

    if re.search(r'\s*"Resource"\s*:\s*"\*"\s*', data):
        return False
    return True


# JSON validator by check objects
def jason_aws_validator_obj(path: str) -> bool:
    with open(path, 'r') as file:
        data = json.load(file)

    if 'PolicyDocument' in data:
        if 'Statement' in data['PolicyDocument']:
            for state in data['PolicyDocument']['Statement']:
                if 'Resource' in state:
                    if state['Resource'] == '*':
                        return False
    return True
