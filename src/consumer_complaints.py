import datetime as dt
import csv
from collections import defaultdict
from collections import Counter
import math
from operator import itemgetter
from io import StringIO
import sys

# initializing empty 'dictionary of list' & list data structures
dt_format = '%Y-%m-%d'
company_dict = defaultdict(list)
report_list = []
input_file = sys.argv[1]
output_file = sys.argv[2]


def normal_round(n):
    """function for  rounding up float val of  0.5 to 1 & rounding down below 0.5 to 0"""
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


# assigning the file handle to f
# skipping first line of the file as it is header
with open(input_file) as f:
    header = next(f)

    # iterating the file through file_handle instead of creating list Ex: big datasets can lead to memory issues
    for line in f:
        line_str = StringIO(line)
        reader = csv.reader(line_str, delimiter=',')
        # assigning first element to variable since reader returns 2 dimensional list of 1 element i.e [[elements]]
        row = list(reader)[0]
        line_str.close()
        company = row[7].lower()
        date_received = row[0]
        product = row[1]
        date_object = dt.datetime.strptime(date_received, dt_format)
        year = date_object.year
        # formatting product and year attributes into single string for creating unique key
        product_year = "{}~{}".format(product, year).lower()
        company_dict[product_year] = company_dict[product_year] + [company]


# Iterating key(str with product and yr) & value (list of companies) pair from company dictionary
#  to Extract product, yr,total complaints,total no of companies receiving at least one complaint
# & highest % of total complaints filed against one company for that respective product and year
for prod_yr, complaint_list in company_dict.items():
    product, year = prod_yr.split('~')
    complaints_total = len(complaint_list)
    unique_companies = len(set(complaint_list))
    company_freq = Counter(complaint_list)
    complaint_highest = company_freq.most_common(1)[0][1]
    top_percent_total = normal_round((complaint_highest/complaints_total)*100)
    report = (product, year, complaints_total, unique_companies, top_percent_total)
    report_list.append(report)

# sorting item in the list by product (alphabetically) and year (ascending)
report_list.sort(key=itemgetter(0, 1))
# generating report file &  enclosing only attributes which contain comma (,) by  quotation marks (")
with open(output_file, 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(report_list)
