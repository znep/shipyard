#! /bin/python
import os
import sys
from jinja2 import Environment, FileSystemLoader


def main(argv):

    template_path = os.abspath(argv[0])
    if len(argv) > 1:
        output_path = os.abspath(argv[1])
    else:
        output_path = template_path.strip('.j2')

    environment_vars = os.environ

    jinja_env = Environment(loader=FileSystemLoader('/'))
    template = jinja_env.get_template(template_path)

    with open(output_path, 'w') as output:
        output.write(template.render(**environment_vars))


if __name__ == '__main__':
    main(sys.argv[1:])
