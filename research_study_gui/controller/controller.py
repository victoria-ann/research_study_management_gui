from model.registry_manager import RegistryManager
from model.participant import Participant, ConsentForm
from model.research_study import ResearchStudy
from model.genomic_dataset import RNASeqDataset, WGSDataset
from controller.sql_functions import SQLFunctions as sf
import tkinter as tk
from tkinter import messagebox

class Controller:
    def __init__(self, view, registry_manager):
        self.view = view
        #self.registry_manager = RegistryManager()
        self.registry_manager = registry_manager


    def add_participant(self):
        participant_id = self.view.participant_id.get()
        name = self.view.name.get()
        age = self.view.age.get()
        sex = self.view.sex.get()

        empty_textbox = 0
        if participant_id == "":
            empty_textbox = empty_textbox + 1
        if name == "":
            empty_textbox = empty_textbox + 1
        if age == "":
            empty_textbox = empty_textbox + 1
        if sex == "":
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in all fields")
            raise Exception("empty textbox", "Please fill in all fields")

        particpant = Participant(participant_id, name, age, sex)
        
        try:
            self.registry_manager.register_participant(particpant)
        except ValueError as e:
            messagebox.showinfo("Error", "Error Registering Participant")
            print(f"Error registering participant: {e}")
            return
        try:
            sf.sql_add_participant(particpant)
        except Exception as e:
            print(f"Error adding participant to database: {e}")
            return

    def delete_participant(self):
        participant_id = self.view.participant_id.get()

        try:
            registry_participant_to_remove = None
            for participant in self.registry_manager.participants:
                if participant.participant_id == participant_id:
                    registry_participant_to_remove = participant
                    break
        except:
            print(f"Participant {participant_id} not found in registry.")
            return
       
        if registry_participant_to_remove:
            for study in self.registry_manager.studies:
                study.participants = [p for p in study.participants if p.participant_id != participant_id]
    
            try:
                self.registry_manager.remove_participant(participant_id)
            except Exception as e:
                print(f"Error removing participant from registry: {e}")
                return
        try:
            sf.sql_delete_participant(participant_id)
            messagebox.showinfo("Success", "Participant deleted successfully")
            print(f"Participant {participant_id} removed from registry db.")
        except Exception as e:
            messagebox.showinfo("Error", "Error removing participant from database")
            print(f"Error removing participant from database: {e}")
            return

    def edit_participant(self):

        participant_id = self.view.participant_id.get()
        name = self.view.name.get()
        age = self.view.age.get()
        sex = self.view.sex.get().lower()

        empty_textbox = 0
        if participant_id == 0:
            empty_textbox = empty_textbox + 1
        if name == "":
            empty_textbox = empty_textbox + 1
        if age == 0:
            empty_textbox = empty_textbox + 1
        if sex == "":
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in all fields")
            raise Exception("empty textbox", "Please fill in all fields")
        
        if sex not in ("male", "female"):
            messagebox.showinfo("Error", "Sex must be male or female")
            raise Exception("Sex entered is not male or female")
        
        participant_to_edit = None
        for participant in self.registry_manager.participants:
            if participant.participant_id == participant_id:
                participant_to_edit = participant
                break

        if participant_to_edit:
            participant_to_edit.name = name
            participant_to_edit.age = age
            participant_to_edit.sex = sex
            print(f"Participant {participant_id} updated.")
        
        try:
            sf.sql_update_participant(participant_id, name, age, sex)
            messagebox.showinfo("Success", "Participant updated successfully")
        except Exception as e: 
            messagebox.showinfo("Error", "Error updating participant in database")
            print(f"Error updating participant in database: {e}")
            return
        
    def search_participants(self):
        participant_id = self.view.participant_id.get()
        
        num_of_rows, rows = sf.sql_search_participant(participant_id)

        if num_of_rows > 0 and rows:
            row = rows[0]  # first row (tuple)
            display_text = (
                f"Participant ID: {row[0]}\n"
                f"Name: {row[1]}\n"
                f"Age: {row[2]}\n"
                f"Sex: {row[3]}")
            print(display_text)
        else:
            display_text = "Participant not found."
            print("Participant not found.")

        self.view.participant_results_text.delete("1.0", tk.END)
        self.view.participant_results_text.insert(tk.END, display_text)
        self.view.master.update_idletasks()  

    def add_consent_form(self):
        participant_id = self.view.participant_id_for_consent.get()
        form_id = self.view.consent_form_id.get()
        date_signed = self.view.date_signed.get()


        empty_textbox = 0
        if participant_id == 0:
            empty_textbox = empty_textbox + 1
        if form_id == 0:
            empty_textbox = empty_textbox + 1
        if date_signed == "":
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in all fields")
            raise Exception("empty textbox", "Please fill in all fields")

        consent_form = ConsentForm(form_id, date_signed, participant_id)
        
        try:
            sf.sql_add_consent_form(consent_form)
            messagebox.showinfo("Success", "Consent form added successfully")
            print(f"Consent form {form_id} added for participant {participant_id}.")
        except Exception as e:
            messagebox.showinfo("Error", "Error adding consent form to database")
            print(f"Error adding consent form to database: {e}")
            return

        try:
            self.registry_manager.add_consent_form(participant_id, consent_form)
        except ValueError as e:
            messagebox.showinfo("Error", "Error adding consent form")
            print(f"Error adding consent form: {e}")
            return
        
    def delete_consent_form(self):
        form_id = self.view.consent_form_id.get()
        participant_id = self.view.participant_id_for_consent.get()

        try:
            sf.sql_delete_consent_form(form_id)
            messagebox.showinfo("Success", "Consent form deleted successfully")
            print(f"Consent form {form_id} removed from registry db.")
        except Exception as e:
            messagebox.showinfo("Error", "Error removing consent form from database")
            print(f"Error removing consent form from database: {e}")
            return

        try:
            result = self.registry_manager.remove_consent_form(participant_id, form_id)
            if result == True:
                print(f"Consent form {form_id} removed from participant {participant_id}.")
            else:
                print(f"Consent form {form_id} not found for participant {participant_id}.")
        except ValueError as e:
            messagebox.showinfo("Error", "Error removing consent form")
            print(f"Error removing consent form: {e}")

    def edit_consent_form(self):
        form_id = self.view.consent_form_id.get()
        participant_id = self.view.participant_id_for_consent.get()
        date_signed = self.view.date_signed.get()

        empty_textbox = 0
        if form_id == 0:
            empty_textbox = empty_textbox + 1
        if participant_id == 0:
            empty_textbox = empty_textbox + 1
        if date_signed == "":
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in all fields")
            raise Exception("empty textbox", "Please fill in all fields")
        
        try:
            sf.sql_edit_consent_form(form_id, participant_id, date_signed)
            messagebox.showinfo("Success", "Consent form updated successfully")
        except Exception as e: 
            messagebox.showinfo("Error", "Error updating consent form in database")
            print(f"Error updating consent form in database: {e}")
            return

        consent_form_to_edit = None
        for participant in self.registry_manager.participants:
            if participant.participant_id == participant_id:
                for consent_form in participant.consent_forms:
                    if consent_form.form_id == form_id:
                        consent_form_to_edit = consent_form
                        break
                break

        if consent_form_to_edit:
            consent_form_to_edit.date_signed = date_signed
            print(f"Consent form {form_id} updated for participant {participant_id}.")
        
    def search_consent_forms(self):
        participant_id = self.view.participant_id_for_consent.get()

        num_of_rows, rows = sf.sql_search_consent_forms(participant_id)

        if num_of_rows > 0 and rows:
            lines = []
            participant_id, name = rows[0][0], rows[0][1]
            lines.append(f"Participant ID: {participant_id}")
            lines.append(f"Name: {name}")
            lines.append("Consent Forms:")
        
            for row in rows:
                form_id = row[2]
                date_signed = row[3]
                lines.append(f"  - Form ID: {form_id}, Date Signed: {date_signed}")
            
            display = "\n".join(lines)
            print("\n".join(lines))
        else:
            display = "No consent forms found for this participant."

        self.view.consent_form_results_text.delete("1.0", tk.END)
        self.view.consent_form_results_text.insert(tk.END, display)
        self.view.master.update_idletasks() 

    def add_genomic_dataset(self):
        participant_id = self.view.dataset_participant_id.get()
        rna_sra_id = self.view.rna_sra_id.get()
        wgs_sra_id = self.view.wgs_sra_id.get()
        rna_fastq_file = self.view.rna_fastq_file.get()
        wgs_fastq_file = self.view.wgs_fastq_file.get()
        bam_file = self.view.bam_file.get()
        file_size = self.view.file_size.get()
        read_type = self.view.read_type.get()
        read_length = self.view.read_length.get()
        primers = self.view.primers.get()
        dataset_id = self.view.dataset_id.get()

        if wgs_sra_id == "":
            empty_textbox = 0
            if participant_id == 0:
                empty_textbox = empty_textbox + 1
            if rna_sra_id == "":
                empty_textbox = empty_textbox + 1
            if rna_fastq_file == "":
                empty_textbox = empty_textbox + 1
            if dataset_id == 0:
                empty_textbox = empty_textbox + 1
            if read_type == "":
                empty_textbox = empty_textbox + 1
            if read_length == 0:
                empty_textbox = empty_textbox + 1
            if primers == "":
                empty_textbox = empty_textbox + 1
            if empty_textbox > 0:
                messagebox.showinfo("Error", "Please fill in all fields")
                raise Exception("empty textbox", "Please fill in all fields")
            
            fastq_file = rna_fastq_file
            sra_id = rna_sra_id

            rnaseq_dataset = RNASeqDataset(dataset_id, sra_id, fastq_file, read_type, read_length, primers)

            try:
                sf.sql_add_rna_dataset(rnaseq_dataset, participant_id)
                messagebox.showinfo("Success", "RNA dataset added successfully")
                print(f"RNA dataset {dataset_id} added for participant {participant_id}.")
            except Exception as e:
                messagebox.showinfo("Error", "Error adding RNA dataset to database")
                print(f"Error adding RNA dataset to database: {e}")
                return
            
            try:
                self.registry_manager.add_dataset_to_participant(participant_id, rnaseq_dataset)
            except ValueError as e:
                messagebox.showinfo("Error", "Error adding WGS dataset")
                print(f"Error adding WGS dataset: {e}")
                return
            
        elif rna_sra_id == "":
            empty_textbox = 0
            if participant_id == 0:
                empty_textbox = empty_textbox + 1
            if wgs_sra_id == "":
                empty_textbox = empty_textbox + 1
            if wgs_fastq_file == "":
                empty_textbox = empty_textbox + 1
            if bam_file == "":
                empty_textbox = empty_textbox + 1
            if file_size == 0.0:
                empty_textbox = empty_textbox + 1
            if dataset_id == 0:
                empty_textbox = empty_textbox + 1
            if empty_textbox > 0:
                messagebox.showinfo("Error", "Please fill in all fields")
                raise Exception("empty textbox", "Please fill in all fields")

            fastq_file = wgs_fastq_file
            sra_id = wgs_sra_id

            wgs_dataset = WGSDataset(dataset_id, sra_id, fastq_file, bam_file, file_size)

            try:
                sf.sql_add_wgs_dataset(wgs_dataset, participant_id)
                messagebox.showinfo("Success", "WGS dataset added successfully")
                print(f"WGS dataset {dataset_id} added for participant {participant_id}.")
            except Exception as e:
                messagebox.showinfo("Error", "Error adding WGS dataset to database")
                print(f"Error adding WGS dataset to database: {e}")
                return
            
            try:
                self.registry_manager.add_dataset_to_participant(participant_id, wgs_dataset)
            except ValueError as e:
                messagebox.showinfo("Error", "Error adding WGS dataset")
                print(f"Error adding WGS dataset: {e}")
                return
    
    def delete_genomic_dataset(self):
        dataset_id = self.view.dataset_id.get()

        try:
            sf.sql_delete_dataset(dataset_id)
            messagebox.showinfo("Success", "Dataset deleted successfully")
            print(f"Dataset {dataset_id} removed from registry db.")
        except Exception as e:
            messagebox.showinfo("Error", "Error removing dataset from database")
            print(f"Error removing dataset from database: {e}")
            return

    def search_genomic_dataset(self):
        participant_id = self.view.dataset_participant_id.get()
        num_of_rows, rows = sf.sql_search_dataset(participant_id)
        if num_of_rows > 0 and rows:
            # Assume participant ID and name are in columns 8 and 9 of each row
            participant_id = rows[0][8]
            participant_name = rows[0][9]

            lines = [
                f"Participant ID: {participant_id}",
                f"Name: {participant_name}",
                "Datasets:"
            ]

            for row in rows:
                dataset_id = row[0]
                sra_id = row[1]
                fastq_file = row[2]
                read_type = row[3]
                read_length = row[4]
                primers = row[5]
                bam_file = row[6]
                file_size = row[7]

                # Construct dataset details
                dataset_line = f"  - Dataset ID: {dataset_id}, SRA ID: {sra_id}, FASTQ File: {fastq_file}"

                if read_type and read_length and primers:
                    dataset_line += f", Read Type: {read_type}, Read Length: {read_length}, Primers: {primers}"
                elif bam_file and file_size is not None:
                    dataset_line += f", BAM File: {bam_file}, File Size: {file_size} GB"

                lines.append(dataset_line)

            display = "\n".join(lines)
            print(display)
        else:
            display = "No datasets found for this participant."
            print("No datasets found for this participant.")
        self.view.dataset_results_text.delete("1.0", tk.END)
        self.view.dataset_results_text.insert(tk.END, display)
        self.view.master.update_idletasks()

    def add_study(self):
        study_id = self.view.study_id.get()
        study_name = self.view.study_name.get()

        empty_textbox = 0
        if study_id == 0:
            empty_textbox = empty_textbox + 1
        if study_name == "":
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in all fields")
            raise Exception("empty textbox", "Please fill in all fields")

        study = ResearchStudy(study_id, study_name)
        
        try:
            sf.sql_add_study(study)
            messagebox.showinfo("Success", "Study added successfully")
            print(f"Study {study_name} added.")
        except Exception as e:
            messagebox.showinfo("Error", "Error adding study to database")
            print(f"Error adding study to database: {e}")
            return
        
        try:
            self.registry_manager.create_study(study)
        except ValueError as e:
            messagebox.showinfo("Error", "Error adding study")
            print(f"Error adding study: {e}")
            return

    def delete_study(self):
        study_id = self.view.study_id.get()

        try:
            sf.sql_delete_study(study_id)
            messagebox.showinfo("Success", "Study deleted successfully")
            print(f"Study {study_id} removed from registry db.")
        except Exception as e:
            messagebox.showinfo("Error", "Error removing study from database")
            print(f"Error removing study from database: {e}")
            return

        try:
            self.registry_manager.remove_study(study_id)
        except ValueError as e:
            messagebox.showinfo("Error", "Error removing study")
            print(f"Error removing study: {e}")
            return

    def search_study(self):
        study_id = self.view.study_id.get()

        num_of_rows, rows = sf.sql_search_study(study_id)
        try:
            if num_of_rows > 0 and rows:
                lines = []

                # Get study info from the first row
                study_id = rows[0][0]
                study_name = rows[0][1]
                lines.append(f"Study ID: {study_id}")
                lines.append(f"Study Name: {study_name}")
                lines.append("")  # Blank line for spacing

                current_participant_id = None

                for row in rows:
                    _, _, participant_id, participant_name, dataset_id, sra_id = row

                    # If we've moved to a new participant, add their header
                    if participant_id != current_participant_id:
                        lines.append(f"Participant ID: {participant_id}, Name: {participant_name}")
                        current_participant_id = participant_id

                    # Add dataset info indented under participant
                    lines.append(f"    - Dataset ID: {dataset_id}, SRA ID: {sra_id}")

                display = "\n".join(lines)
            else:
                display = "No results found."
        except Exception as e:
            messagebox.showinfo("Error", "Error searching study")
            print(f"Error searching study: {e}")
            return

        self.view.study_results_text.delete("1.0", tk.END)
        self.view.study_results_text.insert(tk.END, display)
        self.view.master.update_idletasks()

    def add_participant_to_study(self):
        participant_id = self.view.study_participant_id.get()
        study_id = self.view.study_id.get()

        empty_textbox = 0
        if participant_id == 0:
            empty_textbox = empty_textbox + 1
        if study_id == 0:
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in necessary fields")
            raise Exception("empty textbox", "Please fill in necessary fields")
        
        try:
            sf.sql_add_participant_to_study(participant_id, study_id)
            messagebox.showinfo("Success", "Participant added to study successfully")
            print(f"Participant {participant_id} added to study {study_id}.")
        except Exception as e:
            messagebox.showinfo("Error", "Error adding participant to study")
            print(f"Error adding participant to study: {e}")
            return

        try:
            self.registry_manager.assign_participant_to_study(participant_id, study_id)
        except ValueError as e:
            print(f"Error adding participant to study: {e}")
            return
    
    def remove_participant_from_study(self):
        participant_id = self.view.study_participant_id.get()
        study_id = self.view.study_id.get()

        empty_textbox = 0
        if participant_id == 0:
            empty_textbox = empty_textbox + 1
        if study_id == 0:
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in necessary fields")
            raise Exception("empty textbox", "Please fill in necessary fields")

        try:
            sf.sql_remove_participant_from_study(participant_id, study_id)
            messagebox.showinfo("Success", "Participant removed from study successfully")
            print(f"Participant {participant_id} removed from study {study_id}.")
        except Exception as e:
            messagebox.showinfo("Error", "Error removing participant from study")
            print(f"Error removing participant from study: {e}")
            return

        try:
            self.registry_manager.remove_participant_from_study(participant_id, study_id)
        except ValueError as e:
            messagebox.showinfo("Error", "Error removing participant from study")
            print(f"Error removing participant from study: {e}")
            return
        
    def add_dataset_to_study(self):
        dataset_id = self.view.study_dataset_id.get()
        study_id = self.view.study_id.get()

        empty_textbox = 0
        if dataset_id == 0:
            empty_textbox = empty_textbox + 1
        if study_id == 0:
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in necessary fields")
            raise Exception("empty textbox", "Please fill in necessary fields")

        try:
            sf.sql_add_dataset_to_study(dataset_id, study_id)
            messagebox.showinfo("Success", "Dataset added to study successfully")
            print(f"Dataset {dataset_id} added to study {study_id}.")
        except Exception as e:
            messagebox.showinfo("Error", "Error adding dataset to study")
            print(f"Error adding dataset to study: {e}")
            return
        
    def remove_dataset_from_study(self):
        dataset_id = self.view.study_dataset_id.get()
        study_id = self.view.study_id.get()

        empty_textbox = 0
        if dataset_id == 0:
            empty_textbox = empty_textbox + 1
        if study_id == 0:
            empty_textbox = empty_textbox + 1
        if empty_textbox > 0:
            messagebox.showinfo("Error", "Please fill in necessary fields")
            raise Exception("empty textbox", "Please fill in necessary fields")

        try:
            sf.sql_remove_dataset_from_study(dataset_id, study_id)
            messagebox.showinfo("Success", "Dataset removed from study successfully")
            print(f"Dataset {dataset_id} removed from study {study_id}.")
        except Exception as e:
            messagebox.showinfo("Error", "Error removing dataset from study")
            print(f"Error removing dataset from study: {e}")
            return

        try:
            self.registry_manager.remove_dataset_from_study(study_id, dataset_id)
        except ValueError as e:
            messagebox.showinfo("Error", "Error removing dataset from study")
            print(f"Error removing dataset from study: {e}")
            return
   
    def browse_participants(self):
        num_of_rows, rows = sf.sql_search_all_participants()

        if num_of_rows > 0 and rows:
            lines = []
            lines.append("All Participants:\n")
            lines.append(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Sex':<10}")
            lines.append("-" * 45)

            for row in rows:
                participant_id, name, age, sex = row
                lines.append(f"{participant_id:<5} {name:<20} {age:<5} {sex:<10}")

            display = "\n".join(lines)
        else:
            display = "No participants found."
        
        self.view.all_participants_results_text.delete("1.0", tk.END)
        self.view.all_participants_results_text.insert(tk.END, display)
        self.view.master.update_idletasks()

    def browse_studies(self):
        num_of_rows, rows = sf.sql_search_all_studies()

        if num_of_rows > 0 and rows:
            lines = []
            lines.append("All Research Studies:\n")
            lines.append(f"{'ID':<5} {'Study Name'}")
            lines.append("-" * 60)

            for row in rows:
                study_id, study_name = row
                lines.append(f"{study_id:<5} {study_name}")

            display = "\n".join(lines)
        else:
            display = "No studies found."

        self.view.all_studies_text.delete("1.0", tk.END)
        self.view.all_studies_text.insert(tk.END, display)
        self.view.master.update_idletasks()

    