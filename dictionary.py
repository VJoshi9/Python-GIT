# Dictionary--> used to store data values in key:value pairs.

myDictionary = {
            "name":"Vinay",
            "age":"18",
            "age":"19"

}
age = myDictionary.get("age")
print(age)
# ordered
# changable
# does not allow duplicate values

dict1 = {"one":1, "two":2, "three":3}
dict2 = {"four":4, "five":5, "six":6}
# Merge two dictionaries is one
dict1.update(dict2)
print(dict1)
dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
mydict = dict1.get("class").get("student").get("marks").get("web")
print(mydict)




