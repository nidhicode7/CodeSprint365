--->What is Big O Notation?

Big O notation is a way to describe how efficient an algorithm is, especially as the size of the input grows. It helps answer questions like:
How fast does an algorithm run?
How much memory does it use?
It gives us a "big picture" of the algorithm's performance by focusing on the worst-case scenario.

--->For example:

If an algorithm takes 10 seconds to run on 1,000 inputs, will it take 100 seconds on 10,000 inputs? Big O helps predict that.
Common Big O Notations

Here are some of the most common types of Big O complexities:

**O(1)**: Constant Time
The algorithm takes the same amount of time regardless of input size.
Example: Checking if a number is even or odd.

**O(log n)**: Logarithmic Time
The algorithm gets faster as the input size increases. Each step reduces the problem size significantly.
Example: Binary Search.

**O(n)**: Linear Time
The time taken grows linearly with the input size.
Example: Searching for an item in an unsorted list.

**O(n log n)**: Log-Linear Time
A very common complexity in sorting algorithms like Merge Sort.
It's more efficient than O(n²) for larger inputs.

**O(n²)**: Quadratic Time
The algorithm's time grows exponentially with the input size. It often involves nested loops.
Example: Comparing every pair in a list.
