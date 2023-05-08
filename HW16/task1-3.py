import threading
import time
import requests
import multiprocessing


first_city = "Lviv", "https://api.open-meteo.com/v1/forecast?latitude=49.84&longitude=24.02&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
second_city = "Kyiv", "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
third_city = "Warsaw", "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
fourth_city = "London", "https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.131&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
fifth_city = "Barcelona", "https://api.open-meteo.com/v1/forecast?latitude=41.39&longitude=2.16&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
list_of_today_temperatures = []


def get_weather_forecast(link):
    resp = (requests.get(
        link[1]))
    list_of_temperatures = resp.json()["hourly"]["temperature_2m"]
    average_temperature = (sum(list_of_temperatures) / len(list_of_temperatures))
    print(f"Average temperature in the city {link[0]} - {average_temperature}")
    today_temperature = [link[0], list_of_temperatures[0]]
    list_of_today_temperatures.append(today_temperature)


# looking for the maximum temperature right now
def max_temperature_now():
    max_temperature_today = max(list_of_today_temperatures, key=lambda x: x[1])
    print(f"Now the hottest in {max_temperature_today[0]} - {max_temperature_today[1]}")


# with threads=========================================================
def threads_method():
    threads = []
    start_threads_time = time.time()
    t1 = threading.Thread(target=get_weather_forecast(first_city))
    t2 = threading.Thread(target=get_weather_forecast(second_city))
    t3 = threading.Thread(target=get_weather_forecast(third_city))
    t4 = threading.Thread(target=get_weather_forecast(fourth_city))
    t5 = threading.Thread(target=get_weather_forecast(fifth_city))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    threads.append(t5)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_threads_time = time.time()
    max_temperature_now()
    print(f"Program ended in {end_threads_time - start_threads_time}")


# with multiprocessing ================================================
def multiproc_method():
    print(">>> multiprocessing")
    process = []
    start_multiprocessing_time = time.time()
    m1 = multiprocessing.Process(target=get_weather_forecast(first_city))
    m2 = multiprocessing.Process(target=get_weather_forecast(second_city))
    m3 = multiprocessing.Process(target=get_weather_forecast(third_city))
    m4 = multiprocessing.Process(target=get_weather_forecast(fourth_city))
    m5 = multiprocessing.Process(target=get_weather_forecast(fifth_city))
    process.append(m1)
    process.append(m2)
    process.append(m3)
    process.append(m4)
    process.append(m5)
    for m in process:
        m.start()
    for m in process:
        m.join()
    end_multiprocessing_time = time.time()
    max_temperature_now()
    print(f"Program ended in {end_multiprocessing_time - start_multiprocessing_time}")


if __name__ == "__main__":
    threads_method()
    multiproc_method()
