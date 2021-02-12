# -*- coding: utf-8 -*-
import lxml.html
from urllib.parse import urlencode


def form_encode(form, half_link):
    root = lxml.html.fromstring(form)
    data = {}
    for el in root.xpath('.//input'):
        data[el.get('name')] = el.get('value')
    qstr = urlencode(data)
    form_str = f'{half_link}?{qstr}'
    new_str = form_str[:-48]
    return new_str


def fix_wh(form, half_link):
    root = lxml.html.fromstring(form)
    data = {}
    for el in root.xpath('.//input'):
        data[el.get('name')] = el.get('value')
    qstr = urlencode(data)
    form_str = f'{half_link}?{qstr}'
    new_str = form_str[:-54]
    return new_str


def OpenBox(form, half_link):
    root = lxml.html.fromstring(form)
    data = {}
    for el in root.xpath('.//input'):
        data[el.get('name')] = el.get('value')
    qstr = urlencode(data)
    form_str = f'{half_link}?{qstr}'
    return form_str



