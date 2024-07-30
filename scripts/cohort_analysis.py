import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def cohort_analysis(df):
    df.set_index('Month', inplace=True)
    cohort_size = df['Qty_blog_readers']

    retention_df = pd.DataFrame(index=df.index)
    retention_df['Buy_within_24_hrs'] = df['Buy_within_24_hrs'] / cohort_size
    retention_df['Buy_within_1_week'] = df['Buy_within_1_week'] / cohort_size
    retention_df['Buy_within_2_weeks'] = df['Buy_within_2_weeks'] / cohort_size
    retention_df['Buy_within_3_weeks'] = df['Buy_within_3_weeks'] / cohort_size

    plt.figure(figsize=(12, 8))
    sns.heatmap(retention_df, annot=True, fmt='.0%', cmap='coolwarm')
    plt.title('Cohort Analysis - Retention Rate')
    plt.xlabel('Time')
    plt.ylabel('Cohort (Month)')
    plt.show()