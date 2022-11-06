"""
This file holds all the common functions for analysing IMU data

"""
import os

import plotly
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go

from data.common import VIRIDIS_PALETTE, REPORTS


def collect_data(dataset, h_columns):
    """
    Collects data from files and forms a dataframe

    :param dataset: file which holds data
    :param h_columns: column headers for the data
    :return: dataframe
    """
    dataset_df = pd.read_csv(dataset, sep=' ' * 4, lineterminator='\n', names=h_columns,
                             engine='python')
    dataset_df.fillna(0)
    return dataset_df


def render_interactive(dataset_df, data_type, host_name, clock_count, quantities):
    """
    Creates interactive plot for the time series data

    :param dataset_df: dataframe with MER IMU data
    :param data_type: type of the dataset -> highrate/transformed
    :param host_name: host name of the instrument
    :param clock_count: spacecraft clock count in decimal seconds
    :param quantities: quantities to be plotted from the dataframe
    :return: None
    """
    color_palette = list(sns.color_palette(palette=VIRIDIS_PALETTE, n_colors=len(quantities)).as_hex())
    fig = go.Figure()
    for color, quantity in zip(color_palette, quantities):
        fig.add_trace(go.Scatter(x=dataset_df[clock_count],
                                 y=dataset_df[quantity], line_color=color, name=quantity))
    fig.update_layout(title='Analysing {} IMU {} over spacecraft clock count'.format(host_name, data_type),
                      xaxis_title='Spacecraft clock count',
                      yaxis_title=data_type)
    plotly.offline.plot(fig, filename=os.path.join(REPORTS, host_name+"_"+data_type+".html"))
    fig.show()
