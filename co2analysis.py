#Importing packages
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pan
import numpy as np





#Initializing the data that needs to be initialized
Co2Data = []
validMonthlyYears = []
Years = set()
yearlyMonthlyCo2Dict = {}
secondYearlyMonthlyCo2Dict = {}
yearlyAverageCo2Dict = {}
validYears = []
personalizedYears = []
yearlyCo2Dict = {}
variatingYearlyMonthlyCo2Dict = {}
avgCo2 = []
def bulbs(sort):
  for i in range(len(sort)):
    for i in range(1, len(sort)):
      if sort[i - 1] > sort[i]:
        sort[i - 1], sort[i] = sort[i], sort[i - 1]
  return sort
def predict(m, b, x):
  y = m * x + b
  return y





#Creating the data
f = open('Co2Data.csv', 'r', encoding = "utf-8")
Temp2Co2Data = csv.DictReader(f)
for row in Temp2Co2Data:
  Co2Data.append(row)
for i in range(len(Co2Data)):
  if Co2Data[i]['Carbon Dioxide (ppm)'] != '':
    yearlyMonthlyCo2Dict[int(Co2Data[i]['Year'])] = []
    secondYearlyMonthlyCo2Dict[float(Co2Data[i]['Decimal Date'])] = 0
    yearlyCo2Dict[int(Co2Data[i]['Year'])] = []
    variatingYearlyMonthlyCo2Dict[float(Co2Data[i]['Decimal Date'])] = 0
for i in range(len(Co2Data)):
  Years.add(int(Co2Data[i]['Year']))
  if Co2Data[i]['Carbon Dioxide (ppm)'] != '':
    yearlyMonthlyCo2Dict[int(Co2Data[i]['Year'])].append(float(Co2Data[i]['Carbon Dioxide (ppm)']))
    secondYearlyMonthlyCo2Dict[float(Co2Data[i]['Decimal Date'])] = float(Co2Data[i]['Carbon Dioxide (ppm)'])
    validMonthlyYears.append(float(Co2Data[i]['Decimal Date']))
    validYears.append(int(Co2Data[i]['Year']))
    yearlyCo2Dict[int(Co2Data[i]['Year'])].append(float(Co2Data[i]['Carbon Dioxide (ppm)']))
Years = list(Years)
Years = bulbs(Years)
tempYears = Years
for i in range(len(Years)):
  Years[i] = str(Years[i])
mean = sum(secondYearlyMonthlyCo2Dict.values()) / len(secondYearlyMonthlyCo2Dict.values())
if len(str(mean).split('.')[1]) > 2:
    mean = float(str(mean).split('.')[0] + '.' + str(mean).split('.')[1][0 : 2])
for i in range(len(validMonthlyYears)):
  if mean > secondYearlyMonthlyCo2Dict[validMonthlyYears[i]]:
    variatingYearlyMonthlyCo2Dict[validMonthlyYears[i]] = mean - secondYearlyMonthlyCo2Dict[validMonthlyYears[i]]
  else:
    variatingYearlyMonthlyCo2Dict[validMonthlyYears[i]] = secondYearlyMonthlyCo2Dict[validMonthlyYears[i]] - mean
for j in validMonthlyYears:
  if len(str(variatingYearlyMonthlyCo2Dict[j]).split('.')[1]) > 2:
    variatingYearlyMonthlyCo2Dict[j] = float(str(variatingYearlyMonthlyCo2Dict[j]).split('.')[0] + '.' + str(variatingYearlyMonthlyCo2Dict[j]).split('.')[1][0 : 2])
