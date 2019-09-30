import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

total_months = []
monthly_profit = {}
Monthly_profit_change = {}
total_amount = 0

print("Financial Analysis")
print("-----------------------------")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_months.append(row[0])

        total = (len(total_months))   

        total_amount = total_amount + int(row[1])

        monthly_profit.update({row[0]:row[1]})

feb2010 = int(monthly_profit["Feb-2010"]) - int(monthly_profit["Jan-2010"]) 
mar2010 = int(monthly_profit["Mar-2010"]) - int(monthly_profit["Feb-2010"])
apr2010 = int(monthly_profit["Apr-2010"]) - int(monthly_profit["Mar-2010"])
may2010 = int(monthly_profit["May-2010"]) - int(monthly_profit["Apr-2010"])
jun2010 = int(monthly_profit["Jun-2010"]) - int(monthly_profit["May-2010"])
jul2010 = int(monthly_profit["Jul-2010"]) - int(monthly_profit["Jun-2010"])
aug2010 = int(monthly_profit["Aug-2010"]) - int(monthly_profit["Jul-2010"])
sep2010 = int(monthly_profit["Sep-2010"]) - int(monthly_profit["Aug-2010"])
oct2010 = int(monthly_profit["Oct-2010"]) - int(monthly_profit["Sep-2010"])
nov2010 = int(monthly_profit["Nov-2010"]) - int(monthly_profit["Oct-2010"])
dec2010 = int(monthly_profit["Dec-2010"]) - int(monthly_profit["Nov-2010"])

jan2011 = int(monthly_profit["Jan-2011"]) - int(monthly_profit["Dec-2010"])
feb2011 = int(monthly_profit["Feb-2011"]) - int(monthly_profit["Jan-2011"]) 
mar2011 = int(monthly_profit["Mar-2011"]) - int(monthly_profit["Feb-2011"])
apr2011 = int(monthly_profit["Apr-2011"]) - int(monthly_profit["Mar-2011"])
may2011 = int(monthly_profit["May-2011"]) - int(monthly_profit["Apr-2011"])
jun2011 = int(monthly_profit["Jun-2011"]) - int(monthly_profit["May-2011"])
jul2011 = int(monthly_profit["Jul-2011"]) - int(monthly_profit["Jun-2011"])
aug2011 = int(monthly_profit["Aug-2011"]) - int(monthly_profit["Jul-2011"])
sep2011 = int(monthly_profit["Sep-2011"]) - int(monthly_profit["Aug-2011"])
oct2011 = int(monthly_profit["Oct-2011"]) - int(monthly_profit["Sep-2011"])
nov2011 = int(monthly_profit["Nov-2011"]) - int(monthly_profit["Oct-2011"])
dec2011 = int(monthly_profit["Dec-2011"]) - int(monthly_profit["Nov-2011"])

jan2012 = int(monthly_profit["Jan-2012"]) - int(monthly_profit["Dec-2011"]) 
feb2012 = int(monthly_profit["Feb-2012"]) - int(monthly_profit["Jan-2012"]) 
mar2012 = int(monthly_profit["Mar-2012"]) - int(monthly_profit["Feb-2012"])
apr2012 = int(monthly_profit["Apr-2012"]) - int(monthly_profit["Mar-2012"])
may2012 = int(monthly_profit["May-2012"]) - int(monthly_profit["Apr-2012"])
jun2012 = int(monthly_profit["Jun-2012"]) - int(monthly_profit["May-2012"])
jul2012 = int(monthly_profit["Jul-2012"]) - int(monthly_profit["Jun-2012"])
aug2012 = int(monthly_profit["Aug-2012"]) - int(monthly_profit["Jul-2012"])
sep2012 = int(monthly_profit["Sep-2012"]) - int(monthly_profit["Aug-2012"])
oct2012 = int(monthly_profit["Oct-2012"]) - int(monthly_profit["Sep-2012"])
nov2012 = int(monthly_profit["Nov-2012"]) - int(monthly_profit["Oct-2012"])
dec2012 = int(monthly_profit["Dec-2012"]) - int(monthly_profit["Nov-2012"])

