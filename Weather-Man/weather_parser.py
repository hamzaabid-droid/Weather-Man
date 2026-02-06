# import sys 
# Murree= sys.argv[1]

# with open(Murree, 'r') as f:
#     f_count=f.read()
    
# print(f_count)

# import pickle


# with open("data.pkl", "rb") as f:
#     data = pickle.load(f)
    
# print(data)    

num=[1,2,3,4,5]

def n(s):
    return s*s

num_sqr=list(map(n,num))

print(num_sqr)