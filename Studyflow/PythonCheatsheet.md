

# 🐍 PYTHON CHEATSHEET – Strings, Lists, Sets, Dictionaries



## 🔤 1. **STRINGS** (Immutable)

### ✅ Basics

```python
s = "hello world"
print(s[0])       # h
print(s[-1])      # d
print(len(s))     # 11
```

### ✅ Slicing

```python
print(s[0:5])     # hello
print(s[6:])      # world
print(s[::-1])    # dlrow olleh (reversed)
```

### ✅ Useful Methods

```python
s = "  Python DS queen  "
print(s.strip())         # remove whitespace
print(s.upper())         # PYTHON DS QUEEN
print(s.lower())         # python ds queen
print(s.replace("DS", "ML"))  # Python ML queen
print(s.split())         # ['Python', 'DS', 'queen']
```

### ✅ Check Substring

```python
"queen" in s         # True
s.startswith("Py")   # True
s.endswith("en")     # True
```

### ✅ Loop Over String

```python
for ch in "hello":
    print(ch)
```

### ✅ Format Strings

```python
name = "Nidhi"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

---

## 📃 2. **LISTS** (Mutable, Ordered)

### ✅ Creating Lists

```python
nums = [1, 2, 3, 4]
mixed = [1, "hello", True]
empty = []
```

### ✅ Access + Slicing

```python
print(nums[0])       # 1
print(nums[-1])      # 4
print(nums[1:3])     # [2, 3]
```

### ✅ Modifying

```python
nums[0] = 100
nums.append(5)
nums.insert(1, 200)     # insert at index
nums.pop()              # removes last item
nums.remove(200)        # remove by value
```

### ✅ List Functions

```python
print(len(nums))      
print(min(nums))      
print(max(nums))      
print(sum(nums))      
```

### ✅ Sorting

```python
nums.sort()            # ascending
nums.sort(reverse=True) # descending
```

### ✅ Looping

```python
for x in nums:
    print(x)

for i in range(len(nums)):
    print(i, nums[i])
```

### ✅ List Comprehension

```python
squares = [x*x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 🔁 3. **SETS** (Unordered, No Duplicates)

### ✅ Creating Sets

```python
s = {1, 2, 3}
s = set([1, 2, 2, 3, 4])
print(s)  # {1, 2, 3, 4}
```

### ✅ Adding / Removing

```python
s.add(5)
s.remove(2)      # error if not found
s.discard(100)   # safe remove (no error)
```

### ✅ Useful Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)     # union {1, 2, 3, 4, 5}
print(a & b)     # intersection {3}
print(a - b)     # difference {1, 2}
print(a ^ b)     # symmetric difference {1, 2, 4, 5}
```

### ✅ Check Membership

```python
if 3 in s:
    print("Yes")
```

### ✅ Loop Over Set

```python
for item in s:
    print(item)
```

---

## 🔑 4. **DICTIONARIES** (Key-Value Pairs)

### ✅ Create Dictionary

```python
student = {
    "name": "Nidhi",
    "age": 21,
    "branch": "CSE"
}
```

### ✅ Access & Modify

```python
print(student["name"])
student["age"] = 22
student["cgpa"] = 9.2  # adds new key
```

### ✅ Safe Access

```python
print(student.get("age"))        # 22
print(student.get("gender", "N/A"))  # N/A
```

### ✅ Looping Over Dictionary

```python
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)
```

### ✅ Dictionary Functions

```python
print(student.keys())      # dict_keys(['name', 'age', 'branch', 'cgpa'])
print(student.values())    # dict_values([...])
print(student.items())     # all key-value pairs
```

### ✅ Remove Key

```python
del student["cgpa"]
```

---

## 📚 Summary: Use Cases in DSA

| Type       | Use Case                                    |
| ---------- | ------------------------------------------- |
| **String** | Substring problems, sliding window          |
| **List**   | Arrays, subarrays, sorting, two pointers    |
| **Set**    | Duplicates, unions, unique elements         |
| **Dict**   | Frequency map, hashing, lookup optimization |

---

## ✅ Python Practice Ideas

* ✅ Check if two strings are anagrams (Dict or sort)
* ✅ Remove duplicates from a list (Set)
* ✅ Find most frequent word in a string (Dict)
* ✅ Reverse a string (Slice or loop)
* ✅ Check if string is palindrome (Two pointer + string)

---

## 🧠 Python Interview Insight

💬 “What’s the difference between list and set?”
→ List is ordered and allows duplicates. Set is unordered and does not allow duplicates.

💬 “Why use a dictionary?”
→ For fast lookup, storing key-value pairs, and frequency counting (O(1) access time).

💬 “Are strings mutable?”
→ No. Strings in Python are immutable. You must create a new one to change it.

---

## 🌟 Now You’re Ready

You can now:
✅ Solve most Leetcode easy/mediums
✅ Use Python for ML + projects
✅ Explain code in interviews
✅ Add this to your GitHub as a reference README

