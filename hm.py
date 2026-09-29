print("hello")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("pokemon_complete_stats.csv")

print(data.head())
print(data.info())

# Check datatype
print(type(data["attack"][0]))

# Zorg dat attack numeriek is
data["attack"] = pd.to_numeric(data["attack"], errors="coerce")

print(type(data["attack"][6]))

# Groepeer Pokémon met dezelfde attack-score
data_attack = data.groupby("attack").mean(numeric_only=True)

# FIGURE 1
fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=data_attack.index,
        y=data_attack["height_dm"],
        mode="lines",
        line_color="green"
    )
)

fig1.update_layout(
    title="Average height by attack",
    xaxis_title="Attack",
    yaxis_title="Average height (dm)"
)

fig1.write_html("Fig1.html", auto_open=True)


# FIGURE 2
fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=data_attack.index,
        y=data_attack["defense"],
        mode="lines",
        line_color="green"
    )
)

fig2.update_layout(
    title="Average defense by attack",
    xaxis_title="Attack",
    yaxis_title="Average defense"
)

fig2.write_html("Fig2.html", auto_open=True)


# FIGURE 3
fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(
        x=data_attack.index,
        y=data_attack["generation"],
        mode="lines",
        line_color="blue"
    )
)

fig3.update_layout(
    title="Average generation by attack",
    xaxis_title="Attack",
    yaxis_title="Generation"
)

fig3.write_html("Fig3.html", auto_open=True)