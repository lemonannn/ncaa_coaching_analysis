import pandas as pd

power_four_schools = [
    # SEC
    "Alabama", "Arkansas", "Auburn", "Florida", "Georgia",
    "Kentucky", "LSU", "Ole Miss", "Mississippi State",
    "Missouri", "South Carolina", "Tennessee", "Texas A&M",
    "Texas", "Vanderbilt", "Oklahoma",
    
    # Big Ten
    "Illinois", "Indiana", "Iowa", "Maryland", "Michigan",
    "Michigan State", "Minnesota", "Nebraska", "Northwestern",
    "Ohio State", "Penn State", "Purdue", "Rutgers", "UCLA",
    "USC", "Oregon", "Washington", "Wisconsin",
    
    # Big 12
    "Arizona State", "Arizona", "Baylor", "BYU", "UCF",
    "Cincinnati", "Colorado", "Houston", "Iowa State", 
    "Kansas", "Kansas State", "Oklahoma State", "TCU",
    "Texas Tech", "Utah", "West Virginia",
    
    # ACC
    "Boston College", "California", "Clemson", "Duke", "Florida State",
    "Georgia Tech", "Louisville", "Miami (FL)", "NC State",
    "North Carolina", "Pittsburgh", "Syracuse", "Stanford",
    "Virginia", "Virginia Tech", "Wake Forest", "SMU"
]

fired_coaches = [
    ("Sam Pittman", "Arkansas"),
    ("Hugh Freeze", "Auburn"),
    ("Bryan Harsin", "Auburn"),
    ("Karl Dorrell", "Colorado"),
    ("Billy Napier", "Florida"),
    ("Geoff Collins", "Georgia Tech"),
    ("Dana Holgorsen", "Houston"),
    ("Les Miles", "Kansas"),
    ("Brian Kelly", "LSU"),
    ("Mel Tucker", "Michigan State"),
    ("Zach Arnett", "Mississippi State"),
    ("Mack Brown", "North Carolina"),
    ("Ryan Walters", "Purdue"),
    ("Troy Taylor", "Stanford"),
    ("Matt Wells", "Texas Tech"),
    ("DeShaun Foster", "UCLA"),
    ("Brent Pry", "Virginia Tech"),
    ("Jimmy Lake", "Washington"),
    ("Neal Brown", "West Virginia")
]


new_df = pd.DataFrame(columns=["coach", "team", "years_in_pos", "year_hired", "fired", "current", "success", "type"])

year_range = [2025, 2019]

def grab_coaches():

    hired_coaches = []
    df = pd.read_csv('head_coach_history.csv')
    df = df[2:]
    for row in df.iterrows():
        row = row[1]
        if (row["Key"] in power_four_schools):
            team = row["Key"]
            num_years = 1
            hired_coach = row[1]
            current = True
            fired = False
            for i in range(2027-year_range[0], 2028-year_range[1]):
                coach = row[i]
                print(i)
                print(coach)
                print(num_years)
                if coach != hired_coach:
                    if (hired_coach, team) in fired_coaches:
                        fired = True
                        current = False
                    year_hired = 2027 - i
                    hired_coaches.append([hired_coach, team, num_years, year_hired, fired, current, "BLANK", "NA"])
                    hired_coach = coach
                    num_years = 0
                    current = False
                    fired = False
                num_years += 1
    new_df = pd.DataFrame(hired_coaches, columns=["coach", "team", "years_in_pos", "year_hired", "fired", "current", "success", "type"])
    new_df.to_csv("temp.csv", index=False)
                    
                    
    
grab_coaches()

