#! /usr/bin/env/ python

#================== This line is 79 spaces wide ==============================#

import ggplot

test_data = ggplot.mtcars.tail(15)
print test_data
##def average_weight(df, x_value, w_value):
##    for x_item in df.x_value.unique():
##        for w_item in df.w_value.unique():
##            print df[(df.x_value == x_item) & (df.w_value == w_item)].sum()            
                
##average_weight(test_data, 'cyl', 'carb')

p = ggplot.ggplot(ggplot.aes(x = 'factor(cyl)'), data = test_data) +\
    ggplot.geom_bar()
##    ggplot.facet_grid(x = u'cyl', y = u'gear')

print p





