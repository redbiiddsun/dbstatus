---
# DBStatus

The project aims to create a command-line tool in Python that facilitates the testing of database connections. This tool will enable users to quickly and efficiently verify the connectivity and functionality of various types of databases, including MySQL, PostgreSQL, MongoDB, and more in the futrue.

## Install required dependencies

```bash
pip install -r requirements. txt
```

## Usage
MySQL
```bash
python dbstatus.py -mysql mysql://root:root@localhost:3306/database
```
MongoDB
```bash
python dbstatus.py -mongo mongodb://localhost:27017/
```
PostgreSQL
```bash
python dbstatus.py -postgre postgres://admin:password@localhost:5432/database
```


## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.