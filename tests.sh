#!/bin/bash

docker build -t t_image .

docker run --name t_container t_image # pytest --browser chrome -n 3

docker cp t_container:/app/allure-results .

allure serve allure-results

docker rm t_container

# docker run --name t_container t_image && docker cp t_container:/app/allure-results . && allure serve allure-results
# docker run --name t_container t_image; docker cp t_container:/app/allure-results .; allure serve allure-results