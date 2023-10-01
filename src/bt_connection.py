from plot import generate_data_readings
import data_stat as ds

print(ds.__all__)
print(ds.__doc__)
print(ds.__dict__)
temp = generate_data_readings(start_value=20, end_value=10, num_values=50)
pressure = generate_data_readings(start_value=50, end_value=100, num_values=50)
intensity = generate_data_readings(start_value=20, end_value=160, num_values=50)
alt = generate_data_readings(start_value=206, end_value=290, num_values=50)   

for i in range(len(temp)):
    with open('logs/readings.log', 'a') as file:
        file.write(f"\n{temp[i]}, {pressure[i]}, {intensity[i]}, {alt[i]}")


