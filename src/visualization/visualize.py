import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def yearly_seasonality_plot(
        data: pd.DataFrame, 
        date_column: str, 
        target_column: str, 
        title: str
    ) -> None:
    """
    Create Multiple Line Plots in The Same Place, Differentiate by Year
    
    Args:
        data (pd.DataFrame) : Actual Values.
        date_column (str)   : Data Column Name.         
        target_column (str) : Target Column Name.
        title (str)         : Title for The Plot
    
    Returns:
        None
    """
    data = data
    data.loc[:, 'month'] = data[date_column].dt.month
    data.loc[:, 'year'] = data[date_column].dt.year
    ax = sns.lineplot(
        data=data,
        x='month',
        y=target_column,
        hue='year',
    )
    ax.set(
        title=title,
        xlabel='month',
        ylabel=target_column
    )
    plt.show()
    
    
def subseries_yearly_seasonality_plot(
        data: pd.DataFrame, 
        date_column: str, 
        target_column: str, 
        title: str
    ) -> None:
    """
    Create Multiple Line Plots Separated by Month, and Inside Each Plot Contain The
    Values from The Same Month for Different Year.
    
    Args:
        data (pd.DataFrame) : Actual Values.
        date_column (str)   : Data Column Name.         
        target_column (str) : Target Column Name.
        title (str)         : Title for The Plot
    
    Returns:
        None
    """
    data.loc[:, 'month'] = data[date_column].dt.month
    data.loc[:, 'year'] = data[date_column].dt.year
    mean_by_month = data.groupby(by='month').agg({target_column: 'mean'})
    data = data.merge(mean_by_month, on='month', how='left')
    fg = sns.relplot(
        data=data,
        x='year',
        y=target_column+'_x',
        col='month',
        kind='line'
    )

    for i, ax in enumerate(fg.axes.flat):
        sns.lineplot(data=data[data['month']==i+1], x='year', y=target_column+'_y', color='orange', ax=ax)
    
    fg.figure.suptitle(title)
    plt.show()
    
    
def train_test_plot(
        train: pd.DataFrame, 
        test: pd.DataFrame, 
        date_column: str, 
        target_column: str, 
        title: str
    ) -> None:
    """
    Create Multiple Line Plots Separated by Month, and Inside Each Plot Contain The
    Values from The Same Month for Different Year.
    
    Args:
        data (pd.DataFrame) : Actual Values.
        date_column (str)   : Data Column Name.         
        target_column (str) : Target Column Name.
        title (str)         : Title for The Plot
    
    Returns:
        None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(train[date_column], train[target_column], label='Train')
    plt.plot(test[date_column], test[target_column], label='Test')
    plt.title(title, size=20)
    plt.xlabel("Date", size=15)
    plt.ylabel(target_column, size=15)
    plt.legend()
    plt.show()