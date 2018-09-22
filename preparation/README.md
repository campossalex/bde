### Steps to prepare exercises

1. Decompress taller.zip at /taller directory

2. Install mysql database in any node from the cluster or in a separated node. 

3. Create a new database called taller  
`CRREATE DATABASE taller;`

4. Create a user taller with password taller and grant privileges to taller database.  
`GRANT ALL PRIVILEGES ON taller.* TO 'taller'@'%' IDENTIFIED BY 'taller';`

5. Load data for sqoop ingest  
`mysql -u <user> -p <password> taller < orden.sql`
