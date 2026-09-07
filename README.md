🚢 Titanic Survival Prediction — Machine Learning Model Selection

A complete Titanic Survival Prediction machine learning project focused not only on training a model, but on building a reliable and reproducible model selection pipeline.

The goal is to determine which classification algorithm performs best on the Titanic dataset by combining:

- Feature Engineering
- Feature Scaling
- Cross-Validation
- Hyperparameter Tuning
- Pipeline-based preprocessing
- Multiple evaluation metrics
- Artificial Neural Network (ANN) comparison

Rather than selecting a model based only on accuracy, this project evaluates models using accuracy, precision, recall, F1-score and other relevant classification metrics to identify the most suitable model.

---

🎯 Project Objective

The objective is to predict whether a passenger survived the Titanic disaster based on passenger and travel-related information.

The project focuses on answering an important machine learning question:

«Which model provides the best overall performance after proper preprocessing, cross-validation and hyperparameter optimization?»

---

🧠 Machine Learning Workflow

The project follows a structured machine learning workflow:

Titanic Dataset
      ↓
Exploratory Data Analysis
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Train / Validation Split
      ↓
Preprocessing Pipelines
      ↓
Feature Scaling
      ↓
Multiple ML Models
      ↓
Cross-Validation
      ↓
Hyperparameter Tuning
      ↓
Metric Comparison
      ↓
ANN Comparison
      ↓
Best Model Selection
      ↓
Final Evaluation

---

🔍 1. Data Understanding & EDA

The Titanic dataset contains information such as:

- Passenger class
- Sex
- Age
- Number of siblings/spouses
- Number of parents/children
- Ticket information
- Passenger fare
- Cabin information
- Port of embarkation
- Survival status

Exploratory Data Analysis will be used to understand:

- Missing values
- Feature distributions
- Relationships between features and survival
- Class imbalance
- Potential outliers
- Important patterns in the dataset

---

🛠️ 2. Data Cleaning

Before training the models, the dataset will be cleaned and prepared.

Typical preprocessing steps include:

- Handling missing values
- Removing unnecessary columns
- Correcting data types
- Handling categorical variables
- Preparing the target variable
- Checking for duplicate or inconsistent data

---

⚙️ 3. Feature Engineering

Feature engineering is an important part of this project.

Instead of using only the original columns, useful features can be derived from existing passenger information.

Examples include:

- "FamilySize"
- "IsAlone"
- "Title"
- "FarePerPerson"
- Age groups
- Family-based relationships

The purpose is to create features that provide models with more meaningful information about passenger characteristics.

---

📏 4. Feature Scaling

Feature scaling will be applied where required, especially for algorithms that are sensitive to feature magnitude.

Models such as:

- Logistic Regression
- Support Vector Machine (SVM)
- K-Nearest Neighbors
- Neural Networks

can benefit from appropriately scaled numerical features.

Tree-based algorithms generally do not require feature scaling.

---

🔄 5. Machine Learning Pipelines

To keep preprocessing and model training consistent, Scikit-learn Pipelines will be used.

For example:

Raw Data
   ↓
Imputation
   ↓
Encoding
   ↓
Scaling
   ↓
Model

This approach helps prevent data leakage during cross-validation because preprocessing steps are fitted separately inside each training fold.

Different pipelines can be created for different types of algorithms.

Example

