from noise_generator import generate_noise
from map_creator import create_map_from_noise

"""
MapGenerator
simple python script that creates randomly generated world maps
based on an OpenSiplex noise. This project is currently in a
very early stage of development and doesn't have a graphical user interface
"""

# Ask the user for all required variables
width = int(input("Please enter the desired width (int): "))
height = int(input("Please enter the desired height (int): "))
feature_size = float(input("Please enter the desired feature size (float): "))
seed = input("Please enter the seed (leave blank for random): ")
filename = str(input("Please enter the desired name of the generated file (ending in .png): "))
print("Generating... This might take a while :)")

# generate the noise image
noise = generate_noise(width, height, feature_size, seed)
print("The noise has been generated")

# turn the noise image into a map
noise = noise.tobytes()
result = create_map_from_noise(noise, width, height)
result.save(filename)
print(f"The map has been saved as: {filename}")
input("Press any key to exit")
