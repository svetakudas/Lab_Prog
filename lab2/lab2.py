from spyre import server
from os import mkdir, listdir
import pandas as pd
import json
from matplotlib import pyplot as plt
import sys
sys.path.append("../lab1")
from lab1 import load_into_frame, DEST_FOLDER, COLS
import numpy as np

DEST_FOLDER = '../lab1/' + DEST_FOLDER

class SimpleApp(server.App):

    title = "Regions of Ukraine"

    inputs = [{     "input_type":'dropdown',
                    "label": 'Index',
                    "options" : [ {"label": "VHI", "value": "VHI"},
                                  {"label": "VCI", "value": "VCI"},
                                  {"label": "TCI", "value": "TCI"}],
                    "variable_name": 'index',
                    "action_id": "update_data" },

                {   "input_type":'text',
                    "label": 'Week max range',
                    "value": 10,
                    "variable_name": 'week_range',
                    "action_id": "update_data" }]

    controls = [{   "control_type" : "hidden",
                    "label" : "Refresh",
                    "control_id" : "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{    "output_type" : "plot",
                    "output_id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot",
                    "on_page_load" : True },

                {   "output_type" : "table",
                    "output_id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def getData(self, params):
        return load_into_frame(DEST_FOLDER)

    def getPlot(self, params):
        df = self.getData(params)
        week_range = int(params['week_range'])
        index = params['index']
        index_list = df[index].drop_duplicates().values
        if index_list.size > week_range:
            y = index_list[:week_range]
        else:
            week_range = week_range - index_list.size + 1
        x = np.arange(1, week_range + 1, 1)
        plt.xlabel('Index')
        plt.ylabel('Weeks')
        plt.title('Index Diagram')
        plt.plot(x,y)
        return plt.gcf()

app = SimpleApp()
app.launch(port=9093)
