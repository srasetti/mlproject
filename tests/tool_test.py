# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_tools():
    assert haversine(48.865070, 2.380009,45.526037, -73.5974456) == 8451.45254601196
