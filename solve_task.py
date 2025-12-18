import pandas as pd
import re

file_path = 'data/regexHomeTask.txt'
clean_data = []

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
            tokens = re.findall(r'patient|control|M|F|\d+\.\d+|\d+', line)
            if len(tokens) == 6:
                clean_data.append(tokens)
columns = ['subject', 'group', 'age', 'sex', 'treadmill_speed', 'dva_logmar']
df = pd.DataFrame(clean_data, columns=columns)
df['age'] = pd.to_numeric(df['age'])
mean_age = df['age'].mean()
result = round(mean_age, 1)
final_answer = str(result).replace('.', ',')
print(f"Посчитанный ответ: {final_answer}")

