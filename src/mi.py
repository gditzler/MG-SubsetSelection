#!/usr/bin/env python 
import numpy as np
import ctypes as c

try:
  libMIToolbox = c.CDLL("libMIToolbox.so"); 
except:
  raise Exception("Error: could not load libMIToolbox.so")


def calc_mi(data, labels):
  data, labels = check_data(data, labels)
  n_observations, n_features = data.shape
  c_n_observations = c.c_int(n_observations)
  output = []

  for c_data in data.transpose():
    libMIToolbox.calculateMutualInformation.restype = c.POINTER(
      c.c_double )
    output = libMIToolbox.calculateMutualInformation(
      c_data.ctypes.data_as(c.POINTER(c.c_double)),
      labels.ctypes.data_as(c.POINTER(c.c_double)),
      c_n_observations
      )
    print dir(output)
    for o in output.contents:
      print o

  return None


def check_data(data, labels):
  """
    Check dimensions of the data and the labels.  Raise and exception
    if there is a problem.

    Data and Labels are automatically cast as doubles before calling the 
    feature selection functions

    @param data: the data 
    @param labels: the labels
    @return (data, labels): ndarray of floats
    @rtype: tuple
  """
  if isinstance(data, np.ndarray) is False:
    raise Exception("data must be an numpy ndarray.")
  if isinstance(labels, np.ndarray) is False:
    raise Exception("labels must be an numpy ndarray.")
  if len(data) != len(labels):
    raise Exception("data and labels must be the same length")
  return 1.0*data, 1.0*labels
