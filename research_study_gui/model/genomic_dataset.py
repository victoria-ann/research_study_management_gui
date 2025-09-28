from model.data_check import DataCheck

class GenomicDataset(DataCheck):
    #fastq_file will link to the fastq file downloaded from SRA
    def __init__(self, dataset_id, sra_id,fastq_file):
        self.dataset_id = dataset_id
        self.sra_id = sra_id
        self.fastq_file = fastq_file

    def summary(self):
        return f"SRA ID: {self.sra_id}, FASTQ File: {self.fastq_file}"
    
    def is_valid(self):
        return bool(self.fastq_file and self.fastq_file)

class WGSDataset(GenomicDataset):
    pass
    def __init__(self, dataset_id, sra_id, fastq_file, bam_file, file_size):
        super().__init__(dataset_id, sra_id, fastq_file)
        self.bam_file = bam_file
        self.file_size = file_size

    def summary(self):
        return f"SRA ID: {self.sra_id}, FASTQ File: {self.fastq_file}, BAM File: {self.bam_file}, File Size: {self.file_size}"
    
    def is_valid(self):
        return bool(self.fastq_file and self.bam_file and self.file_size)
      
class RNASeqDataset(GenomicDataset):
    def __init__(self, dataset_id, sra_id, fastq_file, read_type, read_length, primers):
        super().__init__(dataset_id, sra_id, fastq_file)
        self.read_type = read_type
        self.read_length = read_length
        self.primers = primers
        

    def summary(self):
        return f"SRA ID: {self.sra_id}, FASTQ File: {self.fastq_file}, Read Type: {self.read_type}, Read Length: {self.read_length}, Primers: {self.primers}"
    
    def is_valid(self):
        return bool(self.fastq_file and self.read_type and self.read_length and self.primers)
    