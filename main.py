# # # with open("weather_data.csv") as data_file:
# # #     data = data_file.readlines()
# # #     print(data)
# #
# #
# # import csv
# #
# # with open ("weather_data.csv") as data_file:
# #     data =csv.reader(data_file)
# #     Temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             Temperature.append(int(row[1]))
# #     print(Temperature)
# import pandas
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
#
# #to convert it to a dictionary
#
# # p_dict = df.to_dict()
# #
# # p_list = df["temp"].to_list()
# # max_num = max(p_list)
# # print(max_num)
# # sum_of_number = sum(p_list)
# # print(sum_of_number)
# #
# # length_of_number = len(p_list)
# #
# # average = sum_of_number / length_of_number
# #
# # print(round(average, 2))
# #
# # p_list = df["temp"].max()
# # print(p_list)
#
#
#
# # f = 9/5
# # monday  = data[data.day == "Monday"]
# # mon_temp = data[data.temp == data.temp.max()]
# # monday_tem = monday["temp"]
# # mon_tem_in_h = monday_tem * f + 32
# # print(f"the temp in fahreheit is {mon_tem_in_h}")
# #
#
# #for creating data
#
#
# data_dic = {
#     "student": ["daniel", "emeka","Angela"],
#     "scores" : [564, 456, 343]
#
# }
# #to write, we
# new_file = pandas.DataFrame(data_dic)
# print(new_file)
#
# #to write it into a csv file, we
# new_file.to_csv("new_school_data.csv")
import pandas
import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231212.csv")
grey_squirels_lens = len(data[data["Primary Fur Color"] == "Gray"])
red_squirels_lens = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirels_lens = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirels_lens)
print(red_squirels_lens)
print(black_squirels_lens)

squirel_dic = {
    "Colors": ["Gray", "Cinnamon","Black"],
    "counts": [grey_squirels_lens, red_squirels_lens, black_squirels_lens]
}
#convert it to a data frame
df = pandas.DataFrame(squirel_dic)

#convert it to csv
df.to_csv("Squirrel_colour_count.csv")