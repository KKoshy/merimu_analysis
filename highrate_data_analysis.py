"""
This file holds functions to analyse highrate dataset of MER - IMU1 and IMU2

"""

from data.highrate import HIGHRATE_COLUMNS, HIGHRATE_DATASET, HIGHRATE_DATATYPE
from utils import collect_data, render_interactive


def analyse_highrate_data_set(dataset, host):
    """
    Analyses High rate dataset of MER IMU

    :param dataset: file which holds data
    :param host: host name of the instrument
    :return: None
    """
    data_df = collect_data(dataset, HIGHRATE_COLUMNS)
    render_interactive(data_df, HIGHRATE_DATATYPE, host, HIGHRATE_COLUMNS[0], HIGHRATE_COLUMNS[1:])


if __name__ == "__main__":
    for host_name, data_set in HIGHRATE_DATASET.items():
        analyse_highrate_data_set(data_set, host_name)
