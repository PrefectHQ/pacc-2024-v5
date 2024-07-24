# 104 - Run your flows in the cloud and easily switch infrastructure with work pool-based deployments

## Agenda

- Create work pool-based deployments with .deploy()
- Flow code storage
- Hybrid work pools with workers

## Lab

- Create a Process work pool.
- Create and run a deployment with .deploy() that uses the work pool.
- Use flow code stored in your own GitHub repository with a deployment.
  - ❗️Push your code to GitHub manually.
- Pause and resume the work pool from the UI.
- Create a Process work pool from the UI
- Create a deployment that references flow code stored in GitHub

- Stretch 1: If you have Docker installed:
  - Created a deployment where you bake your flow code into a Docker image with .deploy().
  - Don’t push the image to a remote repository (or do log in and push it to DockerHub).

  - Don’t forget to:
    - Start Docker on your machine
    - `pip install -U prefect-docker`
    - Make a Docker work pool

- Stretch 2: add an environment variable to a work pool and use it.
