#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# group.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

print("\n\n年人均产值")
print(df.groupby('year')['lifeExp'].mean())

print("\n\n基于年分组")
grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df)

print("\n\nlifeExp")
grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
print(grouped_year_df_lifeExp)

print("\n\n年平均产值")
mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

print("\n\n基于年和洲分组")
print(df.groupby(['year', 'continent'])[['lifeExp',
'gdpPercap']].mean())

print("\n\n统计每个洲的国家数")
print(df.groupby('continent')['country'].nunique())
