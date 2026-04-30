select * from "DIM_Industry" diM

select * from "FACT_Company_Industry" fci 

select * from "DIM_Experience_Level" del 

select * from "DIM_Location" dl 

select * from "FACT_Job_Location" fjl 

select * from "DIM_Company" dc 

select * from "DIM_Job_Title" djt 


-- Empty the values 
TRUNCATE TABLE "FACT_Job_Skill" CASCADE;
TRUNCATE TABLE "FACT_Job_Location" CASCADE;
TRUNCATE TABLE "FACT_Company_Industry" CASCADE;
TRUNCATE TABLE "FACT_Job_Posting" CASCADE;
TRUNCATE TABLE "DIM_Skill" CASCADE;
TRUNCATE TABLE "DIM_Job_Title" CASCADE;
TRUNCATE TABLE "DIM_Job_Type" CASCADE;
TRUNCATE TABLE "DIM_Experience_Level" CASCADE;
TRUNCATE TABLE "DIM_Date_Posted" CASCADE;
TRUNCATE TABLE "DIM_Location" CASCADE;
TRUNCATE TABLE "DIM_Company" CASCADE;
TRUNCATE TABLE "DIM_Industry" CASCADE;



-- Drop Region Column
ALTER TABLE "DIM_Location" DROP COLUMN region;