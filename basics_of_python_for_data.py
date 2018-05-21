open("US_births_1994-2003_CDC_NCHS.csv").read().split("\n")[0:9]


def read_csv(filename):
    string_list = open(filename).read().split("\n")
    string_list = string_list[1:len(string_list)]
    final_list = []
    for string in string_list:
        int_fields = []
        string_fields = string.split(",")
        for thing in string_fields:
            int_fields.append(int(thing))
        final_list.append(int_fields)
    return(final_list)


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


def month_births(list_of_lists):
    births_per_month = {}
    for l in list_of_lists:
        month = l[1]
        births = l[4]
        if len(births_per_month) < month:
            births_per_month[month] = births
        else:
            births_per_month[month] += births
    return(births_per_month)


cdc_month_births = month_births(cdc_list)


def dow_births(list_of_lists):
    births_per_dow = {}
    for l in list_of_lists:
        dow = l[3]
        births = l[4]
        if dow in births_per_dow.keys():
            births_per_dow[dow] += births
        else:
            births_per_dow[dow] = births
    return(births_per_dow)


cdc_day_births = dow_births(cdc_list)


def calc_counts(data, column):
    births_per = {}
    for l in data:
        per = l[column]
        births = l[4]
        if per in births_per.keys():
            births_per[per] += births
        else:
            births_per[per] = births
    return(births_per)


cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)
