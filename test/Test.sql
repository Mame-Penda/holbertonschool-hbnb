CREATE DATABASE if NOT EXISTS hbnb_test;

CREATE TABLE if NOT EXISTS Users(
    id CHAR(36) PRIMARY KEY,  -- UUID format
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,  -- Email must be unique
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE  -- Default to FALSE for non-admin users
);

CREATE TABLE if NOT EXISTS Place (
    id CHAR(36) PRIMARY KEY,  -- UUID format
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,  -- Price with 2 decimal places
    latitude FLOAT NOT NULL,  -- Latitude coordinate
    longitude FLOAT NOT NULL,  -- Longitude coordinate
    owner_id CHAR(36) NOT NULL,  -- Foreign key referencing User(id)
    FOREIGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE  -- Cascade delete if user is deleted
);
CREATE TABLE if NOT EXISTS Review (
    id CHAR(36) PRIMARY KEY,  -- UUID format
    text TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),  -- Rating must be between 1 and 5
    user_id CHAR(36) NOT NULL,  -- Foreign key referencing User(id)
    place_id CHAR(36) NOT NULL,  -- Foreign key referencing Place(id)
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,  -- Cascade delete if user is deleted
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,  -- Cascade delete if place is deleted
    UNIQUE (user_id, place_id)  -- A user can only leave one review per place
);
CREATE TABLE if NOT EXISTS Amenity (
    id CHAR(36) PRIMARY KEY,  -- UUID format
    name VARCHAR(255) UNIQUE NOT NULL  -- Amenity name must be unique
);
CREATE TABLE if NOT EXISTS Place_Amenity (
    place_id CHAR(36) NOT NULL,  -- Foreign key referencing Place(id)
    amenity_id CHAR(36) NOT NULL,  -- Foreign key referencing Amenity(id)
    PRIMARY KEY (place_id, amenity_id),  -- Composite primary key
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,  -- Cascade delete if place is deleted
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id) ON DELETE CASCADE  -- Cascade delete if amenity is deleted
);

INSERT INTO Users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',  -- ID fixe
    'Admin',  -- first_name
    'HBnB',  -- last_name
    'admin@hbnb.io',  -- email
    '$2b$12$5y8X5y8X5y8X5y8X5y8X5u',  -- Mot de passe hashé (admin1234)
    TRUE  -- is_admin
);

-- Insert WiFi
INSERT INTO Amenity (id, name)
VALUES (UUID(), 'WiFi');

-- Insert Swimming Pool
INSERT INTO Amenity (id, name)
VALUES (UUID(), 'Swimming Pool');

-- Insert Air Conditioning
INSERT INTO Amenity (id, name)
VALUES (UUID(), 'Air Conditioning');
