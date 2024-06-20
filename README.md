# Inventory Management System

This repository contains an Inventory Management System implemented in Python, designed to manage various types of devices and products.

## Overview

The system is structured around a superclass `Device` with subclasses for different product types such as `Phone`, `Laptop`, and `Desktop`. It provides CRUD (Create, Read, Update, Delete) functionalities to manage inventory items efficiently.

## Features

- **Device Class:** Defines the basic attributes and methods common to all devices.
- **Product Classes:** Subclasses like `Phone`, `Laptop`, and `Desktop` inherit from `Device` and add specific attributes.
- **CRUD Operations:** Allows users to:
  - Create new devices or products.
  - Read details of existing items.
  - Update information such as price, quantity, etc.
  - Delete items from the inventory.

## Folder Structure
The repository is organized as follows:
inventory-management/
│
├── README.md
├── device.py # Contains the Device superclass
├── phone.py # Contains the Phone subclass
├── laptop.py # Contains the Laptop subclass
├── desktop.py # Contains the Desktop subclass
├── inventory_manager.py # Main script for CRUD operations
└── requirements.txt # Dependencies required for the project

## Getting Started

To use this system, follow these steps:

1. Clone the repository:
   git clone https://github.com/ehiremengold/inventory-management.git
2. Install dependencies:
   pip install -r requirements.txt
3. run ### python manage.py runserver to interact  with the inventory system.
