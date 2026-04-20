# Artificial Intelligence (AI) – Foundations

## Linear Algebra

### Key Concepts
- Vectors, Matrices, Tensors
- Matrix Multiplication (order matters: AB ≠ BA)
- Dot Product → measures similarity
- Eigenvalues & Eigenvectors → directions of transformation
- SVD → matrix decomposition
- Rank → independent information
- Orthogonality → perpendicular vectors
- Projection → mapping onto subspace
- Norms:
  - L1 → sparsity
  - L2 → smoothness
- Trace → sum of diagonal
- Determinant → scaling factor

### Interview Q&A
Q: Why eigen decomposition is useful in PCA?  
A: It identifies directions (principal components) of maximum variance.

Q: Why use L2 norm in regularization?  
A: It penalizes large weights smoothly and prevents overfitting.

---

## Probability & Statistics

### Key Concepts
- Random Variables (discrete/continuous)
- PMF / PDF
- Expectation, Variance
- Covariance vs Correlation
- Bayes Theorem
- Conditional Probability
- Gaussian Distribution
- Central Limit Theorem
- Law of Large Numbers
- MLE & MAP
- Hypothesis Testing
- Confidence Intervals
- Bias-Variance Tradeoff

### Interview Q&A
Q: Difference between MLE and MAP?  
A: MLE maximizes likelihood, MAP includes prior.

Q: What is bias-variance tradeoff?  
A: Balance between underfitting (high bias) and overfitting (high variance).

---

## Calculus (Optimization)

### Key Concepts
- Derivatives, Partial Derivatives
- Chain Rule (used in backprop)
- Gradients → direction of steepest increase
- Jacobian → multi-variable derivatives
- Hessian → curvature
- Convex vs Non-convex
- Gradient Descent

### Interview Q&A
Q: Why gradients are important?  
A: They guide optimization during training.
