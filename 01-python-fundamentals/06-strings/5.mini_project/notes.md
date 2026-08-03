# Mini Project - Cloud Log Analyzer & User Account Normalizer

## Overview

These projects demonstrate real-world string processing techniques commonly used in backend systems, cloud monitoring tools, and web applications.

---

# Project 1 – Cloud Log Analyzer

## Problem

A cloud server generates log entries in the following format:

2026-07-29|ERROR|PAYMENT-SERVICE|Database connection failed

The goal is to extract meaningful information and generate a structured report.

---

## Concepts Used

- split()
- lower()
- len()
- String indexing
- Membership operator (in)
- Variables
- Formatted output using f-strings

---

## Workflow

1. Read the log entry.
2. Split the string using '|'.
3. Extract date, level, service and message.
4. Convert service name to lowercase.
5. Calculate message length.
6. Check whether the log contains an ERROR.
7. Generate a formatted report.

---

## Skills Learned

- Parsing structured text
- Extracting information from strings
- Creating readable reports
- Log analysis basics

---

# Project 2 – User Account Normalizer

## Problem

User information received from an application may contain unnecessary spaces and inconsistent capitalization.

The objective is to clean the data before storing it in a database.

---

## Concepts Used

- strip()
- lower()
- title()
- endswith()
- Membership operator
- String formatting

---

## Workflow

1. Remove unwanted spaces.
2. Convert username to lowercase.
3. Convert email to lowercase.
4. Convert role to title case.
5. Validate email format.
6. Display a formatted user profile.

---

## Skills Learned

- Data cleaning
- Input normalization
- Email validation basics
- Professional string formatting

---

## Industry Relevance

Similar techniques are used in:

- Backend APIs
- Authentication systems
- Cloud monitoring platforms
- Log processing tools
- Database applications

These projects provide the foundation for larger Python applications involving file processing and automation.