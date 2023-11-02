class Project:
    def __init__(self, name, description, licence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = licence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_details(self, details):
        return "\n- ".join(details) if len(details) > 0 else ""

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n- {self._stringify_details(self.authors)}"
            f"\n\nDependencies:\n- {self._stringify_details(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n- {self._stringify_details(self.dev_dependencies)}"
        )
