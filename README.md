# CI/CD Simulation with GitHub Actions

## Project Overview

### Description

The project is a simulation of a CI/CD pipeline with GitHub Actions. It implements a simple Streamlit app that is a prototype for a bot system.

## Problem Statement

As part of the Data Engineering track, a CI/CD exercise is proposed to test the integration and development capabilities of GitHub Actions.

## Objectives:

### Must-have Features

- CI workflow runs tests on pull requests → main.
- CD workflow deploys automatically:
  - To Dev on push to `dev` branch.
  - To QA on push to `qa` branch.
  - To Prod on push to `main` branch (with approval).
- Each deploy step outputs a log like:
  Deployed to 'environment'

### Nice-to-Have Features

- Add linting before build
- Using Actions secrets to manage environment variables

**IMPORTANT**:

```
 As the main objective was the CI/CD pipeline build, the chat in the app right now just echoes the question tha the user asks.
```

## Requirements and Tools

### Languages

- Python 3.10

### Libraries

- `pymupdf`
- `openai`
- `langchain`
  - `langchain_openai`
  - `langchain_community`

### Requirements

- Others listed in `requirements.txt`

## Module description

### `app` directory

#### `RAG_function.py`

Implements all the functionalities to process the RAG

#### `main.py`

Implements the streamlit app and other functionalities needed for the application (similar to the one described in [RAG Bot for Town Hall Meeting Records](https://github.com/hermstefanny/townhall-meetings-RAG-bot/blob/main/README.md))

## `tests` directory

### `test_unit.py`

Implements a unit test for the `get_pdf_paths` from `RAG_function.py` module

## `.github\workflows`

### `ci.yml`

Runs on pull requests to `main`.
Sets up Python, installs dependencies, lints the code with Ruff, and runs tests with pytest.
Ensures code quality before merging.

### `cd.yml`

Runs on pushes to `dev`, `qa`, or `main`.
Deploys automatically to Dev and QA environments.
Deploys to Prod only after manual approval in GitHub Environments.

## `data` directory

Contains the `raw-pdfs` with three example pdfs for RAG exercise

## Usage

- Clone the repository
- Create a virtual environment with and install the dependencies in `requirements.txt`
- For the streamlit app, run with `streamlit run app/main.py`

## Results

### CI results

![Screenshot of the CI tests](screenshots\CI-results.png "Screenshot of the CI tests")

![Screenshot of the CI sucessful test](screenshots\CI-sucess-result.png "Screenshot of the CI sucessful test")

- A branch `testing` was implemented to test the CI with pull requests
- Several attempts to merge were tried. Errors that prevented sucessful merger in the linting process and in testing were caught and solved

### CD results

#### Deploy to DEV

![Screenshot of the CD dev](screenshots\dev-deployment.png "Screenshot of the CD dev")

![Screenshot of the CD dev deployment messages](screenshots\dev-deployment-results.jpg "Screenshot of the CD dev deployment messages")

![Screenshot of the app in dev environment](screenshots\dev-app.png "Screenshot of the app in dev environment")

- When code is pushed to the dev branch, the CD workflow automatically deploys to the Dev environment.
- No manual approval is required, making it fast and iterative.
- The app shows the appropiate message and background color

#### Deploy to QA

![Screenshot of the CD qa](screenshots\qa-deployment.png "Screenshot of the CD qa")

![Screenshot of the CD qa deployment messages](screenshots\qa-deployment-results.png "Screenshot of the CD qa deployment messages")

![Screenshot of the app inqa environment](screenshots\qa-app.png "Screenshot of the app in qa environment")

- When code is pushed to the qa branch, the workflow deploys to the QA environment.
- This stage simulates a staging/testing setup where quality checks can be performed.
- Deployment happens automatically after the push.
- The app shows the appropiate message and background color

#### Deploy to PROD

![Screenshot of the CD prod](screenshots\prod-deployment-1.png "Screenshot of the CD prod")

![Screenshot of the CD prod - pending approval](screenshots\prod-results-2-pending.png "Screenshot of the CD prod - pending approval")

![Screenshot of the CD prod - approval](screenshots\prod-approval.png "Screenshot of the CD prod - approval")

![Screenshot of the CD prod results with approval](screenshots\prod-results-approval.png "Screenshot of the CD prod rseults with approval")

![Screenshot of the CD prod app](screenshots\prod-app.png "Screenshot of the CD prod app")

- When code is pushed to the main branch, the workflow targets the Prod environment.
- This step is protected with manual approval.
- GitHub Actions pauses and waits for a reviewer to approve the release.
- Once approved, deployment proceeds and final logs confirm success.

### Linting

- Linting is included in the CI workflow using Ruff.
- It enforces consistent code style and catches common errors automatically.

![Screenshot of CI with linting errors](screenshots\linting-errors.png "Screenshot of CI with linting errors")

### Secrets usage

- Sensitive values are stored in GitHub Secrets and Variables.
- In this case, OPENAI_API_KEY is kept as a secret and injected into the workflow when needed.

![Screenshot of Actions Variables in Github](screenshots\actions-secrets-var.png "Screenshot of Actions Variables in Github")
