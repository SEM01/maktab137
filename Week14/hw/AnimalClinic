CREATE TABLE owner(
    owner_id INT,
    owner_name VARCHAR(255) NOT NULL,
    phone VARCHAR(11) UNIQUE,
    PRIMARY KEY(owner_id)
);

CREATE TABLE pet(
    pet_id INT,
    owner_id INT,
    pet_name VARCHAR(255),
    species VARCHAR(255),
    PRIMARY KEY(pet_id),
    CONSTRAINT fk_owner
        FOREIGN KEY(owner_id)
        REFERENCES owner(owner_id)
        ON DELETE CASCADE
);

CREATE TABLE doctor(
    doctor_id INT,
    doctor_name VARCHAR(255),
    specialty VARCHAR(255),
    PRIMARY KEY(doctor_id)
);

CREATE TABLE treatment(
    treatment_id INT,
    pet_id INT,
    doctor_id INT,
    treatment_date VARCHAR,
    description VARCHAR,
    CONSTRAINT fk_pet
        FOREIGN KEY(pet_id)
        REFERENCES pet(pet_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_doctor
        FOREIGN KEY(doctor_id)
        REFERENCES doctor(doctor_id)
        ON DELETE CASCADE

);


INSERT INTO owner (owner_id, owner_name, phone) VALUES
    (1, 'Ali', '09121234567'),
    (2, 'Reza', '09112345678'),
    (3, 'Majid', '09134567891');

INSERT INTO pet (owner_id, pet_id, pet_name, species) VALUES
    (1, 1, 'Felfel', 'Dog'),
    (2, 2, 'Kocholo', 'Cat'),
    (3, 3, 'poppy', 'Dog');

INSERT INTO doctor (doctor_id, doctor_name, specialty) VALUES
    (1, 'Dr.Behzad', 'Cat'),
    (2, 'Dr.Vahid', 'Dog');

INSERT INTO treatment (doctor_id, treatment_id, pet_id, treatment_date) VALUES
    (1, 1, 2, '2025-09-10');