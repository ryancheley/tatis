from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.generic.os import Ubuntu
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.client import Users
from diagrams.onprem.network import Gunicorn, Nginx
from diagrams.onprem.vcs import Github
from diagrams.programming.framework import Django

with Diagram("./custom_resources/Workflow", direction="TB"):
    with Cluster("Local"):
        # local_development = Custom("macOS", "https://download.logo.wine/logo/MacOS/MacOS-Logo.wine.png")
        local_development = Custom("", "MacOS-Logo.png")
    with Cluster("GitHub"):
        github_actions = GithubActions("GitHub Actions")
        github = Github("GitHub")
        local_development >> github >> github_actions
    with Cluster("Digital Ocean", direction="LR"):
        server = Ubuntu("Ubuntu 18.04")
        github_actions >> server

with Diagram("./custom_resources/Internal Working"):
    with Cluster("Internet"):
        users = Users("Site Visitors")

    with Cluster("Digital Ocean", direction="LR"):
        server = Ubuntu("Ubuntu 18.04")
        nginx = Nginx("Nginx")
        static_assets = Custom("Static", "static.png")
        with Cluster("Gunicorn Workers", direction="LR"):
            worker1 = Gunicorn("worker1")
            worker2 = Gunicorn("worker2")
            worker3 = Gunicorn("worker3")
            workers = [worker3, worker2, worker1]
        with Cluster("Django Stack", direction="LR"):
            django_app = Django("Django")
            sqlite = Custom("SQLite", "SQLite.svg")

        django_app - sqlite
        workers - django_app
        nginx - workers
        static_assets - nginx
        users << Edge(color="Orange") << nginx
        users >> Edge(color="#007500") >> nginx
