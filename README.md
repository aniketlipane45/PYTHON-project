

## Subscription Service Management System 

## **Project Created By**  
Lipane Aniket Ashok  
Student of Amrutvahini College of Engineering  
T.E Computer Engineering Department (under Zensar Python and SQL Training)  

---

## **Project Description**  
This project is a robust subscription service management system implemented using **Python Flask** and **MySQL**. It provides functionality for managing users, subscriptions, payments, and services. The system also includes advanced features such as account suspension for overdue payments, automated subscription renewals, and discount calculations based on subscription duration.  

Key components include:  
1. **Users**: Manages user information such as name, email, and account status.  
2. **Services**: Maintains details about subscription plans, including names and prices.  
3. **Subscriptions**: Tracks user subscriptions, including service details, start and end dates.  
4. **Payments**: Logs payment records, ensuring accurate tracking of subscription renewals.  

---

## **Key Features**  

### **RESTful API**
- A fully functional REST API for interaction with the database, built using Python Flask.

### **Data Modeling**
- Designed relational database tables with appropriate data types, constraints, and relationships.  

### **Database Automation**
- **Account Suspension**: Users with overdue payments for over 30 days are automatically suspended.  
- **Subscription Renewal**: Paid subscriptions are renewed automatically for the next cycle.  
- **Discount Calculation**: Discounts are calculated dynamically based on subscription duration.  

### **Data Integrity**
- Referential integrity is enforced through foreign key relationships, ensuring consistent and valid data across all tables.  

### **Ease of Use**
- Simple and intuitive API endpoints to interact with the system using tools like Postman.  

---

## **Technologies Used**  
- **Python Flask**: Backend API development.  
- **MySQL**: Database management.  
- **Postman**: API testing and interaction.  

---

## **Project Setup**  

### **Database Setup**  
1. Install MySQL Server.  
2. Create a database named `empdb`.  
3. Execute the provided SQL scripts to create tables, insert sample data, and implement triggers/functions.  

### **API Setup**  
1. Install Python (3.x recommended).  
2. Install required Python libraries:  
   ```bash
   pip install flask mysql-connector-python
   ```
3. Clone the repository and navigate to the project directory.  
4. Run the Flask application:  
   ```bash
   python api.py
   ```

---

## **How to Use the API**  

### **Endpoints**  

#### **Users**
- `GET /users`: Retrieve all users.  
- `POST /users`: Add a new user (requires JSON input).  

#### **Subscriptions**
- `GET /subscriptions/<user_id>`: Retrieve subscriptions for a specific user.  

#### **Payments**
- `GET /payments`: Retrieve all payments.  
- `POST /payments`: Add a new payment (requires JSON input).  

#### **Discount Calculation**
- `GET /users/<user_id>/discount`: Calculate discount for a user.  

---


## **Guidance**  
This project was created under the guidance of **Sir Aniruddh Gaikwad**.  
```
