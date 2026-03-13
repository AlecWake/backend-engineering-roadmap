# Week 4 — HTTP and Git Fundamentals

## HTTP Basics

### What is an API
An API allows clients to communicate with a server by sending requests to defined endpoints.

### GET vs POST

GET  
Used to retrieve data from the server.

POST  
Used to create new data on the server.

---

## Common HTTP Status Codes

200 OK  
Request succeeded.

201 Created  
A resource was successfully created.

400 Bad Request  
The request was invalid.

401 Unauthorized  
User is not authenticated.

403 Forbidden  
User does not have permission.

404 Not Found  
The requested resource does not exist.

500 Internal Server Error  
The server encountered an error.

---

## JSON

APIs commonly send data using JSON.

Example:

{
  "name": "Alex",
  "age": 21
}

---

## Git Concepts Learned

git add  
Stages changes.

git commit  
Creates a snapshot of the staged changes.

git push  
Uploads commits to GitHub.

Branches allow developers to safely work on new features without breaking the main branch.