# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of values. Tuples are immutable and list can be changed. Tuples are unordered and lists can be ordered and sorted. Because tuples are immutable, they can be used as keys in dictionaries and lists cannot.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets can only contain any element once, lists can contain duplicates. Sets are unordered and lists are indexed. To find items in a set, you can use a hash table lookup which can approximate constant time, whereas finding an item in a list is linear time because it has to search over each item.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a way to write a one time anonymous function that does not use def or return and instead has the format "lambda parameter(s): return value"

say you had a list of tuples and wanted to sort them by some value. you could use lambda like:

sorted(tuple_list, key=lambda index: index[n])

which would sort them by the nth index term

I use more examples with map and filter in the answer to the following question.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Comprehensions, be they list, dictionary or set, are a way of using concise syntax and shorthand that more closely approximates normal mathematical language to write functions to construct or manipulate these structures.

if you wanted all the even number from perfect squares from 1 to 20, you could write:
perfectsqs = [x**2 for x in range(21)]

if you wished to do this with map, you could instead write:

intlist = [1, 2, 3, 4, 5, 6, 7]
sqs = list(map(lambda x: x**2, intlist))

if you then wanted to make a list of all the even number from the list comprehension example, you could write:

evens = [x for x in perfectsqs if x % 2 == 0]

if you wanted to do that with filter from the map example, you could write:

evennum = list(filter(lambda x: x %2 == 0, perfectsqs))

dictionary comprehensions and set comprehensions are the same concept, applied to those information types.

a common use for a dictionary comprehension would be to take two lists and use one as the key and the other as the value for a new dictionary.

set comprehensions are almost the same as the list comprehensions, although the output will be unordered and contain no duplicate elements

list comprehensions are genereally preferred over map and filter in python, as they are easier to parse and faster. maps are generally faster than manually coded for loops.

map allows you to apply the same function to each element in a list

filter allows you to perform some test function on each element in a list and returns a list of all the values for which it was true

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