startAndEndDates = {'Start Date': input('Please type a start year between 1958 and 2017 for a range of data to plot: '), 'End Date': input('Please type a end year higher than your start years and between 1958 and 2017 for a range of data to plot: ')}
while startAndEndDates['Start Date'] == startAndEndDates['End Date'] or (startAndEndDates['Start Date'] not in Years or startAndEndDates['End Date'] not in Years) or (int(startAndEndDates['Start Date']) > int(max(tempYears)) or int(startAndEndDates['Start Date']) < int(min(tempYears))) or (int(startAndEndDates['End Date']) > int(max(tempYears)) and int(startAndEndDates['End Date']) < int(min(tempYears))):
  print('Dates Invalid!')
  startAndEndDates = {'Start Date': input('Please type a start year between 1958 and 2017 for a range of data to plot: '), 'End Date': input('Please type a end year higher than your start years and between 1958 and 2017 for a range of data to plot: ')}
startAndEndDates['Start Date'] = int(startAndEndDates['Start Date'])
startAndEndDates['End Date'] = int(startAndEndDates['End Date'])
if startAndEndDates['Start Date'] > startAndEndDates['End Date']:
  startAndEndDates['Start Date'], startAndEndDates['End Date'] = startAndEndDates['End Date'], startAndEndDates['Start Date']
  print('You set the start year greater than the end year, start year and end year swapped:\n  Start Year: ' + str(startAndEndDates['Start Date']) + '\n  End Year: ' + str(startAndEndDates['End Date']))
barplotLength = input('How many years would you like to analyze on a bar graph and box plot(you need to enter the specific years afterwards): ')
while not barplotLength.isnumeric() or (int(barplotLength) <= 0 or int(barplotLength) > len(Years)):
  print('Invalid Number!')
  barplotLength = input('How many years would you like to analyze on a bar graph and box plot(you need to enter the specific years afterwards): ')
barplotLength = int(barplotLength)
for i in range(barplotLength):
  personalizedYear = input('Type a year from 1958 to 2017 to include in your bar graph: ')
  while (personalizedYear not in Years or (int(personalizedYear) > int(max(tempYears)) or int(personalizedYear) < int(min(tempYears))) or (int(startAndEndDates['End Date']) > int(max(tempYears)) or int(personalizedYear) in personalizedYears)):
    print('Invalid Date/Already have date!')
    personalizedYear = input('Type a year from 1958 to 2017 to include in your bar graph: ')
  personalizedYears.append(int(personalizedYear))
predictionEnd = input('Enter a end year above ' + Years[len(Years) - 1] + ' to plot a co2 prediction in a lineplot: ')
while not predictionEnd.isnumeric() or int(predictionEnd) <= int(Years[len(Years) - 1]):
  print('Invalid Input!')
  predictionEnd = input('Enter a end year above ' + str(Years[len(Years) - 1]) + ' to plot a co2 prediction in a lineplot: ')
predictionEnd = int(predictionEnd)
for i in range(len(Years)):
  Years[i] = int(Years[i])
for j in Years:
  temp = 0
  for i in yearlyMonthlyCo2Dict[j]:
    temp += i
  yearlyAverageCo2Dict[j] = temp / len(yearlyMonthlyCo2Dict[j])
  if len(str(yearlyAverageCo2Dict[j]).split('.')[1]) > 2:
    yearlyAverageCo2Dict[j] = float(str(yearlyAverageCo2Dict[j]).split('.')[0] + '.' + str(yearlyAverageCo2Dict[j]).split('.')[1][0 : 2])
for i in range(len(Years)):
  avgCo2.append(yearlyAverageCo2Dict[Years[i]])
x = np.array(Years)
y = np.array(avgCo2)
m, b = np.polyfit(x, y, 1)
lineplotYearlyAverageCo2Dict = {'Years': Years, 'Co2' : []}
for i in Years:
  lineplotYearlyAverageCo2Dict['Co2'].append(yearlyAverageCo2Dict[i])
df = pan.DataFrame(data = lineplotYearlyAverageCo2Dict)
scatterplotYearlyMonthlyCo2Dict = {'Years': validMonthlyYears, 'Co2': []}
for i in range(len(validMonthlyYears)):
  scatterplotYearlyMonthlyCo2Dict['Co2'].append(secondYearlyMonthlyCo2Dict[validMonthlyYears[i]])
