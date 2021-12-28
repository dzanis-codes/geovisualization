import geoplot as gplt
import geopandas as gpd
import geoplot.crs as gcrs
import imageio
import pandas as pd
import pathlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mapclassify as mc
import numpy as np

%matplotlib inline

pd.options.display.max_rows = 500
pd.options.display.max_columns = 500

usa = gpd.read_file("maps/cb_2018_us_state_20m.shp")
usa.head()

state_pop = pd.read_csv("data/nst-est2018-alldata.csv")
state_pop.head()

pop_states = usa.merge(state_pop, left_on="NAME", right_on="NAME")
pop_states.head()

pop_states[pop_states.NAME=="California"].plot()

path = gplt.datasets.get_path("contiguous_usa")
contiguous_usa = gpd.read_file(path)
contiguous_usa.head()

gplt.polyplot(contiguous_usa)
