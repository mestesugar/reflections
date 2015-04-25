#! /usr/bin/env python 

#=============================================================================#
## This module is meant to create a much smaller set of data with which to
## experiment.  A small data set will help with the Read Evaluate Print Loop
## (REPL) development process move much faster and use much less computer re-
## sources.
#=============================================================================#


#=========================== 79 spaces wide ==================================#

import re

if __name__ == '__main__': 
    input_filename = 'turnstile_data_master_with_weather.csv'
    output_filename = 'turnstile_data_master_with_weather_test.csv'
    dates = {}
    sample_size = 1
    with open(input_filename, 'r') as f_in:
        with open(output_filename, 'w+') as f_out:	
            header_line= f_in.readline()
            f_out.write(header_line)
            for line in f_in:
                day = re.search(r'2011-05-\S\S', line)
                if day.group(0) not in dates:
                    dates[day.group(0)] = 1
                    f_out.write(line)
                elif dates[day.group(0)] < sample_size:
                    dates[day.group(0)] += 1
                    f_out.write(line)
                else:
                    pass
else:
    pass
