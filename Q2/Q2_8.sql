UPDATE country_vaccination_stats AS t1
SET daily_vaccinations = (
  SELECT COALESCE(MEDIAN(daily_vaccinations), 0) 
  FROM country_vaccination_stats AS t2 
  WHERE t1.country = t2.country
)
WHERE daily_vaccinations IS NULL;