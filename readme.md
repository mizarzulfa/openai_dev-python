## OpenAI API progress:

- [x] Direct API request without importing the OpenAI module
- [x] To improve readability, the JSON module format has been added.
- [x] Basic usage of sending POST and GET requests.

## API Key Personal

This repository requires you to create your own API key file named `api_key_personal.py` to access the necessary data.

### Function

The `api()` function in the `api_key_personal.py` file is responsible for providing the API key.

```python
def api():
    secret = "STRING DATA HERE"
    return secret
```

You need to replace `"STRING DATA HERE"` with your actual API key.

Make sure to keep your API key confidential and avoid sharing it with unauthorized individuals.