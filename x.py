from datetime import date
from dateutil.relativedelta import relativedelta

one_month = date.today() + relativedelta( weeks = +1)

print str(one_month)

print date.today()
counter = 2
print 'hi' + str(counter)
