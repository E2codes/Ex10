CREATE TABLE Frogs (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    ScientificName VARCHAR(255),
    Color VARCHAR(255)
);

INSERT INTO Frogs (Name, ScientificName, Color) VALUES
    ('Frog1', 'Scientific1', 'Green'),
    ('Frog2', 'Scientific2', 'Brown');
