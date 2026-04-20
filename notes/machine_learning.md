# Machine Learning

## Fundamentals

### Concepts
- Learning = minimizing loss
- Empirical Risk Minimization
- Loss vs Cost
- Train / Validation / Test Split
- Overfitting vs Underfitting
- Cross-validation
- Regularization

### Interview Q&A
Q: What is overfitting?  
A: Model memorizes training data but fails on new data.

---

## Supervised Learning

### Linear Regression
- Assumptions: linearity, independence
- MSE Loss
- Gradient Descent vs Normal Equation
- R² score

Q: What is R²?  
A: Measure of variance explained.

---

### Logistic Regression
- Sigmoid function
- Log-loss
- Decision boundary

Q: Why not use MSE?  
A: Leads to non-convex optimization.

---

### kNN
- Distance metrics
- Lazy learning
- Curse of dimensionality

---

### Naive Bayes
- Based on Bayes theorem
- Assumes feature independence

Q: Why does it work well?  
A: Even with wrong assumptions, performs well in practice.

---

### Decision Trees
- Entropy, Information Gain
- Gini Index
- Overfitting → pruning

---

### Ensemble Methods

#### Random Forest
- Bagging
- Reduces variance

#### Gradient Boosting
- Sequential learning
- Reduces bias

Q: Bagging vs Boosting?  
A: Bagging reduces variance, boosting reduces bias.

---

### SVM
- Maximum margin classifier
- Kernel trick

Q: Why kernel trick?  
A: Enables non-linear classification.

---

## Unsupervised Learning

### K-Means
- Cluster based on distance
- Sensitive to initialization

### DBSCAN
- Density-based clustering
- Handles noise

### PCA
- Dimensionality reduction
- Uses eigen decomposition

---

## Model Evaluation

- Precision, Recall, F1
- ROC-AUC
- PR Curve
- Imbalanced datasets

---

## Advanced ML

- Feature engineering
- Feature selection
- Hyperparameter tuning
- Grid vs Random Search
- Bayesian Optimization
- Data leakage
- Pipelines