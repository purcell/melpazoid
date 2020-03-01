Python module for checking MELPA recipes.
import io  # noqa: F401 -- used by doctests
from typing import Iterator, TextIO, Tuple
    if not validate_recipe(recipe):
        _fail(f"Recipe '{recipe}' appears to be invalid")
        return
        subprocess.check_output(['cp', '-r', recipe_file, '_elisp/'])
def validate_recipe(recipe: str) -> bool:
    """
    >>> validate_recipe('(abc :repo "xyz" :fetcher github)')
    True
    >>> validate_recipe('??')
    False
    """
    tokenized_recipe = _tokenize_lisp_list(recipe)
    valid = (
        tokenized_recipe[0] == '('
        and tokenized_recipe[-1] == ')'
        and len([pp for pp in tokenized_recipe if pp == '('])
        == len([pp for pp in tokenized_recipe if pp == ')'])
    )
    return valid


    print(f"Building container for {package_name}... 🐳")
    for output_line in output.decode().strip().split('\n'):
    return _tokenize_lisp_list(recipe)[1] if recipe else ''
            with open(filename, 'r') as pkg_el:
                reqs.append(_reqs_from_pkg_el(pkg_el))
            with open(filename, 'r') as el_file:
                reqs.append(_reqs_from_el_file(el_file))
def _reqs_from_pkg_el(pkg_el: TextIO) -> str:
    """
    >>> _reqs_from_pkg_el(io.StringIO('''(define-package "x" "1.2" "A pkg." '((emacs "31.5") (xyz "123.4"))'''))
    '( ( emacs "31.5" ) ( xyz "123.4" ) )'
    """
    reqs = pkg_el.read()
def _reqs_from_el_file(el_file: TextIO) -> str:
    """
    >>> _reqs_from_el_file(io.StringIO(';; x y z\\n ;; package-requires: ((emacs "24.4"))'))
    ';; package-requires: ((emacs "24.4"))'
    """
    for line in el_file.readlines():
        if re.match('[; ]*Package-Requires:', line, re.I):
            return line.strip()
    return ''
    # TODO: this function could be more comprehensive; don't use grep
    # okay to have a -pkg.el file, but doing it incorrectly can break the build.
            basename = os.path.basename(el)
            _fail(f"- Package-Requires mismatch between {basename} and another file!")
    if ':files' in recipe or ':branch' in recipe:
        _note('  - Prefer the default recipe, especially for small packages', CLR_WARN)
        if os.path.isdir(recipe_file):
            print(f"- {recipe_file}: (directory)")
            continue
                header = '(no elisp header)'
            f"- {CLR_ULINE}{recipe_file}{CLR_OFF}"
        if recipe_file.endswith('-pkg.el'):
            _note(f"  - Consider excluding this file; MELPA will create one", CLR_WARN)
def check_recipe(recipe: str = ''):
    """
    Raises RuntimeError if repo doesn't exist, and
    subprocess.CalledProcessError if git clone fails.
    """
    if not requests.get(repo).ok:
        _fail(f"Unable to locate '{repo}'")
        raise RuntimeError
    if branch:
        git_command = ['git', 'clone', '-b', branch, repo, into]
    else:
        git_command = ['git', 'clone', repo, into]
    subprocess.check_output(git_command, stderr=subprocess.STDOUT)
    >>> _branch('(shx ...)')
    ''
    tokenized_recipe = _tokenize_lisp_list(recipe)
    if ':branch' not in tokenized_recipe:
        return ''
    return tokenized_recipe[tokenized_recipe.index(':branch') + 1].strip('"')
    """Check a locally-hosted package (WIP)."""
    if 'changed_files' not in pr_data:
        _note(f"{pr_url} does not appear to be a MELPA PR", CLR_ERROR)
        return
        _note('Please only add one recipe per pull request', CLR_ERROR)
        _note(f"Unable to build the pull request at {pr_url}", CLR_ERROR)
            if (
                'new file mode' not in diff_text
                or 'a/recipes' not in diff_text
                or 'b/recipes' not in diff_text
            ):
                _note('This does not appear to add a new recipe', CLR_WARN)
                return '', ''
        check_recipe(os.environ['RECIPE'])
        sys.exit(return_code())
    elif 'RECIPE_FILE' in os.environ:
        with open(os.environ['RECIPE_FILE'], 'r') as recipe_file:
            check_recipe(recipe_file.read())