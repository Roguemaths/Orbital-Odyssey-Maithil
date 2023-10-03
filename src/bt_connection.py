from plot import generate_data_readings
import time

temp = generate_data_readings(start_value=20, end_value=10, num_values=5)
pressure = generate_data_readings(start_value=50, end_value=100, num_values=5)
intensity = generate_data_readings(start_value=20, end_value=160, num_values=5)
alt = generate_data_readings(start_value=206, end_value=290, num_values=5)

while True:
    time.sleep(10)
    for i in range(len(temp)):
        with open("logs/readings.log", "a") as file:
            file.write(f"\n{temp[i]}, {pressure[i]}, {intensity[i]}, {alt[i]}")
            with open("markdown/live_data.md", "a") as md_data_file:
                md_data_file.write(
                    f"\n| {temp[i]} | {pressure[i]} | {intensity[i]} | {alt[i]} |\n"
                )
                md_data_file.write(
                    "|-------------------------|----------------|----------------|----------------------------|"
                )
