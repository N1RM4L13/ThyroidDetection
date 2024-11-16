
# Thyroid Detection

## Problem Statement

This project aims to build a classification model to predict thyroid types, specifically identifying hypothyroid or hyperthyroid conditions, using the provided training dataset. The goal is to develop a reliable methodology to support accurate diagnosis and effective disorder management.

The model can be utilized by hospitals as a first level of scrutinization. Initially, the model predicts whether a person is suffering from thyroid-related conditions, such as hypothyroidism or hyperthyroidism. If the prediction is positive, the treatment process is fast-tracked, ensuring doctors address the case with priority. For negative predictions, the patient’s file is reviewed by a junior doctor to verify the model's accuracy. While the model is designed for high accuracy, human oversight is crucial in medical cases. If the junior doctor concurs with the model’s negative prediction, the patient is released. However, if the junior doctor identifies inconsistencies, the case is escalated to a senior doctor for further evaluation and treatment. This workflow ensures efficient use of resources while maintaining the reliability and safety of medical care.




## Dataset

- age: Age of the patient.
- sex: Gender of the patient (M/F).
- on_thyroxine: Whether the patient is on thyroxine treatment (t/f).
- query_on_thyroxine: Inquiry if the patient is on thyroxine (t/f).
- on_antithyroid_medication: Whether the patient is on
- anti-thyroid medication (t/f).
- sick: Whether the patient has been sick (t/f).
- pregnant: Whether the patient is pregnant (t/f).
- thyroid_surgery: Whether the patient has undergone thyroid surgery (t/f).
- I131_treatment: History of radioactive iodine treatment (t/f).
- query_hypothyroid: Inquiry about hypothyroid symptoms (t/f).
- query_hyperthyroid: Inquiry about hyperthyroid symptoms (t/f).
- lithium: Whether the patient is on lithium treatment (t/f).
- goitre: Presence of goitre (t/f).
- tumor: History of a tumor (t/f).
- hypopituitary: Presence of hypopituitarism (t/f).
- psych: History of psychological disorders (t/f).
- TSH_measured: Whether TSH (Thyroid Stimulating Hormone) was
- measured (t/f).
- TSH: TSH level.
- T3_measured: Whether T3 hormone was measured (t/f).
- T3: T3 hormone level.
- TT4_measured: Whether TT4 hormone was measured (t/f).
- TT4: Total T4 hormone level.
- T4U_measured: Whether T4 uptake was measured (t/f).
- T4U: T4 uptake value.
- FTI_measured: Whether FTI (Free Thyroxine Index) was measured (t/f).
- FTI: Free Thyroxine Index.
- TBG_measured: Whether TBG (Thyroxine Binding Globulin) was
- measured (t/f).
- TBG: TBG level.
- referral_source: Source of patient referral.
- Class: Target variable indicating thyroid condition (e.g., negative, hypothyroid, hyperthyroid).


## Application Flow
![Application Flow Overview](assets\FlowDiagram.png)

