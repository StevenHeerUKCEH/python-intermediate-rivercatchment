import pandas as pd

pd.read_csv('data/rain_data_2015-12.csv', usecols=['Site', 'Date', 'Rainfall (mm)'])

from catchment import models

dataset = models.read_variable_from_csv('data/rain_data_2015-12.csv')

type(dataset)

dataset.shape

dataset

sample_dataset = models.read_variable_from_csv('data/rain_data_small.csv')
sample_dataset

from catchment.models import daily_total

daily_total(sample_dataset)

import pandas as pd
import pandas.testing as pdt
from catchment.models import daily_mean
import datetime

test_input = pd.DataFrame(
    data=[[1.0, 2.0],
          [3.0, 4.0],
          [5.0, 6.0]],
    index=[pd.to_datetime('2000-01-01 01:00'),
           pd.to_datetime('2000-01-01 02:00'),
           pd.to_datetime('2000-01-01 03:00')],
    columns=['A','B']
)

test_output = pd.DataFrame(
    data=[[3.0, 4.0]],
    index=[datetime.date(2000,1,1)],
    columns=['A','B']
)

pdt.assert_frame_equal(daily_mean(test_input), test_output)

import pytest
...
def test_daily_min_python_list():
    """Test for AttributeError when passing a python list"""
    from catchment.models import daily_min

    with pytest.raises(AttributeError):
        error_expected = daily_min([[3, 4, 7],[-3, 0, 5]])
