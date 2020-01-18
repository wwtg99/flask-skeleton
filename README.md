Flask Skeleton Project
======================

# Description

Place all your apis in `app` directory.

Add config to object in `config.config`.

# Usage

Run in dev mode

```
python run.sh
```

Run in production mode

```
gunicorn -b 0.0.0.0:80 server:app
```

Run in Docker

Use `Dockerfile` to build docker image and run.

```
docker build -t <image>:<tag> .
docker run -d -p 80:80 <image>:<tag>
```

