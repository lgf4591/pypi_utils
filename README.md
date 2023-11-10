# pypi-template
a template for build python package to upload pypi repository


```bash

ppoetry install
poetry run dev

```


## publish


```bash

change pyproject.toml file   --    version = "0.1.5"

git add .
git commit -m "change readme"
git tag v0.1.5 -m "release v0.1.5"
git push origin v0.1.5


```