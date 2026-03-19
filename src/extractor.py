import re


def extract_skills(text):
    skills_map = {
        # Programming Languages
        "python": [r"\bpython\b", r"\bdjango\b", r"\bflask\b", r"\bpandas\b", r"\bnumpy\b"],
        "java": [r"\bjava\b", r"\bspring\b", r"\bspring boot\b"],
        "javascript": [r"\bjavascript\b", r"\bjs\b", r"\bnode\.js\b", r"\breact\b", r"\bvue\b", r"\bangular\b"],
        "c++": [r"\bc\+\+\b", r"\bcpp\b"],
        "c#": [r"\bc#\b", r"\b\.net\b", r"\basp\.net\b"],
        "php": [r"\bphp\b", r"\blaravel\b"],
        "ruby": [r"\bruby\b", r"\brails\b"],
        "go": [r"\bgolang\b", r"\bgo\b"],
        "typescript": [r"\btypescript\b", r"\bts\b"],

        # Frontend
        "html/css": [r"\bhtml\b", r"\bcss\b", r"\bsass\b", r"\bscss\b", r"\bbootstrap\b", r"\btailwind\b"],

        # Databases
        "sql": [r"\bsql\b", r"\bmysql\b", r"\bpostgres\b", r"\bsqlite\b", r"\bmssql\b"],
        "nosql": [r"\bmongodb\b", r"\bredis\b", r"\bfirebase\b", r"\bcassandra\b"],

        # DevOps / Tools
        "git": [r"\bgit\b", r"\bgithub\b", r"\bgitlab\b"],
        "docker": [r"\bdocker\b", r"\bcontainer\b"],
        "kubernetes": [r"\bkubernetes\b", r"\bk8s\b"],
        "ci/cd": [r"\bci/cd\b", r"\bjenkins\b", r"\bgithub actions\b", r"\bgitlab ci\b"],

        # Cloud
        "aws": [r"\baws\b", r"\bamazon web services\b"],
        "azure": [r"\bazure\b", r"\bmicrosoft azure\b"],
        "gcp": [r"\bgcp\b", r"\bgoogle cloud\b"],

        # Data / AI
        "machine learning": [r"\bmachine learning\b", r"\bml\b", r"\btensorflow\b", r"\bpytorch\b", r"\bscikit-learn\b"],
        "data analysis": [r"\bdata analysis\b", r"\bdata analytics\b", r"\bexcel\b", r"\bpower bi\b", r"\btableau\b"],

        # Other
        "api development": [r"\bapi\b", r"\brest api\b", r"\bgraphql\b"],
        "testing": [r"\btesting\b", r"\bunit test\b", r"\bpytest\b", r"\bjest\b"],
    }

    found_skills = {}

    for skill, patterns in skills_map.items():
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text)
            count += len(matches)

        if count > 0:
            found_skills[skill] = count

    return found_skills


def extract_availability(text):
    keywords = [
        "open to work",
        "available",
        "freelance",
        "hire me",
        "seeking opportunities",
        "looking for work",
        "open for projects",
        "contact me",
        "let's work together",
    ]

    return any(keyword in text for keyword in keywords)