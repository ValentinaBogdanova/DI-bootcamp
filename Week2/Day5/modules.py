import requests
import time

def measure_time(url):
    starting_time = time.time()    # узнаем стартовое время
    response = requests.get(url)  # чтобы отправить запрос
    ending_time = time.time()     # узноем конечное время
    load_time = ending_time - starting_time
    return load_time 

#print(measure_time("https://www.google.com/")) # 0.6263329982757568
#print(measure_time("https://developers.institute/"))   #0.2979602813720703
print(measure_time("https://www.netflix.com/il/"))  #1.22139573097229
