# JSON-validator
Project created for recruitment purposes

## How to use
To validate a file JSON use a script as below

~python <path>/JsonValid.py <path/to/json/file>

## Additional information
The script is not fully "idiot-proof"
- File JsonValid.py contains two different functions to check AWS::IAM::Role Policy (validation is according to a specific criterion):
1. by objects structure,
2. by regex.

The JSON validator via object checking is the default.
This is due to one unhandled case yet (I'm not sure if it's even possible)

-The "Resource" field contains a list, but one of the list items is "*"-

regular expression functions need to be improved for this case.
You can still use regex option if you add flag "--regex" as next argument in cmd.
For example: ~python /JsonValid.py <path/to/json/file> --regex