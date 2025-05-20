import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

# Création des tables
c.execute('''
CREATE TABLE IF NOT EXISTS Ville (
    IdVille INTEGER PRIMARY KEY,
    NomVille TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Hotel (
    IdHotel INTEGER PRIMARY KEY,
    NomHotel TEXT NOT NULL,
    IdVille INTEGER,
    Adresse TEXT,
    FOREIGN KEY(IdVille) REFERENCES Ville(IdVille)
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Client (
    IdClient INTEGER PRIMARY KEY,
    Nom TEXT NOT NULL,
    Adresse TEXT,
    Ville TEXT,
    CodePostal INTEGER,
    Email TEXT,
    Telephone TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS TypeChambre (
    IdType INTEGER PRIMARY KEY,
    Type TEXT NOT NULL,
    Prix INTEGER NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Chambre (
    IdChambre INTEGER PRIMARY KEY,
    Numero INTEGER NOT NULL,
    Disponible INTEGER,
    Fumeur INTEGER,
    IdHotel INTEGER,
    IdType INTEGER,
    FOREIGN KEY(IdHotel) REFERENCES Hotel(IdHotel),
    FOREIGN KEY(IdType) REFERENCES TypeChambre(IdType)
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Prestation (
    IdPrestation INTEGER PRIMARY KEY,
    Prix INTEGER,
    Description TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Reservation (
    IdReservation INTEGER PRIMARY KEY,
    DateArrivee TEXT,
    DateDepart TEXT,
    IdClient INTEGER,
    IdChambre INTEGER,
    FOREIGN KEY(IdClient) REFERENCES Client(IdClient),
    FOREIGN KEY(IdChambre) REFERENCES Chambre(IdChambre)
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Evaluation (
    IdEvaluation INTEGER PRIMARY KEY,
    DateEvaluation TEXT,
    Note INTEGER,
    Commentaire TEXT,
    IdReservation INTEGER,
    FOREIGN KEY(IdReservation) REFERENCES Reservation(IdReservation)
)
''')


c.execute("DELETE FROM Ville")
c.executemany("INSERT INTO Ville (IdVille, NomVille) VALUES (?, ?)", [
    (1, 'Paris'), (2, 'Lyon'), (3, 'Marseille'), (4, 'Lille'), (5, 'Nice')
])
c.execute("DELETE FROM Hotel")
c.executemany("INSERT INTO Hotel (IdHotel, NomHotel, IdVille, Adresse) VALUES (?, ?, ?, ?)", [
    (1, 'Hotel Paris Centre', 1, '75001 Paris'),
    (2, 'Hotel Lyon Bellecour', 2, '69002 Lyon')
])
c.execute("DELETE FROM Client")
c.executemany("INSERT INTO Client VALUES (?, ?, ?, ?, ?, ?, ?)", [
    (1, 'Jean Dupont', '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678'),
    (2, 'Marie Leroy', '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789'),
    (3, 'Paul Moreau', '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890'),
    (4, 'Lucie Martin', '27 Rue Nationale', 'Lille', 59800, 'lucie.martin@email.fr', '0645678901'),
    (5, 'Emma Giraud', '3 Rue des Fleurs', 'Nice', 6000, 'emma.giraud@email.fr', '0656789012')
])
c.execute("DELETE FROM TypeChambre")
c.executemany("INSERT INTO TypeChambre VALUES (?, ?, ?)", [
    (1, 'Simple', 70), (2, 'Double', 120), (3, 'Suite', 250)
])
c.execute("DELETE FROM Chambre")
c.executemany("INSERT INTO Chambre VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 101, 1, 0, 1, 1), (2, 102, 1, 1, 1, 2),
    (3, 201, 0, 0, 2, 1), (4, 202, 1, 0, 2, 3)
])
c.execute("DELETE FROM Prestation")
c.executemany("INSERT INTO Prestation VALUES (?, ?, ?)", [
    (1, 10, 'Petit-déjeuner'), (2, 30, 'Navette aéroport'),
    (3, 0, 'Wi-Fi gratuit'), (4, 50, 'Accès piscine'), (5, 20, 'Parking privé')
])
c.execute("DELETE FROM Reservation")
c.executemany("INSERT INTO Reservation VALUES (?, ?, ?, ?, ?)", [
    (1, '2025-06-10', '2025-06-12', 1, 1),
    (2, '2025-06-15', '2025-06-18', 2, 2),
    (3, '2025-07-01', '2025-07-04', 3, 3),
    (4, '2025-07-10', '2025-07-12', 4, 4),
    (5, '2025-08-05', '2025-08-09', 5, 1)
])
c.execute("DELETE FROM Evaluation")
c.executemany("INSERT INTO Evaluation VALUES (?, ?, ?, ?, ?)", [
    (1, '2025-06-12', 4, 'Très bon séjour à Paris.', 1),
    (2, '2025-06-18', 5, 'Service impeccable à Lyon.', 2),
    (3, '2025-07-04', 3, 'Un peu de bruit à Marseille.', 3),
    (4, '2025-07-12', 4, 'Hôtel agréable à Lille.', 4),
    (5, '2025-08-09', 5, 'Excellent hôtel à Paris.', 5)
])

conn.commit()
conn.close()

print("✅ Données marocaines insérées avec succès dans hotel.db !")
