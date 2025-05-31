# 🌱 Soil Quality Prediction System using Modified MLP

A deep learning-based system for classifying soil quality to empower precision agriculture. This project utilizes a *Modified Multilayer Perceptron (MLP)* model to predict soil fertility classes based on chemical and physical soil parameters from the *LUCAS 2018 TOPSOIL* dataset.


## 📌 Overview

Traditional methods of soil testing are expensive, slow, and inaccessible to small farmers. This system leverages machine learning—particularly deep learning—to provide *fast, accurate, and **scalable* soil classification. The modified MLP model achieved *98.72% accuracy*, outperforming other standard ML algorithms.

## 🚀 Features

- Cleaned and preprocessed *LUCAS 2018 TOPSOIL* dataset
- Multi-class soil quality classification (Excellent, Good, Fair, Moderate, Poor)
- Deep learning architecture using *Modified MLP* with 3 hidden layers
- *Dropout regularization* to prevent overfitting
- Evaluation using metrics: Accuracy, Precision, Recall, F1-Score, AUC-ROC
- Visualizations: Training/Validation Accuracy & Loss, ROC Curves

## 📁 Dataset

- *Source*: [LUCAS 2018 TOPSOIL Data](https://esdac.jrc.ec.europa.eu/projects/lucas)
- Features: pH, organic carbon, nitrogen, phosphorus, potassium, CaCO₃, EC, oxalate-extractable Fe/Al, etc.
- Target: Soil Quality (5 classes)

## 🧠 Model Architecture

- Input Layer: Standardized soil features
- Hidden Layers: 3 layers (with ReLU activation)
- Dropout: 30%, 30%, and 20% respectively
- Output Layer: Softmax for 5-class classification
- Optimizer: Adam
- Loss Function: Categorical Crossentropy

## 📊 Performance

| Metric     | Score   |
|------------|---------|
| Accuracy   | 98.72%  |
| F1-Score   | 0.9839  |
| AUC-ROC    | 0.9998  |
| Precision  | 0.9878  |
| Recall     | 0.9822  |

## 📈 Visuals

- 📌 ROC-AUC Curve
- 📌 Training vs Validation Accuracy
- 📌 Training vs Validation Loss

## 🧪 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/tishya283/Soil-Quality-Prediction-System.git

# Create a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install required libraries

# Run the model training script
python train_model.py 
