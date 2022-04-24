# Values Calc
Script to calculate market and auction values using info from an API
### setting a virtual enviroment
1.- Make a tmp directory

`mkdir tmp`

2.- Make a python venv in the tmp directory

`python -m venv venv tmp`

3.- Activate the virtual enviroment

`./tmp/venv/bin/activate`

4.- Install the dependencies needed

`pip install -r requirements.txt`

### Running the script

For using the script, you need to pass at least two arguments
Those being the model and year, in that order
In this case it is important to run the script where the
`api-response.json` file is

`python -m py.function.values_calc 67352 2010`

A third argument can be sent specifying the API url to get the data from

`python -m py.function.values_calc 67352 2010 https://6265cacadbee37aff9a8c10b.mockapi.io/api/ratios/ratios`

### Errors can be shown if

- The script is wrongly used (not enough params)
- No API communication can be established
- A future year is used as a param
- Given model or year do not exist in the data given by the API

### Running the unittests

The ValueCalculator class is tested within the unittests.
To run them type

` python -m unittest py.function.test.value_calculator.ValueCalculatorTest`
