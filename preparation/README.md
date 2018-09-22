### Steps to prepare exercises

1. Decompress taller.zip at /taller directory

2. Install mysql database in any node from the cluster or in a separated node. Create a new database called taller

3. Create a user taller with password taller and grant privileges to taller database.

4. Load data for sqoop ingest: mysql -u <user> -p <password> taller < orden.sql
