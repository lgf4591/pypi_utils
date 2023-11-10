from urllib.request import Request, urlopen
import requests


class Github:
    gh_proxies = [
        "https://gh.h233.eu.org/", "https://gh.ddlc.top/",
        "https://ghdl.feizhuqwq.cf/", "https://slink.ltd/",
        "https://git.xfj0.cn/", "https://gh.con.sh/", "https://ghps.cc/",
        "https://hub.gitmirror.com/", "https://ghproxy.com/"
    ]
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
    }

    # name = NotImplementedError
    def __init__(self,
                 repo: str = "MatsuriDayo/nekoray",
                 version: str = "latest") -> None:
        self.__repo = repo
        self.__version = version

    def __str__(self) -> str:
        return "you are use pypi_github_helper module now!!"

    def __repr__(self) -> str:
        return "you are use pypi_github_helper module now!!"

    @property
    def release_info(self) -> None | dict:
        release_info = None
        if self.__version == "latest":
            url = f"https://api.github.com/repos/{self.__repo}/releases/latest"
        else:
            url = f"https://api.github.com/repos/{self.__repo}/releases/tags/{self.__version}"
        response = requests.get(url=url, timeout=60)
        if response.status_code == 200:
            release_info = response.json()
        return release_info

    @property
    def latest_version(self) -> None | str:
        latest_release_version = None
        url = f"https://api.github.com/repos/{self.__repo}/releases/latest"
        response = requests.get(url=url, timeout=60)
        if response.status_code == 200:
            release_info = response.json()
            latest_release_version = release_info["tag_name"]
        return latest_release_version

    @property
    def download_urls(self) -> None | list[str]:
        download_urls = None
        if self.release_info:
            release_assets = self.release_info["assets"]
            download_urls = [
                asset["browser_download_url"] for asset in release_assets
            ]
        return download_urls

    @property
    def proxy_download_urls(self) -> None | list[str]:
        proxy_download_urls = None
        if len(self.download_urls) > 0:
            for proxy in self.gh_proxies:
                url = proxy + self.download_urls[0]
                # print(url)
                req = Request(url=url, headers=self.headers)
                res = urlopen(req, timeout=60)
                if res.status == 200:
                    print(f"current proxy is {proxy}, it works well")
                    proxy_download_urls = [(proxy + url)
                                           for url in self.download_urls]
                    break
        return proxy_download_urls


if __name__ == "__main__":
    print(Github.gh_proxies)
    # github = Github("MatsuriDayo/nekoray")
    github = Github("MatsuriDayo/nekoray", "3.23")
    print(github)
    print(github.latest_version)
    # print(github.release_info)
    print(github.download_urls)
    print(github.proxy_download_urls)
    # https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-windows64.zip
    # https://github.com/MatsuriDayo/nekoray/releases/download/3.23/nekoray-3.23-2023-10-14-windows64.zip
