import numpy as np
import natsort 
import re

#since ytb marks K>1000 and M>100000
#map those chars to numbers
view_conversion_mapping = {
    'K': 1000,
    'M': 1000000
}

#from natsort documentation
#to change K and M to numbers
all_units = "|".join(view_conversion_mapping.keys())
float_re = natsort.numeric_regex_chooser(natsort.FLOAT | natsort.SIGNED)
unit_finder = re.compile(
    r"(\d+.\d*|\d+)([MK])".format(float_re, all_units), re.IGNORECASE)


def sortByTime(ascending, data_frame):
    pass


def sortByView(ascending, data_frame):
    return data_frame.sort_values(by='views', key=lambda v: np.argsort(natsort.index_natsorted(data_frame['views'], key=lambda x: unit_finder.sub(unit_replacer, x))))

def sortByVideoTitle(ascending, data_frame):

    return data_frame.sort_values(by='title', ascending=ascending, key=lambda title: title.str.lower())

def sortByChannel(ascending, data_frame):
    return data_frame.sort_values(by='channel', ascending=ascending, key=lambda channel: channel.str.lower())

def __get_view(view):
    multiplier = view[-1]
    real_views = int(views)
    if(multiplier == 'M'):
        real_views = int(views[:-1])*1000000
    if(multiplier == 'K'):
        real_views = int(views[:-1])*1000
    view=real_views
    #return real_views

#from natsort documentation
#to change K and M to numbers
def unit_replacer(matchobj):
    """
    Given a regex match object, return a replacement string where units are modified
    """
    number = matchobj.group(1)
    unit = matchobj.group(2)

    if unit==None or unit=='':
        new_number = float(number)
        return "{}".format(new_number)
    else:
        new_number = float(number) * view_conversion_mapping[unit]
        return "{}".format(new_number)
