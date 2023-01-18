# Write an SQL query to report the patient_id, patient_name and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
select patient_id, patient_name, conditions from Patients
where conditions like 'DIAB1%'or conditions like "% DIAB1%"
