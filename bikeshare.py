import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = { 'january': 1,'jan': 1,'february': 2,'feb': 2,'march': 3,'mar': 3,
                'april': 4,'apr': 4,'may': 5,'ma': 5,'june': 6,'jun': 6}
DAY_DATA = {'monday': 0,'mon': 0,'tuesday': 1,'tues': 1,'wednesday': 2,'wed': 2,'thursday': 3,'thur': 3
            ,'friday': 4,'fri': 4,'saturday': 5,'sat': 5, 'sunday': 6,'sun': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    check=True
    while check:
        city=input("enter the city")
        check=False
    
        if city=="ch":
            city=CITY_DATA["chicago"]
            check=False
            
        elif city=="chicago":
            city=CITY_DATA["chicago"]
            check=False
            
            
        elif city=="new york city":
            city=CITY_DATA["new york city"]
            check=False
        elif city=="newyorkcity":
            city=CITY_DATA["new york city"]
            check=False 
        elif city=="nyc":
            city=CITY_DATA["new york city"]
            check=False
         
        elif city=="new":
            city=CITY_DATA["new york city"]
            check=False
            
        elif city=="washington":
            city=CITY_DATA["washington"]
            check=False
        elif city=="wash":
            city=CITY_DATA["washington"]
            check=False
      
            
        else:
            print("invalid input")
            check=True
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
    day_month_check=True
    month=None
    day=None
    while day_month_check :
        h=input(" enter yes if you want filter  with ?? else enter all")
        
        if h.lower()=="yes" or h.lower()=="yuh":
            temp1=input("enter the month that you want to filter from the next ").lower()
            if temp1 =="all":
                month="all"
            else:
                month=MONTH_DATA[temp1]
            temp2=input("enter the day that you want to filter from the next  or all").lower()
            if temp2 =="all":
                day="all"
            else:
                day=DAY_DATA[temp2]
            day_month_check=False
        elif h.lower()=="all":
            day_month_check=False
            month="all"
            day="all"
        
        else:
            print("invalid input")
            day_month_check=True
        
        


    print('-'*40)
    return city,month,day


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
    df = pd.read_csv(city)
    df['day_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if day != 'all':
        df = df[df['day_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]
    df.drop('day_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month_year'] = pd.to_datetime(df['Start Time']).dt.month
    df["month_year"].value_counts().idxmax()


    # TO DO: display the most common day of week
    df['day_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['day_week'] .value_counts().idxmax()
    


    # TO DO: display the most common start hour
    df['hours'] = pd.to_datetime(df['Start Time']).dt.hour 
    df['hours'].value_counts().idxmax()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df["Start Station"].value_counts().idxmax()


    # TO DO: display most commonly used end station
    df["End Station"].value_counts().idxmax()


    # TO DO: display most frequent combination of start station and end station trip
    most_comb=df["Start Station"] +" to "+df["End Station"]
    most_comb.value_counts().idxmax()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ( pd.to_datetime(df['End Time']).dt.hour-pd.to_datetime(df['Start Time']).dt.hour).sum()


    # TO DO: display mean travel time
    ( pd.to_datetime(df['End Time']).dt.hour-pd.to_datetime(df['Start Time']).dt.hour).mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    df['User Type'].unique().size
    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print(' no gender ')
    else:
        
        df['Gender'].nunique()


    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' not in df:
        print('no birth year .')
    else:
        df["Birth Year"].min()
        df["Birth Year"].max()
        int(df["Birth Year"].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df,i=0,j=5):
    demo5 = input('do you want to see 5 rows enter yes else no').lower()
    ty=None
    
    if demo5=="yes":
        ty=True
    if ty:
       
        print(df.iloc[i:j,:])
        
        demo5=input("another rows?")
        if demo5=="yes":
            
            i+=5
            j+=5
            print(df.iloc[i:j,:])
            
        else:
            return
        

   
    
    
    
    
    
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df) 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
