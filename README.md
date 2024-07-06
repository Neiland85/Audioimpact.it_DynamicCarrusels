# Project Structure
plaintext
Copiar código
audiimpact.it/
├── .github/
│   └── workflows/
│       └── cleanup.yml
├── venv/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── emails/
│   ├── carousels/
│   └── sliders/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── config.py
└── manage.py

## Directory Explanation:
.github/workflows: Contains GitHub Actions workflows for CI/CD.
venv: Virtual environment directory (not included in version control).
static: Holds static files like CSS, JavaScript, and images.
templates: Contains HTML templates for different components like emails, carousels, and sliders.
.gitignore: Lists files and directories to be ignored by Git.
README.md: Project documentation.
requirements.txt: Lists project dependencies.
app.py: Main application file.
config.py: Configuration file for the project.
manage.py: Script for managing the project (migrations, server start, etc.).

### Repository Functions
1. Dynamic Carousels on the Homepage
Technologies: HTML5, CSS3, JavaScript, jQuery, Smarty Templates, AJAX
Description: Implements dynamic carousels to showcase featured products and promotions.
2. Dynamic Sliders on the Homepage
Technologies: HTML5, CSS3, JavaScript, jQuery, Smarty Templates
Description: Implements dynamic sliders to highlight specific offers and new products.
3. Customized Emails
Technologies: PHP, SwiftMailer, Twig Templates, PrestaShop Hooks
Description: Sends personalized emails based on user actions such as purchases and abandoned carts.
4. GDPR Compliance
Technologies: PHP, JavaScript, PrestaShop Modules, SSL/TLS
Description: Ensures user data privacy and security, including cookie consent and data management.
5. CI/CD with GitHub Actions
Technologies: GitHub Actions, YAML
Description: Automates testing, building, and deployment processes.
