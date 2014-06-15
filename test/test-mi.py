#!/usr/bin/env python 
import sys 
sys.path.append("../src/")
import bmu 
import utils
import numpy as np 
import mi

biom_fp = "../data/caporaso-gut.biom"
map_fp = "../data/caporaso-gut.txt"


data, samples, features = bmu.load_biom(biom_fp)
map_data = bmu.load_map(map_fp)
labels, label_map = utils.label_formatting(map_data, samples, 
  "SEX", signed=False)
samples = np.array(samples)
features = np.array(features)

m = mi.calc_mi(data, labels)
