'''

models = {
    "Maruti Suzuki": [
        {"model": "Swift", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 600000},
        {"model": "Baleno", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 650000},
        {"model": "Vitara Brezza", "type": "SUV", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 800000},
        {"model": "Dzire", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 700000},
        {"model": "Ertiga", "type": "MPV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 900000},
        {"model": "Alto", "type": "Hatchback", "seating_capacity": 4, "transmission": ["Manual"], "fuel_type": ["Petrol"], "ex_showroom_price": 400000},
        {"model": "WagonR", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "CNG"], "ex_showroom_price": 550000},
        {"model": "Ciaz", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 900000},
        {"model": "S-Presso", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 500000},
        {"model": "XL6", "type": "MPV", "seating_capacity": 6, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 1000000},
    ],
    "Toyota": [
        {"model": "Innova Crysta", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1500000},
        {"model": "Fortuner", "type": "SUV", "seating_capacity": 7, "transmission": ["Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 2500000},
        {"model": "Glanza", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 700000},
        {"model": "Yaris", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 800000},
        {"model": "Urban Cruiser", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 750000},
        {"model": "Corolla", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 1200000},
        {"model": "Camry", "type": "Sedan", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Hybrid(Petrol)"], "ex_showroom_price": 3500000},
        {"model": "Vellfire", "type": "MPV", "seating_capacity": 7, "transmission": ["Automatic"], "fuel_type": ["Hybrid(Petrol)"], "ex_showroom_price": 8000000},
        {"model": "Etios", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol"], "ex_showroom_price": 650000},
        {"model": "Land Cruiser", "type": "SUV", "seating_capacity": 8, "transmission": ["Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 3500000},
    ],
    "Hyundai": [
        {"model": "Creta", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 1100000},
        {"model": "i20", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 800000},
        {"model": "Venue", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 900000},
        {"model": "Verna", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 1000000},
        {"model": "Grand i10 Nios", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "CNG"], "ex_showroom_price": 700000},
        {"model": "Tucson", "type": "SUV", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 1800000},
        {"model": "Santro", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "CNG"], "ex_showroom_price": 550000},
        {"model": "Aura", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 750000},
        {"model": "Kona Electric", "type": "SUV", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Electric"], "ex_showroom_price": 2500000},
        {"model": "i10", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol"], "ex_showroom_price": 600000},
    ],
    "Tata": [
        {"model": "Nexon", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 900000},
        {"model": "Altroz", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 750000},
        {"model": "Harrier", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1500000},
        {"model": "Tiago", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 600000},
        {"model": "Safari", "type": "SUV", "seating_capacity": 6, "transmission": ["Manual", "Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1700000},
        {"model": "Tigor", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Electric"], "ex_showroom_price": 650000},
        {"model": "Nexon EV", "type": "SUV", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Electric"], "ex_showroom_price": 1500000},
        {"model": "Hexa", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1400000},
        {"model": "Zest", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 650000},
        {"model": "Bolt", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol"], "ex_showroom_price": 650000},
    ],
    "Mahindra": [
        {"model": "XUV300", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 900000},
        {"model": "Scorpio", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1200000},
        {"model": "Bolero", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual"], "fuel_type": ["Diesel"], "ex_showroom_price": 800000},
        {"model": "Thar", "type": "SUV", "seating_capacity": 4, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 1300000},
        {"model": "XUV700", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 1800000},
        {"model": "XUV500", "type": "SUV", "seating_capacity": 7, "transmission": ["Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1500000},
        {"model": "Marazzo", "type": "MPV", "seating_capacity": 7, "transmission": ["Manual"], "fuel_type": ["Diesel"], "ex_showroom_price": 1100000},
        {"model": "TUV300", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 900000},
        {"model": "KUV100 NXT", "type": "Hatchback", "seating_capacity": 6, "transmission": ["Manual"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 600000},
        {"model": "Verito", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 700000},
    ],
    "Honda": [
        {"model": "City", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 1000000},
        {"model": "Amaze", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 900000},
        {"model": "WR-V", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 800000},
        {"model": "Civic", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 1200000},
        {"model": "Jazz", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 800000},
        {"model": "CR-V", "type": "SUV", "seating_capacity": 7, "transmission": ["Automatic"], "fuel_type": ["Petrol", "Hybrid(Petrol)"], "ex_showroom_price": 2500000},
        {"model": "BR-V", "type": "SUV", "seating_capacity": 7, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 1100000},
        {"model": "Brio", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 600000},
        {"model": "Accord", "type": "Sedan", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Hybrid(Petrol)"], "ex_showroom_price": 3000000},
        {"model": "Mobilio", "type": "MPV", "seating_capacity": 7, "transmission": ["Manual"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 900000},
    ],
    "Ford": [
        {"model": "EcoSport", "type": "SUV", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 900000},
        {"model": "Endeavour", "type": "SUV", "seating_capacity": 7, "transmission": ["Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 2500000},
        {"model": "Figo", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 650000},
        {"model": "Aspire", "type": "Sedan", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 700000},
        {"model": "Freestyle", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual", "Automatic"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 750000},
        {"model": "Mustang", "type": "Coupe", "seating_capacity": 4, "transmission": ["Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 7500000},
        {"model": "Ranger", "type": "Pickup", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Diesel"], "ex_showroom_price": 1800000},
        {"model": "Edge", "type": "SUV", "seating_capacity": 5, "transmission": ["Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 2000000},
        {"model": "Focus", "type": "Hatchback", "seating_capacity": 5, "transmission": ["Manual"], "fuel_type": ["Petrol", "Diesel"], "ex_showroom_price": 800000},
        {"model": "Explorer", "type": "SUV", "seating_capacity": 7, "transmission": ["Automatic"], "fuel_type": ["Petrol"], "ex_showroom_price": 3000000},
    ]
}











import psycopg2


# Function to generate SQL insert statements
def generate_insert_statements(models):
    insert_statements = []
    for make, models_list in models.items():
        for car_model in models_list:
            print(car_model)
            insert_statement = f"INSERT INTO vehicle_vehicle (make, model,type, seating_capacity, transmission, fuel_type, ex_showroom_price) VALUES ('{make}', '{car_model['model']}', '{car_model['type']}',{car_model['seating_capacity']}, ARRAY{car_model['transmission']}, ARRAY{car_model['fuel_type']}, {car_model['ex_showroom_price']});"
            insert_statements.append(insert_statement)
    return insert_statements

# Function to connect to PostgreSQL and execute insert statements
def insert_into_postgres(insert_statements):
    try:
        # Replace these values with your actual PostgreSQL credentials
        connection = psycopg2.connect(
            dbname="rentopia_2",
            user="elisha",
            password="postgres",
            host="localhost",
            port="5432",
        )


        cursor = connection.cursor()

        for statement in insert_statements:
            cursor.execute(statement)
            print(statement)
            connection.commit()

        cursor.close()
        connection.close()
        print("Insertion successful!")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)

# Generate insert statements
insert_statements = generate_insert_statements(models)

# Insert into PostgreSQL
insert_into_postgres(insert_statements)
'''
def h():
    a = []
    if a:
        print('1')
    else:
        print('2')
h()