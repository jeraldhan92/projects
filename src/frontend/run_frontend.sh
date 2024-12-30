docker run --rm --env-file .env -p 8501:8501 --network lawbot_bridge \
--name frontend \
-v $PWD/src/frontend:/app frontend:v0