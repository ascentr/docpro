# WorkTrack – Demo Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

Lightweight project tracking software for building firms with GPS-verified photo uploads.  


[![Live Demo](https://img.shields.io/badge/demo-live-green)](https://demoapp01.pythonanywhere.com/)

---

## Overview

**WorkTrack** is a demonstration project designed for building and renovation firms to track progress on-site.

The system allows contractors to create projects and add individual tasks.
In this demo scenario, tasks represent **rooms within a property that are being renovated**.

Each task can include an uploaded image which is automatically processed to add verification data such as timestamps and GPS location information.

This provides a simple way to **document work progress and confirm when and where images were taken**.
See demo on 

---

## Features

* Create and manage renovation or construction projects
* Add tasks to projects (e.g., individual rooms)
* Upload photos for each task
* Automatic **timestamping of uploaded images**
* **GPS metadata extraction**
* GPS data written directly onto the image
* Simple responsive interface using Bootstrap
* Lightweight demo database using SQLite

---

## How It Works

1. A project is created for a building or renovation job.
2. Tasks (rooms) are added to the project.
3. Photos can be uploaded to document progress.
4. When an image is uploaded the system automatically:

   * Applies a **date and time stamp**
   * Extracts **GPS metadata**
   * Writes the GPS data onto the image

This helps provide **basic authenticity verification** for site photos.

---

## Tech Stack

### Backend

* Python 3.10
* Django 4.2
* SQLite (demo database)

### Frontend

* HTML
* JavaScript
* Bootstrap 5

---

## Quick Start

Clone the repository

```bash
git clone https://github.com/ascentr/docpro.git
cd docpro
```

Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start the development server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

---

## Screenshots

Screenshots of the interface will be added here.

Example sections:

```
screenshots/
 ├ dashboard.png
 ├ project_view.png
 └ photo_upload.png
```

---

## Notes

* SQLite is used for simplicity in the demo environment.
* In a production environment a database such as **PostgreSQL** would typically be used.
* This project is intended as a **proof-of-concept demonstration** rather than a full production system.

---

## License

This project is released for demonstration and educational purposes.
