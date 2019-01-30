import tabula
import pandas as pd
df = tabula.read_pdf('Sample3.pdf',
	pages='all',
	stream=True,
	columns=(85.571,125.752,270.851,334.843,416.693,472.5),
	encoding='ISO-8859-1',
	area=(77.802,43.158,736.326,475.477),
	guess=False,
	pandas_options={'header':None})
for _, row in df.fillna('').iterrows():


	# print(row.tolist())
	print("====================val:",row[0])
#	print("######################1",row[1])
#	print("######################2",row[2])
#	print("######################3",row[3])
	

df.to_csv('kishore.csv')


# def __extractData(self,response):
#         def rolling_group(val):
#             if pd.notnull(val): 
#             # if pd.notnull(val) and '/' in val and not 'st' in val:
#                 rolling_group.group += 1
#             return rolling_group.group

#         rolling_group.group = 0  

#         def joinFunc(g, column):
#             col = g[column]
#             joiner = "/"
#             s = joiner.join([str(each) for each in col if pd.notnull(each)])
#             s = re.sub("(?<=&)" + joiner, " ", s)  
#             s = re.sub("(?<=-)" + joiner, " ", s)  
#             s = re.sub(joiner * 2, joiner, s)
#             return s

#         def getDf(temp_file, area):
#             return tabula.read_pdf('/home/ait-python/Downloads/Sample.pdf',
#                 pages='8-27',
#                 Stream=True,
#                 silent=True,
#                 guess=False,
#                 columns=[85.571,125.752,270.851,334.843,416.693,472.5],
#                 encoding='ISO-8859-1',
#                 area=[77.802,43.158,736.326,475.477],
#                 pandas_options={'header': 'infer'}
#                 ).replace('\r', ' ', regex=True).dropna(how='all')
#         df.columns = ['serial_no','name','regno','sem','subject','exam_fee'] 
#         groups = df.groupby(df['expiration'].apply(rolling_group), as_index=False)
#         groupFunct = lambda g: pd.Series([joinFunc(g, col) for col in g.columns], index=g.columns)
#         final_df = groups.apply(groupFunct).fillna('')
#         yield final_df.to_dict('records')



# def parse_pdf(self, response):
#         for row in self.__extractData(response):
#             for col in row:
#             	print("####################3",row[1])



# df.to_csv('test.csv')


# 	import tabula
# df = tabula.read_pdf('http://www.cohassetma.org/ArchiveCenter/ViewFile/Item/351',
# 	pages='1',
# 	encoding='ISO-8859-1',
# 	area = (72.45,34.02,531.09,836.64),
# 	guess=True,
# 	pandas_options={'header': 'infer'}).fillna('')
# 	# count = 1
# for _, row in df.fillna('').iterrows():
# 	row=row.tolist()
# 	print()

# -------------------------------------------------------



# jan2015
# overall = 73.166,16.3,539.566,852.3
# 57.766,15.2,543.966,46.0
# 61.066,41.6,549.466,84.5
# 59.966,84.5,547.266,123.0
# 58.866,125.2,550.566,186.8
# 59.966,185.7,549.466,268.2
# 57.766,266.0,551.666,305.6
# 57.766,305.6,552.766,395.8

# 13-july
# 60.899,17.46,546.989,784.71

# 60.899,20.43,547.979,67.95
# 59.909,68.94,547.979,112.5
# 61.889,111.51,546.989,164.97
# 60.899,161.01,545.009,263.97
# 59.909,263.97,547.979,295.65
# 61.889,294.66,554.909,383.76
# 60.899,386.73,548.969,421.38
# 61.889,420.39,546.989,474.84
# 61.889,474.84,547.979,689.67
# 61.889,688.68,546.989,781.74

# 46.049,157.05,545.999,263.97


# [67.95,112.5,164.97,263.97,295.65,383.76,421.38,474.84,689.67,781.74]
# --------------------------------------------------------------------------------------#
# Request URL: https://www.google.com/recaptcha/api2/userverify?k=6LchcFEUAAAAAJdfnpZDr9hVzyt81NYOspe29k-x

# https://azbop.igovsolution.com/online/JS_grd/Grid.svc/Verifycaptcha


# resp	03AO9ZY1DFOP27CJigdCkAIg--LNN5CTusOnebR4d2gyisLc4TdnMSkXcn4YFx1_kin6aP0YNOUf9F_tpR_BhWXtUppmMhROhQg3TtfI0hqBTr_VIAmuEqkSnvEp5FdMc9uvCSR1sN1MZxbEKOteBtJg6dpChUwwo1JN1S0xZqWKcWFrJ5fbYxiEn382xMSHhHckwaRI1yWuGdXfa7xKqGECzscq0ysopPlkuzSkDeGJow4WynqnJ03YJ1D8CGWhY0XTITgTs78XQDFPFhbKnJIgiKH49SLLdBCqC7d6oTrEYejuHksLpPEYc
# uip	

# https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LchcFEUAAAAAJdfnpZDr9hVzyt81NYOspe29k-x&co=aHR0cHM6Ly9hemJvcC5pZ292c29sdXRpb24uY29tOjQ0Mw..&hl=en&v=v1543818755456&size=normal&cb=b3uulwvv49rl
# ar	1
# cb	b3uulwvv49rl
# co	aHR0cHM6Ly9hemJvcC5pZ292c29sdXRpb24uY29tOjQ0Mw..
# hl	en
# k	6LchcFEUAAAAAJdfnpZDr9hVzyt81NYOspe29k-x
# size	normal
# v	v1543818755456



# https://azbop.igovsolution.com/online/JS_grd/Grid.svc/GetIndv_license

# fname	a
# lictype	1
# lname	sa
# lnumber	
# page	1
# pageSize	20
# sdata	[]
# sortby	
# sortexp	
# vid	782665669abc402e86b30e91946578d8