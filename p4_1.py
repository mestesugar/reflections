#! /usr/bin/env python

#================== This line is 79 spaces wide ==============================#\

import pandas
import ggplot
import datetime

def plot_weather_data(turnstile_weather):

    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/\n
    turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving
    you about 1/3 of the actual data in the turnstile_weather dataframe
    '''


    df = turnstile_weather.copy()
        
    # we will remove national holidays from the data. May 30 is Memorial Day,
    # the only national holiday in our data set. Normally this would be done
    # by passing in the data more elegantly, but since this is a bit more
    # constrained, we will simply hard code it into the function.
    national_holidays = ['2011-05-30']
    for holiday in national_holidays:
        df = df[df.DATEn != holiday]

    # add a column to represent the ISO day of the week for each data point.
    df[u'weekday'] = df[u'DATEn'].apply(\
            lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').isoweekday())

    ##now introduce a multiplier variable so that the ENTRIESn_hourly
    ##values can be modified when we have multiple data days. For example
    ##if we have 2 fridays with rain the multiplier is 1/2 so that summing
    ##the modified values will give us the average number of riders
    ##entering the subways system on a rainy friday.

    for day in df.weekday.unique():
        for rain_status in df.rain.unique():

            # number of unique dates with the same weekday and rain status
            u = df[(df.weekday == day) & (df.rain == rain_status)].\
                DATEn.nunique()

            if u != 0:
                multiplier = float(1.0 / u)
            else:
                multiplier = 0

            daily_sum = \
                df[(df.weekday == day) & (df.rain == rain_status)].sum()

            entries_sum = daily_sum.ENTRIESn_hourly

            multiplier_index_list = \
                df[(df.weekday == day) & (df.rain == rain_status)].index

            df.loc[multiplier_index_list, u'ENTRIESn_hourly'] = \
                multiplier * entries_sum

    ##now we have a dataframe wich is ready to be utilized for making our
    ##plot using the data contained within.

    p = ggplot.ggplot(ggplot.aes(x = u'factor(weekday)', \
                                 weight = u'ENTRIESn_hourly', \
                                 fill = u'weekday'),\
                      data = df) +\
        ggplot.geom_bar() +\
        ggplot.facet_grid(x = u'rain', y = u'weekday') +\
        ggplot.ggtitle('Average Ridership on Sunny & Rainy ISO Weekdays')
    print p
    return p


if __name__ == '__main__':
    input_filename = 'turnstile_data_master_with_weather_test.csv'
    output_filename = 'plot.png'
    with open(output_filename, 'wb') as f:
        turnstile_weather = pandas.read_csv(input_filename)
        plot =  plot_weather_data(turnstile_weather)
        ggplot.ggsave(output_filename, plot)
else:
    pass
