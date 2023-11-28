up:
	docker compose up -d db
	docker compose up -d web
down:
	docker compose down
rebuild:
	docker compose up -d --build db
	docker compose up -d --build web
db:
	docker compose up -d db
web:
	docker compose up -d web