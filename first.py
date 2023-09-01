import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import requests, json
def get_cor():
    global city
    api_key="2d6daf4222a55b47ca8865ef6713e971"
    city=input("Enter city name: ")
    request_url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
    response=requests.get(request_url)
    coordinates=response.json()
    latitude=coordinates[0]['lat']
    longitude=coordinates[0]['lon']
    return latitude,longitude,city
def get_temp():
    global city
    latitude,longitude,_=get_cor()
    api_key="2d6daf4222a55b47ca8865ef6713e971"
    request_url=f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response=requests.get(request_url)
    data=response.json()
    temp_kelvin=data["main"]["temp"]
    temp_celsius=int(temp_kelvin - 273.15)
    return temp_celsius
def play_game():
    temp_celsius=get_temp()
    a=temp_celsius+20
    b=temp_celsius-20
    moves=7
    print("The Celsius is between ",b,"C and ",a,"C")
    print("guess the celsius in 7 moves")
    while True:
        ch=int(input("Enter your guess:"))
        moves-=1
        if ch>temp_celsius:
            print("Guess too high")
            if moves==0:
                print("Out of moves")
                break
            print("Moves left",moves)
        elif ch<temp_celsius:
            print("Guess too low")
            if moves==0:
                print("Out of moves")
                break
            print("Moves left",moves)
        elif ch==temp_celsius:
            print("Your guessed it right")
            print("Complted in ",moves,"moves")
            break
play_game()