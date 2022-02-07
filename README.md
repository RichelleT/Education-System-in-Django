## Dependencies

```sh
pip install django-utils-six
```
```sh
pip install mysqlclient
```
```sh
pip install pdfplumber
```
## Manual

| Step | Command | Description |
|----------|-------------|-------------|
|1| A dictionary of metadata key/value pairs, drawn from the PDF's `Info` trailers. Typically includes "CreationDate," "ModDate," "Producer," et cetera.|
|2| A list containing one `pdfplumber.Page` instance per page loaded.| test |
