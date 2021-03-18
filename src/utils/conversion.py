import natsort
import re


#since ytb marks K>1000 and M>100000
#map those chars to numbers
views_conversion_mapping = {
    'K': 1000,
    'M': 1000000
}

#to change K and M to numbers
all_view_units = "|".join(views_conversion_mapping.keys())
float_re = natsort.numeric_regex_chooser(natsort.FLOAT | natsort.SIGNED)

#regex to match views format 
views_unit_finder = re.compile(
    r"(\d+.\d*|\d+)([MK])".format(float_re, all_view_units), re.IGNORECASE)

#regex to match posted time format
posted_time_unit_finder = re.compile(
    r"(^\d*):?(\d{2}):(\d{2})")


#to change K and M to numbers
def views_unit_replacer(matchobj):
    """
    Given a regex match object, return a replacement string where units are modified
    """
    number = matchobj.group(1)
    unit = matchobj.group(2)

    if unit==None or unit=='':
        new_number = float(number)
        return "{}".format(new_number)
    else:
        new_number = float(number) * views_conversion_mapping[unit]
        return "{}".format(new_number)


def posted_time_conversion(matchobj):
    hour = matchobj.group(1)
    min = matchobj.group(2)
    sec = matchobj.group(3)
    #print(matchobj.group(1))
    lista =  [0,1,2,3,4,5,6,7,8,9]
    time_in_min = int(min)*60+int(sec)
    if hour !='':
        time_in_min+=int(hour)*360
    print(time_in_min)
    return "{}".format(time_in_min)