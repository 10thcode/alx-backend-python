# 0x00. Python - Variable Annotations

Python - Variable annotations

## Tasks
- ***[0-add.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/0-add.py)***

    A type-annotated function that takes a float a and a float b as arguments
    and returns their sum as a float. 

- ***[1-concat.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/1-concat.py)***

    A type-annotated function that takes a string str1 and a string str2 as
    arguments and returns a concatenated string.

- ***[2-floor.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/2-floor.py)***

    A type-annotated function which takes a float n as argument and returns the
    floor of the float.

- ***[3-to_str.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/3-to_str.py)***

    A type-annotated function that takes a float n as argument and returns the
    string representation of the float.

- ***[4-define_variables.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/4-define_variables.py)***

    Defines and annotates the following variables with the specified values:

    - `a`, an integer with a value of 1
    - `pi`, a float with a value of 3.14
    - `i_understand_annotations`, a boolean with a value of True
    - `school`, a string with a value of “Holberton”

- ***[5-sum_list.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/5-sum_list.py)***

    A type-annotated function which takes a list input_list of floats as argument
    and returns their sum as a float.

- ***[6-sum_mixed_list.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/6-sum_mixed_list.py)***

    A type-annotated function which takes a list mxd_lst of integers and floats
    and returns their sum as a float.

- ***[7-to_kv.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/7-to_kv.py)***

    A type-annotated function that takes a string k and an int OR float v as
    arguments and returns a tuple.

- ***[8-make_multiplier.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/8-make_multiplier.py)***

    A type-annotated function that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.

- ***[9-element_length.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/9-element_length.py)***

    Duck-typed annotations for the below function:
    ```
    def element_length(lst):
        return [(i, len(i)) for i in lst]
    ```

- ***[100-safe_first_element.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/100-safe_first_element.py)***

    Duck-typed annotations for the below function:
    ```
    # The types of the elements of the input are not know
    def safe_first_element(lst):
        if lst:
            return lst[0]
        else:
            return None
    ```

- ***[101-safely_get_value.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/101-safely_get_value.py)***

    Duck-typed annotations for the below functions:
    ```
    def safely_get_value(dct, key, default = None):
        if key in dct:
            return dct[key]
        else:
            return default
    ```

- ***[102-type_checking.py](https://github.com/10thcode/alx-backend-python/blob/main/0x00-python_variable_annotations/102-type_checking.py)***

    Validated version of the following piece of code:
    ```
    def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
        zoomed_in: Tuple = [
            item for item in lst
            for i in range(factor)
        ]
        return zoomed_in


    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)
    ```
