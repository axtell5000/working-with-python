# Error haandling
# Here we are targetting by error type
while True:
    try:
        age = int(input("How old are you ? "))
        10 / age
        raise ValueError(
            "Please stop mucking around"
        )  # This is manually throwing an error
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError as err:
        print(f"Please enter a number above zero. {err}")
    else:
        print("Thanks")
        break
    finally:
        print("I am finally done !!")
