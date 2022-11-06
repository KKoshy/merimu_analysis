"""
This file holds all the necessary constants for analysing High rate dataset

"""
import os

HIGHRATE_DATASET = {"MARS_EXPLORATION_ROVER_1": os.path.join('pds_data', 'DATA', '1HIGHRATE.TAB'),
                    "MARS_EXPLORATION_ROVER_2": os.path.join('pds_data', 'DATA', '2HIGHRATE.TAB')}
HIGHRATE_COLUMNS = ['spacecraft_clock_start_count_s', 'rimu_rates_x_rad/s',
                    'rimu_rates_y_rad/s', 'rimu_rates_z_rad/s', 'rimu_dvel_x_m/s',
                    'rimu_dvel_y_m/s', 'rimu_dvel_z_m/s', 'bimu_rates_x_rad/s',
                    'bimu_rates_y_rad/s', 'bimu_rates_z_rad/s', 'bimu_dvel_x_m/s',
                    'bimu_dvel_y_m/s', 'bimu_dvel_z_m/s']
HIGHRATE_DATATYPE = 'High_rate_measurements'
