-- highest_donation_assignments

SELECT
	a.assignment_name,
	a.region,
	ROUND(SUM(d.amount), 2) AS rounded_total_donation_amount,
	dr.donor_type
FROM Assignments AS a
INNER JOIN Donations AS d
	ON a.assignment_id = d.assignment_id
INNER JOIN Donors AS dr
	ON d.donor_id = dr.donor_id
GROUP BY
	a.assignment_name,
	a.region,
	dr.donor_type
ORDER BY rounded_total_donation_amount DESC
LIMIT 5;

-- top_regional_impact_assignments

WITH num_don AS (
	SELECT assignment_id, COUNT(*) AS num_total_donations
	FROM Donations
	GROUP BY assignment_id
),

ranked AS (
	SELECT
		a.assignment_name,
		a.region,
		a.impact_score,
		nd.num_total_donations,
	 	ROW_NUMBER() OVER (
    		PARTITION BY a.region
    		ORDER BY a.impact_score DESC
		) AS rn
	FROM Assignments AS a
	INNER JOIN num_don AS nd
	ON a. assignment_id = nd.assignment_id
)

SELECT
	assignment_name,
	region,
	impact_score,
	num_total_donations
FROM ranked
WHERE rn = 1
ORDER BY region ASC;
