from model.participant import Participant
from model.participant import ConsentForm
from model.research_study import ResearchStudy
from controller.sql_functions import SQLSetup as su

class RegistryManager:
    def __init__(self, sql_setup):
        self.studies = []
        self.participants = []

    def setup_objects(self):
        sql_setup = su()
        num_participant_rows, participant_rows = sql_setup.sql_load_participants_from_db()

        for row in participant_rows:
            participant = Participant(row[0], row[1], row[2], row[3])
            self.participants.append(participant)
        
        num_study_rows, study_rows = sql_setup.sql_load_studies()
        for row in study_rows:
            study = ResearchStudy(row[0], row[1])
            self.studies.append(study)

        

    def create_study(self, study):
        self.studies.append(study)
        print(f"Study {study.study_name} with ID {study.study_id} created.")
      

    def remove_study(self, study_id):
        for study in self.studies:
            if study.study_id == study_id:
                self.studies.remove(study)
                print(f"Study {study_id} removed from registry.")
            else:
                print(f"Study {study_id} not found in registry.")
    
    def remove_participant(self, participant_id):
        for participant in self.participants:
            if participant.participant_id == participant_id:
                self.participants.remove(participant)
                print(f"Participant {participant_id} removed from registry.")
            else:
                print(f"Participant {participant_id} not found in registry.")
    

    def register_participant(self, participant: Participant):
        if not isinstance(participant, Participant):
            raise ValueError("Invalid participant type. Must be a Participant.")
        if participant not in self.participants:
            self.participants.append(participant)
            print(f"Participant {participant.participant_id} registered.")
        else:
            print(f"Participant {participant.participant_id} already registered.")

    def assign_participant_to_study(self, participant_id, study_id):
        participant = next((p for p in self.participants if p.participant_id == participant_id), None)
        study = next((s for s in self.studies if s.study_id == study_id), None)

        if participant and study:
            study.add_participant(participant)
            print(f"Participant {participant_id} assigned to study {study_id}.")
        else:
            print(f"Participant {participant_id} or Study {study_id} not found.")

    def remove_participant_from_study(self, participant_id, study_id):
        participant = next((p for p in self.participants if p.participant_id == participant_id), None)
        study = next((s for s in self.studies if s.study_id == study_id), None)

        if participant and study:
            study.remove_participant(participant_id)
            print(f"Participant {participant_id} removed from study {study_id}.")
        else:
            print(f"Participant {participant_id} or Study {study_id} not found.")

    def add_dataset_to_study(self, study_id, dataset_id):
        for study in self.studies:
            if study.study_id == study_id:
                study.add_dataset(dataset_id)
                print(f"Dataset {dataset_id} added to study {study.study_id}.")
                return True
        print(f"Study {study_id} not found.")
        return False
    
    def remove_dataset_from_study(self, study_id, dataset_id):
        for study in self.studies:
            if study.study_id == study_id:
                study.remove_dataset(dataset_id)
                print(f"Dataset {dataset_id} removed from study {study.study_id}.")
                return True
        print(f"Study {study_id} not found.")
        return False

    def add_consent_form(self, participant_id, consent_form: ConsentForm):
        for participant in self.participants:
            if participant.participant_id == participant_id:
                participant.consent_forms.append(consent_form)
        print(f"Consent form {consent_form.form_id} added for participant {participant.participant_id}.")


    def remove_consent_form(self, participant_id, form_id):
        for participant in self.participants:
            if participant.participant_id == participant_id:
                for form in participant.consent_forms:
                    if form.form_id == form_id:
                        participant.consent_forms.remove(form)
                        return True
                    return False
        return False
    
    def add_dataset_to_participant(self, participant_id, dataset):
        for participant in self.participants:
            if participant.participant_id == participant_id:
                participant.genomic_datasets.append(dataset)
                print(f"Dataset {dataset.dataset_id} added to participant {participant.participant_id}.")
                return True
        print(f"Participant {participant_id} not found.")
        return False
    
