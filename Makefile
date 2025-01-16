run-webui:
	docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

update-webui:
	docker stop open-webui
	docker rm open-webui
	make run-webui