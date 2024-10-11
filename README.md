# coding-trial
競技プログラミングやコーディングテスト用の実行環境です。

# usage
VSCodeのdevcontainerを使って、起動するコーディング環境を選択できます。
Dockerイメージは事前にビルドしておく必要があります。使用する環境を下記のコマンドでビルドしてください。

## build
### python3.8

```
DOCKER_BUILDKIT=1 docker build . -f build/python3.8/Dockerfile -t python3.8:latest
```

### python3.12

```
DOCKER_BUILDKIT=1 docker build . -f build/python3.12/Dockerfile -t python3.12:latest
```
