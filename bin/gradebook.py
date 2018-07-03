#!/usr/bin/env python

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Grade Book Service")
    
    parser.add_argument(
        "-c", "--config", default="/etc/gradebook/server.yaml",
        help="Path to config file.")
    
    parser.add_argument("-p", "--port", type=int, default=None,
        help="Override port in config.")
    
    parser.add_argument(
        "-q", "--quiet", action="store_true",
        help="Do not write logs to the screen.")
    
    parser.add_argument(
        "-V", "--version", action="version",
        help="Display version information.")

    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == '__main__':
    main()