df2 = pan.DataFrame(data = scatterplotYearlyMonthlyCo2Dict)
lineplotPersonalizedYearlyAverageCo2Dict = {'Years': [], 'Co2' : []}
for i in range(startAndEndDates['Start Date'], startAndEndDates['End Date'] + 1):
  lineplotPersonalizedYearlyAverageCo2Dict['Years'].append(i)
  lineplotPersonalizedYearlyAverageCo2Dict['Co2'].append(yearlyAverageCo2Dict[i])
df3 = pan.DataFrame(data = lineplotPersonalizedYearlyAverageCo2Dict)
scatterplotPersonalizedYearlyMonthlyCo2Dict = {'Years': [], 'Co2': []}
for i in range(len(validMonthlyYears)):
  if int(str(validMonthlyYears[i]).split('.')[0]) == startAndEndDates['Start Date']:
    startDateIndex = i
    break
for i in range(len(validMonthlyYears) - 1, 0, -1):
  if int(str(validMonthlyYears[i]).split('.')[0]) == startAndEndDates['End Date']:
    endDateIndex = i
    break
for i in range(startDateIndex, endDateIndex + 1):
  scatterplotPersonalizedYearlyMonthlyCo2Dict['Years'].append(validMonthlyYears[i])
  scatterplotPersonalizedYearlyMonthlyCo2Dict['Co2'].append(secondYearlyMonthlyCo2Dict[float(validMonthlyYears[i])])
df4 = pan.DataFrame(data = scatterplotPersonalizedYearlyMonthlyCo2Dict)
barGraphPersonalizedAveragedCo2Dict = {'Years': personalizedYears, 'Co2': []}
for i in range(len(personalizedYears)):
  barGraphPersonalizedAveragedCo2Dict['Co2'].append(yearlyAverageCo2Dict[personalizedYears[i]])
df5 = pan.DataFrame(data = barGraphPersonalizedAveragedCo2Dict)
boxPlotPersonalizedCo2Dict = {'Years': [], 'Co2': []}
for j in range(len(personalizedYears)):
  for i in range(len(yearlyCo2Dict[personalizedYears[j]])):
    boxPlotPersonalizedCo2Dict['Years'].append(personalizedYears[j])
    boxPlotPersonalizedCo2Dict['Co2'].append(yearlyCo2Dict[personalizedYears[j]][i])
df6 = pan.DataFrame(data = boxPlotPersonalizedCo2Dict)
scatterplotVariatingYearlyMonthlyCo2Dict = {'Years': validMonthlyYears, 'Co2': []}
for i in range(len(validMonthlyYears)):
  scatterplotVariatingYearlyMonthlyCo2Dict['Co2'].append(variatingYearlyMonthlyCo2Dict[validMonthlyYears[i]])
df7 = pan.DataFrame(data = scatterplotVariatingYearlyMonthlyCo2Dict)
boxPlotYearlyMonthlyCo2Dict = {'Years': [], 'Co2': []}
for j in range(len(validYears)):
  for i in range(len(yearlyMonthlyCo2Dict[validYears[j]])):
    boxPlotYearlyMonthlyCo2Dict['Years'].append('')
    boxPlotYearlyMonthlyCo2Dict['Co2'].append(yearlyMonthlyCo2Dict[validYears[j]][i])
df8 = pan.DataFrame(data = boxPlotYearlyMonthlyCo2Dict)





