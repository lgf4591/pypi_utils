# pypi-template
a template for build python package to upload pypi repository


```bash

ppoetry install
poetry run dev

```


## publish

change pyproject.toml file   --    version = "0.1.0"
change pypi_utils/__init__.py  --    version = "0.1.0"

```bash

version=0.1.0
git add .
git commit -m "release v${version}"
git tag v${version} -m "release v${version}"
git push origin v${version}


```

```powershell

$version="0.1.0"
git add .
git commit -m "release v$version"
git tag v$version -m "release v$version"
git push origin v$version

```