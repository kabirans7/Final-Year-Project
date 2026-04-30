SELECT 'FACT_Job_Posting' AS table_name, COUNT(*) FROM "FACT_Job_Posting"
UNION ALL
SELECT 'FACT_Company_Industry', COUNT(*) FROM "FACT_Company_Industry"
UNION ALL
SELECT 'DIM_Industry', COUNT(*) FROM "DIM_Industry"
UNION ALL
SELECT 'DIM_Job_Title', COUNT(*) FROM "DIM_Job_Title"
UNION ALL
SELECT 'DIM_Date_Posted', COUNT(*) FROM "DIM_Date_Posted";

SELECT
    di.industry_name,
    jt.job_title,
    COUNT(*) AS demand_count
FROM "FACT_Job_Posting" jp
JOIN "FACT_Company_Industry" fci ON jp.company_id = fci.company_id
JOIN "DIM_Industry" di ON fci.industry_id = di.industry_id
JOIN "DIM_Job_Title" jt ON jp.job_title_id = jt.job_title_id
JOIN "DIM_Date_Posted" d ON jp.date_posted = d.date
GROUP BY di.industry_name, jt.job_title
ORDER BY di.industry_name, demand_count DESC;

SELECT COUNT(*) AS postings_without_industry
FROM "FACT_Job_Posting" jp
LEFT JOIN "FACT_Company_Industry" fci 
ON jp.company_id = fci.company_id
WHERE fci.company_id IS NULL;

SELECT COUNT(*) AS postings_without_job_title
FROM "FACT_Job_Posting" jp
LEFT JOIN "DIM_Job_Title" jt 
ON jp.job_title_id = jt.job_title_id
WHERE jt.job_title_id IS NULL;

SELECT COUNT(*) AS postings_without_date
FROM "FACT_Job_Posting" jp
LEFT JOIN "DIM_Date_Posted" d 
ON jp.date_posted = d.date
WHERE d.date IS NULL;