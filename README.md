# 🐾 Pawfect Paws Grooming System

**Pawfect Paws Grooming System** is a web-based application built using **Python Django** that allows pet owners to conveniently book grooming services online, manage pet profiles, and track appointment history. Groomers and administrators can manage services, customer details, payments, and schedules through a user-friendly dashboard.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Modules](#modules)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

---

## 🐶 Overview

The **Pawfect Paws Grooming System** simplifies pet grooming appointments by providing a digital platform for:
- Pet owners to book grooming services online.
- Groomers to manage bookings, customers, and service packages.
- Admins to oversee the entire system, including payments, reviews, and schedules.

This system ensures smooth communication between pet owners and service providers while reducing manual scheduling and record-keeping.

---

## ✨ Features

### 🧍‍♂️ For Customers:
- Register and log in securely.
- Add and manage pet profiles.
- Browse available grooming services.
- Book appointments for pets.
- View appointment history and status.
- Make payments online (Razorpay integration).
- Submit reviews and feedback.

### 🧑‍🔧 For Groomers/Admin:
- Manage grooming services and pricing.
- View and confirm/cancel customer bookings.
- Manage customers and pet records.
- Dashboard for upcoming appointments and statistics.
- Generate reports on services and revenue.

---

## 💻 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap |
| **Backend** | Python 3.x, Django 5.x |
| **Database** | SQLite / MySQL |
| **Payment Gateway** | Razorpay (Optional) |
| **Authentication** | Django Authentication System |
| **Version Control** | Git & GitHub |

---

## 🧩 Modules

1. **User Authentication Module**
   - Login, Register, Logout (with role-based access)

2. **Pet Profile Management**
   - Add, edit, and delete pet details (name, breed, age, etc.)

3. **Service Management**
   - CRUD operations for grooming services and packages

4. **Appointment Booking**
   - Real-time appointment scheduling with confirmation

5. **Payment Integration**
   - Secure Razorpay payment gateway for service bookings

6. **Admin Dashboard**
   - Overview of all activities, bookings, and payments

---

## ⚙️ Installation Guide

### 🪜 Prerequisites
Make sure you have installed:
- Python (≥ 3.9)
- pip (Python package installer)
- Virtual environment (optional but recommended)
- Git (for version control)

### 🧠 Steps
```bash
# 1. Clone the repository
git clone https://github.com/your-username/pawfect-paws-grooming.git

# 2. Navigate to project directory
cd pawfect-paws-grooming

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create superuser (Admin)
python manage.py createsuperuser

# 8. Run the server
python manage.py runserver
