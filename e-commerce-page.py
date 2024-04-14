import math as m
# importing libraries for data mining
import pandas as pd
import numpy as np

# importing libraries for visualisation
import matplotlib.pyplot as plt
# e commerce project: to do's

# loading dataset
df = pd.read_csv("e-commerce-data.csv")

# class 1: create a blueprint defining a visualisation object
class E_BarChart: 
  def __init__(self, x_data, y_data):
    self.x_data = x_data
    self.y_data = y_data
    
  def visualise_bar(self, n_rows, n_cols):
    fig, bar = plt.subplots(n_rows, n_cols)
    bar_n = plt.plot(kind="bar", x=self.x_data, y=self.y_data, ax=bar)
    return bar_n

  def add_description(label_x, label_y, bar_title):
    plt.xlabel(label_x)
    plt.ylabel(label_y)

# class 2: create a blueprint defining a dataframe object
class Bar_Data: 
  def __init__(self, data, col_name):
    self.data = data
    self.col_name = col_name

  def convert_2_var(self):
    graph_data = self.data[self.col_name].value_counts()
    graph_data = graph_data.reset_index()
    graph_data = graph_data.rename(columns = {"count":"Transaction_total"})
    return graph_data
  
  def reduce_row_num(self, init_data, row_num):
    reduced_data = init_data.iloc[:row_num]
    return reduced_data
# print(df)


# create data object 1
bar_data = Bar_Data(df, "Country")
df_bar = bar_data.convert_2_var()
df_bar = bar_data.reduce_row_num(df_bar, 6)
print(df_bar)

# # create a bar graph object 1
# x_bar_ax = df["Country"].value_counts()
bar_graph1 = E_BarChart(df_bar["Country"], df_bar["Transaction_total"])
graph_bar1 = bar_graph1.visualise_bar(1,1)
print(graph_bar1)