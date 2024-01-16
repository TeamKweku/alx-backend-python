# 0x00. Python - Variable Annotations
>

## Contents

0. [Basic Annotations - Add](0-add.py)
    - Type-annotated function `add` that takes two float arguments and returns their sum as a float.

    ```python
    #!/usr/bin/env python3
    
    add = __import__('0-add').add
    
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
    ```

1. [Basic Annotations - Concat](1-concat.py)
    - Type-annotated function `concat` that takes two string arguments and returns their concatenated string.

    ```python
    #!/usr/bin/env python3
    
    concat = __import__('1-concat').concat
    
    str1 = "egg"
    str2 = "shell"
    
    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
    ```

2. [Basic Annotations - Floor](2-floor.py)
    - Type-annotated function `floor` that takes a float argument and returns the floor of the float.

    ```python
    #!/usr/bin/env python3
    
    import math
    
    floor = __import__('2-floor').floor
    
    ans = floor(3.14)
    
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
    ```

3. [Basic Annotations - To String](3-to_str.py)
    - Type-annotated function `to_str` that takes a float argument and returns the string representation of the float.

    ```python
    #!/usr/bin/env python3
    
    to_str = __import__('3-to_str').to_str
    
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
    ```

4. [Define Variables](4-define_variables.py)
    - Variables with specified values and annotations: `a`, `pi`, `i_understand_annotations`, and `school`.

    ```python
    #!/usr/bin/env python3
    
    a = __import__('4-define_variables').a
    pi = __import__('4-define_variables').pi
    i_understand_annotations = __import__('4-define_variables').i_understand_annotations
    school = __import__('4-define_variables').school
    
    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))
    ```

5. [Complex Types - List of Floats](5-sum_list.py)
    - Type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

    ```python
    #!/usr/bin/env python3
    
    sum_list = __import__('5-sum_list').sum_list
    
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
    ```

6. [Complex Types - Mixed List](6-sum_mixed_list.py)
    - Type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

    ```python
    #!/usr/bin/env python3
    
    sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list
    
    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.
    ```
