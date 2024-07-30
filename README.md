# Docker-Testing Project

Implemented in order to showcase my knowledge in Docker and Testing

## Project Structure and Architecture

This project is composed of two Docker services managed by `docker-compose.yml`:

- **app**: This service is defined in `Dockerfile.task` and is responsible for handling the main tasks of the application.
- **test**: This service is defined in `Dockerfile.test` and is used for running tests over the main app task.

### Directory Structure
Project/ \
├── app.py \
├── orders.csv \
├── unit_testing.py \
├── testing/ \
│   ├── test1.csv \
│   ├── test2.csv \
│   ├── test3.csv \
│   ├── test4.csv \
│   ├── test5.csv \
│   └── test_cases.py \
├── requirements.txt \
├── Dockerfile.task \
├── Dockerfile.test \
└──  docker-compose.yml
- **app.py** : Consists of the Program and functions that are required compute the output of given tasks
- **orders.csv** : This is the sample data taken while building the app.py
- **unit_testing.py** : Contains Program to test the functions in app.py with various sample datasets present in testing folder.
- **testing/** : Contains Various files that are required for testing
- **test1.csv, test2.csv ... test5.csv** : These are the datasets that were used by unit_testing.py
- **test_cases.py** : Contains the desired/ required output of these tests. used by unit_testing to validate the provided output of functions of app.py
- **requirements.txt** : Used to store names of libraries used. Useful to install all libraries in one go
- **Dockerfile.task** : Contains script to create docker container for app.py tasks
- **Dockerfile.test** : Contains script to create docker container for unit_testing.py's testing
- **docker-compose.yml** : This defines the services used in the project namely - app (Dockerfile.task) and test (Dockerfile.test).

### Architecture
![microservice](https://github.com/user-attachments/assets/32b9542c-a0ce-44d2-8a26-9ae67861baf7)

This project employs microservices architecture to separate concers and improve maintainability. The application is divided into two primary Dockerized services 
- **app**: Consists of the core logic for processing data from ```orders.csv``` and produces calculated results based on the defined functions
- **test**: Focuses on validating the task's (app's) behaviour on various other test datasets. Validates these outputs against the expected output present in ```test_cases.py```

The ```docker-compose.yml``` file orchestrates the interaction between these services ensuring proper dependencies and resource allocation 

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup Instructions

### Step 1: Clone the repository

```sh
git clone https://github.com/chanakya-ex3/TestingProject.git
cd TestingProject
```
### Step 2: Build the Docker Images
```sh
docker-compose build
```
### Step 3: To Run Task Service
```sh
docker-compose up app
```
### Step 4: To Run Tests over the Task
```sh
docker-compose up test
```
## Additionally
### Step 5: In order to stop the Services
```sh
docker-compose down
```

Contact
If you have any questions, feel free to contact me at [chanakya.exe@gmail.com]. Discord - ```chanakya_bm```
