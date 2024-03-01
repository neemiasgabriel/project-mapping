import re

regex = r"(?P<filename>(?!(?:acad|apio|cdps|ctas|fepw|parc|rtto|tbgr|trfo|atmo|gcen|mcsv|ctasm)-)\w+)(?<!corp).properties"
examples = ["fwms-corp.properties", "fwms-integration.properties", "acad-corp.properties", "acad-integration.properties"]
allowed_names = ["acad", "apio", "cdps", "ctas", "fepw", "parc", "rtto", "tbgr", "trfo", "atmo", "gcen", "mcsv", "ctasm"]

for filename in examples:
    match = re.search(regex, filename)
    if match:
        print(f"Valid filename: {match.group('filename')}")
    else:
        print(f"Excluded filename: {filename}")
