# 🚀 Credit Card Fraud Detection System

This project focuses on building a machine learning model to detect fraudulent credit card transactions. The dataset used is publicly available and contains anonymized data from credit card transactions. The goal is to create a system that can predict whether a transaction is fraudulent or not based on the given features.

## 📦 Project Overview

The project includes the following key components:
1. **Data Preprocessing:** Cleaning and transforming the data, including handling missing values, scaling features, and balancing the dataset.
2. **Model Development:** Building a machine learning model using **Random Forest** and evaluating performance using metrics such as precision, recall, and F1 score.
3. **Data Visualization:** Visualizing data distributions and insights using **Seaborn** and **Matplotlib**.
4. **Web Interface:** Building an interactive **Dash** application for visualizing the data and making real-time fraud predictions using a **Flask API**.

## 🛠️ Technologies Used

- **Python**: Main programming language
- **Flask**: For building the RESTful API
- **Dash**: For building interactive web interfaces
- **Keras**: For building and training deep learning models
- **Scikit-learn**: For machine learning algorithms and evaluation metrics
- **Pandas**: For data manipulation and analysis
- **NumPy**: For numerical operations
- **Matplotlib & Seaborn**: For data visualization
- **Snaplib**: For data cleaning

## 📊 Visualizations

The project includes visualizations such as:

- **ROC Curve**: Evaluates the trade-off between the true positive rate and false positive rate.
- **Precision-Recall Curve**: Assesses the performance of the model on imbalanced datasets.
- **Histogram Grids**: Visualize the distribution of features based on fraud vs. normal transactions.

## 🧑‍💻 Model Performance

Model performance is evaluated using various metrics, including:

- Precision
- Recall
- F1-score
- ROC-AUC
- Precision-Recall AUC

The model is trained using K-fold cross-validation, and the predictions are aggregated to improve the reliability of results.

## 🎨 Web Interface

The project includes an interactive web interface built with **Dash** to visualize the dataset and test the fraud detection model on new transactions.

### Features:

- Upload a CSV file of transactions for fraud detection
- Visualize transaction distributions and model performance metrics
- Real-time fraud detection for uploaded transaction

## 🚀 How to Run

```bash
1. Clone the repository:
git clone https://github.com/yourusername/credit-card-fraud-detection.git

2. Navigate to the project directory:
cd credit-card-fraud-detection

3. Install the necessary libraries:
pip install -r requirements.txt

4. Run the Flask API for real-time fraud detection:
python app.py

5. To run the Dash Web Interface, run:
python dash_app.py

6. Open your browser and visit http://127.0.0.1:5000 for the Flask API and http://127.0.0.1:8050 for the Dash Web Interface.
