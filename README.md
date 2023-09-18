# docker-tweet-gen

<!-- omit in toc -->
## Table of Contents

1. [Build the Image](#build-the-image)
1. [Run the Container](#build-the-container)
1. [Access via Browser](#access-via-browsers)

## Command Reference

### 1. Build the Image

```bash
docker build -t docker-tweet-gen .
```
You may require `sudo` access.

### 2. Run the Container

```bash
docker run -p 5001:3000 --rm --name tweet-gen-container docker-tweet-gen
```

### 3. Access via Browser

http://localhost:5001