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

sed -i"s#A#B#g" *.txt


version="0.1.0"
sed -i -e "s/__version__ = .*/__version__ = '${version}'/g"
python main.py ${version}
git add .
git commit -m "release v${version}"
git tag v${version} -m "release v${version}"
git push origin v${version}


```

```powershell

$version="0.1.5"
((Get-Content -Path ./pypi_utils/__init__.py) -replace "__version__ = .*","__version__ = '$version'") | Set-Content -Path ./pypi_utils/__init__.py
python main.py $version
git add .
git commit -m "release v$version"
git tag v$version -m "release v$version"
git push origin v$version

```