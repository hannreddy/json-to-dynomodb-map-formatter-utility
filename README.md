# JSON to DynomoDB MAP formatter utility
Python Utility for converting JSON data to store in dynamoDB as MAP object

Recently I got a chance to work with DynamoDB and understood the challenge in converting the JSON payload to convert to DynamoDB accepted MAP format.
DynamoDB needs adding of value type to the JSON data for storing in a Attribute of type MAP.
So formatting to DynamoDB accepted format and also reformatting DynamoDB MAP data to JSON data is a regular activity.

I have written a utility to do this conversion, you can use this to do the conversion and have included only for common datatypes of python, please feel free to enhance for other field types if needed.
* String
* Int
* Float
* Map
* List
* Boolean

Please refer to the [AWS documentation for understanding the conversion format](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#client).

## Code for calling the utility class
```
  from json_to_ddb_formatter import json_to_ddb_formatter

  test = json_to_ddb_formatter(a)
  print(test.format_data())
```

My other utility to convert DynamoDB MAP data to JSON is available [here](https://github.com/hannreddy/Dynamodb-map-to-JSON-formatter).
