import yaml
import pathlib
import shutil

class ConfigManager(object):
    def __init__(self):
        home_directory = pathlib.Path.home()
        self._path = pathlib.Path.joinpath(home_directory, "ZFTunesConfigs")
        exists = self._path.exists()
        self._path.mkdir(exist_ok=True)
        # Copy over the default files if they don't exist
        if not exists:
            cwd = pathlib.Path.cwd()
            config_dir = cwd.joinpath('configs')
            if not config_dir.exists():
                raise RuntimeError(f"Failed to create default configuration files, '{str(config_dir)}' missing!")
            for fname in config_dir.glob('*.yaml'):
                shutil.copy(fname, self._path)
                print(fname)


    @property
    def path(self):
        return self._path

    def list(self):
        files = []
        for file in self._path.iterdir():
            if file.is_file() and file.name.endswith('.yaml'):
                files.append(file)
        return files

    def exists(self, name):
        for config in self.list():
            if name == config.name:
                return True
        return False

    def load(self, fname):
        if not self.exists(fname):
            raise FileNotFoundError(fname)
        fname = pathlib.Path.joinpath(self._path, fname)
        with open(fname, 'r') as f:
            return yaml.safe_load(f.read())
