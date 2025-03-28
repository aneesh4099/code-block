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

def mainstart():
    parent_names = [
        "Amit Kumar", "Suresh Sharma", "Rajesh Gupta", "Vijay Singh", "Anil Verma", 
        "Ravi Patel", "Manoj Kumar", "Pankaj Joshi", "Sunil Kumar", "Deepak Mehta",
        "Rohit Desai", "Vikram Singh", "Pradeep Agarwal", "Nitin Kumar", "Anil Chauhan",
        "Sandeep Yadav", "Deepak Gupta", "Ajay Tiwari", "Sunil Verma", "Arvind Mehta",
        "Santosh Kumar", "Rajeev Sharma", "Pankaj Yadav", "Vijay Verma", "Manoj Joshi",
        "Tarun Reddy", "Shiv Kumar", "Gopal Singh", "Bharat Patel", "Ramesh Sharma",
        "Mukesh Yadav", "Ravindra Singh", "Arvind Kumar", "Kishore Agarwal", "Hari Prakash",
        "Shivendra Reddy", "Vikas Sharma", "Pradeep Kumar", "Sanjay Gupta", "Ajay Mehra",
        "Dinesh Jain", "Sushil Kumar", "Ramesh Choudhary", "Manoj Verma", "Naveen Patel"
    ]

    student_names = [
        "Aryan Kumar", "Ishaan Sunil", "Riya Gupta", "Simran Singh", "Ananya Patel", 
        "Kavya Verma", "Niharika Joshi", "Sanya Mehta", "Aditi Kapoor", "Siddharth Agarwal",
        "Aarav Sharma", "Madhav Yadav", "Neha Gupta", "Vanshika Mehra", "Rohit Kumar",
        "Tanya Verma", "Pranav Patel", "Krishna Sharma", "Jasmin Reddy", "Kriti Sinha",
        "Reyansh Jain", "Palak Agarwal", "Aditya Singh", "Sanya Yadav", "Shivani Joshi",
        "Ishaan Mehta", "Mishika Verma", "Nikhil Patel", "Ritika Sharma", "Vivaan Reddy",
        "Devansh Kumar", "Ishika Singh", "Rohan Yadav", "Shivansh Verma", "Kiran Patel",
        "Aaradhya Joshi", "Manav Mehta", "Pooja Sharma", "Kunal Reddy", "Manya Gupta",
        "Harshita Verma", "Tanmay Agarwal", "Sanya Patel", "Yashika Kapoor",
        "Radhika Sinha", "Aakash Sharma", "Mitali Joshi", "Raghav Kumar"
    ]

    # List of random responses for questions 5 to 8
    q5_responses = [
        "Regular Parent-Teacher Conferences: The school could organize more frequent and accessible parent-teacher conferences to discuss student progress and ways parents can support learning at home.",
        "Workshops for Parents: The school could offer workshops that educate parents on how to support their children's academic and emotional needs at home, such as study habits or stress management.",
        "Parent-Teacher Communication Platforms: Implementing an online platform where teachers can share updates, assignments, and feedback with parents can improve communication and engagement.",
        "Volunteer Opportunities: Offering parents opportunities to volunteer in classrooms or school events can help them be more involved in their child’s learning and development.",
        "Home Learning Support Resources: The school could provide parents with resources like guides or suggested activities to help students with homework or personal projects, encouraging collaboration.",
        "Parent Involvement in School Events: Organizing more school events that involve parents, such as science fairs, book clubs, or career days, can create a stronger sense of community and partnership.",
        "Parent Advisory Committees: Forming advisory committees where parents can contribute ideas on how to improve the school environment and support student development can enhance collaboration.",
        "Encouraging Open Dialogue: Encouraging more open and consistent communication between teachers and parents about any concerns, achievements, or potential challenges can ensure better support for the students.",
        "Regular Feedback Surveys: Conducting periodic surveys where parents can provide feedback on the school’s performance and offer suggestions for improvement can keep the lines of communication open and create a feedback loop.",
        "Engaging Parents in Decision-Making: Including parents in decision-making processes related to school policies, teaching strategies, and extracurricular activities could give them a sense of ownership in their child’s education."
    ]

    q6_responses = [
        "Upgrading Sports Facilities: The school could invest in modernizing and maintaining sports facilities, such as upgrading gymnasiums, adding new equipment, or improving outdoor sports areas.",
        "Diverse Sports Offerings: Expanding the range of sports offered to cater to a variety of student interests (e.g., introducing less common sports like badminton, tennis, or martial arts) can encourage more participation.",
        "After-School Sports Programs: Offering after-school sports clubs or practices can give students more opportunities to develop their skills and participate without conflicting with academic schedules.",
        "Increased Coaching Staff: Hiring more specialized coaches or offering professional development for current coaches to ensure they provide high-quality instruction and training.",
        "Sports Competitions and Tournaments: Organizing regular school-wide sports competitions or inter-school tournaments can motivate students to participate and strive for excellence.",
        "Sports Scholarships or Incentives: Introducing scholarships or awards for outstanding athletes could provide additional motivation for students to excel in sports.",
        "Physical Education Curriculum Enhancements: Revising the physical education curriculum to include a wider range of activities and skills-based learning can engage more students and prepare them for competitive sports.",
        "Health and Fitness Education: Offering workshops or classes on health, fitness, and nutrition would help students understand the importance of physical activity in their overall well-being, leading to better engagement in sports.",
        "Inclusive Sports Programs: Ensuring that sports programs are inclusive of all skill levels and backgrounds will encourage participation from students who may not be initially confident in their athletic abilities.",
        "Peer Mentorship in Sports: Creating a mentorship system where more experienced athletes guide beginners can boost student confidence, foster team spirit, and enhance skill development."
    ]

    q7_responses = [
        "Personalized Learning Plans: The school could implement individualized learning plans to cater to each student’s strengths, weaknesses, and learning pace, ensuring more focused academic growth.",
        "Project-Based Learning: Incorporating more hands-on, project-based learning in the curriculum could help students apply their knowledge practically and build problem-solving skills.",
        "Increased Access to Extracurricular Activities: Expanding extracurricular offerings, including clubs for arts, technology, and leadership, would provide students with more opportunities to explore and develop their interests.",
        "Skill Development Workshops: Organizing workshops on skills such as time management, public speaking, critical thinking, and teamwork can help students prepare for future academic and professional success.",
        "Mentorship Programs: Creating mentorship opportunities where students can receive guidance from teachers, alumni, or professionals in various fields would provide valuable support in both academics and career exploration.",
        "Career Pathway Exploration: The school could offer programs that expose students to various career options, internships, or job shadowing opportunities to help them understand the practical applications of their studies.",
        "Enrichment Programs: Providing access to enrichment programs such as advanced courses, summer camps, or special projects can further challenge high-achieving students and foster a deeper love for learning.",
        "Collaboration with Parents: Regular parent-school communication to discuss student progress and ways parents can support their child's academic and extracurricular activities can ensure a collaborative approach to development.",
        "Encouraging Social-Emotional Learning (SEL): Integrating SEL programs into the curriculum could help students build resilience, self-awareness, and interpersonal skills, which are essential for success in all areas.",
        "Recognition and Rewards: Implementing a system for recognizing academic achievements, extracurricular involvement, and personal growth can motivate students to strive for excellence and take pride in their contributions."
    ]

    q8_responses = [
        "Advanced Technology Integration: The school could implement cutting-edge technology in classrooms, such as virtual classrooms, augmented reality (AR) learning tools, and AI-driven personalized learning experiences.",
        "Sustainability Initiatives: A focus on sustainable practices, like green buildings, energy-efficient systems, and environmental education, would help foster a sense of responsibility for the planet among students.",
        "Global Learning Opportunities: The school could establish international partnerships, exchange programs, and global learning projects that allow students to experience different cultures and perspectives.",
        "Holistic Education Approach: A shift towards a more balanced curriculum that emphasizes emotional intelligence, social skills, and creative thinking alongside academic subjects could help develop well-rounded individuals.",
        "Inclusive and Diverse Community: The school could prioritize diversity and inclusion initiatives, ensuring that all students, regardless of background, feel represented and valued in both academic and social settings.",
        "Health and Well-Being Focus: Offering more programs dedicated to mental health, wellness, and physical fitness could better support students' overall well-being and success.",
        "Flexible Learning Options: Providing more flexible learning environments, such as hybrid learning models, online courses, and self-paced study options, would allow students to personalize their learning experience.",
        "Stronger Career Development Programs: The school could develop more career-focused initiatives, such as internships, apprenticeships, and job shadowing, to help students explore career paths early.",
        "Innovative Teaching Methods: The adoption of more project-based, inquiry-driven, and interdisciplinary teaching methods could foster a deeper understanding of subjects and critical thinking skills.",
        "Community Engagement and Leadership: Encouraging students to take active roles in community service, leadership projects, and social impact initiatives could help them develop a sense of civic responsibility and leadership."
    ]
    for lop1 in range(100): 
        # Function to generate random answers
        def random_choice(response_list):
            return random.choice(response_list)

        def random_name(name_list):
            return random.choice(name_list)

        # Setup WebDriver
        service = Service(ChromeDriverManager().install())

        # Initialize WebDriver with the Service object
        driver = webdriver.Chrome(service=service)
        # Get the screen width and height
        screen_width = driver.execute_script("return window.screen.availWidth")
        screen_height = driver.execute_script("return window.screen.availHeight")
        window_width = int(screen_width * 0.5)  # 50% of screen width
        window_height = int(screen_height * 0.5)  # 50% of screen height

        # Set the window size to 50% of the screen
        driver.set_window_size(window_width, window_height)

        # Open the Google Form
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdaZX309rEQLFoO-8lwo20Bg11HJ7_C5D2lu27xEe4UhhFNYw/viewform"
        driver.get(form_url)
        time.sleep(0.5)
        driver.maximize_window()

        # Wait for the form to load
        time.sleep(1.5)

        # Fill in NAME OF THE PARENT
        name_of_parent = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')  # Replace with the actual XPath
        name_of_parent.send_keys(random_name(parent_names))

        # Fill in NAME OF THE STUDENT
        name_of_student = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')  # Replace with the actual XPath
        name_of_student.send_keys(random_name(student_names))




        # Wait for the dropdown options to appear and select one
        time.sleep(0.5)

        class_options = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        class_options.click()
        driver.execute_script("arguments[0].scrollIntoView(true);", class_options)
        class_list = [str(i) for i in range(4, 13)]  # List of classes from 4 to 12
        random_class = random.choice(class_list)

        time.sleep(0.5)

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

        time.sleep(0.5)

        sec_options = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        try:
            sec_options.click()
        except:
            driver.quit()
            mainstart()

            break
        
        time.sleep(0.5)
        if (random_class == '6') or (random_class == '7') or (random_class == '8') or (random_class == '9') or (random_class == '10'):
            sec_list = [str(i) for i in range(1, 4)]
            random_sec = random.choice(sec_list)
            if random_sec == '1':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span')
                choice.click()
            elif random_sec == '2':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span')
                choice.click()
            elif random_sec == '3':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[5]/span')
                choice.click()
                
        else:
            sec_list = [str(i) for i in range(1,6)]
            random_sec = random.choice(sec_list)
            if random_sec == '1':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span')
                choice.click()
            elif random_sec == '2':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span')
                choice.click()
            elif random_sec == '3':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[5]/span')
                choice.click()
            elif random_sec == '4':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[6]/span')
                choice.click()
            elif random_sec == '5':
                choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[7]/span')
                choice.click()
            
        
        #choice = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span')
        #choice.click()
        


        time.sleep(0.5)
        # Fill in Question 5 (Random response)
        q5 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
        driver.execute_script("arguments[0].scrollIntoView(true);", q5)
        q5.send_keys(random_choice(q5_responses))
        time.sleep(0.5)
        # Fill in Question 6 (Random response)
        q6 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
        driver.execute_script("arguments[0].scrollIntoView(true);", q6)
        q6.send_keys(random_choice(q6_responses))
        time.sleep(0.5)
        # Fill in Question 7 (Random response)
        q7 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
        driver.execute_script("arguments[0].scrollIntoView(true);", q7)
        q7.send_keys(random_choice(q7_responses))
        time.sleep(0.5)
        # Fill in Question 8 (Random response)
        q8 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea')  # Replace with the actual XPath
        driver.execute_script("arguments[0].scrollIntoView(true);", q8)
        q8.send_keys(random_choice(q8_responses))
        time.sleep(0.5)
        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')  # Replace with the actual XPath
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        time.sleep(0.5)
        # Wait for the form to be submitted and close the browser
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    mainstart()
