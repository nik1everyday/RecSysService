'''import dill
import pandas as pd
import joblib
import yaml

from rectools import Columns
from rectools.model_selection import TimeRangeSplit

from models.ann import Ann

with open('config/config_models.yml') as stream:
    config = yaml.safe_load(stream)

ANN = {
    'model_loaded': False,
    'model': None,
    'label': None,
    'distance': None,
}

interactions = None
# do not train
train = None






# def load_ann():
#     global ANN
#     if not ANN['model_loaded']:
#         ANN['label'] = joblib.load(
#             config['ANN_model_conf']['label'],
#         )
#         ANN['distance'] = joblib.load(
#             config['ANN_model_conf']['distance'],
#         )
#         ANN['model'] = Ann(ANN['label'], ANN['distance'])
#
#
# def main():
#     global interactions
#     global train
#     load_ann()
#     interactions = train
'''