Pipeline([
    ("preprocessor", preprocessor),
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

For models that do not require scaling, the pipeline can omit the scaler.

---

🤖 6. Models

Multiple classification algorithms will be evaluated rather than relying on a single model.

Classical Machine Learning Models

- Logistic Regression
- Support Vector Machine (SVM)
- Naive Bayes
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Gradient Boosting
- Other suitable ensemble models

Deep Learning Model

An Artificial Neural Network (ANN) will also be implemented and compared against the traditional machine learning approaches.

The ANN experiment can involve tuning:

- Number of hidden layers
- Number of neurons
- Activation functions
- Learning rate
- Batch size
- Number of epochs
- Regularization
- Dropout

The ANN is included as a genuine model-selection candidate rather than assuming that deep learning will automatically perform better.

---

🔁 7. Cross-Validation

Instead of relying on a single train-validation split, cross-validation will be used to obtain a more reliable estimate of model performance.

For example:

Training Data
      ↓
 ┌────┬────┬────┬────┬────┐
 │ F1 │ F2 │ F3 │ F4 │ F5 │
 └────┴────┴────┴────┴────┘
      ↓
Multiple Training / Validation Rounds
      ↓
Average Performance

This helps determine whether a model performs consistently across different subsets of the training data.

---

🎛️ 8. Hyperparameter Tuning

Each candidate model will be optimized using hyperparameter search.

Depending on the model, techniques such as:

- "GridSearchCV"
- "RandomizedSearchCV"

can be used.

Examples of hyperparameters include:

Logistic Regression

- "C"
- "penalty"
- Solver

SVM

- "C"
- "kernel"
- "gamma"

Random Forest

- "n_estimators"
- "max_depth"
- "min_samples_split"
- "min_samples_leaf"

KNN

- "n_neighbors"
- Distance metric

ANN

- Hidden-layer architecture
- Learning rate
- Batch size
- Epochs
- Dropout

The goal is to find a well-performing configuration, not simply the default model settings.

---

📊 9. Model Evaluation

Model selection will not be based on accuracy alone.

The following metrics will be compared:

Metric| Purpose
Accuracy| Overall percentage of correct predictions
Precision| How many predicted survivors were actually survivors
Recall| How many actual survivors were correctly identified
F1-Score| Balance between precision and recall
ROC-AUC| Measures ranking/discrimination performance
Confusion Matrix| Shows detailed prediction errors

Why Recall Matters

For this problem, recall is particularly useful because it measures how many actual survivors the model successfully identifies.

However, the final model will not automatically be chosen using recall alone.

The model will be selected by considering the complete evaluation profile and the specific trade-offs between:

«Recall + Precision + Accuracy + F1-Score + ROC-AUC»

---

🏆 10. Best Model Selection

After cross-validation and hyperparameter tuning, the models will be compared side-by-side.

A final comparison table will contain results such as:

Model| CV Score| Accuracy| Precision| Recall| F1| ROC-AUC
Logistic Regression| —| —| —| —| —| —
SVM| —| —| —| —| —| —
Naive Bayes| —| —| —| —| —| —
Random Forest| —| —| —| —| —| —
Gradient Boosting| —| —| —| —| —| —
ANN| —| —| —| —| —| —

The "—" values will be replaced after experiments are completed.

The final model will be selected based on validated performance and generalization, rather than simply choosing the model with the highest training accuracy.

---

🧪 11. ANN vs Classical Machine Learning

A major part of this project is comparing a neural network with traditional machine learning algorithms.

The experiment will investigate whether an ANN actually provides a meaningful performance improvement on this dataset.

The comparison will answer:

Classical ML
      vs
Artificial Neural Network
      ↓
Cross-Validation
      ↓
Hyperparameter Optimization
      ↓
Metric Comparison
      ↓
Best Performing Approach

This provides practical experience in deciding when traditional machine learning is sufficient and when a neural network may be useful.

---

📁 Project Structure

Titanic/
│
├── backend/
│   └── model.py
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
│
├── requirements.txt
│
└── README.md

«The project structure will evolve as the ML pipeline, experiments and final model implementation are added.»

---

🧰 Technologies

Programming

- Python

Data Analysis

- Pandas
- NumPy
- Matplotlib
- Seaborn

Machine Learning

- Scikit-learn

Deep Learning

- TensorFlow / Keras

Development

- Jupyter Notebook
- Git
- GitHub

---

📌 Key Concepts Demonstrated

This project is designed to demonstrate practical understanding of:

Data Science

- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Data preprocessing

Machine Learning

- Classification
- Model comparison
- Cross-validation
- Hyperparameter tuning
- Feature scaling
- Pipelines
- Model evaluation
- Overfitting and generalization

Deep Learning

- Artificial Neural Networks
- Neural-network hyperparameter tuning
- Comparison with classical ML models

---

🚀 Future Improvements

Possible future extensions include:

- Feature selection
- Ensemble stacking / voting
- Threshold optimization
- SHAP-based model explainability
- Error analysis
- Model deployment with FastAPI
- Dockerization
- Cloud deployment

---

👨‍💻 Author

Gurpreet Singh

GitHub:
"https://github.com/Gurpreet-Singh-Git" (https://github.com/Gurpreet-Singh-Git)

---

⭐ Project Goal

The main goal of this project is not simply to achieve a high Titanic leaderboard score.

It is to demonstrate a professional machine learning workflow:

«Engineer better features → build reliable pipelines → compare multiple algorithms → validate with cross-validation → tune hyperparameters → evaluate using multiple metrics → compare with ANN → select the model that generalizes best.»

This project is intended to demonstrate the reasoning and methodology behind model selection, not just model training.