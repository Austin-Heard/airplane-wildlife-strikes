import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def strikes_yearly(database):
    incident_per_year = database["INCIDENT_YEAR"].value_counts().sort_index()
    incident_per_year.plot(kind='line', title='Incidents per Year', xlabel="Incident Year").get_figure().savefig('../imgs/Incident_per_year.png')

def strikes_monthly(database):
    incident_per_month = database["INCIDENT_MONTH"].value_counts().sort_index()
    incident_per_month.plot(kind='line', title='Incidents per Month', grid=True, xlabel="Month Strike Occured").get_figure().savefig('../imgs/Incidents_monthly.png')

def airline_strikes(database):
    database_named_operators = database[(database["OPERATOR"] != "UNKNOWN") & (database["OPERATOR"] != "BUSINESS")]
    incident_per_airline = database_named_operators["OPERATOR"].value_counts().sort_values(ascending=False).head(8)
    incident_per_airline.plot(kind='barh', title='Incidents per Airline', xlabel="Total Strikes Reported").get_figure().savefig('../imgs/Incident_per_airline.png')

def phase_of_flight_pie(database):
    most_common_PHASE_OF_FLIGHT = database["PHASE_OF_FLIGHT"].value_counts().sort_index()
    labels = ["Approach", "Arrival", "Climb","Departure","Descent","En Route","Landing Roll","Local","Parked","Take-off Run","Taxi"]
    fig, ax = plt.subplots(figsize=(11, 11))
    ax.pie(most_common_PHASE_OF_FLIGHT, labels=labels, autopct='%.1f%%',
        wedgeprops={'linewidth': 4.0, 'edgecolor': 'white'},
        textprops={'size': 'x-large'})
    ax.set_title('Incidents by Phase of Flight', fontsize=18)
    fig.savefig('../imgs/Phase_Of_Flight_Pie.png')

def state_occurance(database):
    database["STATE"].value_counts().sort_values(ascending=False).head(5).plot(kind='barh', title='Incidents by State').get_figure().savefig('../imgs/Incident_per_State.png')

def state_map(database):
    state_code_minus_guam = database[database["STATE"] != "GU"]

    state_data = pd.DataFrame({
                            "State Code": state_code_minus_guam["STATE"].unique(),
                            "Count": database["STATE"].value_counts()
                            })
    fig = px.choropleth(state_data, locations="State Code", color="Count",
                        color_continuous_scale="Viridis",
                        locationmode="USA-states",
                        scope="usa",
                        labels={'Count':'Strikes Reported'}
                        )
    #Save the image to the imgs folder using kaleido
    #fig.write_image('../imgs/State_Incident_Map.png')
    fig.show()


def state_less_than_median(database):
    state_strikes_below_median = database["STATE"].value_counts().where(database["STATE"].value_counts() < database["STATE"].value_counts().median()).dropna()
    state_strikes_below_median.sort_values(ascending=False).head(5).plot(kind='barh', title='Incidents by State').get_figure().savefig('../imgs/Incident_per_State_Med.png')

def incident_by_airport(database):
    database["AIRPORT"].value_counts().sort_values(ascending=False).head(5).plot(kind='barh', title='Incidents by Airport').get_figure().savefig('../imgs/Incident_by_airport.png')

def incident_by_runway(database):
    database.groupby("AIRPORT")["RUNWAY"].value_counts().sort_values(ascending=False).head(10).plot(kind='barh', title='Incidents by Airport Runway', ylabel="Airport, Runway #").get_figure().savefig('../imgs/Incident_by_airport_runway.png')

def damge_level_counts(database):
    database.dropna(subset=["DAMAGE_LEVEL"], axis=0)
    database_damage = pd.DataFrame({
    "Damage Level": ["None", "Minor", "Undetermined", "Substantial", "Destroyed"],
    "Count": database["DAMAGE_LEVEL"].value_counts()
    })
    database_damage.set_index("Damage Level")
    print(database_damage)

def non_airplane_strikes(database):
    non_airplane_strikes = database[database["AC_CLASS"] != "A"]
    non_airplane_strikes.value_counts().sort_values(ascending=False).head(10).plot(kind='barh', title="Reports by Aircraft Class").get_figure().savefig('../imgs/non_airplane_strikes.png')

def bird_strikes_by_species(database):
    bird_species = database[(database["SPECIES"] != "Unknown bird - small") & (database["SPECIES"] != "Unknown bird - medium") & (database["SPECIES"] != "Unknown bird") & (database["SPECIES"] != "Unknown bird - large")]
    bird_species["SPECIES"].value_counts().sort_values(ascending=False).head(20).plot(kind='barh', title='Bird Strikes By Species', ylabel="Bird Species").get_figure().savefig('../imgs/Incident_by_species.png')

def species_strikes_by_state(database):
    bird_species = database[(database["SPECIES"] != "Unknown bird - small") & (database["SPECIES"] != "Unknown bird - medium") & (database["SPECIES"] != "Unknown bird") & (database["SPECIES"] != "Unknown bird - large")]
    print(bird_species.groupby("STATE")["SPECIES"].value_counts().sort_values(ascending=False).head(10))

if __name__ == "__main__":
    database = pd.read_csv('../data/STRIKE_REPORTS.csv')
    strikes_yearly(database)
    strikes_monthly(database)
    airline_strikes(database)
    phase_of_flight_pie(database)
    state_occurance(database)
    state_map(database)
    state_less_than_median(database)
    incident_by_airport(database)
    incident_by_runway(database)
    damge_level_counts(database)
    non_airplane_strikes(database)
    bird_strikes_by_species(database)
    species_strikes_by_state(database)