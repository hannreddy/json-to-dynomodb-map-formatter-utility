# JSON to DynomoDB MAP formatter utility
Utility for converting JSON data to store in dynamoDB as MAP object

Recently I got a chance to work with DynamoDB and understood the challenge in converting the JSON payload to convert to DynamoDB accepted MAP format.

I have written a utility to do this conversion, you can use this to do the conversion.

Please refer to the AWS documentation for understanding the conversion format.
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#client

## Code for calling the utility class
```
from json_to_ddb_formatter import json_to_ddb_formatter
test = json_to_ddb_formatter(a)
print(test.format_data())
```
