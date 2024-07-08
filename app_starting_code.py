from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px
from faicons import icon_svg
from shinywidgets import render_plotly
from state_choices import STATE_CHOICES

from shiny import reactive
from shiny.express import input, render, ui

# ---------------------------------------------------------------------
# Reading in Files
# ---------------------------------------------------------------------
new_listings_df = pd.read_csv(Path(__file__).parent / "Metro_new_listings_uc_sfrcondo_sm_month.csv")
median_listing_price_df = pd.read_csv(Path(__file__).parent / "Metro_mlp_uc_sfrcondo_sm_month.csv")
for_sale_inventory_df = pd.read_csv(Path(__file__).parent / "Metro_invt_fs_uc_sfrcondo_sm_month.csv")


# ---------------------------------------------------------------------
# Helper functions - converting to DateTime
# ---------------------------------------------------------------------
def string_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def filter_by_date(df: pd.DataFrame, date_range: tuple):
    rng = sorted(date_range)
    dates = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.date
    return df[(dates >= rng[0]) & (dates <= rng[1])]


# ---------------------------------------------------------------------
# Visualizations
# ---------------------------------------------------------------------

# Plotly visualization of Median Home Price Per State
def list_price_plot():
    # Grouping by State Name and specifying the Date Columns
    price_grouped = median_listing_price_df.groupby('StateName').mean(numeric_only=True)     
    date_columns = median_listing_price_df.columns[6:]
    price_grouped_dates = price_grouped[date_columns].reset_index()   
    price_df_for_viz = price_grouped_dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")
    # Creating Visualization using Ployly
    fig = px.line(price_df_for_viz, x="Date", y="Value", color="StateName")
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")
    return fig


# Plotly visualization of Homes For Sale Per State
def for_sale_plot():
    # Grouping by State Name and specifying the Date Columns
    df2_grouped = for_sale_inventory_df.groupby('StateName').sum(numeric_only=True)
    date_columns = for_sale_inventory_df.columns[6:]
    df2_grouped_dates = df2_grouped[date_columns].reset_index()
    df2_melted = df2_grouped_dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")
    # Creating Visualization using Ployly
    df = for_sale_filtered()
    fig = px.line(df, x="Date", y="Value", color="StateName")
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")
    return fig

# Plotly visualization of Listings Per State
def listings_plot():
    # Grouping by State Name and specifying the Date Columns
    df3_grouped = new_listings_df.groupby('StateName').sum(numeric_only=True)
    date_columns = new_listings_df.columns[6:]
    df3_grouped_dates = df3_grouped[date_columns].reset_index()
    df3_melted = df3_grouped_dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")
    # Creating Visualization using Ployly
    df = listings_filtered()
    fig = px.line(df, x="Date", y="Value", color="StateName")
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")
    return fig



