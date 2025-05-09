def get_population():
    keys =[ 'col', 'bol']
    values = [ 10000, 2000]
    return keys, values

def get_population_api(country_dic):
    population_dic = {
        '2022': int(country_dic['2022Population']),
        '2020': int(country_dic['2020Population']),
    }

    '''
        '2015':  country_dic['2015 Population'],
        '2010': country_dic['2010 Population'],
        '2000': country_dic['2000 Population'],
        '1990': country_dic['1990 Population'],
        '1980': country_dic['1980 Population'],
        '1970': country_dic['1970 Population'],
    '''

    labels = population_dic.keys()
    values = population_dic.values()

    return labels, values

def popultion_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result