jan2013 = int(monthly_profit["Jan-2013"]) - int(monthly_profit["Dec-2012"])
feb2013 = int(monthly_profit["Feb-2013"]) - int(monthly_profit["Jan-2013"]) 
mar2013 = int(monthly_profit["Mar-2013"]) - int(monthly_profit["Feb-2013"])
apr2013 = int(monthly_profit["Apr-2013"]) - int(monthly_profit["Mar-2013"])
may2013 = int(monthly_profit["May-2013"]) - int(monthly_profit["Apr-2013"])
jun2013 = int(monthly_profit["Jun-2013"]) - int(monthly_profit["May-2013"])
jul2013 = int(monthly_profit["Jul-2013"]) - int(monthly_profit["Jun-2013"])
aug2013 = int(monthly_profit["Aug-2013"]) - int(monthly_profit["Jul-2013"])
sep2013 = int(monthly_profit["Sep-2013"]) - int(monthly_profit["Aug-2013"])
oct2013 = int(monthly_profit["Oct-2013"]) - int(monthly_profit["Sep-2013"])
nov2013 = int(monthly_profit["Nov-2013"]) - int(monthly_profit["Oct-2013"])
dec2013 = int(monthly_profit["Dec-2013"]) - int(monthly_profit["Nov-2013"])

jan2014 = int(monthly_profit["Jan-2014"]) - int(monthly_profit["Dec-2013"])
feb2014 = int(monthly_profit["Feb-2014"]) - int(monthly_profit["Jan-2014"]) 
mar2014 = int(monthly_profit["Mar-2014"]) - int(monthly_profit["Feb-2014"])
apr2014 = int(monthly_profit["Apr-2014"]) - int(monthly_profit["Mar-2014"])
may2014 = int(monthly_profit["May-2014"]) - int(monthly_profit["Apr-2014"])
jun2014 = int(monthly_profit["Jun-2014"]) - int(monthly_profit["May-2014"])
jul2014 = int(monthly_profit["Jul-2014"]) - int(monthly_profit["Jun-2014"])
aug2014 = int(monthly_profit["Aug-2014"]) - int(monthly_profit["Jul-2014"])
sep2014 = int(monthly_profit["Sep-2014"]) - int(monthly_profit["Aug-2014"])
oct2014 = int(monthly_profit["Oct-2014"]) - int(monthly_profit["Sep-2014"])
nov2014 = int(monthly_profit["Nov-2014"]) - int(monthly_profit["Oct-2014"])
dec2014 = int(monthly_profit["Dec-2014"]) - int(monthly_profit["Nov-2014"])

jan2015 = int(monthly_profit["Jan-2015"]) - int(monthly_profit["Dec-2014"])
feb2015 = int(monthly_profit["Feb-2015"]) - int(monthly_profit["Jan-2015"]) 
mar2015 = int(monthly_profit["Mar-2015"]) - int(monthly_profit["Feb-2015"])
apr2015 = int(monthly_profit["Apr-2015"]) - int(monthly_profit["Mar-2015"])
may2015 = int(monthly_profit["May-2015"]) - int(monthly_profit["Apr-2015"])
jun2015 = int(monthly_profit["Jun-2015"]) - int(monthly_profit["May-2015"])
jul2015 = int(monthly_profit["Jul-2015"]) - int(monthly_profit["Jun-2015"])
aug2015 = int(monthly_profit["Aug-2015"]) - int(monthly_profit["Jul-2015"])
sep2015 = int(monthly_profit["Sep-2015"]) - int(monthly_profit["Aug-2015"])
oct2015 = int(monthly_profit["Oct-2015"]) - int(monthly_profit["Sep-2015"])
nov2015 = int(monthly_profit["Nov-2015"]) - int(monthly_profit["Oct-2015"])
dec2015 = int(monthly_profit["Dec-2015"]) - int(monthly_profit["Nov-2015"])

jan2016 = int(monthly_profit["Jan-2016"]) - int(monthly_profit["Dec-2015"])
feb2016 = int(monthly_profit["Feb-2016"]) - int(monthly_profit["Jan-2016"]) 
mar2016 = int(monthly_profit["Mar-2016"]) - int(monthly_profit["Feb-2016"])
apr2016 = int(monthly_profit["Apr-2016"]) - int(monthly_profit["Mar-2016"])
may2016 = int(monthly_profit["May-2016"]) - int(monthly_profit["Apr-2016"])
jun2016 = int(monthly_profit["Jun-2016"]) - int(monthly_profit["May-2016"])
jul2016 = int(monthly_profit["Jul-2016"]) - int(monthly_profit["Jun-2016"])
aug2016 = int(monthly_profit["Aug-2016"]) - int(monthly_profit["Jul-2016"])
sep2016 = int(monthly_profit["Sep-2016"]) - int(monthly_profit["Aug-2016"])
oct2016 = int(monthly_profit["Oct-2016"]) - int(monthly_profit["Sep-2016"])
nov2016 = int(monthly_profit["Nov-2016"]) - int(monthly_profit["Oct-2016"])
dec2016 = int(monthly_profit["Dec-2016"]) - int(monthly_profit["Nov-2016"])

