# Pythonのキャッシュを全て削除する
.PHONY: it-build
TAG ?= latest
it-build:
	DOCKER_BUILDKIT=1 docker build . -f build/python3.8/Dockerfile -t python3.8:latest
	DOCKER_BUILDKIT=1 docker build . -f build/python3.12/Dockerfile -t python3.12:latest