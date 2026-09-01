-- top_five_products_each_category
WITH ranked AS (
	SELECT
		p.category,
		p.product_name,
		ROUND(SUM(o.sales::numeric), 2) AS product_total_sales,
		ROUND(SUM(o.profit::numeric), 2) AS product_total_profit,
 		ROW_NUMBER() OVER (
     			PARTITION BY p.category
     			ORDER BY SUM(o.sales) DESC
 			) AS product_rank
    FROM orders AS o
    INNER JOIN products AS p
        ON o.product_id = p.product_id
    GROUP BY
        p.category,
        p.product_name
)

SELECT
	category,
	product_name,
	product_total_sales,
	product_total_profit,
	product_rank
FROM ranked
WHERE product_rank IN (1,2,3,4,5)
ORDER BY category ASC, product_rank ASC;


-- impute_missing_values
WITH price_per_product AS (
	SELECT product_id, discount, region, market, AVG(sales / ((1 - discount) * quantity)) AS price_per_product
	FROM orders
	GROUP BY
		product_id,
        discount,
        region,
        market
)

SELECT
	o.product_id,
	o.discount,
	o.market,
	o.region,
	o.sales,
	o.quantity,
	ROUND(o.sales::numeric / ppp.price_per_product::numeric) AS calculated_quantity
FROM orders AS o
FULL JOIN price_per_product AS ppp
	ON o.product_id = ppp.product_id
	AND o.discount = ppp.discount
	AND o.region = ppp.region
	AND o.market = ppp.market
WHERE o.quantity IS NULL;