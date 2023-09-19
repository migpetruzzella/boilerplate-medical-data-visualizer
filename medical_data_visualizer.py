import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')


# Add 'overweight' column
bmi = df['weight'] / ((df['height'] * 0.01)** 2)

df['overweight'] = bmi.apply(lambda x: 1 if x > 25 else 0)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol']=  df['cholesterol'].apply( lambda x: 0 if x==1 else 1)
df['gluc']=  df['gluc'].apply( lambda x: 0 if x==1 else 1)



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='total')
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = df_cat.groupby(['cardio', 'variable', 'total'])['total'].count().reset_index(name='count')

    # Draw the catplot with 'sns.catplot()'
    plot= sns.catplot(data=df_cat, x='variable', hue='total', col='cardio', kind='count')
    plot.set_axis_labels("variable", "total")

    # Get the figure for the output
    fig=plt.gcf()
    fig.savefig('catplot.png')
    plt.show()


    # Do not modify the next two lines
    return fig



# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    

    # Calculate the correlation matrix
    corr = df_heat.corr()
    

    # Generate a mask for the upper triangle
    fig, ax = plt.subplots()
    sns.heatmap(corr, cmap='inferno', annot=False, mask=np.triu(corr))


    # Show the plot
    fig=plt.gcf()
    plt.show()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig




