This is **sandbox** Python code for figuring out how to patch oauth2client
4.0.0 to accept 1.4.2 objects.

### Running this code

The short version, with included credentials:

```
$ python -m unittest read_credentials.py
```


To generate your own credentials for oauth2client 1.4.2:

```
$ mkvirtualenv --python=`which python3.6` oauth2-1.4.2
$ pip install oauth2client==1.4.2
$ python write_old_credential.py
```

To generate your own credentials for oauth2client 4.0.0:

```
$ mkvirtualenv --python=`which python3.6` oauth2-4.0.0
$ pip install oauth2client==4.0.0
$ python write_new_credential.py
```
