import datetime
import json

def write_logs(data):
    with open("first.txt", "w") as file:
        file.write(data)

def division():
    first = int
    second = int
    try:
        first = int(input("first number: "))
        second = int(input("second number: "))
        print(first / second)

    except Exception as e:
        print("there is some technical error")

        dictdata = {
            "error": str(e),
            "datetime": str(datetime.datetime.now()),
            "function_name": "division",
            "first_number": first,
            "second_number": second
        }

        write_logs(json.dumps(dictdata))   

division()