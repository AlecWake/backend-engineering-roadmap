# FastAPI Basics (Week 5)

## Overview

This project is my first FastAPI application. It demonstrates how to build basic API endpoints using Python.

## Features

* GET endpoints
* Path parameters
* Query parameters
* Basic filtering
* Error handling (404 responses)

## Endpoints

### GET /

Returns a simple welcome message.

### GET /tasks

Returns all tasks.

### GET /tasks/{task_id}

Returns a specific task by ID.

### GET /tasks/search

Filters tasks using query parameters:

* completed (true/false)
* title (substring search)

## How to Run

1. Activate virtual environment:

```
venv\Scripts\activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run server:

```
uvicorn main:app --reload
```

4. Open in browser:

```
http://127.0.0.1:8000/docs
```

## Notes

* Data is stored in-memory (not a database)
* This is a learning project for backend fundamentals