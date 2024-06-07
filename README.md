# FastAPI CRUD with InfluxDB

This is a simple FastAPI application demonstrating CRUD (Create, Read, Update, Delete) operations with an InfluxDB database. The application uses object-oriented programming principles for better organization and separation of concerns.

## Project Structure

The project is organized as follows:

- main.py: This file initializes the FastAPI application and includes the API routes.
- routes/: This directory contains the API route definitions.
  - data_routes.py: This file defines the routes for CRUD operations on data.
- crud/: This directory contains the CRUD functions.
  - data_crud.py: This file contains functions for performing CRUD operations on data.
- db/: This directory contains the database connection setup.
  - db_connection.py: This file establishes a connection to the InfluxDB instance.

## Setup and Installation

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```