CREATE SCHEMA IF NOT EXISTS air_quality_uci;

DROP TABLE IF EXISTS air_quality_uci.airquality_uci_raw;
CREATE TABLE air_quality_uci.airquality_uci_raw (
  "Date"           TEXT,
  "Time"           TEXT,
  "CO(GT)"         TEXT,
  "PT08.S1(CO)"    TEXT,
  "NMHC(GT)"       TEXT,
  "C6H6(GT)"       TEXT,
  "PT08.S2(NMHC)"  TEXT,
  "NOx(GT)"        TEXT,
  "PT08.S3(NOx)"   TEXT,
  "NO2(GT)"        TEXT,
  "PT08.S4(NO2)"   TEXT,
  "PT08.S5(O3)"    TEXT,
  "T"              TEXT,
  "RH"             TEXT,
  "AH"             TEXT
);

DROP TABLE IF EXISTS air_quality_uci.aggregated_metrics;
CREATE TABLE air_quality_uci.aggregated_metrics (
    feature TEXT NOT NULL,
    min_val TEXT,
    max_val TEXT,
    avg_val TEXT,
    std_val TEXT,
    source_file TEXT,
    source_system TEXT,
    record_time TEXT  -- fixed column name
);
