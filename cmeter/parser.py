import re

power = re.compile('\$\{\^\-?[0-9]\}\$')
power_numerical = re.compile('[\-]?[0-9]')
comma = re.compile('^[0-9,-]*')
allowed = "1234567890, "
numerical = "1234567890."


def remove_junk(file):
    result = []
    for line in file:
        current = []
        for c in line:
            if c in allowed:
                current.append(c)
        result.append(''.join(current))
    return [c.split() for c in result]


def strdata_to_float(str):
    #print(str)
    result = ""
    power_test = power.search(str)
    comma_test = comma.match(str)
    result += comma_test.group(0)
    if ',' in result:
        result = right_comma(result)
    number = float(result)
    #print(power_test)
    if power_test:
        pwrz = power_numerical.search(power_test.group(0))
        pwr = pwrz.group(0)
        int_pwr = int(pwr)
        number *= 10**int_pwr
    return number


def right_comma(str):
    result = ""
    for c in str:
        if c == ',':
            result += '.'
            continue
        result += c
    return result
    

def final_data(l):
    result = []
    for subl in l:
        sub_result = []
        for e in subl:
            sub_result += [strdata_to_float(e)]
        result.append(sub_result)
    return result
