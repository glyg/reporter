import json
import subprocess

from .header import create_header
from .graph import make_graph


class Generator:

    def __init__(self, json_path, link):
        self.json_path = json_path
        self.link = link
        self.authors = self._get_authors()

    def _get_authors(self):
        with open(self.json_path, 'r') as jf:
            authors = json.load(jf)
        return authors

    def get_header(self):
        return create_header(self.authors)

    def get_graph(self):
        self.fig, self.ax = make_graph(self.link)

    def make_report(self):
        text = self.get_header()
        self.get_graph()
        self.fig.savefig('graph.png')
        text += '\n![el graphe](graph.png)\n'
        with open("report.md", 'w') as rf:
            rf.write(text)

    def export(self, fmt):

        return subprocess.run(['pandoc', 'report.md','-o', f'report.{fmt}'])
