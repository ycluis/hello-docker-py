from datetime import datetime
import json


def main():
    print("Hello Docker!")

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Current date and time: {dt_string}")


if __name__ == "__main__":
    main()
    print(json.dumps({"complete": 1, "code": 0}))
