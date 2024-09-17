# Privacy-Preserving Data Sharing System User Guide

## Introduction
This guide provides instructions on how to set up and use the Privacy-Preserving Data Sharing System to securely share data using homomorphic encryption and differential privacy.

## Prerequisites
- Python 3.x
- Required Python libraries: seal, numpy, syft

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Barrosleo/Privacy-Preserving-Data-Sharing-System.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd Privacy-Preserving-Data-Sharing-System
    ```

3. **Install Required Libraries**:
    ```bash
    pip install seal numpy syft
    ```

## Usage

### Homomorphic Encryption
- Run the homomorphic encryption script:
    ```bash
    python src/homomorphic_encryption.py
    ```

### Differential Privacy
- Run the differential privacy script:
    ```bash
    python src/differential_privacy.py
    ```

### Secure Data Sharing
- Run the secure data sharing script:
    ```bash
    python src/secure_data_sharing.py
    ```

## Troubleshooting
- Ensure all required libraries are installed.
- Verify the paths to your data files are correct.
