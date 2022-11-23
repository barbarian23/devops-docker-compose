### DOCKER
1. To remove docker that created more than n hours, use command
    ```
    docker image prune -a --force --filter "until=168h"
    ```
2. Limit docker log
    ```
    docker run --log-driver json-file --log-opt max-size=10m --log-opt max-file=3 image_name
    ```
### DOCKER-COMPOSE
1. To run docker compose as a daemon, use command:
    ```
    docker-compose up -d
    ```
2. Docker compose provide healcheck config, add healcheck to docker-compose.yml
    ```
    ```
3. Limit log file for a docker
    ```
    services:
      app:
        image: ...
        logging:
          options:
            max-size: "10m"
            max-file: "3"
    ```

### Kubernetes