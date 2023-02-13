#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET


class GetTests:
    def __init__(self, filename, filter_type):
        self.filename = filename
        self.filter_type = filter_type
        self.api_test_list = []

    def filter_test_cases(self):
        tree = ET.parse(args.file)
        root = tree.getroot()

        for child in root.iter():
            if child.tag == 'testcase':
                splitted_name = child.get('name').split('[')
                if len(child) > 0:
                    if child[0].tag == 'skipped':
                        continue

                if 'setUpClass' not in splitted_name[0] and \
                        not 'manila' in splitted_name[0]:
                    if not 'setUpClass' in splitted_name[0]:
                        if args.test_type:
                            if f'{args.test_type},' in splitted_name[1]:
                                self.api_test_list.append(('- {}.{}').format(
                                    child.get('classname'), splitted_name[0]))
                        else:
                            self.api_test_list.append(('- {}.{}').format(
                                child.get('classname'), splitted_name[0]))
        return self.api_test_list

    def show_list(self):
        sorted_list = sorted(self.api_test_list)
        for test in sorted_list:
            print(test)
        print(len(sorted_list))


parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--type', dest='test_type', choices=['api', 'backend'],
                    default=None)
args = parser.parse_args()


def main():
    tests = GetTests(args.file, args.test_type)
    tests.filter_test_cases()
    tests.show_list()


if __name__ == '__main__':
    main()