#All code responsible for plotting
Co2AvgLevelsLineplot = sns.lineplot(x = 'Years', y = 'Co2', data = df)
Co2AvgLevelsLineplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2AvgLevelsLineplot.png')
plt.clf()
Co2LevelsScatterplot = sns.scatterplot(x = 'Years', y = 'Co2', data = df2)
Co2LevelsScatterplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2LevelsScatterplot.png')
plt.clf()
Co2PersonalizedAvgLevelsLineplot = sns.lineplot(x = 'Years', y = 'Co2', data = df3)
Co2PersonalizedAvgLevelsLineplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2PersonalizedAvgLevelsLineplot.png')
plt.clf()
Co2LevelsPersonalizedScatterplot = sns.scatterplot(x = 'Years', y = 'Co2', data = df4)
Co2LevelsPersonalizedScatterplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2PersonalizedLevelsScatterplot.png')
plt.clf()
Co2LevelsPersonalizedAvgBarplot = sns.barplot(x = 'Years', y = 'Co2', data = df5)
Co2LevelsPersonalizedAvgBarplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2PersonalizedAvgLevelsBarplot.png')
plt.clf()
Co2LevelsPersonalizedBoxplot = sns.boxplot(x = 'Years', y = 'Co2', data = df6)
Co2LevelsPersonalizedBoxplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2LevelsPersonalizedBoxplot.png')
plt.clf()
Co2VariatingLevelsScatterplot = sns.scatterplot(x = 'Years', y = 'Co2', data = df7)
Co2VariatingLevelsScatterplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Variability', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2VariatingLevelsScatterplot.png')
plt.clf()
Co2LevelsBoxplot = sns.boxplot(x = 'Years', y = 'Co2', data = df8)
Co2LevelsBoxplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "All Years: " + str(Years[0]) + ' to ' + str(Years[len(Years) - 1]))
plt.savefig('Co2LevelsBoxplot.png')
plt.clf()
plt.plot(x, y, 'o')
plt.plot(x, m * x + b)
plt.title('Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged')
plt.savefig('AvgCo2LevelsLineOfBestFit.png')
plt.clf()





#Printing the key
print('Key in ppm of carbon dioxide levels:\n  <450 = Best\n  450-700 = Great\n  700-1000 = Okay\n  1000-2500 = Bad\n  2500-5000 = Horrible\n  >5000 = Intolerable')





#Printing the prediction for a certain year
print('Prediction for year ' + str(predictionEnd) + ': ' + str(predict(m, b, predictionEnd)))





#Printing the analysis
print('Analysis:\n  From the data in "Co2AvgLevelsLineplot.png" and "Co2LevelsScatterplot.png" I observed that there is a positive trend between the years and the co2 levels. The difference between "Co2AvgLevelsLineplot.png" and "Co2LevelsScatterplot.png" is that in "Co2LevelsScatterplot.png", the data is more spread out, which helps in plotting more data points and getting an in depth view of the data.\n  In "Co2PersonalizedAvgLevelsLineplot.png" and "Co2PersonalizedLevelsScatterplot.png", the data can be adjusted to your favor, focusing on the part you want to see.\n  In "Co2PersonalizedAvgLevelsBarplot.png", you can see different co2 levels of years of your choice and any length, this helps you compare different years and how they changed.\n  In "Co2LevelsPersonalizedBoxplot.png", the data is the same from "Co2PersonalizedAvgLevelsBarplot.png", but it is not averaged, box plots show data more detailed and that is why I chose to do a box plot too instead of just a bar plot.\n  In "Co2VariatingLevelsScatterplot.png", I chose to show how much the co2 level variates from the mean which is the average of all the co2 levels.\n  "Co2LevelsBoxplot.png", shows the grouping of data, that it is skewed more towards the minimum and many more details about the data.\n  "AvgCo2LevelsLineOfBestFit.png", shows the trend line of the co2 levels every within the available years. The line of best fit helps us compute the slope and the intersect which in turn is used for prediction of co2 values for any year entered by the user, which you can see right before the analysis.\n  By studying and analyzing these graphs, I conclude that the air pollution levels have been steadily increasing over the years. Hence, we should all participate ihow n the effort to reduce co2 by planting more trees, riding your bike, using public transport, carpooling and many more actions can help reduce co2.')





#Closing the csv file
f.close()