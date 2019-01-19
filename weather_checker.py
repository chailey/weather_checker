import requests
import time



def weather_checker_normal():

    loc = input("Where are you?")

    if "," in loc:
        loc1 = loc[0:loc.find(",")+1]
        loc2 = loc[loc.find(",")+1:]
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + loc1 + "," + loc2 + "&appid=03b4149f3b619dcdeea070bee44d1963"
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=03b4149f3b619dcdeea070bee44d1963"
    response = requests.get(url)
    if response.status_code != 200:
        print("You spelled the city wrong [e.g New Yrok] , or you did not type in a city [e.g California], or you did not include a comma between the city and its state/country [e.g New York NY instead of New York, NY] . Try again.")
        return -1
    else:
        json_response = response.json()
        temp = float(json_response["main"]["temp"])
        tempF = round(((temp - 273.15)*(9/5) + 32), 2)
        tempC = round((temp-273.15), 2)
        print("The weather in " + loc + " is currently " + str(tempF) + " degrees Fahrenheit/" + str(tempC) + " degrees Celsius.")
        return 0



def weather_checker_testing(user_input):
    loc = user_input

    if "," in loc:
        loc1 = loc[0:loc.find(",") + 1]
        loc2 = loc[loc.find(",") + 1:]
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + loc1 + "," + loc2 + "&appid=03b4149f3b619dcdeea070bee44d1963"
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=03b4149f3b619dcdeea070bee44d1963"
    response = requests.get(url)
    if response.status_code != 200:
        print("You spelled the city wrong [e.g New Yrok] , or you did not type in a city [e.g California], or you did not include a comma between the city and its state/country [e.g New York NY instead of New York, NY] . Try again.")
        return "Failed"
    else:
        json_response = response.json()
        temp = float(json_response["main"]["temp"])
        tempF = round(((temp - 273.15) * (9 / 5) + 32), 2)
        tempC = round((temp - 273.15), 2)
        print("The weather in " + loc + " is currently " + str(tempF) + " degrees Fahrenheit/" + str(tempC) + " degrees Celsius.")
        return "Passed"


def test():
    print("Begin testing")
    time.sleep(2)
    print("Part 1: These should all be Passes")
    print("User input: chicago... ")
    print(weather_checker_testing("chicago"))
    print("User input: Chicago...")
    print(weather_checker_testing("Chicago"))
    print("User input: Chicago, IL...")
    print(weather_checker_testing("Chicago, IL"))
    print("User input: Los Angeles...")
    print(weather_checker_testing("Los Angeles"))
    print("User input: Los Angeles, USA")
    print(weather_checker_testing("Los Angeles, USA"))
    print("User input: Los Angeles, CA")
    print(weather_checker_testing("Los Angeles, CA"))
    print("User input: beijing...")
    print(weather_checker_testing("beijing"))
    print('\n')
    print('\n')
    time.sleep(3)
    print("Part 2: These should all be Fails")
    print("User input: asdf... ")
    print(weather_checker_testing("asdf"))
    print("User input: -1...")
    print(weather_checker_testing("-1"))
    print("User input: Chicago IL...")
    print(weather_checker_testing("Chicago IL"))
    print("User input: Los anglez")
    print(weather_checker_testing("Los anglez"))
    print("User input: Southern California")
    print(weather_checker_testing("Southern California"))
    print("User input: ILoveDWOLLA")
    print(weather_checker_testing("ILoveDWOLLA"))

    print('\n')
    print('\n')
    print("Testing complete")