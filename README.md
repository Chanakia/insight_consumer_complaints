# Insight Data Engineering coding challenge
## Report on Consumer Complaints
Goal of this project is to analyze  Consumer Finance Protection Bureau's consumer complaints data-set and  generate report which consists of
each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of 
complaints directed at a single company.

### Analyzing the scenario
#### The above scenario can be converted to sql statement
SELECT
	product ,
	YEAR,
	sum (no_of_complaints) AS total_complaints ,
	count(company) AS tot_companies_with_at_least_one,
	(CAST(max(no_of_complaints) AS float)/ sum(no_of_complaints))* 100 AS highest_percent_of_total_against_one
FROM
	(
	SELECT
		product, YEAR, company, count(1) AS no_of_complaints
	FROM
		consumer_table
	GROUP BY
		product, YEAR, company);
		
#### Replicating the above sql statement into pythonic way by using dictionary of lists

Since the key in the dataset report consists of two fields product and year
unique value based on these two fields can be created by concatenating both columns or generating
a hash value(i.e md5 checksum).Can be achieved by following steps: 
- formatting product and yr from dataset into single string : product_year = "{}~{}".format(product, year).lower()
- generating dictionary similar to {'product_year' : ['company_1', 'company_2'], 'creditcard_2020':['experian','dnb']}

#### Generate report from dictionary of company list items
- Iterating key(str with product and yr) & value (list of companies) pair from company dictionary
- Extract product, yr,total complaints,total no of companies receiving at least one complaint

- Calculate highest % of total complaints filed against one company for that respective product and year
        "top_percent_total = normal_round((complaint_highest/complaints_total)*100)"
- sorting item in the list by product (alphabetically) and year (ascending)
       report_list.sort(key=itemgetter(0, 1)) 
- writing report to a file &  enclosing only attributes which contain comma (,) by  quotation marks (")
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)