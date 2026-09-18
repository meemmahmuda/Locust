# Locust Performance Testing

A collection of **performance and load testing scripts using Locust and Python**.

This repository contains practical examples of web application performance testing, including login flows, authenticated page access, OTP-based authentication, CSRF token handling, and HTTP request validation.

## 🚀 Overview

**Locust** is a Python-based performance testing tool that allows user behavior to be defined directly in Python. It can simulate multiple concurrent users and provides real-time metrics such as response time, request rate, and failures.

This repository was created to practice and demonstrate **performance testing and load testing using Locust**.

## 🛠️ Technologies

* Python
* Locust
* HTTP/HTTPS
* REST/API Requests
* CSRF Token Handling
* Session-Based Authentication
* OTP Authentication
* PDF Processing
* Pandas
* OpenPyXL

## 📂 Repository Structure

```text
Locust/
│
├── locustfile.py
└── README.md
```

### `locustfile.py`

Main Locust performance testing script.

It includes examples of:

* Login performance testing
* Authenticated page access
* Response validation
* Session-based authentication
* CSRF token extraction
* OTP verification flow
* WordPress login testing
* Multiple web application testing scenarios

The active Locust scenario uses:

```python
HttpUser
task
between
catch_response
```

to simulate user behavior and validate HTTP responses.

### `locust.txt`

Contains test notes and examples for different authentication flows.

The documented OTP flow follows:

```text
Login Page
    ↓
Submit Credentials
    ↓
OTP Verification
    ↓
Verify OTP
    ↓
Authenticated Session
```

It also includes examples of extracting CSRF tokens from HTML forms before submitting authentication requests.

## ⚡ Locust Installation

Install Locust using pip:

```bash
pip install locust
```

Verify the installation:

```bash
locust --version
```

## ▶️ Running the Tests

Run the default Locust file:

```bash
python -m locust -f locustfile.py
```

Or specify the target host:

```bash
python -m locust -f locustfile.py --host https://your-application.com
```

After starting Locust, open:

```text
http://localhost:8089
```

From the Locust web interface, configure:

* Number of users
* Spawn rate
* Test duration
* Target host

## 📊 Performance Metrics

During a test, Locust can be used to monitor:

* Total Requests
* Requests per Second (RPS)
* Average Response Time
* Median Response Time
* Minimum Response Time
* Maximum Response Time
* Failure Count
* Failure Percentage
* Response Time Percentiles

These metrics help identify performance bottlenecks and application behavior under concurrent user load.

## 🧪 Test Scenarios

### 1. Login Performance Test

Simulates multiple users attempting to log in concurrently.

```text
User
 ↓
Login Request
 ↓
Validate Response
 ↓
Authenticated Session
```

### 2. Authenticated Page Access

After successful authentication, the script accesses a protected page to verify that the session remains valid.

### 3. CSRF-Protected Login

The test can retrieve a login page, extract the CSRF token, and submit the token together with the login credentials.

```text
GET Login Page
      ↓
Extract CSRF Token
      ↓
POST Login Request
      ↓
Validate Authentication
```

### 4. OTP Authentication

An OTP-based authentication flow is also documented for testing multi-step login scenarios.

```text
Credentials
     ↓
Login
     ↓
OTP Verification
     ↓
Authenticated Access
```

## 📈 Example Load Test Configuration

A basic test can be configured with:

```text
Users:       50
Spawn Rate:  5 users/second
Duration:    5 minutes
```

The exact load should be selected according to the application's expected traffic and the purpose of the test.

## 🎯 Purpose

This repository demonstrates practical experience with:

* Performance Testing
* Load Testing
* Concurrent User Simulation
* HTTP Request Testing
* Authentication Flow Testing
* OTP Flow Testing
* CSRF Token Handling
* Response Validation
* Python-based Test Automation
* Performance Metrics Analysis

## 📚 Learning Outcomes

Through these scripts, I practiced designing realistic user flows with Locust rather than testing individual HTTP requests in isolation.

Key areas include:

* Creating virtual users with Python
* Defining user behavior
* Handling login sessions
* Validating server responses
* Testing authentication workflows
* Simulating concurrent users
* Monitoring application performance
* Identifying request failures and slow responses

## 🔗 References

* [Locust Documentation](https://docs.locust.io/)
* [Locust GitHub](https://github.com/locustio/locust)

## 👩‍💻 Author

**Mahmuda Binte Sayeed**

Software QA Engineer
Dhaka, Bangladesh

GitHub: [@meemmahmuda](https://github.com/meemmahmuda)
