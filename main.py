# st1 = "How many times the times are repeating in the sentence. Let's count"
import pandas as pd
import openpyxl 
with open("text1.txt", "r") as f:
  st1 = f.read()
result = []
result1 = []
sent1 = st1.split(" ")
for i in sent1:
  result.append(st1.count(i))
  
  result1.append(i)

# print(result)
final = []
for a, i in zip(result, result1):
  final.append(i + " " + str(a))
# print(max(result), min(result))

def del_dub(x):
  lis1 = []
  for i in x:
    if i not in lis1:
      lis1.append(i)

  return lis1

print(del_dub(final))

# with open("excel1.xlsx", "w") as ex:
#   ex.write(del_dub(final))


df1 = pd.DataFrame([[del_dub(final)]],

                   index=['row 1'],

                   columns=['col 1'])

df1.to_excel("output.xlsx")  
#++++++++++++++++++++++++++++++++++++++++++
# def votes(x):
#   vote = []
#   vote1 = []

#   for i in x:
    
#     if i not in vote:
#       vote.append(i)
#     else:
#       vote1.append(i)
  
#   return f"{vote1} voted two times"
  
#+++++++++++++++++++++++++++++++++++++++++++++++++


# print(votes(["Rinat", "Rava", "Rinat", "Nurkyz"]))

# a = ["one", "two", "three", "one", "three", "four"]
# b  = []
# c = []
# for i in a:
#   print(i)
#   if i not in b:
#     b.append(i)
#     print(b)
#   else:
#     c.append(i)


# print(b)
# print(c)