CREATE DATABASE investing;

CREATE TABLE exchange_market (
	company_name VARCHAR(40),
    ticker VARCHAR(40),
    market VARCHAR(40),
    currency_adjustment INT,
    PRIMARY KEY(company_name)
    );

INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
	"China Carbon Graphite", "CHGI", "NASDAQ");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Directa Plus Plc", "DTPKF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Elcora Advanced Materials Corp.", "ECORF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"First Graphene Limited", "FGPHF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"G6 Materials Corp.", "GPHBF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Graphene NanoChem Plc", "GRPEF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Group NanoXplore Inc.", "NNXPF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Haydale Graphene Industries Plc", "HDGHF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Saint Jean Carbon Inc.", "SJL.V", "TSXV");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Talga Resources Ltd.", "TLGRF", "Other OTC");
INSERT INTO exchange_market (company_name, ticker, market)
VALUES(
"Versarien Plc", "VRSRF", "Other OTC");