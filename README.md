# NothingAPI - The Official Python API Wrapper for the Nothing Currency!
## Basic Syntax
### Installing the API using pip:
```
pip install nothingapi
```

### Fetching a User Dict and printing its balance:
```
import nothingapi as api
user = api.get_user(user_id)
print(user["balance"])
```