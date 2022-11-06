"""
This file holds functions to analyse transformed dataset of MER - IMU1 and IMU2

"""

from data.transformed import TRANSFORMED_COLUMNS, TRANSFORMED_DATASET, TRANSFORMED_DATATYPE
from utils import collect_data, render_interactive


def analyse_transformed_data_set(dataset, host):
    """
    Analyses Transformed dataset of MER IMU

    :param dataset: file which holds data
    :param host: host name of the instrument
    :return: None
    """
    data_df = collect_data(dataset, TRANSFORMED_COLUMNS)
    render_interactive(data_df, TRANSFORMED_DATATYPE, host, TRANSFORMED_COLUMNS[0], TRANSFORMED_COLUMNS[1:])


if __name__ == "__main__":
    for host_name, data_set in TRANSFORMED_DATASET.items():
        analyse_transformed_data_set(data_set, host_name)
