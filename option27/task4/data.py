import datetime
import json
import re


class Data(object):
    _all_lang = {
        'ru': 'ru-lang.json',
        'en': 'en-lang.json'
    }

    _templates = {}

    def __init__(self, lang='ru', time=datetime.datetime.now()):
        with open(Data._all_lang[lang], 'r', encoding='utf-8') as file_read:
            self._lang = json.loads(file_read.read())
        self.time = time

    def format(self, template: str) -> str:
        templates = Data._templates
        result = template
        for key in templates.keys():
            groups = re.findall(key, template)
            if groups:
                for group in groups:
                    result = result.replace(group, templates[key](g=group, la=self._lang, t=self.time))
        return result

    @staticmethod
    def add_template(temp: str, f):
        Data._templates[temp] = f


def same_low_up_case(origin: str, same: str):
    if origin.islower():
        return same.lower()
    elif origin.isupper():
        return same.upper()
    else:
        return same[0].upper() + same[1:]


def year(**kwargs):
    y = str(kwargs['t'].year)
    size = len(kwargs['g'])
    if size < len(y):
        return y[size:]
    else:
        return y.zfill(size)


def _mm(**kwargs):
    m = str(kwargs['t'].month)
    return m.zfill(2)


def _mon(**kwargs):
    i = kwargs['t'].month
    m = kwargs['la']['month']['short'][i-1]
    return same_low_up_case(kwargs['g'], m)


def _month(**kwargs):
    i = kwargs['t'].month
    m = kwargs['la']['month']['long'][i-1]
    return same_low_up_case(kwargs['g'], m)


def _day(**kwargs):
    i = kwargs['t'].weekday()
    d = kwargs['la']['day']['long'][i]
    return same_low_up_case(kwargs['g'], d)


def _dy(**kwargs):
    i = kwargs['t'].weekday()
    d = kwargs['la']['day']['short'][i]
    return same_low_up_case(kwargs['g'], d)


def _dd(**kwargs):
    d = str(kwargs['t'].day)
    return d.zfill(2)


def _ddd(**kwargs):
    d = str(kwargs['t'].timetuple().tm_yday)
    return d.zfill(3)


def _hour12(**kwargs):
    h = kwargs['t'].hour
    if h < 12:
        suffix = kwargs['la']['12h']['am']
    else:
        suffix = kwargs['la']['12h']['pm']
    h = str(h % 12)
    h = h.zfill(2) + suffix
    return h


def _hour24(**kwargs):
    h = str(kwargs['t'].hour)
    return h.zfill(2)


_functions = {
    'Y[Y]+': year,
    'Year': year,
    'DD': _dd,
    'DDD': _ddd,
    '[Dd][Yy]': _dy,
    'Day|DAY|day': _day,
    'MM': _mm,
    'Month|MONTH|month': _month,
    'Mon|MON|mon': _mon,
    'HH12': _hour12,
    'HH24': _hour24
}

for item in _functions.items():
    Data.add_template(item[0], item[1])
