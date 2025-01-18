import os
import pandas as pd

input_directory = r'C:\Users\Admin\Desktop\Akshat\input_directory'
output_csv = r'C:\Users\Admin\Desktop\Akshat\summary_statistics.csv'


def numerical_calculation(df):
    stats = []
    for column in df.select_dtypes(include='number').columns:
        mean_val = df[column].mean()
        median_val = df[column].median()
        stats.append({"Column": column, "Mean": mean_val, "Median": median_val})
    return pd.DataFrame(stats)


all_stats = []

for file in os.listdir(input_directory):
        filepath = os.path.join(input_directory, file)  
        df = pd.read_csv(filepath)
        stats_df = numerical_calculation(df)
        stats_df.insert(0, "File", file)  
        all_stats.append(stats_df)
    


final_stats = pd.concat(all_stats, ignore_index=True)
final_stats.to_csv(output_csv, index=False)
print(f"Summary statistics saved to {output_csv}")
