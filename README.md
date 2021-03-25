# Supertouch

Easily create files and folders with a single specification.

### Installation

```bash
python3 -m pip install supertouch
```

### Usage

From the command line, the package is available under the `st` alias.

* Create a file and all the intermediate directories: 
    ```bash
    st ~/long/path/with/files.py
    ```
* Create a nested directories ending by ending the path with a `/`:
    ```bash
    st ~/very/complex/directory/structure/
    ```

* Multiple files at once:
    ```bash
    st ~/path/with/files.py ./folder/items.txt
    ```

