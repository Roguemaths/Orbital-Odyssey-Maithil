"""
Author: Aviraj Saha
Date: 30-09-2023
Purpose: Plotting graphs from datasets and saving them to specified paths.
"""


# Metadata
__author__: str = "Aviraj Saha"
__description__: str = "Plotting graphs from datasets and saving them to specified paths."
__all__: tuple[str] = ("generate_data_readings", "create_dataset", "create_figure","scatter_data_3d","main",)
__depedencies__: tuple[str] = (
    "numpy==1.26.0",
    "matplotlib==3.8.0",
    "python_standard_libs"
)
__keywords__: tuple[str] = ("__author__", "__description__", "__all__", "__depedencies__", "__keywords__",
                "generate_data_readings", "create_dataset", "create_figure","scatter_data_3d","main")


# Importing dependencies
import numpy as np
import matplotlib.pyplot as plt
# import typing


# Parameters to plot
pressure: float
temp: float
alt: float
# time: float
light_intensity: float


# Graphs
fig_1: plt.Figure # Temperature vs Pressure vs Light intensity
fig_1_axes: plt.Axes

fig_2: plt.Figure # Temperature vs Altitude vs Light intensity
fig_2_axes: plt.Axes

fig_3: plt.Figure # Temperature vs Pressure vs Altitude
fig_3_axes: plt.Axes

fig_4: plt.Figure # Altitude vs Pressure vs Light intensity
fig_4_axes: plt.Axes


# Paths
fig_1_path: str = 'plots/temp_vs_pressure_vs_intensity.png'
fig_2_path: str = 'plots/temp_vs_alt_vs_intensity.png'
fig_3_path: str = 'plots/temp_vs_pressure_vs_alt.png'
fig_4_path: str = 'plots/alt_vs_pressure_vs_intensity.png'


# Datasets used
dataset_1: list[tuple[float, float, float]] # (temp, pressure, intensity)
dataset_2: list[tuple[float, float, float]] # (temp, alt, intensity)
dataset_3: list[tuple[float, float, float]] # (temp, pressure, alt)
dataset_4: list[tuple[float, float, float]] # (alt, pressure, intensity)


def generate_data_readings(start_value: float, 
                           end_value: float, 
                           num_values: int) -> tuple[float, ...]:  # This function is no more needed when the actual readings are available
    """This function provides mock data and is no more needed when the actual readings are available."""
    float_values: np.ndarray = np.random.uniform(start_value, end_value, num_values) # Generating random values using numpy
    return tuple(i for i in float_values) # returning a tuple using tuple comprihenson


def create_dataset(reading_x: tuple[float, ...],
                    reading_y: tuple[float, ...], 
                    reading_z: tuple[float, ...]) -> list[tuple[float, float, float]]: # Number of observations in all readings must be same
    """
     Number of observations in all readings provided must be same.
    """
    dataset: list = [] # Declearing an empty dataset
    if not len(reading_x) == len(reading_y) == len(reading_z):
        raise ValueError(f"""Expected equal no. of obs. for all quantaties but insted got:
                         {reading_x=}, no of obs:{len(reading_x)}
                         {reading_y=}, no of obs:{len(reading_y)}
                         {reading_z=}, no of obs:{len(reading_z)}""")
    
    # Looping and unpacking the readings and generating a dataset structure
    index: int
    for index in range(len(reading_x)):
        
        individual_data = (reading_x[index], reading_y[index], reading_z[index])
        dataset.append(individual_data)

    return dataset


def create_figure(title:str, x_label:str, 
                  y_label: str, z_label: str) -> tuple[plt.Figure, plt.Axes]:
    """
    """
    # The figure object is basically the actual graph
    fig: plt.Figure = plt.figure() # Instantiating the figure object
    axes: plt.Axes = fig.add_subplot(projection="3d") # Setting up projection axes for the figure object
    
    # Setting up Graph parameters
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    axes.set_zlabel(z_label)
    return fig, axes


def scatter_data_3d(axes: plt.Axes, data_set: list[tuple[float, float, float]]) -> None:
    """ This function plots the graph for the axes and dataset provided."""
    for index, data in enumerate(data_set):
        x: float = data[0]
        y: float = data[1]
        z: float = data[2]

        axes.scatter(x, y, z)


def main() -> None:
    """
    Execution of plot.py starts from here
    """
    # Remove or comment out this code when the actual data is accessable
    temperature_data_readings: list[float,] = generate_data_readings(start_value=20.0, 
                                                                     end_value=50.0,
                                                                       num_values=20) # Generating random values in the provided range
    
    lightintensity_data_readings: list[float,] = generate_data_readings(start_value=10.0, 
                                                                        end_value=20.0, 
                                                                        num_values=20)  # Generating random values in the provided range
    
    pressure_data_readings: list[float,] = generate_data_readings(start_value=0, 
                                                                  end_value=60, 
                                                                  num_values=20)  # Generating random values in the provided range
    
    altitude_data_readings: list[float,] = generate_data_readings(start_value=0, 
                                                                  end_value=20, 
                                                                  num_values=20)  # Generating random values in the provided range
    
    # Creating the processing structure (datasets)
    dataset_1 = create_dataset(reading_x=temperature_data_readings, 
                               reading_y=pressure_data_readings,
                               reading_z=lightintensity_data_readings)

    dataset_2 = create_dataset(reading_x=temperature_data_readings, 
                               reading_y=altitude_data_readings,
                               reading_z=lightintensity_data_readings)
    
    dataset_3 = create_dataset(reading_x=temperature_data_readings, 
                               reading_y=pressure_data_readings,
                               reading_z=altitude_data_readings)
    
    dataset_4 = create_dataset(reading_x=altitude_data_readings, 
                               reading_y=pressure_data_readings,
                               reading_z=lightintensity_data_readings)
    
    # creating the figures and corresponding axes objects
    fig_1, fig_1_axes = create_figure('Temperature vs Pressure vs Light intensity',"temperature", "pressure", "light intensity")
    fig_2, fig_2_axes = create_figure('Temperature vs Altitude vs Light intensity',"temperature", "altitude", "light intensity")
    fig_3, fig_3_axes = create_figure('Temperature vs Pressure vs Altitude',"temperature", "pressure", "altitude")
    fig_4, fig_4_axes = create_figure('Altitude vs Pressure vs Light intensity',"altitude", "pressure", "light intensity")

    # plotting
    scatter_data_3d( axes=fig_1_axes, data_set=dataset_1)
    scatter_data_3d( axes=fig_2_axes, data_set=dataset_2)
    scatter_data_3d( axes=fig_3_axes, data_set=dataset_3)
    scatter_data_3d( axes=fig_4_axes, data_set=dataset_4)

    # showing figure
    # fig_1.show()
    # fig_2.show()
    # fig_3.show()
    # fig_4.show()
    plt.show()
    
    # saving figures as png
    fig_1.savefig(fig_1_path)
    fig_2.savefig(fig_2_path)
    fig_3.savefig(fig_3_path)
    fig_4.savefig(fig_4_path)


if __name__ == "__main__":
    main()