#Scripts/process.py
input_file = "../data/clean.txt"
output_file = "../data/result.txt"

temps = [] #placeholder for data
voltages = [] #placeholder for data

with open(input_file, "r") as f: #open the archive in read mode
    for line in f:
        date, temp, volt = line.strip().split(",") #goes line by line

        temps.append(float(temp)) #adds to temps
        voltages.append(float(volt)) # adds to voltages

avg_temp = sum(temps) / len(temps) #takes the average of temp
avg_volt = sum(voltages) / len(voltages) #takes the average of voltages

with open(output_file, "w") as f: #creates ouputfile
    f.write(f"Average temperature: {avg_temp}\n")
    f.write(f"Average voltage: {avg_volt}\n")

print("Proccesing Complete")