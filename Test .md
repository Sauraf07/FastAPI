# School Management System (Terminal Based)

## Project Overview

The School Management System is a terminal-based application developed using Python, MySQL, SQLAlchemy ORM, Alembic, and AsyncIO.

The purpose of this project is to manage students, teachers, classes, subjects, attendance, and marks while demonstrating real-world database relationships.

The main focus of the project is to showcase:

* CRUD Operations
* SQLAlchemy ORM
* Alembic Migrations
* Async Database Operations
* One-to-Many Relationships
* Many-to-Many Relationships
* Layered Architecture (DAO + Service Layer)
* Menu-Driven Terminal Application

---

# System Modules

## 1. Student Management

### Responsibilities

Manage student records.

### Operations

* Add Student
* View All Students
* Search Student
* Update Student Details
* Delete Student

### Student Attributes

| Field        | Description       |
| ------------ | ----------------- |
| id           | Unique Student ID |
| name         | Student Name      |
| age          | Student Age       |
| gender       | Student Gender    |
| email        | Student Email     |
| phone        | Contact Number    |
| classroom_id | Assigned Class    |

---

## 2. Teacher Management

### Responsibilities

Manage teacher information.

### Operations

* Add Teacher
* View Teachers
* Search Teacher
* Update Teacher
* Delete Teacher

### Teacher Attributes

| Field         | Description               |
| ------------- | ------------------------- |
| id            | Unique Teacher ID         |
| name          | Teacher Name              |
| email         | Email Address             |
| phone         | Contact Number            |
| qualification | Educational Qualification |
| experience    | Years of Experience       |

---

## 3. Subject Management

### Responsibilities

Manage school subjects.

### Operations

* Add Subject
* View Subjects
* Update Subject
* Delete Subject

### Subject Attributes

| Field | Description  |
| ----- | ------------ |
| id    | Subject ID   |
| name  | Subject Name |
| code  | Subject Code |

Examples:

* Mathematics
* Science
* English
* Hindi
* Computer Science

---

## 4. Classroom Management

### Responsibilities

Manage school classes.

### Operations

* Add Classroom
* View Classroom
* Update Classroom
* Delete Classroom

### Classroom Attributes

| Field       | Description          |
| ----------- | -------------------- |
| id          | Classroom ID         |
| class_name  | Example: 10-A        |
| room_number | Physical Room Number |

Examples:

* Class 8-A
* Class 9-B
* Class 10-A

---

# Relationships

## Relationship 1

### Classroom → Students

One Classroom can have many Students.

Example:

Class 10-A

* Rahul
* Priya
* Aman

Relationship Type:

One-to-Many

---

## Relationship 2

### Teacher → Subject

One Teacher teaches one Subject.

Example:

Mr. Sharma → Mathematics

Relationship Type:

One-to-Many

---

## Relationship 3

### Student ↔ Teacher

A student can be taught by multiple teachers.

A teacher can teach multiple students.

Example:

Rahul

* Mathematics → Mr. Sharma
* Science → Mrs. Gupta
* English → Mr. Verma

Relationship Type:

Many-to-Many

Association Table:

StudentTeacher

---

## Relationship 4

### Subject ↔ Teacher

Multiple teachers may teach different subjects.

Relationship Type:

One-to-Many

---

# Attendance Module

## Purpose

Track daily attendance.

### Operations

* Mark Attendance
* View Attendance
* Update Attendance
* Attendance Report

### Attendance Fields

| Field      | Description     |
| ---------- | --------------- |
| id         | Attendance ID   |
| student_id | Student         |
| date       | Attendance Date |
| status     | Present/Absent  |

---

# Marks Module

## Purpose

Store examination marks.

### Operations

* Add Marks
* Update Marks
* Delete Marks
* View Student Report Card

### Marks Fields

| Field      | Description    |
| ---------- | -------------- |
| id         | Marks ID       |
| student_id | Student        |
| subject_id | Subject        |
| marks      | Obtained Marks |
| exam_type  | Midterm/Final  |

---

# Database Design

## Tables

### student

Stores student information.

### teacher

Stores teacher information.

### classroom

Stores class details.

### subject

Stores subject details.

### student_teacher

Stores Teacher-Student mapping.

### attendance

Stores attendance records.

### marks

Stores examination marks.

---

# Application Menus

## Main Menu

1. Student Management
2. Teacher Management
3. Subject Management
4. Classroom Management
5. Attendance Management
6. Marks Management
7. Relationship Management
8. Exit

---

# Student Menu

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Back

---

# Teacher Menu

1. Add Teacher
2. View Teachers
3. Search Teacher
4. Update Teacher
5. Delete Teacher
6. Back

---

# Subject Menu

1. Add Subject
2. View Subjects
3. Update Subject
4. Delete Subject
5. Back

---

# Attendance Menu

1. Mark Attendance
2. View Attendance
3. Attendance Report
4. Back

---

# Marks Menu

1. Add Marks
2. Update Marks
3. Delete Marks
4. View Report Card
5. Back

---

# Relationship Menu

1. Assign Teacher to Student
2. Remove Teacher from Student
3. View Student's Teachers
4. View Teacher's Students
5. Back

---

# Project Architecture

School Management System

├── config

├── models

├── dao

├── services

├── menus

├── utils

├── migrations

├── main.py

---

# DAO Layer Responsibilities

Responsible for:

* Database CRUD Operations
* Query Execution
* Data Retrieval

Examples:

* StudentDAO
* TeacherDAO
* SubjectDAO
* AttendanceDAO

---

# Service Layer Responsibilities

Responsible for:

* Business Logic
* Validation
* Calling DAO Methods
* Error Handling

Examples:

* StudentService
* TeacherService
* AttendanceService

---

# AsyncIO Usage

Async operations should be used for:

* Insert Student
* Insert Teacher
* Fetch Students
* Fetch Teachers
* Mark Attendance
* Generate Reports

Benefits:

* Faster Database Operations
* Better Scalability
* Non-blocking Execution

---

# Alembic Usage

Alembic will manage:

* Table Creation
* Schema Changes
* Version Control for Database

Examples:

* Create Student Table
* Add New Column
* Modify Existing Schema
* Rollback Migration

---

# Future Enhancements

* Login System
* Role Based Access
* Admin Module
* Fees Management
* Examination Module
* Timetable Management
* Library Management
* Export Reports to PDF
* Export Reports to Excel

---

# Learning Outcomes

After completing this project, you will gain experience in:

* Python
* MySQL
* SQLAlchemy ORM
* Alembic
* AsyncIO
* CRUD Operations
* Database Relationships
* Layered Architecture
* Terminal Based Application Development

This project is suitable for a fresher Python Developer portfolio and demonstrates practical backend development skills.
