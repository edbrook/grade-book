import yaml

class Settings:
    def __init__(self, initial_settings):
        self.settings = initial_settings
    
    def update_from_config(self, filename):
        with open(filename, 'r') as config:
            data = yaml.safe_load(config)
        
        settings = {}
        settings.update(data)

        for key, value in settings.items():
            key = key.lower()

            if key not in self.settings:
                continue
            
            self.settings[key] = value
    
    def __getitem__(self, key):
        return self.settings[key]
    
    def __getattr__(self, key):
        try:
            return self.settings[key]
        except KeyError as err:
            # __getattr__ should raise AttributeError not KeyError
            raise AttributeError(err)
    
    def __repr__(self):
        settings_brief = ', '.join([f"{key}:..." for key in self.settings])
        return f"Settings({{{settings_brief}}})"


settings = Settings({
    "bind_address": "0.0.0.0",
    "port": 8080,
    "database": None,
    "cookie_secret": "SECRET_KEY"
})