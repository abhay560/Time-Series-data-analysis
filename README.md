## Data-Engineering-Internship-Bosch

This project implements an end-to-end data engineering pipeline for handling Air Quality data. The pipeline covers ingestion, validation, transformation, and loading into PostgreSQL. The project follows a modular, production-style architecture.

```
Data-Engineering-Internship-Bosch/
│
├── artifacts/                       # Stores raw, valid, transformed & quarantined data
│   ├── data_ingestion/              # Stores raw data
│   ├── data_validation/             # Stores status of file (if Validated successfully stores "True" else "False")
│   ├── metrics_dir/                 # stores aggregated metrics files
│   ├── quarantine/                  # Store failed datasets
│   └── valid_data/                  # Stores valid datasets
│
├── config/                          # Configuration files
│   └── config.yaml
│
├── logs/                            # Logging outputs
├── notebook/                        # Jupyter notebooks for exploration
├── sql/                             # SQL schema definitions
│   └── schema.sql
│
├── src/
│   ├── dataEngineer/                # Core pipeline package
│   │   ├── components/              # Modular pipeline components
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_transformation.py
│   │   │   └── data_validation.py
│   │   │
│   │   ├── config/                  # Centralized configuration handler
│   │   │   └── Configuration.py
│   │   │
│   │   ├── entity/                  # Entities for structured configs
│   │   │   └── config_entity.py
│   │   │
│   │   ├── pipeline/                # High-level pipeline runners
│   │   │   ├── data_ingestion_pipeline.py
│   │   │   ├── data_transformation_pipeline.py
│   │   │   └── data_validation_pipeline.py
|   |   |   |__ data_loading_pipeline.py
│   │   │
│   │   └── utils/                   # Reusable utilities
│   │       └── common.py
│   │
│   └── db/                          # Database layer
│       ├── engine.py                # PostgreSQL connection engine
│       ├── init_db.py               # Apply schema to DB
│       ├── load_data.py             # Load raw and aggregated data into DB
│       
│
├── main.py                          # Main pipeline orchestrator
├── requirements.txt                 # Python dependencies
├── params.yaml                      # Pipeline parameters
|__ schema.yaml                      # List of columns present for validation purpose
|__ template.py                      # Making creation of Folders automatically only by running the script
└── README.md                        # Project documentation

```

## How to Run

# Steps

# Clone the Repository
```https://github.com/abhay560/Data-Engineering-Internship-Bosch```

# Create a conda environment after opening the repository
```conda create -n env python=3.8 -y```

```conda activate env```

# Install the requirements
```pip install -r requirements.txt```

# Database setup
```DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD1999@localhost:PORTNO/DATABASE_NAME"```           
Add it inside ```src/db/engine.py   and  src/db/load_data.py```
Currently the code for Data Loading to the Database is commented, you can see it in main.py. After adding your DATABASE_URL, uncomment the code and run main.py again.

# Initialize the database schema
If you have added your DATABASE_URL then only run the below command. Otherwise leave this step, directly run ``` python main.py ```
```python -m src.db.init_db```

# Run
```python main.py```
