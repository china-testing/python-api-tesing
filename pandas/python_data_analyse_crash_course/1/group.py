#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-12
# group.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df)

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
print(grouped_year_df_lifeExp)

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)


print(df.groupby(['year', 'continent'])[['lifeExp',
'gdpPercap']].mean())

# 统计每个洲的国家数
print(df.groupby('continent')['country'].nunique())
