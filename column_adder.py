import pandas as pd

def add_coached_prior():
    hires = pd.read_csv("coach_hires_2019-25.csv")
    hires['prior_hc'] = ((hires["prior_p4_or_nfl_hc"] == True) | (hires["type"] == "Cignetti") | (hires["type"] == "DeBoer") | (hires["type"] == "Brohm"))
    hires.to_csv('new_coach_hires_2019-25.csv')