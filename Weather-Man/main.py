#!/usr/bin/env python3
# response=requests.post('https://jsonplaceholder.typicode.com/posts', json={'title':'boo','body': 'baa', 'userId': '1'
#  })
# print(response.status_code)
# print(response.json())







import argparse
parser= argparse.ArgumentParser(
    prog="Ca;lculator",
    description="Perform Calculation",
)
parser.add_argument('int1', help="This is number 1", type=int)
parser.add_argument('int2', help="This is number 2", type=int)
parser.add_argument('operation', help="add sub divd and mul")

args=parser.parse_args()
# print(args.int1)
# print(args.int2)
# print(args.operation)

int1, int2, operation = args.int1, args.int2, args.operation

if operation == 'add':
    print(int1+int2)
elif operation == 'sub':
    print(int1-int2)    
elif   operation == 'divd':
    print(int1/int2)
elif operation == 'mul':
    print(int1*int2)
else:
   raise ValueError("Invalid Operator")    




# # import os

# # file_path = os.path.join("/Users/hamza.abid/Desktop/Weather-Man/weatherfiles", "/Users/hamza.abid/Desktop/Weather-Man/weatherfiles/Murree_weather_2009_May.txt")

# # with open(file_path, "r") as file:
# #     content = file.read()
# #     print(content)
# # file=os.listdir(file_path)
# # print(file)
# # print(os.getcwd())


# # import sys

# # file_path = sys.argv[0]

# # with open(file_path, "r") as file:
# #     content = file.read()
# #     print(content)