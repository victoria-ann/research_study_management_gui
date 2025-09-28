import db_functions as db
import pymysql
from tkinter import messagebox
import pymysql
from model.participant import Participant
from pymysql import DatabaseError

class SQLSetup:
    def __init__(self):
        pass

    def sql_load_participants_from_db(self):
        # connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        sql = "SELECT * FROM participant"
        try:
            num_of_rows, rows = db.query_database(con, sql, None)
        except pymysql.ProgrammingError as e:
            print("Error loading participants:", e)

        return num_of_rows, rows
    
    def sql_load_studies(self):
        # connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        sql = "SELECT * FROM research_study"
        try:
            num_of_rows, rows = db.query_database(con, sql, None)
        except pymysql.ProgrammingError as e:
            print("Error loading studies:", e)

        return num_of_rows, rows
    
class SQLFunctions:
    def __init__(self):
        pass
    def sql_add_participant(participant):
        # connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        try:
            sql = "INSERT INTO participant (participant_id, name, age, sex) VALUES (%s, %s, %s, %s)"
            values = (participant.participant_id, participant.name, participant.age, participant.sex)
            db.insert_database(con, sql, values)
            messagebox.showinfo("Success", "Participant added successfully")
        except pymysql.ProgrammingError as e:
            print("Error adding participant:", e)
        #cursor = con.cursor()
        #cursor.execute(sql, values)
        #con.commit()
        con.close()

    def sql_delete_participant(participant_id):
        # connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        try:
            sql = "DELETE FROM participant WHERE participant_id = %s"
            values = (participant_id,)
            db.insert_database(con, sql, values)
            messagebox.showinfo("Success", "Participant deleted successfully")
        except pymysql.ProgrammingError as e:
            print("Error deleting participant:", e)
        #cursor = con.cursor()
        #cursor.execute(sql, values)
        #con.commit()
        con.close()

    def sql_update_participant(participant_id, name, age, sex):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()

        try:
            sql = """
            UPDATE participant
            SET name = %s,
                age = %s,
                sex = %s
            WHERE participant_id = %s
            """
            values = (name, age, sex, participant_id)
            db.insert_database(con, sql, values)
            con.close()
        except pymysql.ProgrammingError as e:
            print("Error updating participant:", e)

    def sql_search_participant(participant_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()

        sql = "SELECT participant_id, name, age, sex FROM participant WHERE participant_id = %s"
        values = (participant_id)
        try:
            num_of_rows, rows = db.query_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error searching participant:", e)
        return num_of_rows, rows
    
    def sql_add_consent_form(consent_form):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
       
        try:
            sql = """
            INSERT INTO consent_form (consent_form_id, date_signed, participant_participant_id)
            VALUES (%s, %s, %s)
            """
            values = (consent_form.form_id, consent_form.date_signed, consent_form.participant_id)
            db.insert_database(con, sql, values)
            con.close()
            print(f"Consent form {consent_form.form_id} added for participant {consent_form.participant_id}.")
        except pymysql.ProgrammingError as e:
            print("Error adding consent form:", e)
            messagebox.showinfo("Error", "Error adding consent form")

    def sql_delete_consent_form(consent_form_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = "DELETE FROM consent_form WHERE consent_form_id = %s"
            values = consent_form_id
            db.insert_database(con, sql, values)
            con.close()
        except pymysql.ProgrammingError as e:
            print("Error removing consent form:", e)

    def sql_search_consent_forms(participant_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        sql = """
        SELECT p.participant_id, p.name,
            cf.consent_form_id, cf.date_signed
        FROM participant p
        LEFT JOIN consent_form cf ON p.participant_id = cf.participant_participant_id
        WHERE p.participant_id = %s
        """
        value = participant_id
        try:
            num_of_rows, rows = db.query_database(con, sql, value)
            return num_of_rows, rows
        except pymysql.ProgrammingError as e:
            print("Error searching consent forms:", e)
            messagebox.showinfo("Error", "Error searching consent forms")
    
    def sql_edit_consent_form(form_id, participant_id, date_signed):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        try:
            sql = """
            UPDATE consent_form
            SET date_signed = %s
            WHERE consent_form_id = %s AND participant_participant_id = %s;
            """
            values = (date_signed, form_id, participant_id)
            db.insert_database(con, sql, values)
            con.close()
        except pymysql.ProgrammingError as e:
            print("Error updating consent form:", e)
            raise DatabaseError(e)

    def sql_add_rna_dataset(rna_seq_dataset, participant_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            INSERT INTO dataset (dataset_id, sra_id, fastq_file, read_type, read_length, primers, participant_participant_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (rna_seq_dataset.dataset_id,
                      rna_seq_dataset.sra_id,
                      rna_seq_dataset.fastq_file,
                      rna_seq_dataset.read_type,
                      rna_seq_dataset.read_length,
                      rna_seq_dataset.primers,
                      participant_id)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error adding RNA dataset:", e)
        con.close()

    def sql_add_wgs_dataset(wgs_dataset, participant_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            INSERT INTO dataset (dataset_id, sra_id, fastq_file, bam_file, file_size, participant_participant_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (wgs_dataset.dataset_id,
                      wgs_dataset.sra_id,
                      wgs_dataset.fastq_file,
                      wgs_dataset.bam_file,
                      wgs_dataset.file_size,
                      participant_id)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error adding WGS dataset:", e)
        con.close()

    def sql_search_dataset(participant_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
                SELECT d.*, p.name
                FROM dataset d
                JOIN participant p ON d.participant_participant_id = p.participant_id
                WHERE p.participant_id = %s
            """
            value = participant_id
            num_of_rows, rows = db.query_database(con, sql, value)
            return num_of_rows, rows
        except pymysql.ProgrammingError as e:
            print("Error searching dataset:", e)
            messagebox.showinfo("Error", "Error searching dataset")

    def sql_delete_dataset(dataset_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = "DELETE FROM dataset WHERE dataset_id = %s"
            values = dataset_id
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error deleting dataset:", e)
        con.close()

    def sql_add_study(study):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            INSERT INTO research_study (study_id, study_name)
            VALUES (%s, %s)
            """
            values = (study.study_id, study.study_name)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error adding study:", e)
        con.close()

    def sql_search_study(study_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        sql = """
            SELECT 
                s.study_id, s.study_name, 
                p.participant_id, p.name,
                d.dataset_id, d.sra_id
            FROM research_study s
            JOIN study_participants sp ON s.study_id = sp.research_study_study_id
            JOIN participant p ON sp.participant_participant_id = p.participant_id
            JOIN study_datasets sd ON s.study_id = sd.research_study_study_id
            JOIN dataset d ON sd.dataset_dataset_id = d.dataset_id
            WHERE sp.participant_participant_id = d.participant_participant_id
            AND s.study_id = %s
            ORDER BY p.participant_id, d.dataset_id
            """
        values = study_id
        try:
            num_of_rows, rows = db.query_database(con, sql, values)
            return num_of_rows, rows
        except pymysql.ProgrammingError as e:
            print("Error searching study:", e)
            messagebox.showinfo("Error", "Error searching study")

    def sql_delete_study(study_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = "DELETE FROM research_study WHERE study_id = %s"
            values = study_id
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error deleting study:", e)
        con.close()

    def sql_add_participant_to_study(participant_id, study_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            INSERT INTO study_participants (research_study_study_id, participant_participant_id)
            VALUES (%s, %s)
            """
            values = (study_id, participant_id)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error adding participant to study:", e)
        con.close()

    def sql_remove_participant_from_study(participant_id, study_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            DELETE FROM study_participants
            WHERE research_study_study_id = %s AND participant_participant_id = %s
            """
            values = (study_id, participant_id)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error removing participant from study:", e)
        con.close()
    
    def sql_add_dataset_to_study(dataset_id, study_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            INSERT INTO study_datasets (research_study_study_id, dataset_dataset_id)
            VALUES (%s, %s)
            """
            values = (study_id, dataset_id)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error adding dataset to study:", e)
        con.close()

    def sql_remove_dataset_from_study(dataset_id, study_id):
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        try:
            sql = """
            DELETE FROM study_datasets
            WHERE research_study_study_id = %s AND dataset_dataset_id = %s
            """
            values = (study_id, dataset_id)
            db.insert_database(con, sql, values)
        except pymysql.ProgrammingError as e:
            print("Error removing dataset from study:", e)
        con.close()

    def sql_search_all_participants():
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        sql = "SELECT * FROM participant"
        try:
            num_of_rows, rows = db.query_database(con, sql, None)
            return num_of_rows, rows
        except pymysql.ProgrammingError as e:
            print("Error searching all participants:", e)
            messagebox.showinfo("Error", "Error searching all participants")

    def sql_search_all_studies():
        #connect to DB
        try:
            con = db.open_database()
        except (Exception) as e:
            messagebox.showinfo("Database connection error")
            exit()
        
        sql = "SELECT * FROM research_study"
        try:
            num_of_rows, rows = db.query_database(con, sql, None)
            return num_of_rows, rows
        except pymysql.ProgrammingError as e:
            print("Error searching all studies:", e)
            messagebox.showinfo("Error", "Error searching all studies")