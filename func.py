def city_country(city_name, country_name):
    city_info=city_name+','+country_name
    return city_info.title()

while True:
    print('Tell me where are you from(enter q if you want to quit)')
    country = input('Please input your country:')
    if country == 'q':
        break
    city=input('Please input your city:')
    if city=='q':
        break
    mess=city_country(city, country)
    print(mess)
print('Nice try!')
