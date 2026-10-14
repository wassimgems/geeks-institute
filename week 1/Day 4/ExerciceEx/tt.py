brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}
more_on_zara = {
  'creation_date': "1975",
  'number_stores': "10000"
}

brand ['number_stores'] = 2
print(f" clients zaras are {brand['type_of_clothes'][0]} and {brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]} .")
brand ["country_creation"] = 'spain'
if 'intrenational_competitors' in brand :
    brand ['international_competitors'].append('desigual')

del brand ['creation_date']
print(brand ['international_competitors'][2])
print(brand['major_color']['US'])
print(len(brand))
for keys in brand.keys():
    print(keys)
brand.update(more_on_zara)
print(brand['number_stores'])
# l valeur dyal number_stores tbalat man 2 l 10000 


   
