from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_content = toml.loads(content)
        project_name = parsed_content["tool"]["poetry"]["name"]
        description = parsed_content["tool"]["poetry"]["description"]
        # licence on optional, joten se voi puuttua. Käytetään sanaa licence, koska license on varattu Pythonissa
        licence = None
        try:
            licence = parsed_content["tool"]["poetry"]["license"]
        except KeyError:
            pass
        authors = parsed_content["tool"]["poetry"]["authors"]
        dependencies = []
        for name, version in parsed_content["tool"]["poetry"]["dependencies"].items():
            dependencies.append(name)
        dev_dependencies = []
        # dev-dependencies on optional, joten se voi puuttua
        try:
            for name, version in parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"].items():
                dev_dependencies.append(name)
        except KeyError:
            pass

        return Project(project_name, description, licence, authors, dependencies, dev_dependencies)
