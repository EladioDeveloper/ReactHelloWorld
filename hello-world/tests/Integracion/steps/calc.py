from behave import *
import api

@given("que deseo sumar dos numeros")
def step_implementation(context):
    context.app =  api.app.test_client()
    
@when('yo ingrese los numeros {num1} y {num2}')
def step_implementation(context, num1, num2):
    api_response = context.app.get('/sumar?num1={num1}&num2={num2}')
    print(f"{api_response}")