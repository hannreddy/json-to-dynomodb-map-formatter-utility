__author__ = "Hanumanth Reddy Aredla"
__version__ = "1.0"
__maintainer__ = "Hanumanth Reddy Aredla"
__email__ = "hann.reddy@gmail.com"


class json_to_ddb_formatter:
    """
    DynamoDB needs extra formatting to JSON data to be stored in a Attribute of type MAP.
    So formatting to DynamoDB accepted format and also reformatting DynamoDB MAP data to JSON data is a regular activity.

    I have handled both the formattings. Utility to convert DynamoDB MAP data to JSON is available at:
    https://github.com/hannreddy/Dynamodb-map-to-JSON-formatter

    This utility class is used to convert any json payload into dynamodb accepted map data format.

    Please refer to AWS documentation for understanding the dynamodb accepted format.
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#client
    """

    def __init__(self, input_payload):
        self.formatted_payload = {}
        self.input_payload = input_payload

    def format_data(self):
        """
        Processing the data
            Input: JSON object
            Output: JSON object in DnamoDB supported format
        """
        if type(self.input_payload) == dict:
            self.formatted_payload["M"] = self.map_formatter(self.input_payload)
        elif type(self.input_payload) == list:
            self.formatted_payload["L"] = self.list_formatter(self.input_payload)
        elif type(self.input_payload) == str:
            self.formatted_payload = self.string_formatter(self.input_payload)
        elif type(self.input_payload) == int or type(self.input_payload) == float:
            self.formatted_payload = self.number_formatter(self.input_payload)
        elif type(self.input_payload) == bool:
            self.formatted_payload = self.boolean_formatter(self.input_payload)
        return self.formatted_payload

    def string_formatter(self, data):
        """
        Takes string as input and converts it to ddb format
        i.e. {
            "S": "....."
        }
        """
        return {"S": data}

    def number_formatter(self, data):
        """
        Takes number as input and converts it to ddb format
        i.e. {
            "N": "23.23"
        }
        """
        return {"N": str(data)}

    def boolean_formatter(self, data):
        """
        Takes boolean as input and converts it to ddb format
        i.e. {
            "BOOL": true/false
        }
        """
        return {"BOOL": data}

    def map_formatter(self, data):
        """
        Recursion is used for processing dict data
        """
        temp_dict = {}
        for item in data:
            if type(data[item]) == dict:
                temp_dict[item] = {"M": self.map_formatter(data[item])}
            elif type(data[item]) == list:
                temp_dict[item] = {"L": self.list_formatter(data[item])}
            elif type(data[item]) == str:
                temp_dict[item] = self.string_formatter(data[item])
            elif type(data[item]) == int or type(data[item]) == float:
                temp_dict[item] = self.number_formatter(data[item])
            elif type(data[item]) == bool:
                temp_dict[item] = self.boolean_formatter(data[item])
        return temp_dict

    def list_formatter(self, data):
        """
        Recursion is used for processing List data
        """
        temp_list = []
        for item in data:
            if type(item) == dict:
                temp_list.append({"M": self.map_formatter(item)})
            elif type(item) == list:
                temp_list.append({"L": self.list_formatter(item)})
            elif type(item) == str:
                temp_list.append(self.string_formatter(item))
            elif type(item) == int or type(item) == float:
                temp_list.append(self.number_formatter(item))
            elif type(item) == bool:
                temp_list.append(self.boolean_formatter(item))
        return temp_list
