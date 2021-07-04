#!/bin/bash

docker build -t t_image .

docker run --name t_container t_image pytest --browser chrome -n 4

docker cp t_container:/app/allure-report .

allure serve allure-report

docker rm t_container

# docker run --name t_launch t_image && docker cp t_launch:/app/allure-report . && allure serve allure-report
