#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader, Template
import yaml

ENV = Environment(loader=FileSystemLoader('Git\\Projects\\Project_Blue\\Jinja'))

template = ENV.get_template('template.j2')

with open('Git\\Projects\\Project_Blue\\Yaml\\data.yml') as f:
    interfaces = yaml.load(f)
    print(template.render(interface_list=interfaces))