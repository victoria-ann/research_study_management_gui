import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import db_functions as db
import pymysql
from controller.controller import Controller
from controller.sql_functions import SQLFunctions as sf

class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("MCGI Registry System")
        self.controller = None
        self.master.geometry("1500x700")
    
    def set_controller(self, controller):
        self.controller = controller
        self.create_widgets()


    def create_widgets(self):
        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill='both', expand=True)
        
        # Create and add tabs
        self.create_tabs()

    def create_tabs(self):
        # Welcome Tab
        self.tab_welcome = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_welcome, text="Welcome")
        self.setup_welcome_tab()

        # Participants Tab
        self.tab_participants = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_participants, text="Participants")
        self.notebook.pack(expand=1, fill="both")
        self.setup_participant_tab()

        # Consent Forms Tab
        self.tab_consent_forms = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_consent_forms, text="Consent Forms")
        self.setup_consent_form_tab()

        # Genomic Datasets Tab
        self.tab_datasets = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_datasets, text="Genomic Datasets")
        self.setup_genomic_dataset_tab()

        # Studies Tab
        self.tab_studies = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_studies, text="Studies")
        self.setup_study_tab()

        # Search and Summarize Tab
        self.tab_search = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_search, text="Search")
        self.setup_search_tab()

    def setup_welcome_tab(self):
        label = ttk.Label(self.tab_welcome, text="Welcome to the MCGI Registry System!", font=("Arial", 40))
        label.pack(pady=50)

    def setup_participant_tab(self):
        if self.controller is None:
            raise ValueError("Controller not set. Please set the controller before creating the participant tab.")

        label = ttk.Label(self.tab_participants, text="Manage Participants", font=("Arial", 14))
        label.pack(pady=10)

        # Frame for Search
        search_frame = ttk.Frame(self.tab_participants)
        search_frame.pack(pady=10, padx=10, fill="x", anchor="center")

        self.participant_id = tk.IntVar()

        ttk.Label(search_frame, text="Search By Participant ID:").grid(row=0, column=0, padx=5)
        self.search_participant_entry = ttk.Entry(search_frame, textvariable=self.participant_id, state="normal")
        self.search_participant_entry.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.controller.search_participants)
        search_button.grid(row=0, column=2, padx=5)

        self.participant_results_text = tk.Text(search_frame, height=10, width=80)
        self.participant_results_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


        # Frame for Participant Form
        form_frame = ttk.Frame(self.tab_participants)
        form_frame.pack(pady=10)

        self.name = tk.StringVar()
        self.age = tk.IntVar()
        self.sex = tk.StringVar()

        ttk.Label(form_frame, text="Participant ID:").grid(row=0, column=0, sticky='e')
        self.participant_id_entry = ttk.Entry(form_frame, textvariable=self.participant_id, state="normal")
        self.participant_id_entry.grid(row=0, column=1)

        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky='e')
        self.name_entry = ttk.Entry(form_frame, textvariable=self.name, state="normal")
        self.name_entry.grid(row=1, column=1)

        ttk.Label(form_frame, text="Age:").grid(row=2, column=0, sticky='e')
        self.age_entry = ttk.Entry(form_frame, textvariable=self.age, state="normal")
        self.age_entry.grid(row=2, column=1)

        ttk.Label(form_frame, text="Sex:").grid(row=3, column=0, sticky='e')
        self.sex_entry = ttk.Entry(form_frame, textvariable=self.sex, state="normal")
        self.sex_entry.grid(row=3, column=1)


        # Frame for Action Buttons
        button_frame = ttk.Frame(self.tab_participants)
        button_frame.pack(pady=10)

        add_button = ttk.Button(button_frame, text="Add Participant", command=self.controller.add_participant)
        add_button.grid(row=0, column=0, padx=5)

        edit_button = ttk.Button(button_frame, text="Edit Participant", command=self.controller.edit_participant)
        edit_button.grid(row=0, column=1, padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Participant", command=self.controller.delete_participant)
        delete_button.grid(row=0, column=2, padx=5)


    def setup_consent_form_tab(self):
        label = ttk.Label(self.tab_consent_forms, text="Manage Consent Forms", font=("Arial", 14))
        label.pack(pady=10)

        # Frame for Search
        search_frame = ttk.Frame(self.tab_consent_forms)
        search_frame.pack(pady=10, padx=10, fill="x", anchor="center")
        
        self.participant_id_for_consent = tk.IntVar()

        ttk.Label(search_frame, text="Search Consent Form by Participant ID:").grid(row=0, column=0, padx=5)
        self.search_consent_form_entry = ttk.Entry(search_frame, textvariable=self.participant_id_for_consent, state="normal")
        self.search_consent_form_entry.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.controller.search_consent_forms)
        search_button.grid(row=0, column=2, padx=5)

        self.consent_form_results_text = tk.Text(search_frame, height=10, width=80)
        self.consent_form_results_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Frame for Consent Form Form
        form_frame = ttk.Frame(self.tab_consent_forms)
        form_frame.pack(pady=10)

        self.date_signed = tk.StringVar()
        self.consent_form_id = tk.IntVar()

        ttk.Label(form_frame, text="Form ID:").grid(row=0, column=0, sticky='e')
        self.form_id_entry = ttk.Entry(form_frame, textvariable=self.consent_form_id, state="normal")
        self.form_id_entry.grid(row=0, column=1)


        ttk.Label(form_frame, text="Date Signed (YYYY-MM-DD):").grid(row=1, column=0, sticky='e')
        self.date_signed_entry = ttk.Entry(form_frame, textvariable=self.date_signed, state="normal")
        self.date_signed_entry.grid(row=1, column=1)

        ttk.Label(form_frame, text="Participant ID:").grid(row=2, column=0, sticky='e')
        self.participant_id_consent_entry = ttk.Entry(form_frame, textvariable=self.participant_id_for_consent, state="normal")
        self.participant_id_consent_entry.grid(row=2, column=1)

        # Frame for Action Buttons
        button_frame = ttk.Frame(self.tab_consent_forms)
        button_frame.pack(pady=10)

        add_button = ttk.Button(button_frame, text="Add Consent Form", command=self.controller.add_consent_form)
        add_button.grid(row=0, column=0, padx=5)

        edit_button = ttk.Button(button_frame, text="Edit Consent Form", command=self.controller.edit_consent_form)
        edit_button.grid(row=0, column=1, padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Consent Form", command=self.controller.delete_consent_form)
        delete_button.grid(row=0, column=2, padx=5)


    def setup_genomic_dataset_tab(self):
        label = ttk.Label(self.tab_datasets, text="Manage Genomic Datasets", font=("Arial", 14))
        label.pack(pady=10)

        # Frame for Search
        search_frame = ttk.Frame(self.tab_datasets)
        search_frame.pack(pady=10, padx=10, fill="x", anchor="center")

        self.dataset_participant_id = tk.IntVar()

        ttk.Label(search_frame, text="Search by Participant ID:").grid(row=0, column=0, padx=5)
        self.search_dataset_entry = ttk.Entry(search_frame, textvariable=self.dataset_participant_id, state="normal")
        self.search_dataset_entry.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.controller.search_genomic_dataset)
        search_button.grid(row=0, column=2, padx=5)

        self.dataset_results_text = tk.Text(search_frame, height=10, width=160)
        self.dataset_results_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        
        # Frame for Dataset Form
        form_frame = ttk.Frame(self.tab_datasets)
        form_frame.pack(pady=10)

        self.rna_sra_id = tk.StringVar()
        self.wgs_sra_id = tk.StringVar()
        self.rna_fastq_file = tk.StringVar()
        self.wgs_fastq_file = tk.StringVar()
        self.dataset_id = tk.IntVar()
        self.read_type = tk.StringVar()
        self.read_length = tk.IntVar()
        self.primers = tk.StringVar()
        self.bam_file = tk.StringVar()
        self.file_size = tk.IntVar()

        ttk.Label(form_frame, text="RNA Seq Dataset").grid(row=0, column=0, sticky='e')

        ttk.Label(form_frame, text="Dataset ID:").grid(row=1, column=0, sticky='e')
        self.sra_id_entry = ttk.Entry(form_frame, textvariable=self.dataset_id, state="normal")
        self.sra_id_entry.grid(row=1, column=1)
        
        ttk.Label(form_frame, text="SRA ID:").grid(row=2, column=0, sticky='e')
        self.sra_id_entry = ttk.Entry(form_frame, textvariable=self.rna_sra_id, state="normal")
        self.sra_id_entry.grid(row=2, column=1)

        ttk.Label(form_frame, text="Participant ID:").grid(row=3, column=0, sticky='e')
        self.fastq_file_entry = ttk.Entry(form_frame, textvariable=self.dataset_participant_id, state="normal")
        self.fastq_file_entry.grid(row=3, column=1)

        ttk.Label(form_frame, text="Fastq File:").grid(row=4, column=0, sticky='e')
        self.participant_id_dataset_entry = ttk.Entry(form_frame, textvariable=self.rna_fastq_file, state="normal")
        self.participant_id_dataset_entry.grid(row=4, column=1)
    
        
        ttk.Label(form_frame, text="Read Type:").grid(row=5, column=0, sticky='e')
        self.read_type_entry = ttk.Entry(form_frame, textvariable=self.read_type, state="normal")
        self.read_type_entry.grid(row=5, column=1)

        ttk.Label(form_frame, text="Read Length:").grid(row=6, column=0, sticky='e')
        self.read_length_entry = ttk.Entry(form_frame, textvariable=self.read_length, state="normal")
        self.read_length_entry.grid(row=6, column=1)

        ttk.Label(form_frame, text="Primers:").grid(row=7, column=0, sticky='e')
        self.primers_entry = ttk.Entry(form_frame, textvariable=self.primers, state="normal")
        self.primers_entry.grid(row=7, column=1)

        ttk.Label(form_frame, text="WGS Dataset").grid(row=0, column=2, sticky='e')

        ttk.Label(form_frame, text="Dataset ID:").grid(row=1, column=2, sticky='e')
        self.sra_id_entry = ttk.Entry(form_frame, textvariable=self.dataset_id, state="normal")
        self.sra_id_entry.grid(row=1, column=3)

        ttk.Label(form_frame, text="SRA ID:").grid(row=2, column=2, sticky='e')
        self.sra_id_entry = ttk.Entry(form_frame, textvariable=self.wgs_sra_id, state="normal")
        self.sra_id_entry.grid(row=2, column=3)

        ttk.Label(form_frame, text="Participant ID:").grid(row=3, column=2, sticky='e')
        self.fastq_file_entry = ttk.Entry(form_frame, textvariable=self.dataset_participant_id, state="normal")
        self.fastq_file_entry.grid(row=3, column=3)

        ttk.Label(form_frame, text="Fastq File:").grid(row=4, column=2, sticky='e')
        self.participant_id_dataset_entry = ttk.Entry(form_frame, textvariable=self.wgs_fastq_file, state="normal")
        self.participant_id_dataset_entry.grid(row=4, column=3)

        ttk.Label(form_frame, text="BAM File:").grid(row=5, column=2, sticky='e')
        self.bam_file_entry = ttk.Entry(form_frame, textvariable=self.bam_file, state="normal")
        self.bam_file_entry.grid(row=5, column=3)

        ttk.Label(form_frame, text="File Size:").grid(row=6, column=2, sticky='e')
        self.file_size_entry = ttk.Entry(form_frame, textvariable=self.file_size, state="normal")
        self.file_size_entry.grid(row=6, column=3)


        # Frame for Action Buttons
        button_frame = ttk.Frame(self.tab_datasets)
        button_frame.pack(pady=10)

        add_button = ttk.Button(button_frame, text="Add Dataset", command=self.controller.add_genomic_dataset)
        add_button.grid(row=0, column=0, padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Dataset", command=self.controller.delete_genomic_dataset)
        delete_button.grid(row=0, column=1, padx=5)

    def setup_study_tab(self):
        label = ttk.Label(self.tab_studies, text="Manage Studies", font=("Arial", 14))
        label.pack(pady=10)

        # Frame for Search
        search_frame = ttk.Frame(self.tab_studies)
        search_frame.pack(pady=10)
        search_frame.pack(pady=10, padx=10, fill="x", anchor="center")

        self.study_id = tk.IntVar()

        ttk.Label(search_frame, text="Search Study ID:").grid(row=0, column=0, padx=5)
        self.search_study_entry = ttk.Entry(search_frame, textvariable=self.study_id, state="normal")
        self.search_study_entry.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.controller.search_study)
        search_button.grid(row=0, column=2, padx=5)

        self.study_results_text = tk.Text(search_frame, height=20, width=90)
        self.study_results_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Frame for Study Form
        form_frame = ttk.Frame(self.tab_studies)
        form_frame.pack(pady=10)

        self.study_name = tk.StringVar()
        self.study_participant_id = tk.IntVar()
        self.study_dataset_id = tk.IntVar()

        ttk.Label(form_frame, text="Study ID:").grid(row=0, column=0, sticky='e')
        self.study_id_entry = ttk.Entry(form_frame, textvariable=self.study_id, state="normal")
        self.study_id_entry.grid(row=0, column=1)

        ttk.Label(form_frame, text="Study Name:").grid(row=1, column=0, sticky='e')
        self.study_name_entry = ttk.Entry(form_frame, textvariable=self.study_name, state="normal")
        self.study_name_entry.grid(row=1, column=1)

        ttk.Label(form_frame, text="Participant ID (to Add/Remove):").grid(row=2, column=0, sticky='e')
        self.study_participant_entry = ttk.Entry(form_frame, textvariable=self.study_participant_id, state="normal")
        self.study_participant_entry.grid(row=2, column=1)

        ttk.Label(form_frame, text="Dataset ID (to Add/Remove):").grid(row=3, column=0, sticky='e')
        self.study_dataset_entry = ttk.Entry(form_frame, textvariable=self.study_dataset_id, state="normal")
        self.study_dataset_entry.grid(row=3, column=1)

        # Frame for Action Buttons
        button_frame = ttk.Frame(self.tab_studies)
        button_frame.pack(pady=10)

        create_button = ttk.Button(button_frame, text="Create Study", command=self.controller.add_study)
        create_button.grid(row=0, column=0, padx=5)

        add_participant_button = ttk.Button(button_frame, text="Add Participant to Study", command=self.controller.add_participant_to_study)
        add_participant_button.grid(row=0, column=1, padx=5)

        remove_participant_button = ttk.Button(button_frame, text="Remove Participant from Study", command=self.controller.remove_participant_from_study)
        remove_participant_button.grid(row=0, column=2, padx=5)

        add_dataset_button = ttk.Button(button_frame, text="Add Dataset to Study", command=self.controller.add_dataset_to_study)
        add_dataset_button.grid(row=1, column=0, padx=5, pady=5)

        remove_dataset_button = ttk.Button(button_frame, text="Remove Dataset from Study", command=self.controller.remove_dataset_from_study)
        remove_dataset_button.grid(row=1, column=1, padx=5, pady=5)

        delete_study_button = ttk.Button(button_frame, text="Delete Study", command=self.controller.delete_study)
        delete_study_button.grid(row=1, column=2, padx=5, pady=5)

    def setup_search_tab(self):
        label = ttk.Label(self.tab_search, text="Browse Studies and Available Participants", font=("Arial", 14))
        label.pack(pady=10)

        # Frame for Participant Search
        participant_search_frame = ttk.LabelFrame(self.tab_search, text="Browse Participants")
        participant_search_frame.pack(pady=10, padx=10, fill="x")

        participant_search_button = ttk.Button(participant_search_frame, text="Browse", command=self.controller.browse_participants)
        participant_search_button.grid(row=0, column=0, padx=5, pady=5)

        self.all_participants_results_text = tk.Text(participant_search_frame, height=15, width=80)
        self.all_participants_results_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Frame for Study Search
        study_search_frame = ttk.LabelFrame(self.tab_search, text="Browse Studies")
        study_search_frame.pack(pady=10, padx=10, fill="x")

        study_search_button = ttk.Button(study_search_frame, text="Browse", command=self.controller.browse_studies)
        study_search_button.grid(row=0, column=0, padx=5, pady=5)

        self.all_studies_text = tk.Text(study_search_frame, height=15, width=80)
        self.all_studies_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(master=root)
    app.pack(fill='both', expand=True)
    app.mainloop()








    