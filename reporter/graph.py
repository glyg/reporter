import requests
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

LINK = 'http://samples.openweathermap.org/data/2.5/forecast/hourly?id=524901&appid=b6907d289e10d714a6e88b30761fae22'


def get_data(link):
    """Retrieves weather data from openweathermap API
    """
    response = requests.get(link)


    content = json.loads(response.content)
    response.close()
    raw_data = pd.DataFrame(content['list'])

    main_data = pd.DataFrame.from_records(raw_data["main"])
    weather_data_ = raw_data['weather'].apply(lambda seq: seq[0])
    # weather_data_ est une seaquence de dictionnaires
    weather_data = pd.DataFrame.from_records(weather_data_)

    main_data = pd.concat((main_data, weather_data), axis=1)
    main_data.set_index(raw_data['dt_txt'], inplace=True)
    main_data.index = pd.DatetimeIndex(main_data.index)
    return main_data


def make_graph(link=LINK):
    data = get_data(link)
    fig, ax = plt.subplots()
    ax.plot(
        data.index,
        data["temp"] - 273.15)
    fig.savefig('graph.png')
    return fig, ax
