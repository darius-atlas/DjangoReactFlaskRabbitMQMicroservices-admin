# Run
1. docker-compose up

# Open docker cmd
1. docker-compose exec backend sh

backend - is nme of docker continer in .yml<br>

#Migrate DB
1. docker-compose up
2. docker-compose exec backend sh
3. python manage.py makemigrations