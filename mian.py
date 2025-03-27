from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


parent_names = [
    "Amit Kumar", "Suresh Sharma", "Rajesh Gupta", "Vijay Singh", "Anil Verma", 
    "Ravi Patel", "Manoj Kumar", "Pankaj Joshi", "Sunil Kumar", "Deepak Mehta"
]

student_names = [
    "Aryan Kumar", "Ishaan Sunil", "Riya Gupta", "Simran Singh", "Ananya Patel", 
    "Kavya Verma", "Niharika Joshi", "Sanya Mehta", "Aditi Kapoor", "Siddharth Agarwal"
]

# List of random responses for questions 5 to 8
q5_responses = [
    "The school can enhance collaboration by organizing regular parent-teacher meetings.",
    "Collaborative workshops between parents and teachers will help in student development.",
    "Providing platforms for parents to participate in school events will strengthen the bond."
]

q6_responses = [
    "Improvement in sports infrastructure and regular practice sessions will boost student participation.",
    "The school should offer more diverse sports options and promote a competitive spirit.",
    "Increased focus on fitness and nutrition alongside sports training will help students achieve more."
]

q7_responses = [
    "The school should offer more specialized academic guidance, skill-building workshops, and extracurricular activities.",
    "Better integration of real-world skills in the curriculum will help students thrive.",
    "Focusing on developing critical thinking skills and problem-solving abilities will support student growth."
]

q8_responses = [
    "By 2030, I hope the school will have state-of-the-art infrastructure and modern teaching methods.",
    "The school should focus on sustainability, making it an eco-friendly and technology-driven institution.",
    "Increased emphasis on mental health and overall well-being for students would be a welcome change."
]
for lop1 in range(20): 
    # Function to generate random answers
    def random_choice(response_list):
        return random.choice(response_list)

    def random_name(name_list):
        return random.choice(name_list)

    # Setup WebDriver
    service = Service(ChromeDriverManager().install())

    # Initialize WebDriver with the Service object
    driver = webdriver.Chrome(service=service)

    # Open the Google Form
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdaZX309rEQLFoO-8lwo20Bg11HJ7_C5D2lu27xEe4UhhFNYw/viewform"
    driver.get(form_url)
    time.sleep(0.5)
    driver.maximize_window()

    # Wait for the form to load
    time.sleep(2)

    # Fill in NAME OF THE PARENT
    name_of_parent = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')  # Replace with the actual XPath
    name_of_parent.send_keys(random_name(parent_names))

    # Fill in NAME OF THE STUDENT
    name_of_student = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')  # Replace with the actual XPath
    name_of_student.send_keys(random_name(student_names))




    # Wait for the dropdown options to appear and select one
    time.sleep(1)

    class_options = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    class_options.click()
    driver.execute_script("arguments[0].scrollIntoView(true);", class_options)
    class_list = [str(i) for i in range(4, 13)]  # List of classes from 4 to 12
    random_class = random.choice(class_list)

    time.sleep(1)

    if random_class == '6':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[9]/span')
        choice.click()
    elif random_class == '7':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[10]/span')
        choice.click()
    elif random_class == '8':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[11]/span')
        choice.click()
    elif random_class == '9':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[12]/span')
        choice.click()
    elif random_class == '10':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[13]/span')
        choice.click()
    elif random_class == '11':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[14]/span')
        choice.click()
    elif random_class == '12':
        choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[15]/span')
        choice.click()

    time.sleep(1)

    sec_options = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", sec_options)
    sec_options.click()
    time.sleep(1)
    choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span')
    choice.click()
        
    time.sleep(1)
    # Fill in Question 5 (Random response)
    q5 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
    driver.execute_script("arguments[0].scrollIntoView(true);", q5)
    q5.send_keys(random_choice(q5_responses))
    time.sleep(1)
    # Fill in Question 6 (Random response)
    q6 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
    driver.execute_script("arguments[0].scrollIntoView(true);", q6)
    q6.send_keys(random_choice(q6_responses))
    time.sleep(1)
    # Fill in Question 7 (Random response)
    q7 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
    driver.execute_script("arguments[0].scrollIntoView(true);", q7)
    q7.send_keys(random_choice(q7_responses))
    time.sleep(1)
    # Fill in Question 8 (Random response)
    q8 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
    driver.execute_script("arguments[0].scrollIntoView(true);", q8)
    q8.send_keys(random_choice(q8_responses))
    time.sleep(1)
    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')  # Replace with the actual XPath
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    time.sleep(1)
    # Wait for the form to be submitted and close the browser
    time.sleep(2)
    driver.quit()
