import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','washington','new york city']

MONTHS = ['All','January','February','March','April','May','June','July','August','September','October','November','December']

DAYS = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data! The available cities are')
    print(CITIES)
    print('Please select one city from the above list')
    print('')
    city = input('Enter the value of city : ').lower()
    while city not in ['chicago','washington','new york city']:
        city = input('Invalid city name. Please re enter : ').lower()
    print('-'*40)
    return city

def load_data(city):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    return df

def popular_traveltimes(df):
    print('#1 Popular times of travel \n')
    print('The most common month is : ', MONTHS[df['month'].mode()[0]])
    print('The most common day of the week is :', DAYS[df['day_of_week'].mode()[0]])
    print('The most common hour of the day is : ', df['hour'].mode()[0])
    print('-'*40)

def popular_stations(df):
    print('#2 Popular stations and trip \n')
    print('The most popular start station is : ', df['Start Station'].mode()[0])
    print('The most popular end station is : ', df['End Station'].mode()[0])
    df['route map'] = df['Start Station'] + " " + df['End Station']
    print('The most popular combination of start and end point is : ', df['route map'].mode()[0])
    print('-'*40)

def trip_duration(df):
    print('#3 Trip duration \n')
    print('The total travel time in minutes is : ', (df['Trip Duration'].sum())/60)
    print('The average travel time in minutes is : ', (df['Trip Duration'].mean())/60)
    print('-'*40)

def user_info(df, city):
    print('#4 User info \n')
    print('The count of each user type is : \n', df['User Type'].value_counts())

    if 'Gender' in df:
        print('The total count for each gender : \n', df['Gender'].value_counts())

    if 'Birth Year' in df:
        print('The most recent year of birth is : ', int(df['Birth Year'].max()))
        print('The earliest year of birth is : ', int(df['Birth Year'].min()))
        print('The most common year of birth is : ', int(df['Birth Year'].mode()[0]))   

def raw_data(df):
    
    data = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[data : data+5])
            data += 5

        else:
            break


def main():
    city = get_filters()
    df = load_data(city)
    raw_data(df)
    popular_traveltimes(df)
    popular_stations(df)
    trip_duration(df)
    user_info(df,city)


if __name__ == '__main__':
    main()