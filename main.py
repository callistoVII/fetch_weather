import json, requests

#code works with zip, while loop doesnt begin again where needed.
print('Welcome to my Weather Program!')
print('')
print('')

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "60d881cc499d9d328ff8e50c021ad6f2"

fetchAgain = "yes"
restartProgram = True

def fetchWeatherData(city, zip_code):
  try:
    if city is not None:
      url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    elif zip_code is not None:
      #zip_code = zip_code + whateverthefuckcountrycode
      url = f"{base_url}?q={zip_code},us&units=imperial&APPID={appid}"
    response = requests.get(url)
    unformatted_data = response.json()
    return unformatted_data
  except Exception as err:
    print(f"Unexpected error occurred, {err}")

def formatWeatherData(city, unformatted_data):
  temp = unformatted_data["main"]["temp"]
  if (city is None):
    city = unformatted_data["name"]
  print(f"The temprature in {city}: {temp}")
  temp_max = unformatted_data["main"]["temp_max"]
  print(f"The high there is: {temp_max}")
  feels_like = unformatted_data["main"]["feels_like"]
  print(
    f"It actually feels more like {city} is {feels_like} degrees, at this time."
  )
  #include more data around the weather conditions
  humidity = unformatted_data["main"]["humidity"]
  print(f"The humidity in {city} is currently: {humidity}%.")
  pressure = unformatted_data["main"]["pressure"]
  print(f"The pressure in {city} is currently {pressure}hPa.")


while restartProgram == True:
  city = None
  zip_code = None

  try:
    user_selection = input(
      "For the weather information on a city, enter 1 - for a zipcode, enter 2: "
    )
    if (user_selection == "1"):
      city = input("Enter the city would you like weather details on: ")
    elif (user_selection == "2"):
      zip_code = input("Enter the 5 digit zipcode, please: ")
    else:
      #these are not the droids you are looking for.
      print("Sorry, the option you have entered will not work.")

    unformatted_data = fetchWeatherData(city, zip_code)
    if unformatted_data is not None:
      formatWeatherData(city, unformatted_data)
    else:
      print("Weather data could not be fetched for the input given. Please try again.")

  except Exception as err:
    print(f"Unexpected error occurred, {err}")

  print("Do you want to try again: Yes or No?")
  fetchAgain = input()

  if fetchAgain.lower() == "yes":
    restartProgram = True
  else:
    print("Thank you for using this program.")
    restartProgram = False