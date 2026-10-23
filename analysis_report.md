# NumPy Matrix Operations — Analysis Report

## 1. Project Overview

The project demonstrates basic matrix operations using NumPy. Two 2 × 2 matrices are created and used to perform addition, subtraction, matrix multiplication, and transpose operations.

## 2. Objective

The objective is to understand how NumPy simplifies matrix calculations and how matrix dimensions affect mathematical operations.

## 3. Dataset

Matrix A:

\[
A = \begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}
\]

Matrix B:

\[
B = \begin{bmatrix}5 & 6\\7 & 8\end{bmatrix}
\]

Both matrices have the shape (2, 2).

## 4. Methodology

The matrices are created using `numpy.array()`. NumPy arithmetic operators perform addition and subtraction. The `@` operator performs matrix multiplication, while the `.T` attribute calculates the transpose of each matrix.

The program checks matrix shapes before performing addition and subtraction and verifies the dimensions required for matrix multiplication.

## 5. Results

### Addition

\[
A+B=\begin{bmatrix}6&8\\10&12\end{bmatrix}
\]

### Subtraction

\[
A-B=\begin{bmatrix}-4&-4\\-4&-4\end{bmatrix}
\]

### Matrix Multiplication

\[
AB=\begin{bmatrix}19&22\\43&50\end{bmatrix}
\]

### Transpose of Matrix A

\[
A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}
\]

### Transpose of Matrix B

\[
B^T=\begin{bmatrix}5&7\\6&8\end{bmatrix}
\]

## 6. Analysis

Addition and subtraction combine corresponding elements of matrices with matching dimensions. Matrix multiplication follows the row-by-column rule and produces a new matrix. Transposition exchanges rows and columns.

These operations are important for representing and transforming numerical data in machine learning and scientific computing.

## 7. Applications

Matrix operations are used in machine learning algorithms, linear regression, neural networks, image processing, scientific simulations, and numerical analysis.

## 8. Conclusion

The project successfully demonstrates the four required types of matrix operations using NumPy. It provides practical experience with matrix creation, shape validation, arithmetic operations, and transposition.
