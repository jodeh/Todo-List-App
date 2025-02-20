# Todo App with GitHub Actions Example

This project is a simple Todo web application built using **Python Flask** and **Docker**. It serves as an example to demonstrate how to automate the build and deployment process using **GitHub Actions**.


## GitHub Actions Workflow

The project includes a GitHub Actions workflow (`todo-workflow.yml`) that automates the following steps:

1. **Checkout Repository**:
   - Clones the repository to the runner.

2. **Login to Docker Hub**:
   - Authenticates with Docker Hub using secrets stored in GitHub.

3. **Set up QEMU**:
   - Configures QEMU for multi-architecture builds (if needed).

4. **Set up Docker Buildx**:
   - Configures Docker Buildx for advanced build capabilities.

5. **Build and Push Docker Image**:
   - Builds the Docker image and pushes it to Docker Hub with the tag `jodeh/todo-app:latest`.
