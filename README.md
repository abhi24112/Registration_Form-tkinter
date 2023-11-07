# Registration Form Interface with Admin Portal

## Overview

This project is a simple yet effective Registration Form Interface created using Tkinter in Python. The registration form collects candidate details and stores them in an SQLite3 database and it also have some additional feature like if details are not filled properly to tells the user to enter the data correctly. Additionally, there's an Admin Portal that allows administrators to view all the details submitted by candidates. There is also a security layer for accessing the data means Login and password is required to access the data.And if admin enter the wrong password it show "Please enter the correct password".

## Features

- User-friendly Registration Form Interface.
- It show data within the application.
- Seamless integration with SQLite3 for efficient data storage.
- Admin Portal to access and review candidate details.
- Attachments: Screenshots of the Registration Form and Admin Portal for quick reference.

## Screenshots

### Registration Form Interface

#### 1.If No Error Is Found:
![image](https://github.com/abhi24112/Registration_Form-tkinter/assets/91802093/af8abdc3-261d-485e-9288-9275d33b0588)

#### 2.If Entry Is Not Filled Perfectly:
![image](https://github.com/abhi24112/Registration_Form-tkinter/assets/91802093/74889d2f-a132-40ef-8567-918ca2434429)

### Admin Portal

#### 1.If No Error Is Found:
![image](https://github.com/abhi24112/Registration_Form-tkinter/assets/91802093/8b8bc76d-8dfd-49b7-a267-1522b4bf96d8)

#### 2.If Error is Found:
![image](https://github.com/abhi24112/Registration_Form-tkinter/assets/91802093/940b7605-fd01-489d-bb2e-bd56a4bd0c7e)

## Requirements

- Python 3.x
- Tkinter library
- SQLite3

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/your-username/registration-form.git
   ```

2. Navigate to the project directory:

   ```
   cd Registration_form
   ```

3. Run the main application:

   ```
   python Form.py
   ```
4. Run the Admin application:

   ```
   python data_acces.py
   ```

## Database

The project uses SQLite3 as the backend database. The database file (`RegForm.db`) is automatically created upon the first run.


**Note:** For security purposes, it's recommended to change the default admin credentials in a production environment.

## Contributions

Feel free to contribute to the project by creating issues or submitting pull requests. Your feedback and suggestions are highly appreciated.
---

Happy Coding! 🚀
