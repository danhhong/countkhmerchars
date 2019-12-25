#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
រាប់ចំនួនអក្សរដែលប្រើញឹកញាប់ក្នុងអត្ថបទភាសាខ្មែរ
Created on Tue Dec 24 21:12:27 2019
@author: danhhong
"""
khmerchars = ['\u1780','\u1781','\u1782','\u1783','\u1784','\u1785',
    '\u1786','\u1787','\u1788','\u1789','\u178A','\u178B','\u178C',
    '\u178D','\u178E','\u178F','\u1790','\u1791','\u1792','\u1793',
    '\u1794','\u1795','\u1796','\u1797','\u1798','\u1799','\u179A',
    '\u179B','\u179C','\u179D','\u179E','\u179F','\u17A0','\u17A1',
    '\u17A2','\u17A3','\u17A4','\u17A5','\u17A6','\u17A7','\u17A8',
    '\u17A9','\u17AA','\u17AB','\u17AC','\u17AD','\u17AE','\u17AF',
    '\u17B0','\u17B1','\u17B2','\u17B3','\u17B6','\u17B7','\u17B8',
    '\u17B9','\u17BA','\u17BB','\u17BC','\u17BD','\u17BE','\u17BF',
    '\u17C0','\u17C1','\u17C2','\u17C3','\u17C4','\u17C5','\u17C6',
    '\u17C7','\u17C8','\u17C9','\u17CA','\u17CB','\u17CC','\u17CD',
    '\u17CE','\u17CF','\u17D0','\u17D1','\u17D2','\u17D3','\u17D4',
    '\u17D5','\u17D6','\u17D7','\u17D8','\u17D9','\u17DA','\u17DB',
    '\u17DC','\u17DD','\u17E0','\u17E1','\u17E2','\u17E3','\u17E4',
    '\u17E5','\u17E6','\u17E7','\u17E8','\u17E9']

def countchar(char,string):
    result = {}
    count = 0
    for i in string:
        if i == char:
            count = count + 1
            result[char] = count
    return result

def CountKhmerChar(string):
    dictresult = {}
    for i in khmerchars:
        dictresult.update(countchar(i,string))
    #យកចំនួនអក្សរប្រើច្រើនមកខាងលើ
    sortdict = {k: v for k, v in sorted(dictresult.items(),
                                        key=lambda item: item[1], 
                                        reverse=True)}
    resulttext = ''
    for j in sortdict:
        resulttext = resulttext + j + ' : ' + str(sortdict[j]) + ', '
    return resulttext
