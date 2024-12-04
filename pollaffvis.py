# -*- coding: utf-8 -*-
"""PollAffVis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10V6sqM__v17MDX1IYH44kNRYYwBGbRCw
"""



import pandas as pd
import matplotlib.pyplot as plt

#Code for NYC
df = pd.read_csv ('NYCPollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in NYC (data from 2024 presidential election)")
plt.show()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Code for Boston
df = pd.read_csv ('BostonPollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in Boston (data from 2024 presidential election)")
plt.show()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Code for Chicago
df = pd.read_csv ('ChicagoPollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in Chicago (data from 2024 presidential election)")
plt.show()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Code for Houston
df = pd.read_csv ('HoustonPollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in Houston (data from 2024 presidential election)")
plt.show()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Code for LA
df = pd.read_csv ('LAPollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in Los Angeles (data from 2024 presidential election)")
plt.show()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Code for Miami
df = pd.read_csv ('MiamiPollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in Miami (data from 2024 presidential election)")
plt.show()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#Code for Seattle
df = pd.read_csv ('SeattlePollAff.csv')

party_data = df["Party"]
vote_data = df["Votes"]

explode = (0.1, 0, 0)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(vote_data, labels=party_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Party Affiliation Demographics in Seattle (data from 2024 presidential election)")
plt.show()

plt.show()