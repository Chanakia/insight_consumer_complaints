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

