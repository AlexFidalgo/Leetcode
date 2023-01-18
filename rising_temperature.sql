# Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
select s.id as Id from Weather p join Weather s
on s.recordDate = date_add(p.recordDate, interval 1 day)
where p.temperature < s.temperature
