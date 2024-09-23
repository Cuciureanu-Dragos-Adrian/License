# The Role of Geometric Algorithms in Cryptography

This project focuses on exploring the role of **elliptic curve cryptography (ECC)** within the broader scope of cryptographic algorithms. It demonstrates how geometric algorithms are applied in modern cryptographic systems using elliptic curves over finite fields.

## Overview

Elliptic curve cryptography (ECC) offers several advantages over traditional cryptographic methods, including **smaller key sizes**, **faster computations**, and **increased security**. The project simulates key cryptographic algorithms like **Diffie-Hellman key exchange**, **ElGamal encryption**, and **Elliptic Curve Digital Signature Algorithm (ECDSA)**, while also exploring the mathematical foundations of elliptic curves.

This repository contains both theoretical insights and an accompanying application that allows users to interactively explore various geometric algorithms in cryptography.

## Features

- **Elliptic Curve Arithmetic**:
  - Addition and scalar multiplication on elliptic curves, both over real numbers (R) and finite fields (Fp).
  - Order of elliptic curves and points over Fp.
- **Cryptographic Protocols**:
  - Simulation of **ECDH** (Elliptic Curve Diffie-Hellman) and **ElGamal encryption** over elliptic curves.
  - Simulation of **ECDSA** (Elliptic Curve Digital Signature Algorithm).
  - Approximation and simulation of **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

## Application Details

The application is built using **Python** and employs frameworks such as **Flask** for the user interface, allowing users to:
1. **Simulate elliptic curve operations**: Perform elliptic curve addition, scalar multiplication, and explore key cryptographic functions interactively.
2. **Educational tool**: Walk through each step of the algorithm, with intermediate calculations displayed to enhance learning and understanding.
3. **Random elliptic curve generator**: Generate random elliptic curves for experimentation.

## Implemented Algorithms

The following algorithms are implemented and can be simulated within the application:
- **Elliptic Curve Point Addition**: Both in real numbers (R) and finite fields (Fp).
- **Elliptic Curve Scalar Multiplication**: Both in real numbers (R) and finite fields (Fp).
- **Diffie-Hellman Key Exchange**: Normal and enhanced simulations.
- **ElGamal Encryption**: Normal and enhanced simulations.
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Full simulation of the signing and verification process.
- **ECDLP (Elliptic Curve Discrete Logarithm Problem)**: Approximation and simulation of this fundamental cryptographic challenge.

## Structure

1. **Preliminary Concepts**: Overview of elliptic curves and their properties.
2. **Elliptic Curve Cryptography**: Key cryptographic protocols adapted for elliptic curves.
3. **Application**: Implementation of various geometric algorithms in cryptography.
4. **Simulations**: Step-by-step simulations of cryptographic protocols like ECDH, ElGamal, and ECDSA.
5. **Conclusions**: Final insights and potential future work.

## Technologies

- **Python**: Core programming language.
- **Flask**: Web framework for creating the interactive user interface.
- **SymPy, Tinyec**: Libraries used for elliptic curve operations and simulations.

## Future Work

The project can be extended with:
- **Optimization of elliptic curve operations** for larger datasets and more complex simulations.
- **Integration with existing cryptographic libraries** for real-world applications.
- **Advanced visualizations** to better represent the mathematical operations behind elliptic curve cryptography.
