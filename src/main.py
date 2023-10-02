import plot
import data_stat as ds
import md_updater as mdu
import numpy as np
import matplotlib.pyplot as plt
# import bt_connection as btcon


def featch_readings(no_readings: int) -> list[list[float, float, float],]:
    """
    This function reads records from readings.log and returns a list of records as lists of floats.
    """
    data_readings: list = []
    with open('logs/readings.log', 'r') as file:
        raw_readings = file.readlines()[:-no_readings-1:-1]
        
        for reading in raw_readings:
            reading = reading.replace(',', '').strip().split()
            reading = [float(i) for i in reading]
            data_readings.append(reading)

    return data_readings
    

def main() -> None:
    """
    This is where the execution starts.
    """

    data_readings: list[list[float, float, float],] = featch_readings(9)
    
    for reading in data_readings:
        print(f"temperature: {reading[0]}", end=", ")
        print(f"pressure: {reading[1]}", end=", ")
        print(f"altitude: {reading[3]}\n")
if __name__ == "__main__":
    main()