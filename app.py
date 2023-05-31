from flask import Flask, request, Response, make_response
import re

app = Flask(__name__)

@app.route("/roman", methods = ['GET', 'POST'])
def toRoman():
    queryParameters = request.args

    if 'num' not in queryParameters:
        return Response(
            status=400, 
            response="No parameters passed"
            )
    
    num = queryParameters['num']

    try:
        num = int(num)
    except:
        return Response(
            status=401, 
            response="Please pass an integer as the parameter 'num'"
            )

    RomanNumerals = {
        1000: 'M', 
        900: 'CM', 
        500: 'D', 
        400: 'CD', 
        100: 'C', 
        90: 'XC', 
        50: 'L', 
        40: 'XL', 
        10: 'X', 
        9: 'IX', 
        5: 'V', 
        4: 'IV', 
        1: 'I'
    } 
    roman_num = ""
    for i in RomanNumerals:
        roman_num += (num//i) * RomanNumerals[i]
        num %= i

    return Response(
        status=200, 
        response=roman_num
        )

@app.route("/convert", methods = ['GET', 'POST'])
def toNum():
    queryParameters = request.args

    if 'num' not in queryParameters:
        return Response(
            status=400, 
            response="No parameters passed"
            )
    
    try:
        string = str(queryParameters['num'])
    except:
        return Response(
            status=401, 
            response="Please pass an string as the parameter 'num'"
            )
    
    if not re.search("^[MDCLXVI]+$", string):
        return Response(
            status=401, 
            response="Please pass a Roman Integer as the parameter 'num'"
            )
    
    RomanNumerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    string = string.replace("IV", "IIII").replace("IX", "VIIII")
    string = string.replace("XL", "XXXX").replace("XC", "LXXXX")
    string = string.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in string:
        number += RomanNumerals[char]
    
    return Response(
        status=200, 
        response=f"{number}"
        )

def toNum(str):
    RomanNumerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    str = str.replace("IV", "IIII").replace("IX", "VIIII")
    str = str.replace("XL", "XXXX").replace("XC", "LXXXX")
    str = str.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in str:
        number += RomanNumerals[char]
    return number

def toRoman(num):
    RomanNumerals = {
        1000: 'M', 
        900: 'CM', 
        500: 'D', 
        400: 'CD', 
        100: 'C', 
        90: 'XC', 
        50: 'L', 
        40: 'XL', 
        10: 'X', 
        9: 'IX', 
        5: 'V', 
        4: 'IV', 
        1: 'I'
    } 
    roman_num = ""
    for i in RomanNumerals:
        roman_num += (num//i) * RomanNumerals[i]
        num %= i
    return roman_num

@app.route("/product", methods = ['GET', 'POST'])
def Product():
    queryParameters = request.args

    params = ['x', 'y']
    for i in range(2):
        if params[i] not in queryParameters:
            return Response(
                status=400, 
                response=f"{params[i]} not passed in as a parameter"
                )
        
        try:
            params[i] = str(queryParameters[params[i]])
        except:
            return Response(
                status=401, 
                response=f"Please pass an string as the parameter '{params[i]}'"
                )
        
        if not re.search("^[MDCLXVI]+$", params[i]):
            return Response(
                status=401, 
                response=f"Please pass a Roman Integer as the parameter '{params[i]}'"
                )
        
    roman = queryParameters['roman'] if 'roman' in queryParameters else 'True'
    x_int = toNum(params[0])
    y_int = toNum(params[1])
    result = x_int * y_int
    result = toRoman(result) if roman.upper().replace(" ", "") == 'TRUE' else result
    return Response(
        status=200, 
        response=f"{result}"
        )

@app.route("/sum", methods = ['GET', 'POST'])
def Sum():
    queryParameters = request.args

    params = ['x', 'y']
    for i in range(2):
        if params[i] not in queryParameters:
            return Response(
                status=400, 
                response=f"{params[i]} not passed in as a parameter"
                )
        
        try:
            params[i] = str(queryParameters[params[i]])
        except:
            return Response(
                status=401, 
                response=f"Please pass an string as the parameter '{params[i]}'"
                )
        
        if not re.search("^[MDCLXVI]+$", params[i]):
            return Response(
                status=401, 
                response=f"Please pass a Roman Integer as the parameter '{params[i]}'"
                )
    
    roman = queryParameters['roman'] if 'roman' in queryParameters else 'True'
    x_int = toNum(params[0])
    y_int = toNum(params[1])
    result = x_int + y_int
    result = toRoman(result) if roman.upper().replace(" ", "") == 'TRUE' else result
    return Response(
        status=200, 
        response=f"{result}"
        )

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)