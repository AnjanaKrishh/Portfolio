from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
class About(View):
    def get(self,request):
        data = {
            "ID":101,
            "Name":"Anjana",
            "Tittle":"Python Fullstack Developer",
            "Bio":"Python FullStack Developer with Hands on Experience in Real world Projects.",
            "Email":"anjanakrishh@gmail.com",
            "contact":9087654321,
            "DOB":"03-03-2004",
            "Github":"https://github.com/AnjanaKrishh",
            "Linkedin":"https://www.linkedin.com/in/anjanakrishna-p-s-121b84257/",
            
        }
        return JsonResponse(data)
class EducationView(View):
    def get(self,request):
        edu = {
            "ID":101,
            "Institution":"AISET",
            "Degree":"B.Tech",
            "University":"APJAKTU",
            "Location":"Thrissur",
            "Start Year":2022,
            "End Year":2026,
            "CGPA":8.5,
            "Description":"Graduated with B.Tech in Mechanical Engg from AISET in 2026 with a CGPA Of 8.5"
            
        }
        return JsonResponse(edu)
class ProjectView(View):
    def get(self,request):
        project = [
        {
            "ID":101,
            "Title":"FoodMart",
            "Short_Description":"Web application used to buy groceries ",
            "Long_Description":"Developed using python Django and Dtabase as mysql",
            "Technologies_Used":"Python, Django, MySQL",
            "Live_URL":"https://foodmart.com",
            "Github_URL":"https://github.com/AnjanaKrishh/FoodMart",
            "Image_URL":"https://foodmart.com/image.png",
            "Featured":True
        },       
        {
            "ID":102,
            "Title":"Panash Website",
            "Short_Description":"Website for Panash Online Clothing Store",
            "Long_Description":"Developed using python Django and Database as PostgreSQL",
            "Technologies_Used":"Python, Django,SQL",
            "Live_URL":"https://panash.com",
            "Github_URL":"https://github.com/AnjanaKrishh/Panash",
            "Image_URL":"https://panash.com/image.png",
            "Featured":False
        },
        {
            "ID":103,
            "Title":"E-Commerce Platform",
            "Short_Description":"E-Commerce Platform for Online Shopping",
            "Long_Description":"Developed using python Django and Database as MySQL",
            "Technologies_Used":"Python, Django, MySQL",
            "Live_URL":"https://ecommerce.com",
            "Github_URL":"https://github.com/AnjanaKrishh/E-Commerce",
            "Image_URL":"https://ecommerce.com/image.png",
            "Featured":True
        }]
        return JsonResponse(project, safe=False)
class SkillsView(View):
    def get(self,request):
        skills = [
        {
            "ID":101,
            "Skill_Name":"Python",
            "Category":"Programming Language",
            "Proficiency":"Intermediate",
            "Years_of_Experience":1
               
        },
        {
            "ID":102,
            "Skill_Name":"Django",
            "Category":"Web Framework",
            "Proficiency":"Intermediate",
            "Years_of_Experience":1
        },
        {
            "ID":103,
            "Skill_Name":"MySQL",
            "Category":"Database",
            "Proficiency":"Intermediate",
            "Years_of_Experience":1
        }]
        return JsonResponse(skills, safe=False)
class ExperienceView(View):
    def get(self,request):
        experience = [
        {
            "ID":101,
            "Job Tittle":"FullStack Developer Intern",
            "Company_Name":"Tech Solutions",
            "Location":"Bangalore, India",
            "Employement_Type":"Remote",
            "Start_Date":"2024-06-01",
            "End_Date":"2025-08-31",
            "Currently_Working":False,
            "Description":"Worked on developing web applications using Python Django and MySQL."
        },
        {
            "ID":102,
            "Job Tittle":"Software Engineer Intern",
            "Company_Name":"Innovatetech",
            "Location":"Hyderabad, India",
            "Employement_Type":"Onsite",
            "Role":"Backend Developer Intern",
            "Start_Date":"2025-10-15",
            "End_Date":"2026-04-15",
            "Description":"Contributed to building RESTful APIs and optimizing database queries."
        }]
        return JsonResponse(experience, safe=False)
class CertificateView(View):
    def get(self,request):
        certificate = [
        {
            "ID":101,
            "Certificate_Name":"Python Programming",
            "Issuing_Organization":"Coursera",
            "Issued_Year":"2024",
        },
        {
            "ID":102,
            "Certificate_Name":"Django Web Development",
            "Issuing_Organization":"Udemy",
            "Issued_Year":"2025",
        }]
        return JsonResponse(certificate, safe=False)
class SevicesView(View):
    def get(self,request):
        services = [
        {

            "Service_Name":"Web Development",
            "Description":"Building responsive and dynamic web applications using modern technologies.",
            "Technologies":"Python, Django, HTML, CSS, JavaScript"
        },
        {
            "ID":102,
            "Service_Name":"API Development",
            "Description":"Designing and implementing RESTful APIs for seamless integration with frontend applications.",
            "Technologies":"Python, Django REST Framework"
        }]
        return JsonResponse(services, safe=False)
# Create your views here.
