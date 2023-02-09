# Case Task for Skatteetaten

API for Social Security Numbers.

## Installation

Install by either pulling from Docker or cloning.

### Docker

Pull the file from Dockerhub by running:

```bash
docker pull matiasvian/snn_api:latest
```

and run it using: 

```bash
docker run --name snn_api --publish 8000:8000 matiasvian/snn_api:latest 
```

### Git

Clone repository:

```bash
git clone https://github.com/matiasvian/snn_api.git 
```

CD to **app folder**, and run API with command:

```bash
uvicorn SNN_api:app --host=0.0.0.0 --port=8000
```
## Test

Run tests by opening a new terminal window and running. This can either be done locally after cloning the repository or within the docker terminal in a runnning container.
```bash
python3 SNN_tests.py
