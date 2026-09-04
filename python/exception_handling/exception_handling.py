import datetime
import json

def write_logs(data):
    with open("error_log.txt", "a") as file:  
        file.write(data + "\n")

def get_element():
    try:
        numbers = [10, 20, 30]
        index = int(input("Enter index number: "))
        print("Element is:", numbers[index])

    except Exception as e:
        print("Some error occurred")

        error_data = {
            "error": str(e),
            "datetime": str(datetime.datetime.now()),
            "function_name": "get_element",
            "entered_index": index
        }

        write_logs(json.dumps(error_data))

get_element()