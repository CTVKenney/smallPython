#!/usr/bin/env python3

from math import atan as arctan
from math import tan
from math import tau
import datetime
from dateutil.relativedelta import relativedelta

class Goal:
    def __init__(self, initial, firstjump, maximal, startdate, timestride, name, units):
        """
        Parameters
        ----------
        initial : float
            amount (of exercise, or other habit that can be done to different numeric extents)
        firstjump : float
            the difference between the first and second periods, in terms of amount
        maximal : float
            the asymptotically-approached amount
        startdate : datetime.date
            the initial period
        timestride : datetime.timedelta or str
            the length of a period, or 'month' if counting-by-months is to be used
        name : str
            the name of the goal, e.g. 'Pushups'
        units : str
            the units of the amount of the goal
        """
        self.initial = initial
        self.firstjump = firstjump
        self.maximal = maximal
        self.startdate = startdate
        self.timestride = timestride
        self.name = name
        self.units = units

    def current(self, date):
        """
        Parameters
        ----------
        date : datetime.date
            the date for which the current amount is to be computed
        
        Returns
        -------
        float
            the current amount
        """
        if self.timestride == 'month':
            #Current period will be computed according to what month we're in, with the month of self.startdate being treated as 0

            period = 12*(date.year - self.startdate.year) + (date.month - self.startdate.month)

        else:
            #Current period will be computed according to how many complete steps have been taken, of length self.timestride

            elapsed = date - self.startdate #a datetime.timedelta object

            period = elapsed // self.timestride #an integer, the floor of the time elapsed divided by the length of a period

        return self.initial + 4 * (self.maximal - self.initial) * arctan( period * tan ( tau * self.firstjump / ( 4 * (self.maximal - self.initial) ) ) ) / tau

    def print_today(self, precision = 2):
        current_amount = round(self.current(datetime.date.today()), precision)
        print(f'Goal: {self.name}\nToday\'s Amount: {current_amount} {self.units}\n')


def main():
    my_goals = [Goal(initial = 6.0, firstjump = 0.2, maximal = 20.0, startdate = datetime.date(year = 2022, month = 1, day = 1), timestride = 'month', name = 'Running', units = 'kilometers'),
                Goal(initial = 0.0, firstjump = 5.0, maximal = 100.0, startdate = datetime.date(year = 2022, month = 1, day = 1), timestride = 'month', name = 'Pushups', units = 'reps')]
    
    for goal in my_goals:
        goal.print_today()

if __name__ == '__main__':
    main()
