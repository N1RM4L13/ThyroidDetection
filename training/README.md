# Process Overview

## 1. Data Validation
This step ensures that the provided training files meet predefined standards. Several validation checks are performed:

### 1.1. Name Validation
- File names are validated against a regex pattern defined in the schema file.
- Additional checks include:
  - Length of the date in the file name.
  - Length of the time in the file name.
- Files that meet all criteria are moved to the **Good_Data_Folder**. Otherwise, they are moved to the **Bad_Data_Folder**.

### 1.2. Number of Columns
- The number of columns in each file is validated against the value specified in the schema file.
- Files with an incorrect number of columns are moved to the **Bad_Data_Folder**.

### 1.3. Name of Columns
- Column names are validated to ensure they match those in the schema file.
- Files with incorrect column names are moved to the **Bad_Data_Folder**.

### 1.4. Data Type of Columns
- Data types of the columns are validated during the database insertion process, as specified in the schema file.
- Files with incorrect data types are moved to the **Bad_Data_Folder**.

### 1.5. Null Values in Columns
- If a column in a file has all its values as `NULL` or missing, the file is discarded and moved to the **Bad_Data_Folder**.

---

## 2. Data Insertion into Database
This step involves organizing and storing validated data into a database.

### 2.1. Database Creation and Connection
- A database is created using the specified name.
- If the database already exists, a connection to it is established.

### 2.2. Table Creation
- A table named **Good_Data** is created in the database to store files from the **Good_Data_Folder**.
- If the table already exists, new files are appended to the existing table to enable training on both new and old data.

### 2.3. File Insertion
- All files from the **Good_Data_Folder** are inserted into the **Good_Data** table.
- Files with invalid data types are skipped and moved to the **Bad_Data_Folder**.

---

## 3. Model Training
The final step involves preparing the data, clustering it, and training machine learning models.

### 3.1. Data Export from Database
- Data stored in the database is exported as a CSV file for model training.

### 3.2. Data Preprocessing
The exported data undergoes the following steps:
- **Drop Unnecessary Columns:** Remove columns deemed irrelevant during Exploratory Data Analysis (EDA).
- **Handle Invalid Values:** Replace invalid values with `NaN` using NumPy.
- **Encode Categorical Values:** Convert categorical data into numerical form.
- **Handle Null Values:** Use the KNN imputer to fill missing values.
- **Handle Imbalanced Dataset:** Use RandomOverSampler to balance the dataset.

### 3.3. Clustering
- The **KMeans** algorithm is applied to cluster the preprocessed data.
- The optimal number of clusters is determined using the elbow plot and the **KneeLocator** function.
- The trained KMeans model is saved for future use during predictions.

### 3.4. Model Selection
- For each cluster, two algorithms are evaluated: **Random Forest** and **KNN**.
- **GridSearch** is used to find the best parameters for both algorithms.
- The model with the highest **AUC** score is selected for each cluster.
- All selected models are saved for use during prediction.
