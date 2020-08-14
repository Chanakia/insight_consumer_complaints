import datetime as dt
import csv
from collections import defaultdict
from collections import Counter
import math
from operator import itemgetter
from io import StringIO
import sys

dt_format = '%Y-%m-%d'
company_dict = defaultdict(list)
report_list = []
input_file = sys.argv[1]
output_file = sys.argv[2]


# function for  rounding float val of  0.5 to 1 and below 0.5 to 0
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


# opening the file & assigning the file handle to f
with open(input_file) as f:
    # skipping first line as it is header
    header = next(f)

    for line in f:
        # treating each line as file object for memory optimization
        line_str = StringIO(line)
        reader = csv.reader(line_str, delimiter=',')
        row = list(reader)[0]
        line_str.close()
        company = row[7].lower()
        date_received = row[0]
        product = row[1]
        date_object = dt.datetime.strptime(date_received, dt_format)
        year = date_object.year
        product_year = "{}~{}".format(product, year).lower()
        company_dict[product_year] = company_dict[product_year] + [company]


for prod_yr, complaint_list in company_dict.items():
    product, year = prod_yr.split('~')
    complaints_total = len(complaint_list)
    unique_companies = len(set(complaint_list))
    company_freq = Counter(complaint_list)
    complaint_highest = company_freq.most_common(1)[0][1]
    top_percent_total = normal_round((complaint_highest/complaints_total)*100)
    report = (product, year, complaints_total, unique_companies, top_percent_total)
    report_list.append(report)

report_list.sort(key=itemgetter(0, 1))
with open(output_file, 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(report_list)
