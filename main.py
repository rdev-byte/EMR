import mysql.connector


def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return connection


def add_patient(
        connection,
        full_name,
        date_of_birth,
        sex, address,
        phone_number,
        email_address,
        marital_status,
        guardian_status,
        guardian_full_name,
        guardian,
        guardian_phone_number,
        guardian_email_address,
        guardian_address,
        guardian_relationship
):
    cursor = connection.cursor()
    sql = "INSERT INTO patients (full_name, date_of_birth, sex, address, phone_number, email_address, marital_status, guardian_status, guardian_full_name, guardian, guardian_phone_number, guardian_email_address, guardian_address, guardian_relationship) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        full_name,
        date_of_birth,
        sex, address,
        phone_number,
        email_address,
        marital_status,
        guardian_status,
        guardian_full_name,
        guardian,
        guardian_phone_number,
        guardian_email_address,
        guardian_address,
        guardian_relationship
    )
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    connection = connect_to_database()

    # Prompt the user to enter patient information
    full_name = input("Full name: ")
    date_of_birth = input("Date of birth (YYYY-MM-DD): ")
    sex = input("Sex: ")
    address = input("Address: ")
    phone_number = input("Phone number: ")
    email_address = input("Email address: ")
    marital_status = input("Marital status: ")
    guardian_status = input("Guardian status: ")
    guardian_full_name = input("Guardian full name: ")
    guardian = input("Guardian: ")
    guardian_phone_number = input("Guardian's phone number: ")
    guardian_email_address = input("Guardian's email address: ")
    guardian_address = input("Guardian's address: ")
    guardian_relationship = input("Guardian relationship: ")

    add_patient(full_name, date_of_birth, sex, address, phone_number, email_address, marital_status, guardian_status,
                guardian_full_name, guardian, guardian_phone_number, guardian_email_address, guardian_address, guardian_relationship)
