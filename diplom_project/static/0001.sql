BEGIN;
--
-- Create model Account
--
CREATE TABLE "main_account" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "login" varchar(30) NOT NULL,
    "password" varchar(30) NOT NULL,
    "email" varchar(50) NOT NULL);
COMMIT;
