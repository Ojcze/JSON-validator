import json
import re


# JSON validator by check regex (default)
def json_resource_validator_regex(path: str) -> bool:
    with open(path, 'r') as file:
        data = file.read()

    if re.search(r'\s*"Resource"\s*:\s*"\*"\s*', data):
        return False
    return True


# JSON validator by check objects
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
