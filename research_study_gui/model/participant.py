# This module defines classes for managing participant information and consent forms in a genomic study.
from model.genomic_dataset import GenomicDataset

class ConsentForm:
    def __init__(self, form_id, date_signed, participant_id):
        self.form_id = form_id
        self.date_signed = date_signed
        self.participant_id = participant_id

class Participant:
    def __init__(self, participant_id, name, age, sex):
        self.participant_id = participant_id
        self.name = name
        self.age = age
        self.sex = sex
        self.consent_forms = []
        self.genomic_datasets = []

    def add_consent_form(self, consent_form: ConsentForm):
        if not isinstance(consent_form, ConsentForm):
            raise ValueError("Invalid consent form type. Must be a ConsentForm.")
        self.consent_forms.append(consent_form)
        print(f"Consent form {consent_form.form_id} added for participant {self.participant_id}.")

    def remove_consent_form(self, form_id):
        for form in self.consent_forms:
            if form.form_id == form_id:
                self.consent_forms.remove(form)
                print(f"Consent form {form_id} removed for participant {self.participant_id}.")
            else:
                print(f"Consent form {form_id} not found for participant {self.participant_id}.")
        
    def add_genomic_dataset(self, dataset: GenomicDataset):
        if not isinstance(dataset, GenomicDataset):
            raise ValueError("Invalid dataset type. Must be a GenomicDataset.")
        self.genomic_datasets.append(dataset)
        print(f"Genomic dataset {dataset.sra_id} added for participant {self.participant_id}.")

    def remove_genomic_dataset(self, sra_id):
        for dataset in self.genomic_datasets:
            if dataset.sra_id == sra_id:
                self.genomic_datasets.remove(dataset)
                print(f"Genomic dataset {sra_id} removed for participant {self.participant_id}.")
            else:
                print(f"Genomic dataset {sra_id} not found for participant {self.participant_id}.")

    def summary(self):
        return f"Participant ID: {self.participant_id}, Name: {self.name}, Age: {self.age}, Sex: {self.sex}, Consent Forms: {len(self.consent_forms)}, Genomic Datasets: {len(self.genomic_datasets)}"

