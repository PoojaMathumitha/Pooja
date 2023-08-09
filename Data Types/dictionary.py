mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
print(mine_dictionary)

mini_values ={
    (1,2): 20,
    (22,24): [10,2],
}
print(mini_values)


country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}
print(country_capitals["Italy"])

minimum_values ={}
print(minimum_values)


mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
print(len(mine_dictionary))

mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
print(mine_dictionary["pooja"])
print(mine_dictionary["jupi"])


mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
print(mine_dictionary.get("pooja"))

mine_dictionary ={
    "pooja": 19,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
mine_dictionary["pooja"]=20
print(mine_dictionary)

mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
mine_dictionary["python"]="intern"
print(mine_dictionary)

mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
mine_dictionary.clear()
print(mine_dictionary)

#change element in dictionary
mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
mine_dictionary["numbers"]="even"
print(mine_dictionary)

#add element in dictionary
mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
mine_dictionary["even"]="odd"
print(mine_dictionary)

#delete the element
mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numbers": "infinity",
}
del mine_dictionary["numbers"]
print(mine_dictionary)

#remove the element
mine_dictionary ={
    "numbers": "infinity",
    "python": "intern",
    "laptop": "jio",
}
mine_dictionary.pop("python")
print(mine_dictionary)

#update the dictionary
values={
    "odd": 23,
    "even": 20,
}
sample={
    "total": 43,
}
values.update(sample)
print(values)

#return keys and values
mine_dictionary ={
    "numbers": "infinity",
    "python": "intern",
    "laptop": "jio",
}
dictionarykeys=mine_dictionary.keys()
print(dictionarykeys)

mine_dictionary ={
    "numbers": "infinity",
    "python": "intern",
    "laptop": "jio",
}
dictionaryvalues=mine_dictionary.values()
print(dictionaryvalues)

#get function
scores = {
    'Physics': 67,
    'Maths': 87,
    'History': 75
}
result = scores.get('Physics')
print(result)

#popitem
mine_dictionary ={
    "numbers": "infinity",
    "python": "intern",
    "laptop": "jio",
}
result =mine_dictionary.popitem()
print("return values=" ,result)
print(mine_dictionary)

#copy the element
original_scores = {
    'Physics': 67,
    'Maths': 87,
    'History': 75
}
copied_scores = original_scores.copy()
print("original= " ,original_scores)
print("copied= " ,copied_scores)
