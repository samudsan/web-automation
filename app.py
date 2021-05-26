# importing required libraries
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from flask import Flask,render_template, url_for, request
import csv
import os


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/registration", methods=["POST", "GET"])
def registration():

    if request.method == 'POST':
        
        # defining url paths
        driver_path = "/home/sandeep/Desktop/herokuEnv/chromedriver"
        url_path = "file:///home/sandeep/Desktop/herokuEnv/templates/registration.html"


        # initializing webdriver and calling url
        driver = webdriver.Chrome(driver_path)
        driver.get(url_path)

        # fetching data from file        
        with open ("data.csv") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  
                for row in csv_reader:
                

                        # for choosing dropdown.
                        dept_name = { 'Department of Engineering':0,
                        'Department of Agriculture':1, 
                        'Accounting Office':2,
                        'MPDC':3, 
                        'MCTC':4 }

                        # for storing results
                        status = []
                        # first_name = "Rohan"
                        # last_name = "vemala"
                        # dept_name = {"Department of Agriculture":2}
                        # username = "vrohon"
                        # password = "vrohan"
                        # confirm_Passw = "vrohan"
                        # email = "vrohan@gmail.com"
                        # contact_no = "9050239234" 

                        # accessing firstname
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[1]/div/div/input")
                        first_name_element.send_keys(row[0])

                        # accessing lastname
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[2]/div/div/input")
                        first_name_element.send_keys(row[1])


                        # accessing department
                        department_element = Select(driver.find_element_by_xpath("/html/body/div/form/fieldset/div[3]/div/div/select"))
                        department_element.select_by_index(dept_name[row[2]])

                        # accessing username
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[4]/div/div/input")
                        first_name_element.send_keys(row[3])

                        # accessing password
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[5]/div/div/input")
                        first_name_element.send_keys(row[4])

                        # accessing confirm password
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[6]/div/div/input")
                        first_name_element.send_keys(row[5])

                        # accessing email
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[7]/div/div/input")
                        first_name_element.send_keys(row[6])

                        # accessing contact number
                        first_name_element = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[8]/div/div/input")
                        first_name_element.send_keys(row[7])

                        # clicking submit button
                        button = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[9]/div/button")
                        button.click()
        return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)
