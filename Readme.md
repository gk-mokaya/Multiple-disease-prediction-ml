# Disease Prediction System

### Author: gk-mokaya | kevinmokaya001@gmail.com | 0797252133

### Demo url: https://mediscanmldiseaseprediction.streamlit.app/

## Overview

This project is a comprehensive disease prediction system that allows users to predict the likelihood of various diseases based on specific input parameters. The system currently supports predictions for Diabetes, Breast Diseases, Heart Diseases, and Parkinson's Disease. The goal is to provide an easy-to-use interface for users to input their health data and receive predictions about potential diseases.


## Installation

To set up and run this project on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

If you don't have Git installed, you can download the repository as a ZIP file and extract it.

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can install the necessary packages manually. Common packages might include:

```bash
pip install numpy pandas scikit-learn flask
```

### Step 4: Run the Application

Once the dependencies are installed, you can run the application.

```bash
    streamlit run '.\multiple disease predict.py'
```

This will start the application, and you can access it via a web browser at `  Local URL: http://localhost:8501`.

### Step 5: Access the Application

Open your web browser and navigate to the local server address (e.g., `  Local URL: http://localhost:8501/`). You should see the disease prediction system interface, where you can select the type of disease prediction and input the required parameters.


## Features

- **Diabetes Disease Prediction**: Predicts the likelihood of diabetes based on factors such as glucose level, insulin level, age, blood pressure, BMI, and more.
- **Breast Disease Prediction**: Predicts breast diseases using tumor characteristics like mean radius, texture, perimeter, area, and other related metrics.
- **Heart Disease Prediction**: Assesses the risk of heart disease using parameters like age, sex, chest pain type, resting blood pressure, and electrocardiographic results.
- **Parkinson's Disease Prediction**: Evaluates the presence of Parkinson's disease based on voice and speech characteristics, including jitter, shimmer, and other frequency measures.

## Usage

1. **Diabetes Disease Prediction**:
   - Input parameters such as number of pregnancies, skin thickness, diabetes pedigree function, glucose level, insulin level, age, blood pressure, and BMI.
   - Click "Diagnose" to get the prediction.

2. **Breast Disease Prediction**:
   - Enter tumor characteristics like mean radius, texture, perimeter, area, smoothness, compactness, concavity, and more.
   - The system will provide a prediction based on the input data.

3. **Heart Disease Prediction**:
   - Provide details such as age, sex, chest pain type, resting blood pressure, fasting blood sugar, resting electrocardiographic results, maximum heart rate, and exercise-induced angina.
   - The system will output the heart disease test result.

4. **Parkinson's Disease Prediction**:
   - Input voice and speech characteristics including average word frequency, jitter, shimmer, and other related metrics.
   - The system will determine if the person has Parkinson's disease.

## Disease Menu

The system includes a disease menu for easy navigation between different disease prediction modules:
- Diabetes Diseases
- Breast Diseases
- Heart Diseases
- Parkinson's Diseases

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## Acknowledgments
- Thanks to Omondi Charles and Prof Becky Aloo for your sincere contributions and guidance
- Thanks to all contributors who have helped in developing this project.
- Special thanks to the open-source community for providing valuable resources and tools.

## Contact

For any questions or suggestions, please contact Mokaya Kevin at kevinmokaya001@gmail.com. or +254790886755

---