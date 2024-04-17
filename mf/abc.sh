```bash
pushd dev

pushd kind
    ./create-cluster.sh
popd

export IPD_NS=local-hack

./deploy.sh \
  --set "ingress.path=/${IPD_NS}(/|$)(.*)" \
  --set runner.replicas=0 \
  --set setupJob.enabled=false \
  --set restoreJob.enabled=true \
  --set "matchserver.openai.apikey=nope"
```
