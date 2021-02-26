```python
python3 -m doctest foo.py
```

### List comprehension

```python
num_column = 3
num_rows = 2
grid = [[0 for _ in range (num_columns)] for _ in range (num_rows)]

[(lambda x: x % 2 == 1)(num) for num in [1,-5,2]]
>>> [True, True, False]
any([(lambda x: x % 2 == 1)(num) for num in [1,-5,2]])
>>> True
all([(lambda x: x % 2 == 1)(num) for num in [1,-5,2]])
>>> False
```

### Breackpoints

```python
for i in range(10):
  breakpoint() // > Python 3.7
  imoport pdb;pdb.set_trace() // < Python 3.7
  i *= 2
```
  
### f-string

```python
class A(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __repr__(self):
    return f"""
      My name is {self.name}.
      I am {self.age} years old.
    """
```  
    
### Sorting

```python
sorted(animals, key=lambda animal: animal['age'], reversed=True)
animal.sort(key=lambda animal: animal['age'])
```  

### Set

```python
return (len(set(s))) // Count number of unique character in a string s
Or return (len({c for c in s}))

```


sql alchemy and postgres

 #for JSONB type
  objects = objects.filter(objectModel.attribute.has_key('field'))
objects1 = objects.filter(not_(text("objects.attribute::jsonb ? 'field'")))

  objects2 = objects.filter(not_(objectModel.attribute['field'].as_string().contains("word")))
  objects_result = objects1.union_all(objects2)


  objects = objects.filter(not_(objectModel.attribute['field'].astext.cast(String).contains("word")))
  objects = objects.filter(not_(objectModel.attribute['field'].as_string().contains("word")))
