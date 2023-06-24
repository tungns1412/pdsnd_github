#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/tungnguyen/Desktop/Udacity/Bike Data/chicago.csv',
              'new york city': '/Users/tungnguyen/Desktop/Udacity/Bike Data/new_york_city.csv',
              'washington': '/Users/tungnguyen/Desktop/Udacity/Bike Data/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city (or Chicago, New York City or Washington) you would like to see data of? ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid city. Pleas enter a valid city name.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input("Please specify which month? (January, February, March, April, May, June or type 'all' if you do not have any preference? ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid month. Please enter a valid month.")
                  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please specify which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' if you do not have any preference? ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid day. Please enter a valid day.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    
    #Filter by month of applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common Month: ", popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day: ", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour: ", popular_hour)


    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station: ", popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common End Station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combined_trip'] = df['Start Station'] + " to " + df['End Station']
    popular_combined_trip = df['combined_trip'].mode()[0]
    print("The most combined trip: ", popular_combined_trip)


    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", round(total_travel_time, 2))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: ", round(mean_travel_time, 2))


    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_count = df['User Type'].value_counts()
    print("\nCounts of user types:\n", users_count)
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if city.lower() != 'washington':
        gender = df['Gender'].value_counts()
        print('\nCount of Genders:\n', gender)
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:\n', int(earliest_year))
        recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:\n', int(recent_year))
        common_year = df['Birth Year'].mode()[0]
        print('\nMost Common Year:\n', int(common_year))
    else:
        print('\nThis dataset does not have Gender or Birth Year information\n')

    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                break
        
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


# In[ ]:




