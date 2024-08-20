# Python Services Backend

Backend Micro Services for built with: AWS, Terraform, FastAPI, and Python.

## Key Components
- **Infrastructure as Code**: Terraform `infrastructure/`.
- **Microservices**: Source code located in `services/<service-name>`. 
- **Shared Libraries**: Models, schemas, utilities. Source code located in `services/shared/`.
- **CI/CD Pipeline**: Defined in `.github/workflows/`.
- **Development Tools**: Taskfile, Docker, Terraform, Cursor IDE / Pycharm IDE

## Repo Structure
```commandline
/
├── services/
│   ├── service_1_ecs/
│   ├── service_2_lambda/
│   └── service_3_lambda/
├── shared/
│   ├── shared_lib/
│   │   ├── models/
│   │   └── utilities/
│   └── ...
├── infrastructure/
│   ├── main/
│   ├── shared/
│   └── ...
└── .github/
    ├── workflows/
    └── ...
```

## Development Setup
### Pre-requirements
1. [Cursor IDE](https://www.cursor.com/) or [Pycharm IDE](https://www.jetbrains.com/pycharm/): Development IDEs
2. [Pyenv](https://github.com/pyenv/pyenv-installer) & pyenv-virtualenv
3. [Python 3.12+ Installed with Pyenv](https://www.python.org/)
4. [Taskfile](https://taskfile.dev/): Improved version of Makefile
5. [Docker](https://www.docker.com/): Containers
6. [Terraform](https://www.terraform.io/): Infrastructure as Code

### 1. Install Virtual Environments
Service-specific Virtual Environment
(For each service) 
```bash
cd services/<service_name>
task pyenv-create
pyenv activate <service_name>
task pyenv-setup
```

### 2. Setup Terraform (Main)
#### 2.a Create Terraform variable files
1. Create `terraform.tfvars` in `infrastructure/main` directory
2. Add the variables following the `terraform.tfvars.template` file
3. Create `backend.tfvars` in `infrastructure/main` directory
4. Add the variables following the `backend.tfvars.template` file

#### 2.b Initialize Terraform
```bash
cd infrastructure/main
task terraform-init
```

#### 2.c Test Creating a Terraform Plan
```bash
task terraform-plan
```