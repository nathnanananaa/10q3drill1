from pyscript import document, display
from js import console


def Login(e):   
    password = document.getElementById("password_input").value
    email = document.getElementById("email_input").value


    if email == "nathan@email.com" and password == "nathanspassword1234":
            result = "login success"
    else:
            result = "failure"

    document.getElementById("result1").innerText = result