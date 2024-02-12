import argparse
import json

from core.generators import SimpleGenerator
from utils.util import log

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates records (json lines) to output file')
    parser.add_argument('-o', '--out', help='output filename', required=True)
    parser.add_argument('-l', '--lines', type=int, default=100, help='number of json lines', required=False)

    args = vars(parser.parse_args())
    print(args)

    with open(args['out'], 'w+') as f:
        num_lines = int(args['lines'])
        log.info("generating %s lines", num_lines)
        generator = SimpleGenerator()
        for _ in range(num_lines):
            f.write(json.dumps(generator.generate().to_json()) + '\n')

