Set:

```
SIMEX_VERSION=0.4
REPO_URL=sipecam/simex
DIR=/home/<user>/<midir>/sipecam-metadata-extractor/ #path where this git repository is cloned, example: /home/user/sipecam-metadata-extractor
BUILD_DIR=$DIR/dockerfiles/$JUPYTERLAB_VERSION
CONTAINER_NAME=sipecam-simex
```

Clone:

```
git clone https://github.com/CONABIO/sipecam-metadata-extractor.git $DIR
```

Build:

```
docker build $BUILD_DIR --force-rm -t $REPO_URL:$JUPYTERLAB_VERSION
```
