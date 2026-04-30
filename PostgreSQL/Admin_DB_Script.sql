SET search_path TO public;

-- admin table
CREATE TABLE IF NOT EXISTS admin (
  admin_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name  VARCHAR(100) NOT NULL,
  university_name VARCHAR(100),
  university_occupation VARCHAR(100)
);

-- credential table 
CREATE TABLE IF NOT EXISTS credential (
  credential_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  password_hash TEXT NOT NULL,
  start_date DATE NOT NULL DEFAULT CURRENT_DATE,
  end_date   DATE,
  admin_id INT NOT NULL,
 
-- User_Feedback Table
CREATE TABLE IF NOT EXISTS user_feedback (
    feedback_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    rating INT,
    suggestion TEXT,
    issue TEXT,
    submitted_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    admin_id INT,

    CONSTRAINT fk_user_feedback_admin
    FOREIGN KEY (admin_id)
    REFERENCES admin(admin_id)
    ON DELETE SET NULL
);

-- Dataset_Import Table
CREATE TABLE IF NOT EXISTS dataset_import (
    import_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    file_name VARCHAR(255),
    file_type VARCHAR(50),
    file_size BIGINT,
    source VARCHAR(100),
    import_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50),
    admin_id INT NOT NULL,

    CONSTRAINT fk_dataset_import_admin
    FOREIGN KEY (admin_id)
    REFERENCES admin(admin_id)
    ON DELETE CASCADE
);
  
  
--FK Constraints 
  CONSTRAINT fk_credential_admin
    FOREIGN KEY (admin_id)
    REFERENCES admin(admin_id)
    ON DELETE CASCADE,

  CONSTRAINT chk_credential_dates
    CHECK (end_date IS NULL OR end_date >= start_date)
);

--Email is unique 
CREATE UNIQUE INDEX IF NOT EXISTS ux_credential_email
ON credential (email);

-- Speed up joins
CREATE INDEX IF NOT EXISTS ix_credential_admin_id
ON credential (admin_id);

-- Optional for only 1 active credential per admin (end_date IS NULL)
CREATE UNIQUE INDEX IF NOT EXISTS ux_one_active_credential_per_admin
ON credential (admin_id)
WHERE end_date IS NULL;


-- Password Reset Table
create table password_reset (
reset_id BIGSERIAL primary key, 
credential_id INT not null, 
token_hash TEXT not null, 
expires_at TIMESTAMPTZ not null, 
used_at TIMESTAMPTZ null, 
created_at TIMESTAMPTZ not null default now(), 

constraint fk_password_reset_credential
foreign key (credential_id)
references credential (credential_id)
on delete cascade 
);

--Speed up searches when looking for rows in password_reset by token_hash
CREATE INDEX IF NOT EXISTS idx_password_reset_token_hash
ON password_reset(token_hash);


--Test
select * from admin
select * from credential
SELECT * FROM password_reset LIMIT 1;
select * from password_reset 

SELECT
  credential_id,
  email,
  start_date,
  end_date,
  admin_id
FROM credential
ORDER BY credential_id DESC;

--delete code 
delete from admin 
where last_name = 'Ansari'



ALTER TABLE public.credential
ADD COLUMN last_login_at TIMESTAMP NULL;

SELECT email, last_login_at
FROM public.credential
ORDER BY last_login_at DESC;



SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public';

select * from user_feedback

select * from dataset_import





