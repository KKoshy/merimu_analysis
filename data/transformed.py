"""
This file holds all the necessary constants for analysing Transformed dataset

"""
import os

TRANSFORMED_DATASET = {"MARS_EXPLORATION_ROVER_1": os.path.join('pds_data', 'DATA', '1TRANSFORMED.TAB'),
                       "MARS_EXPLORATION_ROVER_2": os.path.join('pds_data', 'DATA', '2TRANSFORMED.TAB')}
TRANSFORMED_COLUMNS = ['spacecraft_clock_start_count_s', 'rover_imu_quaternion_1',
                       'rover_imu_quaternion_2', 'rover_imu_quaternion_3',
                       'rover_imu_quaternion_4', 'back_imu_quaternion_1',
                       'back_imu_quaternion_2', 'back_imu_quaternion_3',
                       'back_imu_quaternion_4', 'rimu_dvel_x_m/s',
                       'rimu_dvel_y_m/s', 'rimu_dvel_z_m/s', 'bimu_accel_x_m/s',
                       'bimu_accel_y_m/s',  'bimu_accel_z_m/s']
TRANSFORMED_DATATYPE = 'Transformed_measurements'
