# sipecam-metadata-extractor

`simex` uses:

[pyexiftool](https://github.com/sylikc/pyexiftool), see [pyexiftool/examples](https://sylikc.github.io/pyexiftool/examples.html)

# Running `sipecam/simex:0.4` docker image in CONABIO cluster

Ssh to one node of CONABIO cluster as user `madmex_admin`.

```
SIMEX_VERSION=0.4
REPO_URL=sipecam/simex
```

Delete previous docker image of `simex` to have the latest one:

```
docker rmi $REPO_URL:$SIMEX_VERSION
```

# list_of_files_and_subdirectories_to_extract_metadata

```
dir_with_sipecam_data=/LUSTRE/sacmod/SIPECAM/Entregas_2021/octubre_2021/SIPECAM/
docker run --rm -v /LUSTRE:/LUSTRE -v $HOME:/shared_volume -d $REPO_URL:$SIMEX_VERSION list_of_files_and_subdirectories_to_extract_metadata --input_directory $dir_with_sipecam_data
```

## check

```
wc -l sipecam_files_to_extract_metadata_from_*

wc -l sipecam_subdirectories_*
```

# generate_sipecam_zendro_schema

```
docker run --rm -v /LUSTRE:/LUSTRE -v $HOME:/shared_volume -it $REPO_URL:$SIMEX_VERSION

echo "SIPECAM_ZENDRO_GQL_URL=https://gql.sipecamdata.conabio.gob.mx/" > ~/.simex_env
echo "SIPECAM_ZENDRO_GQL_USER=<user zendro>" >> ~/.simex_env
echo "SIPECAM_ZENDRO_GQL_PASSWORD=<password zendro>" >> ~/.simex_env

generate_sipecam_zendro_schema

#check:

ls -lh sipecam-metadata-extractor/src/simex/sipecam_zendro_schema.*

head -n 10 /root/sipecam-metadata-extractor/src/simex/sipecam_zendro_schema.py

```

# extract_serial_numbers_dates_and_metadata_of_files_and_device

```
dir_to_be_processed="/LUSTRE/sacmod/SIPECAM/Entregas_2021/octubre_2021/SIPECAM/Playon 1338/Camaras/1338_1/100RECNX/"
#default for parallel execution are 4 processes
docker run --rm -v /LUSTRE:/LUSTRE $REPO_URL:$SIMEX_VERSION extract_serial_numbers_dates_and_metadata_of_files_and_device --input_dir "$dir_to_be_processed" --parallel
```

## check

```
dir_to_be_processed="/LUSTRE/sacmod/SIPECAM/Entregas_2021/octubre_2021/SIPECAM/Playon 1338/Camaras/1338_1/100RECNX/"
file_for_logs=$(find "$dir_to_be_processed" -name "logs_simex_extract_serial_numbers_dates_and_metadata_of_files_and_device.logs")
head -n 15 "$file_for_logs"

file_json=$(find "$dir_to_be_processed" -name "*.json")
python3 -mjson.tool "$file_json"|head -n 15
```


# move_files_to_standard_directory

```
dir_to_be_processed="/LUSTRE/sacmod/SIPECAM/Entregas_2021/octubre_2021/SIPECAM/Playon 1338/Camaras/1338_1/100RECNX/"
path_std_dir="/LUSTRE/users/epalacios/sipecam_simex"
docker run --rm -v /LUSTRE:/LUSTRE move_files_to_standard_directory --directory_with_file_of_serial_number_and_dates "$dir_to_be_processed" --path_for_standard_directory "$path_std_dir"
```

## check

```
dir_to_be_processed="/LUSTRE/sacmod/SIPECAM/Entregas_2021/octubre_2021/SIPECAM/Playon 1338/Camaras/1338_1/100RECNX/"
file_for_logs=$(find "$dir_to_be_processed" -name 'logs_simex_copy_files_to_standard_directory.logs')
head -n 72 "$file_for_logs"
```

# Using slurm (next doc needs to be updated for extract serial numbers, datetimes and copy clis)

Ssh to one node of CONABIO cluster as user `madmex_admin`.

## Parallel-ssh to rmi and pull docker image for each node at CONABIO

Create

```
~/nodos_sipecam.txt
```

```
nodo5
nodo6
nodo7
```

then:

```
SIMEX_VERSION=0.4
REPO_URL=sipecam/simex
parallel-ssh -i -p 2 -v -h nodos_sipecam.txt -l madmex_admin "docker rmi $REPO_URL:$SIMEX_VERSION"
parallel-ssh -i -p 2 -v -h nodos_sipecam.txt -l madmex_admin "docker pull $REPO_URL:$SIMEX_VERSION"
```

**Every time metadata will be extracted run last command of `parallel-ssh` (setting env variables) to download latest docker image of `sipecam/simex`.**


## For execution using `slurm`

Set:

```
SIMEX_VERSION=0.4
REPO_URL=sipecam/simex
CONTAINER_NAME=sipecam-simex
```

Command `list_of_files_to_extract_metadata`

```
dir_with_sipecam_data=/LUSTRE/sacmod/SIPECAM/Entregas_2021/octubre_2021/SIPECAM/
docker run --rm -v /LUSTRE:/LUSTRE -v $HOME:/shared_volume --name $CONTAINER_NAME -d $REPO_URL:$SIMEX_VERSION list_of_files_to_extract_metadata --input_directory $dir_with_sipecam_data
```

Check number of files whose metadata will be extracted

```
wc -l sipecam_files_to_extract_metadata_from_02-12-2021.txt
```

### Create slurm jobs

Only first time: create 

```
~/slurm_extract_metadata_and_ingest_it.sh
```

```
#!/bin/bash
# first parameter is file whose metadata will be extracted

#SBATCH --exclude nodo1,nodo2,nodo3,nodo4

SIMEX_VERSION=0.4
REPO_URL=sipecam/simex

echo $(hostname)
echo "$1"
docker run --rm -v /LUSTRE:/LUSTRE -v $HOME:/shared_volume -d $REPO_URL:$SIMEX_VERSION extract_metadata_and_ingest_it --input_file "$1"
```

Create directory with name of date of launch:

```
today_date=$(printf '%(%d-%m-%Y)T\n' -1)
mkdir sipecam_extract_metadata_$today_date
```

Create shell 

```
~/sipecam_extract_metadata_$today_date/script_to_generate_slurm_jobs.sh
```

```
#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
today_date=$(printf '%(%d-%m-%Y)T\n' -1)

for f in $(cat ~/sipecam_files_to_extract_metadata_from_$today_date.txt)
do
  echo "sbatch -D ~/sipecam_extract_metadata_$today_date ~/slurm_extract_metadata_and_ingest_it.sh \""$f"\"" >> ~/sipecam_extract_metadata_$today_date/slurm_jobs_extract_metadata_and_ingest_it.sh
done
IFS=$SAVEIFS
```

Get jobs that will be executed with `slurm`

```
bash ~/sipecam_extract_metadata_$today_date/script_to_generate_slurm_jobs.sh
```

Check number of jobs that will be launched will slurm

```
wc -l ~/sipecam_extract_metadata_$today_date/slurm_jobs_extract_metadata_and_ingest_it.sh
```

Launch them

```
bash ~/sipecam_extract_metadata_$today_date/slurm_jobs_extract_metadata_and_ingest_it.sh
```

Check running jobs:

```
squeue -u madmex_admin
```

Check logs of slurm inside 

```
~/sipecam_extract_metadata_$today_date
```

Use `scontrol show jobid -dd <jobid>` to get info from job.

## Next just an example command of `extract_metadata_and_ingest_it`

```
file_to_be_processed=$(head -n 1 ~/sipecam_files_to_extract_metadata_from_*)
docker run --rm -v /LUSTRE:/LUSTRE -v $HOME:/shared_volume --name $CONTAINER_NAME -d $REPO_URL:$SIMEX_VERSION extract_metadata_and_ingest_it --input_file "$file_to_be_processed"
```

## Running `sipecam/simex/` docker image in a docker container `jupyterlab` cmd

```
docker run --rm -v $HOME:/shared_volume --name $CONTAINER_NAME -p 3000:8888 -d $REPO_URL:$SIMEX_VERSION /usr/local/bin/jupyter lab --ip=0.0.0.0 --no-browser --allow-root
```
