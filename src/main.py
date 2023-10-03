import plot
import time
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
    while True: 
        data_readings: list[list[float, float, float],] = featch_readings(9)
        temperature_data: list[float] = [] 
        pressure_data: list[float]= [] 
        light_data: list[float]= []
        altitude_data: list[float]= [] 
        
        for reading in data_readings:
            temperature_data.append(reading[0])  # temperature
            pressure_data.append(reading[1])  # pressure
            light_data.append(reading[2])  # light intensity
            altitude_data.append(reading[3])  #altitude
            
        mdu.update(md_live_path='markdown/live.md', 
                # Mean values
                Temperature_Mean_Value=u"{} \N{DEGREE SIGN}C".format(ds.mean(temperature_data)),
                Pressure_Mean_Value=f"{ds.mean(pressure_data)} Pa",
                Altitude_Mean_Value=f"{ds.mean(altitude_data)*100} cm",
                Light_Level_Mean_Value=f"{ds.mean(light_data)} Candela",
                
                # Median values
                Temperature_Median_Value=f"{ds.median(temperature_data)} °C",
                Pressure_Median_Value=f"{ds.median(pressure_data)} Pa",
                Altitude_Median_Value=f"{ds.median(altitude_data)*100} cm",
                Light_Level_Median_Value=f"{ds.median(light_data)} Candela",
                
                # Mode values
                Temperature_Mode_Value=f"{ds.mode(temperature_data)} °C",
                Pressure_Mode_Value=f"{ds.mode(pressure_data)} Pa",
                Altitude_Mode_Value=f"{ds.mode(altitude_data)*100} cm",
                Light_Level_Mode_Value=f"{ds.mode(light_data)} Candela",
                
                # Varience
                Temperature_Variance_Value=f"{ds.variance(temperature_data)} °C",
                Pressure_Variance_Value=f"{ds.variance(pressure_data)} Pa",
                Altitude_Variance_Value=f"{ds.variance(altitude_data)*100} cm",
                Light_Level_Variance_Value=f"{ds.variance(light_data)} Candela",
                
                # Standard Deviation
                Temperature_Standard_Deviation_Value=f"{ds.standard_deviation(temperature_data)} °C",
                Pressure_Standard_Deviation_Value=f"{ds.standard_deviation(pressure_data)} Pa",
                Altitude_Standard_Deviation_Value=f"{ds.standard_deviation(altitude_data)*100} cm",
                Light_Level_Standard_Deviation_Value=f"{ds.standard_deviation(light_data)} Candela"
                )
        
        
         
        # Creating the processing structure (datasets)
        dataset_1 = plot.create_dataset(reading_x=temperature_data,
                                reading_y=pressure_data,
                                reading_z=light_data)

        dataset_2 = plot.create_dataset(reading_x=temperature_data, 
                                reading_y=altitude_data,
                                reading_z=light_data)
        
        dataset_3 = plot.create_dataset(reading_x=temperature_data, 
                                reading_y=pressure_data,
                                reading_z=altitude_data)
        
        dataset_4 = plot.create_dataset(reading_x=altitude_data, 
                                reading_y=pressure_data,
                                reading_z=light_data)
        
        # creating the figures and corresponding axes objects
        fig_1, fig_1_axes = plot.create_figure('Temperature vs Pressure vs Light intensity',"temperature", "pressure", "light intensity")
        fig_2, fig_2_axes = plot.create_figure('Temperature vs Altitude vs Light intensity',"temperature", "altitude", "light intensity")
        fig_3, fig_3_axes = plot.create_figure('Temperature vs Pressure vs Altitude',"temperature", "pressure", "altitude")
        fig_4, fig_4_axes = plot.create_figure('Altitude vs Pressure vs Light intensity',"altitude", "pressure", "light intensity")

        # plotting
        plot.scatter_data_3d( axes=fig_1_axes, data_set=dataset_1)
        plot.scatter_data_3d( axes=fig_2_axes, data_set=dataset_2)
        plot.scatter_data_3d( axes=fig_3_axes, data_set=dataset_3)
        plot.scatter_data_3d( axes=fig_4_axes, data_set=dataset_4)

        # showing figure
        # fig_1.show()
        # fig_2.show()
        # fig_3.show()
        # fig_4.show()
        plt.show()
        
        input('Press Enter to continue: ') 
        # saving figures as png
        fig_1.savefig(plot.fig_1_path)
        fig_2.savefig(plot.fig_2_path)
        fig_3.savefig(plot.fig_3_path)
        fig_4.savefig(plot.fig_4_path)


        
        time.sleep(10) 
        mdu.restore(md_live_path='markdown/live.md', md_backup_path='markdown/backup.md') 
if __name__ == "__main__":
    main()