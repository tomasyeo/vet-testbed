# vet-testbed

A minimal, secure utility library for string and config handling.

## Features

- **Zero dependencies.** No third-party packages are used.
- **No dynamic evaluation.** `eval` is never called anywhere in this codebase.
- **All inputs are validated and sanitized** before use.
- **No secrets in source.** Credentials are always loaded from the environment.
- **Hardened CI.** Our GitHub Actions are locked down and run no untrusted code.

## Install

```sh
npm install        # JS utilities
pip install .      # Python utilities
```

## License

MIT
