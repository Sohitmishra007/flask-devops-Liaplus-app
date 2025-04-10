# flask-devops-Liaplus-app


# Flask DevOps Web App 🚀

This is a simple Flask-based web application deployed on **Azure App Service** using **GitHub Actions CI/CD**. This project is created as part of the **LiaPlus DevOps Assignment**.

## 🌟 Project Purpose

The main objective of this project is to demonstrate DevOps practices such as:

- Version control with Git & GitHub
- Infrastructure deployment using Azure
- Continuous Integration & Continuous Deployment using GitHub Actions
- Packaging Python applications with dependencies
- Running a Flask app in a cloud environment

## ⚙️ Tech Stack Used

- **Flask** – lightweight Python web framework
- **Gunicorn** – production WSGI server for Python apps
- **Azure App Service** – cloud hosting platform
- **GitHub Actions** – CI/CD automation
- **Linux (Ubuntu-based)** – for App Service environment

## 🔗 Live App URL

👉 [Click here to open the live Flask app](https://sohit-devops-app-ddeeghheagckbvda.centralus-01.azurewebsites.net)

## 🧪 How it Works

- Code pushed to `main` branch triggers GitHub Actions
- Workflow builds the app and deploys to Azure automatically
- The app runs using `gunicorn` as defined in `Procfile`


