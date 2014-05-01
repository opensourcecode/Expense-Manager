# This is to plot the expenses over time or to create a pie chart for expenditure over various categories
# The categories are [TRAVEL, FOOD, GROCERY, MEDICAL, CONVEYANCE, MISC]

#import db
import matplotlib.pyplot as plt
import numpy as np

categories = ["TRAVEL", "FOOD", "GROCERY", "MEDICAL", "CONVEYANCE", "MISC"]
days = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":30, "September":30, "October":31, "November":30, "December":31}

#######################################################################################################################
def draw_pie_chart(xlist, ylist):
	x = tuple(xlist)
	y = tuple(ylist)
	plt.figure(figsize = (8, 8))
	exp = (0.1,)*len(x)
	plt.pie(y, explode = exp, labels = x, autopct = '%1.1f%%', shadow = True)
	plt.title('Expenses')
	plt.show()

#######################################################################################################################

def draw_bar_chart_categories(xlist, ylist):
	N = len(xlist)
	yvalues = tuple(ylist)
	std = (2,)*N

	ind = np.arange(N)
	width = 0.35

	fig, ax = plt.subplots()
	bar1 = ax.bar(ind + width/2.0, yvalues, width, color='b', yerr=std)

	ax.set_ylabel('Total money spent')
	ax.set_title('Expenses')
	ax.set_xticks(ind+width)
	xl = tuple(xlist)
	ax.set_xticklabels(xl)

	plt.show()




#######################################################################################################################

def draw_pie_chart_for_year(xlist, ylist):
	xlist = months
	ylist = db.get_monthly_total_for_a_year(year)
	plt.figure(figsize = (8, 8))
	exp = (0.1) * 12
	plt.pie(ylist, explode = exp, labels = xlist, autopct = '%1.1f%%', shadow = True)
	plt.title('Expenses')
	show()

#######################################################################################################################

def draw_bar_chart_year(year):
	n_groups = 12

	means_men = (20, 35, 30, 35, 27, 33, 20, 35, 30, 35, 27, 33)
	std_men = (2, 3, 4, 1, 2, 2, 2, 3, 4, 1, 2, 2)

	index = np.arange(n_groups)
	bar_width = 0.35

	opacity = 0.4
	error_config = {'ecolor': '0.3'}

	rects1 = plt.bar(index, means_men, bar_width,
	                 alpha=opacity,
	                 yerr = std_men,
	                 color='b',
	                 error_kw=error_config,
	                 label='Expenses')

	plt.xlabel('Months')
	plt.ylabel('Total Money Spent')
	plt.title('Expenses for the year' + year)
	plt.xticks(index + bar_width, ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))
	plt.legend()

	plt.tight_layout()
	plt.show()	

#######################################################################################################################

