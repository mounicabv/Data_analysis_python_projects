import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
df['date'] = pd.to_datetime(df['date'])

# Clean data
df =  df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df.head()
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.lineplot(x = 'date', y = 'value', ax=ax, data=df,color='red').set(
        title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel = 'Date', ylabel = 'Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] =df_bar.index.year
    df_bar['Month'] =df_bar.index.month_name()

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
    table = pd.pivot_table(df_bar, values='value', index='year', columns='months', dropna=False)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    table = table.reindex(columns=months)

    # Draw bar plot
    ax = table.plot(kind='bar', figsize = (16,9), xlabel = 'Year', ylabel = 'Average Page Views')
    fig = ax.get_figure()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,(ax1, ax2) = plt.subplots(1, 2, figsize = (16, 9))
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1).set(title = "Year-wise Box Plot (Trend)", xlabel = 'Year', ylabel = 'Page Views')
    sns.boxplot(x="month", y="value", data=df_box, ax=ax2, 
    order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']).set(title = "Month-wise Box Plot (Seasonality)", xlabel = 'Month', ylabel = 'Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
