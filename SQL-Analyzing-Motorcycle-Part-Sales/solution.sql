SELECT
	product_line,
	CASE EXTRACT(MONTH from date)
    	WHEN 1 THEN 'January'
    	WHEN 2 THEN 'February'
    	WHEN 3 THEN 'March'
    	WHEN 4 THEN 'April'
    	WHEN 5 THEN 'May'
    	WHEN 6 THEN 'June'
    	WHEN 7 THEN 'July'
    	WHEN 8 THEN 'August'
   	 	WHEN 9 THEN 'September'
    	WHEN 10 THEN 'October'
    	WHEN 11 THEN 'November'
    	WHEN 12 THEN 'December'
	END AS month,
	warehouse,
	SUM(total) - SUM(payment_fee) AS net_revenue
FROM sales
WHERE client_type = 'Wholesale'
GROUP BY
	product_line,
	month,
	warehouse
ORDER BY
	product_line ASC,
	month ASC,
	net_revenue DESC;