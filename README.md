# Neuro-NGS Genome Assembly Project

This project utilizes the NCBI SRA database to perform deNovo assembly and variant analysis.

## Project Goals
- Assemble read datasets of subjects with Alzheimer's disease to assess a possible contributing casuse
- Identify possible mutations using variant call files

## Team Members
- Heather Ho
- Solhee Tucker
- Jimmy Du
- Jordan Sasaki

## Workflow
1. Download data from SRA
2. Trim reads with Trimmomatic
3. Assemble genome with SPades
4. Analyze assembly statistics with QUAST
5. Perform variant analysis

## Tools
- SRA toolkit
- Trimmomatic
- SPAdes
- QUAST
- bcftools / samtools

## Requirements
- Linux or WSL
- Python 3.8+
- JupyterLab

## Data Sources
- [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra)

