import time
import pandas as pd
import numpy as np
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
 
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
        city = input("Please, insert the name of a city: ").lower()
        if city == 'chicago' or city=='new york city' or city=='washington':
            break
        else:
            print("You can only input: chicago, new york city or washington")
 
 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please, insert the name of a month: ").lower()
        if month == 'all' or month == 'january' or month == 'february' or month == 'march' or month =='april' or month == 'may' or month =='june':
            break
        else:
            print("You can only input the name of the first six months or the word all")
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day  = input("Please, insert the day of week: ").lower()
        if day == 'all' or day =='monday' or day =='tuesday' or day =='thursday' or day =='wednesday' or day =='friday' or day =='saturday' or day==day =='sunday':
            break
        else:
            print("You can only input the name of the days of weeks or the word all")
 
 
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
 
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
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
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[df['month'].mode()[0] - 1]
    print('The most common month is "{}"'.format(most_common_month.title()))
 
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is "{}"'.format(common_day.title()))
 
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the Start Time column to datetime
    df['hour'] = df['Start Time'].dt.hour # extract hour from the Start Time column to create an hour column
    popular_hour = df['hour'].mode()[0]  # find the most popular hour
    print('The most common start hour is "{}"'.format(popular_hour))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]  # find the most popular hour
    print('The most used start station is "{}"'.format(popular_start_station))
 
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]  # find the most popular hour
    print('The most used end station is "{}"'.format(popular_end_station))
 
    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station']+'"'+ " and " + '"' +df['End Station']
    popular_station_combination = df['station_combination'].mode()[0]
    print('The most frequent combination of stations are "{}"'.format(popular_station_combination))
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    # TO DO: display total travel time
    travel_time_seconds = int(df['Trip Duration'].sum())
    travel_time_minutes = int(travel_time_seconds / 60)
    travel_time_hours = int(travel_time_seconds / (60 * 60))
    print('The total travel time in seconds: {} sec'.format(travel_time_seconds))
    print('The total travel time in minutes: {} min'.format(travel_time_minutes))
    print('The total travel time in hours:   {} hrs'.format(travel_time_hours))
    print('\n')
 
    # TO DO: display mean travel time
    mean_travel_time_seconds = int(df['Trip Duration'].mean())
    mean_travel_time_minutes = round(mean_travel_time_seconds / 60, 2)
    mean_travel_time_hours = round(mean_travel_time_seconds / (60 * 60), 2)
    print('The mean travel time in seconds: {} sec '.format(mean_travel_time_seconds))
    print('The mean travel time in minutes: {} min'.format(mean_travel_time_minutes))
    print('The mean travel time in hours:   {} hrs'.format(mean_travel_time_hours))
 
 
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types:\n{}'.format(user_types))
    print('\n')
 
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Count of genders:\n{}'.format(gender_count))
        print("\n")
 
    except Exception:
        print("For the city selected there aren't gender data")
 
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year   = int(df['Birth Year'].max())
        common_year   = int(df['Birth Year'].mode()[0])
        print('The earlies year of birth is "{}"'.format(earliest_year))
        print('The most recent year of birth is "{}"'.format(recent_year))
        print('The most common year of birth is "{}"'.format(common_year))
 
    except Exception:
        print("\nFor the city selected there aren't birth year data")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def get_raw_data(df):
    """Ask to visualize raw data"""
    
    print('\nHello! Let\'s explore raw US bikeshare data!')
    start_time = time.time()
 
    # TO DO: get user input for visualize row data
    start = 0
    end = 5
    while True:
        while True:
            answer = input("\nDo you want visualize five rows of raw data?\n Answer yes or no: ").lower()
            if answer == 'yes' or answer =='no':
                break
            else:
                print("You can only input: yes or no")

        if answer == 'yes':
            print(df.iloc[start:end])
            start += 5
            end += 5
            if end > df.shape[0] + 1:
                break
        else:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_raw_data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
 
if __name__ == "__main__":
        main()