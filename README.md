# Prediction_Of_Disease_Outbreak

## Overview
This repository contains machine learning models for **disease prediction**, including:
- **Diabetes Prediction**
- **Heart Disease Prediction**
- **Parkinson's Detection**

The models are deployed using **Streamlit** via `web.py`, allowing users to input relevant health data and receive predictions in real time.

## Features
✅ Pre-trained machine learning models for disease prediction  
✅ Web-based interface powered by **Streamlit**  
✅ Supports real-time data input and visualization  
✅ Interactive and easy-to-use dashboard  

## Repository Structure
```
📂 Saved_Models/
├── diabetes_model.sav                         # Stores trained models (.pkl files)
├── heart_disease_model.sav                    # Sample datasets
├── parkinsons_prediction_model.sav            # Data preprocessing and model training scripts
├── web.py                                     # Streamlit app to run predictions
├── requirements.txt                           # Dependencies for the project
├── README.md                                  # Project documentation (this file)
```

## Installation
Ensure you have **Python 3.8+** installed, then clone the repository:
```bash
git clone https://github.com/ItsWip/Prediction_Of_Disease_Outbreak.git
cd Prediction_Of_Disease_Outbreak
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
To launch the **Streamlit web app**, simply run:
```bash
streamlit run web.py
```
This will open the application in your default browser.

## How to Use
1. Open the web interface.
2. Select the disease model you want to use (**Diabetes, Heart Disease, or Parkinson's**).
3. Enter the required health parameters.
4. Click the **Predict** button to get the model's diagnosis.
5. View the prediction results and confidence score.

## Model Details
Each model is trained using **Support Vector Machine (SVM)**

## Future Improvements
🔹 Integrating **real-time data streams** for better accuracy  
🔹 Enhancing the UI with more visual analytics  
🔹 Expanding to other disease prediction models  

## Contributing
If you'd like to contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a **pull request**!

## License
This project is open-source and available under the **MIT License**.

## Contact
For any questions or suggestions, feel free to reach out:
📧 Email: pswaraj0614@gmail.com  
🐙 GitHub: ItsWip(https://github.com/ItsWip/)

