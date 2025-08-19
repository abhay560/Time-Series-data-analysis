-- Table for raw sensor data
CREATE SCHEMA IF NOT EXISTS air_quality_uci;
CREATE TABLE air_quality_uci.airquality_uci_raw (
    "Date" TEXT,
    "Time" TEXT,
    "CO(GT)" FLOAT,
    "PT08.S1(CO)" FLOAT,
    "NMHC(GT)" FLOAT,
    "C6H6(GT)" FLOAT,
    "PT08.S2(NMHC)" FLOAT,
    "NOx(GT)" FLOAT,
    "PT08.S3(NOx)" FLOAT,
    "NO2(GT)" FLOAT,
    "PT08.S4(NO2)" FLOAT,
    "PT08.S5(O3)" FLOAT,
    "T" FLOAT,
    "RH" FLOAT,
    "AH" FLOAT
);

-- Table for aggregated metrics
CREATE TABLE air_quality_uci.aggregated_metrics (
    feature TEXT NOT NULL,
    min_val FLOAT,
    max_val FLOAT,
    avg_val FLOAT,
    std_val FLOAT,
    source_file TEXT,
    source_system TEXT,
    record_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
