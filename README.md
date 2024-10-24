# Application 1 : Rule Engine with Abstract Syntax Tree (AST)

> Zeotap | Software Engineer Intern | Assignment | Application 1

# introduction

Hi, I'm Pankajkrjain , a Software Developer and AI enthusiast skilled in python, Kotlin/java, React, Next.js, Django, and machine learning.
I'm currently working on projects as mobile music application and travellers Application integrated with safty features for navigation , always eager to learn!
[LinkedIn](https://www.linkedin.com/in/pankajkumar2849/). 

## Overview
This project is a simple 3-tier rule engine application that determines user eligibility based on attributes like age, department,
income, spend, etc. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, 
and modification of these rules.

## Features
- **Dynamic Rule Creation**: Create rules using an abstract syntax tree.
- **Rule Combination**: Combine multiple rules into a single AST.
- **Rule Evaluation**: Evaluate rules against user data to determine eligibility.
- **Database Integration**: Store rules and their corresponding AST representations in a database.

## Prerequisites
- Python 3.x
- Virtual environment

## Installation

1. **Clone the Repository:**
   ```sh
   git clone  https://github.com/PankajKrJain2804/Application-1-Rule-Engine-with-AST.git

   cd rule-engine-ast
- Create and Activate a Virtual Environment:

sh

python -m venv venv
venv\Scripts\activate  # On Windows
- source venv/bin/activate  # On macOS/Linux
Install Dependencies:

sh

pip install -r requirements.txt
Set Up the Database:

sh

python database.py
Usage
Creating and Evaluating Rules
Create a Rule:

python

from rule_engine import create_rule

rule_string = "age > 30 AND department = 'Sales'"
ast = create_rule(rule_string)
print(ast)
Combine Multiple Rules:

python

from rule_engine import combine_rules

rules = ["age > 30 AND department = 'Sales'", "salary > 50000 OR experience > 5"]
combined_ast = combine_rules(rules)
print(combined_ast)
Evaluate a Rule:

python

from rule_engine import evaluate_rule

data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(combined_ast, data)
print(result)
Running the Application
Run the Application:

sh

python app.py
API Endpoints
Create Rule
Endpoint: /create_rule

Method: POST

- Description: Takes a rule string and returns a Node object representing the corresponding AST.

Combine Rules
Endpoint: /combine_rules

Method: POST

- Description: Takes a list of rule strings and combines them into a single AST.

Evaluate Rule
Endpoint: /evaluate_rule

Method: POST

- Description: Takes a JSON representing the combined rule's AST and a dictionary of data containing attributes. Evaluates the rule against the provided data and returns True if the user is eligible based on the rule, False otherwise.

Test Cases
System Setup:

Verify that the system starts successfully and connects to the database.

Data Retrieval:

- Simulate API calls and ensure the system retrieves and parses data correctly.

Rule Evaluation:

Create individual rules and verify their AST representation.

Combine example rules and ensure the resulting AST reflects the combined logic.

Test evaluation of sample JSON data against various scenarios.

Alerting Thresholds:

Define and configure user thresholds for different conditions.

Simulate data exceeding or breaching the thresholds and verify that alerts are triggered correctly.

Future Enhancements
User-Defined Functions: Support user-defined functions within the rule language for advanced conditions.

Error Handling: Implement error handling for invalid rule strings or data formats.
