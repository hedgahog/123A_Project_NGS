import subprocess
reference_sequence = 
bam_sequence=
output_vcf = 
subprocess.run([
        "bcftools", "mpileup",
        "-f", reference_sequence,
        "-Ou", bam_sequence
    ])
    mpileup_proc = subprocess.Popen(
        ["bcftools", "mpileup", "-f", reference_sequence, "-Ou", bam_sequence],
        stdout=subprocess.PIPE
    )
    call_proc = subprocess.run(
        ["bcftools", "call", "-mv", "-Ov", "-o", output_vcf],
        stdin=mpileup_proc.stdout,
        check=True
    )
    mpileup_proc.stdout.close()
    mpileup_proc.wait()