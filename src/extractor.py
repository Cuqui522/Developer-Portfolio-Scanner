import re

def extract_skills(text: str) -> dict[str, int]:
    """Scan text for known skill keywords and return a dict of skill name to mention count."""
    skills_map = {
        "python": [r"\bpython\b", r"\bdjango\b", r"\bflask\b", r"\bpandas\b", r"\bnumpy\b"],
        "java": [r"\bjava\b(?!script)", r"\bspring boot\b", r"\bspring\b"],
        "javascript": [r"\bjavascript\b", r"\bnode\.js\b", r"\breact\b", r"\bvue\.?js\b", r"\bangular\b"],
        "c++": [r"\bc\+\+\b", r"\bcpp\b"],
        "c#": [r"\bc#\b", r"\.net\b", r"\basp\.net\b"],
        "php": [r"\bphp\b", r"\blaravel\b"],
        "ruby": [r"\bruby\b", r"\brails\b", r"\bruby on rails\b"],
        "go": [r"\bgolang\b", r"\bgo programming\b", r"\bwritten in go\b"],  # "go" alone is too noisy
        "typescript": [r"\btypescript\b"],
        "html/css": [r"\bhtml5?\b", r"\bcss3?\b", r"\bsass\b", r"\bscss\b", r"\bbootstrap\b", r"\btailwind\b"],
        "sql": [r"\bsql\b", r"\bmysql\b", r"\bpostgres(?:ql)?\b", r"\bsqlite\b"],
        "nosql": [r"\bmongodb\b", r"\bredis\b", r"\bfirebase\b", r"\bcassandra\b"],
        "git": [r"\bgit\b", r"\bgithub\b", r"\bgitlab\b"],
        "docker": [r"\bdocker\b", r"\bcontaineriz\w+\b"],
        "kubernetes": [r"\bkubernetes\b", r"\bk8s\b"],
        "ci/cd": [r"\bci/cd\b", r"\bjenkins\b", r"\bgithub actions\b", r"\bgitlab ci\b"],
        "aws": [r"\baws\b", r"\bamazon web services\b", r"\blambda\b", r"\bec2\b", r"\bs3\b"],
        "azure": [r"\bazure\b"],
        "gcp": [r"\bgcp\b", r"\bgoogle cloud\b"],
        "machine learning": [r"\bmachine learning\b", r"\bdeep learning\b", r"\btensorflow\b", r"\bpytorch\b", r"\bscikit-learn\b", r"\bllm\b"],
        "data analysis": [r"\bdata analysis\b", r"\bdata analytics\b", r"\bpower bi\b", r"\btableau\b"],
        "api development": [r"\brest(?:ful)? api\b", r"\bgraphql\b", r"\bopenapi\b"],
        "testing": [r"\bunit test(?:ing)?\b", r"\bpytest\b", r"\bjest\b", r"\btdd\b"],
    }

    found_skills = {}
    for skill, patterns in skills_map.items():
        count = sum(
            len(re.findall(pattern, text, re.IGNORECASE))
            for pattern in patterns
        )
        if count > 0:
            found_skills[skill] = count

    return found_skills

def extract_availability(text: str) -> bool:
    """Return True if the text contains any signal that the developer is open to work."""
    patterns = [
        r"\bopen to work\b",
        r"\bopen for work\b",
        r"\bavailable for hire\b",
        r"\bfreelance\b",
        r"\bhire me\b",
        r"\bseeking (?:new )?opportunities\b",
        r"\blooking for (?:a )?(?:new )?(?:job|role|position|work|opportunities)\b",
        r"\bopen for projects\b",
        r"\blet[''`]?s work together\b",
        r"\bcurrently available\b",
        r"\bopen to (?:new )?opportunities\b",
        r"\bopen to freelance\b",
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)