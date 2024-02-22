def get_tags_matching(repo, regexes):
    """
    goal: get tags in a repo matching 1+ regexes. similar to `git tag --list | grep $PATTERN`
    """
    return [t for t in repo.tags if any([re.match(pattern, t.name) for pattern in regexes])]


def get_branches_matching(repo, regexes):
    """
    goal: get branches in a repo matching 1+ regexes.
    similar to `git branch -r --format "%(refname:short)" | grep $PATTERN`
    """
    return [b for b in repo.remote().refs if any([re.match(pattern, b.remote_head) for pattern in regexes])]


def git_write_sha1(repo, sha1, base_dir):
    """ wrapper around: `git show sha1 > base_dir/sha1`"""
    logger.debug("attempting to 'git show %s'", sha1)
    contents = repo.git.show(sha1)
    path = os.path.join(base_dir, sha1)
    with open(path, "wb") as outfile:
        try:
            outfile.write(contents.encode('utf-8', 'surrogateescape'))
        except:
            logger.warning("failed to write sha %s, contents %s", sha1, contents)
            raise
        return path