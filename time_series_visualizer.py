import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date']).set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (20,10))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12-2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df)
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month_name()]).mean().value.unstack()
    df_bar.columns.name = 'Months'

    # Draw bar plot
    fig, ax = plt.subplots()
    fig = df_bar.plot(kind = 'bar', xlabel = 'Years', ylabel = 'Average Page Views', figsize=(15,10)).get_figure()



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
    df_box = df_box.sort_values('month', key = lambda x : pd.to_datetime(x, format = '%b').dt.month)
    fig, ax = plt.subplots(1, 2, figsize = (25,10))
    sns.boxplot(
        ax = ax[0],
        data = df_box,
        y = 'value',
        x = 'year'
    )
    sns.boxplot(
        ax = ax[1],
        data = df_box,
        y = 'value',
        x = 'month'
    )
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
