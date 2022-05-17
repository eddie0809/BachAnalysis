from tokenize import String
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import entr, rel_entr, kl_div
import py_midicsv as pm
import sys


def header_skipper(filename):
    csv_string = pm.midi_to_csv(str(filename) + ".mid")

    with open(str(filename) + ".csv", "w") as f:
        f.writelines(csv_string)

    n=1
    with open(str(filename) + ".csv", "r") as csvfile:
        for i in csvfile:
            n = n+1
            if "2, 0, Start_track" in i:
                break
    return n


def file_getter():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Filename (no extension): ")
    return filename