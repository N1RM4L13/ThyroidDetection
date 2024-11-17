# Prediction Workflow Documentation

## 1. Prediction Data Description
- **Input Data:** The client provides multiple files in batches, each containing wafer names and 590 sensor values for each wafer.
- **Schema File:** The client provides a schema file that includes:
  - File naming conventions.
  - Length of the date and time values in the filename.
  - Number of columns.
  - Names and datatypes of columns.

---

## 2. Data Validation
To ensure data integrity, the following validation checks are performed:

### 2.1. Name Validation
- A regex pattern is created based on the file naming conventions in the schema file.
- Validation checks include:
  - File name matches the regex pattern.
  - Date and time lengths in the file name conform to the schema.
- Files that pass validation are moved to the **Good_Data_Folder**; others are moved to the **Bad_Data_Folder**.

### 2.2. Number of Columns
- The number of columns in the file must match the schema file.
- Files with an incorrect number of columns are moved to the **Bad_Data_Folder**.

### 2.3. Name of Columns
- Column names in the file are validated against the schema file.
- Files with mismatched column names are moved to the **Bad_Data_Folder**.

### 2.4. Datatype of Columns
- Column datatypes are validated during insertion into the database.
- Files with incorrect datatypes are moved to the **Bad_Data_Folder**.

### 2.5. Null Values in Columns
- Files where any column has all values as `NULL` are discarded and moved to the **Bad_Data_Folder**.

---

## 3. Data Insertion into Database
The validated data is inserted into the database following these steps:

### 3.1. Database Creation and Connection
- A database is created with the specified name.
- If the database already exists, a connection is established.

### 3.2. Table Creation
- A table named **Good_Data** is created to store files from the **Good_Data_Folder**.
- If the table already exists, new files are appended to it, enabling training on both new and old data.

### 3.3. File Insertion
- Files in the **Good_Data_Folder** are inserted into the **Good_Data** table.
- Files with invalid data types are skipped and moved to the **Bad_Data_Folder**.

---

## 4. Prediction Workflow
Once the data is validated and inserted into the database, the following steps are performed to generate predictions:

### 4.1. Data Export from Database
- Data stored in the database is exported as a CSV file for prediction.

### 4.2. Data Preprocessing
The exported data undergoes the following steps:
- **Dropping Unnecessary Columns:** Columns identified as irrelevant during EDA are removed.
- **Handling Invalid Values:** Replace invalid values with `NaN` for imputation.
- **Encoding Categorical Values:** Convert categorical variables to numeric format.
- **Null Value Imputation:** Fill missing values using the KNN imputer.

### 4.3. Clustering
- The **KMeans** model created during training is loaded.
- Clusters for the preprocessed prediction data are predicted using this model.

### 4.4. Prediction
For each cluster:
- The respective trained model (**Random Forest** or **KNN**) is loaded.
- Predictions are made for the data in that cluster.
- Predictions for all clusters are aggregated.

### 4.5. Saving Predictions
- Predictions, along with the original column names (decoded from label encoding), are saved to a CSV file at the specified location.
- The file location is returned to the client.
