"""
Author: Aviraj Saha
Date: 1-10-2023
Purpose: Shortlisting required statistics techniques from various libraries.
"""

# Metadata
__author__: str = "Aviraj Saha"
__description__: str = "Shortlisting required statistics techniques from various libraries."
__all__: tuple[str] = ("mean", "median", "mode","mean_deviation_","standard_deviation","variance")
__depedencies__: tuple[str] = (
    "numpy==1.26.0",
)
__keywords__: tuple[str] = ("__author__", "__description__", "__all__", "__depedencies__", "__keywords",
                "mean", "median", "mode","mean_deviation_","standard_deviation","variance")


# importing dependencies
import numpy as np
# Otherwise the user-defined 'mode' function will overwrite this imported function.
from statistics import mode as stat_mode 
from logging import basicConfig, warning, WARNING

# setup for logging
basicConfig(level=WARNING)

# Parameters in use
data_readings: list[float,]


def mean(data_readings: list[float,]) -> float:
    """
    This function returns mean reading.
    """
    return np.mean(data_readings)


def median(data_readings: list[float,]) -> float:
    """
    This function returns median reading.
    """
    return np.median(data_readings)


def mode(data_readings: list[float,]) -> float:
    """
    This function returns mode reading.
    """
    return stat_mode(data_readings)


def standard_deviation(data_readings: list[float,]) -> float:
    """
    This function returns standard deviation of readings.
    """
    return np.std(data_readings)


def variance(data_readings: list[float,]) -> float:
    """
    This function returns variance of readings.
    """
    return np.var(data_readings)

if __name__ == "__main__":
    warning("This is a statistics module for the project. Do not run this as a script.")


