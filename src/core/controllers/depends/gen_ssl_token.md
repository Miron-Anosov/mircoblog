root: ./src/

Gen private token
```shell
openssl genrsa -out src/certs/jwt-private.pem 2048
```
Gen public token
```shell
openssl rsa  -in src/certs/jwt-private.pem -outform PEM -pubout -out src/certs/jwt-public.pem
```