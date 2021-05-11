# Intercom Test

## Getting started

Install the dependencies and activate the new environment with:

```
$ poetry install && source .venv/bin/activate
```

Then run the tests with:

```
$ pytest -v
```

## Usage

Zero configuration startup:
```
python cli.py
```

Or specifying some parameters:
```
python cli.py --dataset='dataset/customers.txt' --max-distance=100.0
```

## Authors

- **Giacomo Trudu** - [Wicker25](https://github.com/Wicker25)

## License

The code in this repository is [MIT licensed](https://github.com/paguro/browser-detection/blob/master/LICENSE).
