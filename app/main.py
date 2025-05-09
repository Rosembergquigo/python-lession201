import utils
import read_csv
import charts 

keys, values = utils.get_population()
print('keys: ', keys)
print('values: ', values)



def run():
    data = read_csv.read_csv('./data.csv')
    data = list(filter(lambda x: x['Continent'] == 'Oceania', data))
    zone = data[0]['Continent']
    countries = list(map(lambda x: x['Country'], data))
    percentage = list(map(lambda x: x['Percentage'], data))
    #charts.generate_bar_chart(countries, percentage)
    charts.generate_pie_chart(countries, percentage, zone)
    '''
    country = input('Enter the country: ')

    result = utils.popultion_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population_api(country)
        charts.generate_bar_chart(labels, values)
    print('result: ', result)'''

#manejar la dualidad de la importacion y script
if __name__ == '__main__': run()