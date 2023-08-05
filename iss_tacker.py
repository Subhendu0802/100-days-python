import time
import requests
from datetime import datetime
import smtplib
email=input()
password=input()
lati=21.251385
longi=81.629639
def is_iss_overhead():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_location = response.json()
    iss_latitude=float(iss_location["iss_position"]["latitude"])
    iss_longitude=float(iss_location ["iss_position"] ["longitude"])
    #your position is within +5 or -5 degrees of the iss position
    if lati-5 <= iss_latitude <= lati+5 and longi-5 <= iss_latitude <= longi+5:
        return True

def is_Night():
   
    parameters={
        "lat":lati,
        "lng": longi,
        "formatted":0,
    }
    #response=requests.get("https://api.sunrise-sunset.org/json?lat=21.251385&lng=81.629639")
    response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    #in 24 hr formatr
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=datetime.now().hour
    if time_now>=sunset and time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_Night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login({email}, {password})
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:The UP \n\n THE ISS is above you in the sky")








