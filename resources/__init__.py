application_properties_files = ['application.properties', 'application-hml.properties', 'application-dev.properties', 'application-prd.properties']
application_properties_regex = r"(?P<name>.*?)\s*=\s*(https?://)(?P<url_text>.*)"

feign_folder_regex = r".*/feign/.*\.java"
feign_url_regex = r"url\s*=\s*(?P<url_text>.*?)(?:,|\))"

bootstrap_regex = r"name\s*:\s*(?P<integrations>.*)"

ignored_files = ['.gitignore', 'README.md', 'Dockerfile', 'Jenkinsfile', 'pom.xml']

fernanda_acronyns = ['acad', 'apio', 'cdps', 'ctas', 'fepw', 'parc', 'rtto', 'tbgr', 'trfo', 'atmo', 'gcen', 'mcsv', 'ctasm']