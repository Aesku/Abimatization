import re
import os

os.system('grep E0 q*/sl* > energies_aux.txt')

qarray = []
E0_array = []

with open("energies_aux.txt", "r") as infile, open("dispersion_aux.txt", "w") as outfile:
    for line in infile:
        match = re.match(r"(q[\d\._-]+)/.*E0=\s*(-?\.\d+E[+-]\d+)", line)
        if match:
            q = match.group(1)
            E0 = match.group(2)
            outfile.write(f"{q}  {E0}\n")
            qarray.append(q)
            E0_array.append(float(E0))

# Read the desired order
with open("qorder.txt", "r") as f:
    desired_order = [line.strip() for line in f]

# Read the existing output into a dictionary
with open("dispersion_aux.txt", "r") as f:
    output_lines = {}
    for line in f:
        parts = line.strip().split()
        if parts:
            qinfo = parts[0]
            output_lines[qinfo] = parts[1]  # Store only E0

# Write reordered and formatted lines
with open("dispersion.txt", "w") as f:
    for q in desired_order:
        if q in output_lines:
            q_formatted = q[1:].replace("_", " ")  # Remove 'q' and replace '_' with space
            f.write(f"{q_formatted}  {output_lines[q]}\n")
        else:
            print(f"Warning: {q} not found in output.txt")

file_path = "dispersion.txt"

with open(file_path, "r+") as f:
    lines = f.readlines()
    seventeenth_line = lines[16]  # Line 17 is at index 16
    f.write(seventeenth_line.rstrip())

os.system('rm *aux.txt')
