## Resources used
Dataset: https://www.kaggle.com/datasets/dianaddx/aircraft-wildlife-strikes-1990-2023
Programs: Pandas, Numpy, Matplotlib, Plotly Express

# Motivations and Data
  Bird strikes are a common reason for aircraft take-off delays, non-routine maintenance, and expensive investigations. The dataset used ranges from 1990 to 2023 and has almost 300,000 incidents reported from 2,614 airports. The dataset only includes commercial airliners, but could be transformed for military use with some modification.
  Unfortunately, some redacted information includes damage costs, a field for the damage cost adjusted for inflation, class of aircraft and some PII including pilot names and callsigns. This could have been helpful in determining, for example, the statistically most damaging species, and potentially any pilots that may be prone to strikes.

## Initial Impressions and Questions
  At what point do most wildlife strikes occur? Where do these strikes seem most prevalent (State, Airport, Rural vs City, etc.)? Is there any correlation between company and wildlife strike incidence? Does weather have any effect or is it seemingly coincidence? Do certain types of aircraft have more strikes?

# Strikes Over Time
### Immediate Question
  The most immediate question to me was, has the frequency of bird strikes increased over time? Through plotting the reports of strikes over time, we see a great increase up until about 2019. Which requires a more up close view.
![Incident Per Year Graph](/imgs/Incident_per_year.png)
  Looking closer at the drop off, we can see a steep decline occurs between 2019 and 2020. We can infer that this was likely due to the COVID-19 outbreak, as we see it start to increase again as COVID was beginning to become less of a factor in travel. The dataset drops off at the end due to the recency of the data, as this dataset came out during 2023 where reported data would not be yet available.
![Incident_2019_to_2023 Graph](/imgs/Incident_2019_to_2023.png)
  Over the course of 1990 to 2023, I plotted for each month how many bird strikes occurred. We can see the general trend is as the weather warms and changes, bird strikes greatly increase peaking around the August timeframe, likely due to breeding seasons and migration.
![Incidents_monthly Graph](/imgs/Incidents_monthly.png)

# Regional Influences
  Exploring if United States regions or climate have an influence, I graphed reported strikes across the states. From this data it appears that warmer climates may have a slightly higher incident rate. I believe that this is misleading however, as these states contain some of the biggest airports in the US, for travel to the state or commonly used for connecting flights.
![State_Incident_Map Graph](/imgs/State_Incident_Map.png)
  Further supporting this point, we see that the most strikes occur at airports that see lots of (is foot still applicable as a term here?) traffic rather than climate playing a defining role.
![Incident_by_airport Graph](/imgs/Incident_by_airport.png)
  Further exploring this point, by indexing at every state that falls directly below the median amount of strikes, it appears weather may play a factor, but it doesn’t seem to be overwhelmingly integral to the amount of strikes
![Incident_per_State_Med Graph](/imgs/Incident_per_State_Med.png)

# Operators and Errors

# Further Expansion
  Given more time, 

# Why Should Individuals Take Interest?
  What steps can be taken to avoid potential injury to personal or equipment? Where should more precautions be taken, or more thorough inspections take place to make sure strikes don't go unnoticed? Are any airlines particularly vulnerable to these attacks and potentially need to be put under more scrutiny?
