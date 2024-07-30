import pandas as pd
import matplotlib.pyplot as plt


def funnel_analysis(df):
    activities = ['Buy_within_24_hrs', 'Buy_within_1_week', 'Buy_within_2_weeks', 'Buy_within_3_weeks']
    funnel_data = df[activities].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(funnel_data.index, funnel_data.values, marker='o')
    plt.title('Funnel Analysis')
    plt.xlabel('Activity')
    plt.ylabel('Number of Users')
    plt.show()