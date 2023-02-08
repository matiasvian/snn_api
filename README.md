# Case Task for Skatteetaten

API for Social Security Numbers.

## Installation

Install by either pulling from Docker or cloning.

### Docker

Pull the file from Dockerhub by running.

```bash
docker pull 
```

### Git

Clone repository:

```bash
git clone  
```

CD to **app folder**, and run API with command:

```bash
uvicorn SNN_api:app --host=0.0.0.0 --port=8000
```
## Test

Run tests by opening a new terminal window and running
```bash
python3 SNN_tests.py