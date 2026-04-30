-- =========================
-- Database Schema
-- CSV MySQL ETL Project
-- =========================

-- STATES TABLE
CREATE TABLE states (
    state_id INT AUTO_INCREMENT PRIMARY KEY,
    state_name VARCHAR(100) NOT NULL,
    state_code VARCHAR(10) NOT NULL UNIQUE
);

-- CITIES TABLE
CREATE TABLE cities (
    city_id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(state_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- CUSTOMERS TABLE
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address VARCHAR(255),
    city_id INT,
    state_id INT,
    phone_number VARCHAR(30),
    email VARCHAR(150),

    FOREIGN KEY (city_id) REFERENCES cities(city_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,

    FOREIGN KEY (state_id) REFERENCES states(state_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Creating index to scan data faster
CREATE INDEX idx_states_code ON states(state_code);
CREATE INDEX idx_cities_state ON cities(state_id);
CREATE INDEX idx_customers_city ON customers(city_id);
CREATE INDEX idx_customers_state ON customers(state_id);