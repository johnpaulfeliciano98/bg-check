# ICU Insulin Infusion Calculator

A lightweight [Flask](https://flask.palletsprojects.com/) application that automates insulin drip rate adjustments for ICU patients, based on a paper reference table used at Riverside University Health System (RUHS). The app streamlines complex BG (blood glucose) tracking and rate-change decisions for nurses, reducing potential errors and saving time.

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Installation & Setup](#installation--setup)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Screenshots](#screenshots)  
7. [Future Enhancements](#future-enhancements)  
8. [Acknowledgments](#acknowledgments)  
9. [License](#license)

---

## Overview
My sister, an ICU nurse at RUHS, needed a faster and more consistent way to determine insulin drip adjustments for patients with different blood sugar levels. Instead of manually referring to (and interpreting) a paper-based table, this app calculates and displays recommended rate changes in real time.

**Live Demo:**  
Hosted on [PythonAnywhere](https://johnpaulfeliciano98.pythonanywhere.com/).

---

## Features
- **Automated Calculations:** Enter current/previous BG values and the current infusion rate, and the app instantly returns the recommended action.
- **Clear, Nurse-Friendly Output:** Plain-language recommendations (e.g., hold infusion, bolus, or change rate by X).
- **Branching Logic:** Covers multiple thresholds and edge cases from the original paper guide.
- **Lightweight Flask Design:** Easy to deploy locally or on a small server (like PythonAnywhere or Heroku).
- **Adaptable:** The table-driven logic can be updated to match changing hospital policies.

---

## Installation & Setup

1. **Clone or Download**  
   
    ```
    git clone https://github.com/your_username/icu-insulin-calculator.git
    cd icu-insulin-calculator
    ```

2. **Create a Virtual Environment (Recommended)**  
   
    ```
    python3 -m venv venv
    source venv/bin/activate   # macOS/Linux
    # or on Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**  
   
    ```
    pip install -r requirements.txt
    ```

4. **Run the App**  
   
    ```
    python app.py
    ```
   By default, Flask runs on port `5000`. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Usage

1. **Navigate to the App** in your browser (e.g., `http://127.0.0.1:5000`).
2. **Enter the Following:**
   - *Current BG* (mg/dL)
   - *Previous BG* (mg/dL)
   - *Current Infusion Rate* (units/hour)
3. **Click Submit** and the app returns:
   - An overview of the entered values.
   - A text recommendation on whether to hold, decrease, or increase the rate.

---

## Project Structure

```
icu-insulin-calculator/
│
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # HTML form and result template
├── static/              # (Optional) CSS or JS files
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

- **`app.py`**: Houses all logic for interpreting BG changes, referencing the “Table A” and “Table B” thresholds, and returning results to `index.html`.
- **`templates/index.html`**: Minimal Jinja2 template for the user interface.

---

## Screenshots

### 1. Input Form
![Input Form](./images/bg-check-input.png)

**Description:** The user inputs current/previous BG and current infusion rate, then clicks “Submit.”

### 2. Output/Recommendation
![Output Recommendation](./images/bg-check-result.png)

**Description:** The app returns a clear, text-based recommendation based on the logic from the original table.

---

## Future Enhancements
- **Automated EHR Integration:** Fetch BG levels directly from patient records, reducing manual data entry.
- **Logging & Analytics:** Store BG trends and recommended changes to see how patient glucose stabilizes over time.
- **Scalability:** Convert the rule sets into a more dynamic structure (e.g., a config file) for quick policy updates.
- **Multiple Dosing Protocols:** Extend beyond insulin to handle other drip adjustments (e.g., sedation, vasopressors).

---

## Acknowledgments
- **RUHS ICU Staff:** For providing the paper-based table and direct feedback on how to make the interface user-friendly.
- **My Sister (RN):** For testing in a clinical simulation and ensuring real-world accuracy.

---

## License
This project is released under the [MIT License](LICENSE). Feel free to adapt or modify for your own use, but please keep in mind that **this tool is not a substitute for professional medical judgment**. Always validate results with current clinical protocols.  

---

**Thank you for checking out the ICU Insulin Infusion Calculator!**  
If you have suggestions or would like to contribute, feel free to open an issue or a pull request.  
Enjoy coding and stay safe!
