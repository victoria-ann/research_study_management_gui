from model.participant import Participant
from model.genomic_dataset import GenomicDataset

class ResearchStudy:
    def __init__(self, study_id, study_name):
        self.study_id = study_id
        self.study_name = study_name
        self.participants = []
        self.datasets = []

    def add_participant(self, participant):
        if participant not in self.participants:    
            self.participants.append(participant)
            print(f"Participant {participant.participant_id} added to study {self.study_id}.")
        else:
            print(f"Participant {participant.participant_id} already exists in study {self.study_id}.")

    def remove_participant(self, participant_id):
        for participant in self.participants:
            if participant.participant_id == participant_id:
                self.participants.remove(participant)
                print(f"Participant {participant_id} removed from study {self.study_id}.")
            else:
                print(f"Participant {participant_id} not found in study {self.study_id}.")

    def add_dataset(self, dataset):
        if dataset not in self.datasets:
            self.datasets.append(dataset)
            print(f"Dataset {dataset.dataset_id} added to study {self.study_id}.")
        else:
            print(f"Dataset {dataset.dataset_id} already exists in study {self.study_id}.")

    def remove_dataset(self, dataset_id):
        for dataset in self.datasets:
            if dataset.dataset_id == dataset_id:
                self.datasets.remove(dataset)
                print(f"Dataset {dataset_id} removed from study {self.study_id}.")
            else:
                print(f"Dataset {dataset_id} not found in study {self.study_id}.")

    def summary(self):
        return f"Study ID: {self.study_id}, Study Name: {self.study_name}, Participants: {len(self.participants)}, Datasets: {len(self.datasets)}"

    