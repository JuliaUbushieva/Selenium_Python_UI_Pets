# Selenium UI Testing 🖥️

### Project Overview
This project automates UI testing for a web application using **Selenium** and **Python**. It covers various user interactions across multiple web pages, ensuring that critical functionalities such as form submissions, page navigations, and validations work as intended.

### Project Structure
- **pages/**: Contains files for each page of the web application. Each file includes the page title and methods representing user actions (such as filling out forms, clicking buttons, or verifying elements on the page).
- **tests/**: Contains test files for each page. These files test the logic and interactions defined in the corresponding page files.

### Key Features
- Automated tests for core UI functionality such as:
  - Form submissions.
  - Page navigations.
  - Error handling and validation.
- Modular approach: Reusable methods for actions on each page.
- Integrated test reports using **pytest**.

### Tech Stack
- **Python**
- **Selenium WebDriver**
- **pytest** (for running tests and generating reports)

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JuliaUbushieva/Selenium_UI.git
    cd Selenium_UI
    ```

2. **Install dependencies**:
    Make sure you have Python and pip installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tests**:
    Execute all tests using `pytest`:
    ```bash
    pytest
    ```

4. **Generate a test report**:
    If you want to generate a detailed test report, you can use:
    ```bash
    pytest --html=report.html
    ```

### How It Works
- **pages/**: Each file in the `pages/` folder represents a specific page of the web application. Each page class includes:
  - Methods for interacting with UI elements (e.g., filling out forms, clicking buttons).
  - Helper methods to validate the state of the page.
  
- **tests/**: Each file in the `tests/` folder corresponds to a page and contains test cases to validate the functionality of the page. These tests utilize the methods from the `pages/` files.

### Example Usage

Here’s a simple example of how to run a specific test:
```bash
pytest tests/test_login_page.py
```

This runs the test suite for the login page, ensuring that all functionalities (like successful login or error messages) work correctly.

### Continuous Integration
This project can be integrated with **GitHub Actions** for continuous testing.

### Contributing

If you'd like to contribute:
- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Commit your changes (`git commit -m 'Add feature'`).
- Push to the branch (`git push origin feature-name`).
- Open a pull request.

---

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Future Enhancements
- Adding more complex test cases (e.g., multi-step workflows).
- Integrating the project with a CI/CD pipeline for automated test execution on new commits.

---
