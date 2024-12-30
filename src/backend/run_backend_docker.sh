# For Macos
# sudo xhost local:root

docker run --rm  -it -v $PWD:/app \
-e LC_ALL=C.UTF-8 \
-e LANG=C.UTF-8 \
-p 8080:8080 \
--network lawbot_bridge \
--name backend \
backend:v0 serve