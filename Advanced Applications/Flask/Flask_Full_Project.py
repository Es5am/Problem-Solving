from flask import Flask,render_template

skills_app = Flask(__name__)

skills = [("Html",20),("Css",80),("Python",50),("Java",95),("C++",15)]

@skills_app.route("/")
def homepage():
    return render_template("homepage.html",pagetitle="H", cssfile = 'home')

@skills_app.route("/about")
def aboutpage():
    return render_template("about.html",pagetitle="A")

@skills_app.route("/add")
def addpage():
    return render_template("add.html",pagetitle="ADD", cssfile = 'add')

@skills_app.route("/skills")
def skillspage():
    return render_template("skills.html",
                            pagetitle="skills",
                            cssfile = 'skills',
                            head_title = "My Skills", 
                            description = "This Is My Skills Page : ", 
                            myskill= skills  )


if __name__ == "__main__":
    skills_app.run(debug=True,port=8000)
