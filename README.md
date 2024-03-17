# python-fastapi-crud

# Create Conda Environment

```
conda create -n BNP python=3.7
```

# Activate Conda Environment

```
conda activate BNP
```

# Install Dependencies

```
pip install -r requirements.txt
```

# Run Server

```
uvicorn app:app --reload --port 4444
```

# Change .env

```
DB_NAME = <db_name>
MONGO_URI = <mongo_uri>
```
