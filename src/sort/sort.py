import numpy as np
import natsort 

from utils.conversion import views_unit_replacer,views_unit_finder, posted_time_unit_finder, posted_time_conversion


def sortByTime(ascending, data_frame):
    return data_frame.sort_values(by='duration', key=lambda v: np.argsort(natsort.index_natsorted(data_frame['duration'], key=lambda x: posted_time_unit_finder.sub(posted_time_conversion, x))))


def sortByView(ascending, data_frame):
    return data_frame.sort_values(by='views', key=lambda v: np.argsort(natsort.index_natsorted(data_frame['views'], key=lambda x: views_unit_finder.sub(views_unit_replacer, x))))

def sortByVideoTitle(ascending, data_frame):

    return data_frame.sort_values(by='title', ascending=ascending, key=lambda title: title.str.lower())

def sortByChannel(ascending, data_frame):
    return data_frame.sort_values(by='channel', ascending=ascending, key=lambda channel: channel.str.lower())
