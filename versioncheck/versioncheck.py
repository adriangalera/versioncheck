"""Module to check the reported version in the projects vs the version reported in the
last tagged commit. This program search in the current directory the defined version
file and compare it with the version in the tag"""
import argparse
import re


def version_regex():
    """Returns a regex to detect version with 3 or 5 numbers and optional character
    subversioning"""
    return r"(\d{1,3}[.].+){1,2}"


def apply_regex(regex, text):
    """Apply the regex"""
    return re.search(regex, text)


def get_version_from_tag(tag):
    """Extract the version number from the tag using a regex"""
    matcher = apply_regex(version_regex(), tag)
    if matcher:
        return matcher.groups()[0]


def extract_from_python():
    """Extract the current version from a setup.py file. For the sake of simplicty use
    the same regex even though that it could collide if there are other strings with
    the same format in the setup.py"""
    version_file = "setup.py"
    # print 'Using setup.py as version file'
    with open(version_file, 'r') as version_file:
        version_file_contents = version_file.read()
        matcher = apply_regex(version_regex(), version_file_contents)
        if matcher:
            version = matcher.groups()[0]
            return version.replace("\"", "")


GIT_NO_VERSION_EXIT_CODE = 1
PROJ_NO_VERSION_EXIT_CODE = 2
PROJ_TYPE_NO_VERSION_EXIT_CODE = 3
NO_FILE_FOUND = 4
VERSION_MISMATCH = 5

EXTRACT_VERSION_DICT = {
    'python': extract_from_python
}

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Check the defined version on the project '
                    'depending on the project type.')
    parser.add_argument('project_type', metavar='project-type',
                        help='Project type. Accepted '
                             'values are: python, c')
    parser.add_argument('git_tag', metavar="git-tag",
                        help='Git tag that specify the version')

    args = parser.parse_args()

    git_tag = args.git_tag
    project_type = args.project_type

    tag_version = get_version_from_tag(git_tag)
    if not tag_version:
        print 'Unable to get version from tag %s' % git_tag
        exit(GIT_NO_VERSION_EXIT_CODE)

    if project_type not in EXTRACT_VERSION_DICT.keys():
        print 'Unable to get version from project type %s' % project_type
        exit(PROJ_TYPE_NO_VERSION_EXIT_CODE)

    version_project = EXTRACT_VERSION_DICT[project_type]()

    if not version_project:
        print 'Unable to get version from project'
        exit(PROJ_NO_VERSION_EXIT_CODE)

    print 'Tag version %s, Project version %s' % (tag_version, version_project)

    if version_project == tag_version:
        exit(0)
    else:
        exit(VERSION_MISMATCH)