jan2017 = int(monthly_profit["Jan-2017"]) - int(monthly_profit["Dec-2016"])
feb2017 = int(monthly_profit["Feb-2017"]) - int(monthly_profit["Jan-2017"])

Monthly_profit_change.update({
    "Feb-2010":feb2010, "Mar-2010":mar2010, "Apr-2010":apr2010, "May-2010":may2010, "Jun-2010":jun2010, "Jul-2010":jul2010, "Aug-2010":aug2010, "Sep-2010":sep2010, "Oct-2010":oct2010, "Nov-2010":nov2010, "Dec-2010":dec2010,
    "Jan-2011":jan2011, "Feb-2011":feb2011, "Mar-2011":mar2011, "Apr-2011":apr2011, "May-2011":may2011, "Jun-2011":jun2011, "Jul-2011":jul2011, "Aug-2011":aug2011, "Sep-2011":sep2011, "Oct-2011":oct2011, "Nov-2011":nov2011, "Dec-2011":dec2011,
    "Jan-2012":jan2012, "Feb-2012":feb2012, "Mar-2012":mar2012, "Apr-2012":apr2012, "May-2012":may2012, "Jun-2012":jun2012, "Jul-2012":jul2012, "Aug-2012":aug2012, "Sep-2012":sep2012, "Oct-2012":oct2012, "Nov-2012":nov2012, "Dec-2012":dec2012,
    "Jan-2013":jan2013, "Feb-2013":feb2013, "Mar-2013":mar2013, "Apr-2013":apr2013, "May-2013":may2013, "Jun-2013":jun2013, "Jul-2013":jul2013, "Aug-2013":aug2013, "Sep-2013":sep2013, "Oct-2013":oct2013, "Nov-2013":nov2013, "Dec-2013":dec2013,
    "Jan-2014":jan2014, "Feb-2014":feb2014, "Mar-2014":mar2014, "Apr-2014":apr2014, "May-2014":may2014, "Jun-2014":jun2014, "Jul-2014":jul2014, "Aug-2014":aug2014, "Sep-2014":sep2014, "Oct-2014":oct2014, "Nov-2014":nov2014, "Dec-2014":dec2014,
    "Jan-2015":jan2015, "Feb-2015":feb2015, "Mar-2015":mar2015, "Apr-2015":apr2015, "May-2015":may2015, "Jun-2015":jun2015, "Jul-2015":jul2015, "Aug-2015":aug2015, "Sep-2015":sep2015, "Oct-2015":oct2015, "Nov-2015":nov2015, "Dec-2015":dec2015,
    "Jan-2016":jan2016, "Feb-2016":feb2016, "Mar-2016":mar2016, "Apr-2016":apr2016, "May-2016":may2016, "Jun-2016":jun2016, "Jul-2016":jul2016, "Aug-2016":aug2016, "Sep-2016":sep2016, "Oct-2016":oct2016, "Nov-2016":nov2016, "Dec-2016":dec2016,
    "Jan-2017":jan2017, "Feb-2017":feb2017
    })

average_change = (feb2010 + mar2010 + apr2010 + may2010 + jun2010 + jul2010 + aug2010 + sep2010 + oct2010 + nov2010 + dec2010 +
    jan2011 + feb2011 + mar2011 + apr2011 + may2011 + jun2011 + jul2011 + aug2011 + sep2011 + oct2011 + nov2011 + dec2011 +
    jan2012 + feb2012 + mar2012 + apr2012 + may2012 + jun2012 + jul2012 + aug2012 + sep2012 + oct2012 + nov2012 + dec2012 +
    jan2013 + feb2013 + mar2013 + apr2013 + may2013 + jun2013 + jul2013 + aug2013 + sep2013 + oct2013 + nov2013 + dec2013 +
    jan2014 + feb2014 + mar2014 + apr2014 + may2014 + jun2014 + jul2014 + aug2014 + sep2014 + oct2014 + nov2014 + dec2014 +
    jan2015 + feb2015 + mar2015 + apr2015 + may2015 + jun2015 + jul2015 + aug2015 + sep2015 + oct2015 + nov2015 + dec2015 +
    jan2016 + feb2016 + mar2016 + apr2016 + may2016 + jun2016 + jul2016 + aug2016 + sep2016 + oct2016 + nov2016 + dec2016 +
    jan2017 + feb2017 
    ) / int(total - 1)


print(f"Total Months : {total}")
print(f"Total: ${total_amount}")
print(f"Average Change: $ {round(average_change, 2)}")


max_increase = max(Monthly_profit_change.items(), key=lambda x: x[1])
min_increase = min(Monthly_profit_change.items(), key=lambda x: x[1])

print(f"Greatest Increase in Profits: {max_increase}")
print(f"Minimum Increase in Profits: {min_increase}")






    

