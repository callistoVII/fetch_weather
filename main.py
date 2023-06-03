import json, requests

#a simple greeting
def greet_user():
  """display a simple greeting, and let user know purpose of program."""
  print('Welcome to my Weather Program!')
  print('The purpose of this program is to fetch weather details based on a city, or a zipcode.')
  print('')
  print('') 
  
greet_user()
  
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "60d881cc499d9d328ff8e50c021ad6f2"

fetchAgain = "yes"
restartProgram = True

while restartProgram == True:
  city = None
  zip_code = None
  #try block
  try:
    user_selection = input("For the weather information on a city, enter 1 - for a zipcode, enter 2: ")
    if (user_selection == "1"):
      city = input("Enter the city would you like weather data on: ")
      url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    elif (user_selection == "2"):
      zip_code = input("Enter the 5 digit US zipcode you would like weather data on: ")
      #zip_code = zip_code + US only?
      url = f"{base_url}?q={zip_code},us&units=imperial&APPID={appid}"
    else:
      #these are not the droids you are looking for. 
      print("Sorry, the option you have entered will not work.")
    
    response = requests.get(url)
    unformated_data = response.json()
    temp = unformated_data["main"]["temp"]
    if (city is None):
      city = unformated_data["name"]
    print(f"The temprature in {city}: {temp}")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The high there is: {temp_max}")
    feels_like = unformated_data["main"]["feels_like"]
    print(f"It actually feels more like {city} is {feels_like} degrees, at this time.")
    #include more data around the weather conditions
    humidity = unformated_data["main"]["humidity"]
    print(f"The humidity in {city} is currently: {humidity}%.")
    pressure = unformated_data["main"]["pressure"]
    print(f"The pressure in {city} is currently {pressure}hPa.")  
  except Exception as err:
    print(f"Unexpected error occurred, {err}")
    #print error message

  print("Do you want to try again: Yes or No?")
  fetchAgain = input()
  #loop   
  if fetchAgain.lower() == "yes": 
    restartProgram = True
  else:
    print("Thank you for using this program.")
    restartProgram = False